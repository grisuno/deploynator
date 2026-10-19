from __future__ import annotations

import os
import shlex
import shutil
import subprocess

from deploynator._config import Config
from deploynator._toml import TomlConfig, list_make_targets


class DebRunner:
    """Construye paquetes .deb desde fuentes C, espejo del flujo PyPI.

    Detección (is_deb_project):
      - debian/control existe, o
      - Makefile expone un target de paquetización
        (deb | package-deb | dist-deb | deb-package | package).

    Build (run):
      - [deb] build explícito (shlex, shell=False) manda,
      - si no: `make <target-deb>` si existe,
      - si no: `dpkg-buildpackage -us -uc -b` si hay debian/control,
      - artefactos *.deb se consolidan en [deb] outdir (default dist-deb/).
    """

    DEB_MAKE_TARGETS: tuple[str, ...] = (
        "deb",
        "package-deb",
        "dist-deb",
        "deb-package",
        "package",
    )

    def __init__(self, config: Config) -> None:
        self._config = config

    def deb_make_target(self, project_path: str) -> str | None:
        try:
            targets = list_make_targets(project_path)
        except ValueError:
            return None
        for candidate in self.DEB_MAKE_TARGETS:
            if candidate in targets:
                return candidate
        return None

    def is_deb_project(self, project_path: str) -> bool:
        control = os.path.join(project_path, "debian", "control")
        if os.path.isfile(control) and not os.path.islink(control):
            return True
        return self.deb_make_target(project_path) is not None

    def _outdir(self, project_path: str, toml: TomlConfig) -> str:
        out = (toml.deb_outdir or "dist-deb").strip() or "dist-deb"
        # Evita path traversal: solo nombre relativo simple.
        out = os.path.basename(out) if not out.startswith((".", "/")) else "dist-deb"
        if out in (".", "..", ""):
            out = "dist-deb"
        return os.path.join(project_path, out)

    def clean(self, project_path: str, toml: TomlConfig) -> None:
        if not toml.deb_clean_dist:
            return
        target = self._outdir(project_path, toml)
        if os.path.islink(target):
            raise ValueError(f"Symlink rejected: {target}")
        if os.path.isdir(target):
            shutil.rmtree(target)

    def _collect_debs(self, project_path: str, outdir: str) -> list[str]:
        """Busca *.deb en outdir, raíz del proyecto y dir padre.

        dpkg-buildpackage deja los .deb en el padre; `make deb`
        suele dejarlos en la raíz o en outdir. Se consolidan
        (copia) en outdir para subirlos como assets.
        """
        found: dict[str, str] = {}
        candidates = [outdir, project_path, os.path.dirname(os.path.abspath(project_path))]
        for directory in candidates:
            try:
                if not os.path.isdir(directory) or os.path.islink(directory):
                    continue
                for entry in sorted(os.listdir(directory)):
                    if not entry.endswith(".deb"):
                        continue
                    full = os.path.join(directory, entry)
                    if os.path.islink(full) or not os.path.isfile(full):
                        continue
                    if os.path.getsize(full) > self._config.max_file_size_bytes * 10:
                        continue
                    found[entry] = full
            except OSError:
                continue
        consolidated: list[str] = []
        os.makedirs(outdir, exist_ok=True)
        for name in sorted(found):
            src = found[name]
            dst = os.path.join(outdir, name)
            if os.path.abspath(src) != os.path.abspath(dst):
                try:
                    shutil.copy2(src, dst)
                except OSError:
                    continue
                consolidated.append(dst)
            else:
                consolidated.append(src)
        return sorted(consolidated)

    def build_command(self, project_path: str, toml: TomlConfig) -> list[str] | None:
        custom = (toml.deb_build or "").strip()
        if custom:
            try:
                argv = shlex.split(custom)
            except ValueError:
                return None
            return argv or None
        target = self.deb_make_target(project_path)
        if target:
            return ["make", target]
        control = os.path.join(project_path, "debian", "control")
        if os.path.isfile(control) and not os.path.islink(control):
            return ["dpkg-buildpackage", "-us", "-uc", "-b"]
        return None

    def run(
        self, project_path: str, toml: TomlConfig, version: str,
        verbose: bool = False,
    ) -> tuple[bool, str, list[str]]:
        custom = (toml.deb_build or "").strip()
        if not custom and not self.is_deb_project(project_path):
            return True, "deb skipped: no debian/control nor make deb target", []
        try:
            self.clean(project_path, toml)
        except (ValueError, OSError) as exc:
            return False, f"deb clean failed: {exc}", []
        cmd = self.build_command(project_path, toml)
        if not cmd:
            return False, f"deb build failed for {version}: no build command ([deb] build vacío y sin target deb ni debian/control)", []
        outdir = self._outdir(project_path, toml)
        os.makedirs(outdir, exist_ok=True)
        if verbose:
            print(f"[...] {subprocess.list2cmdline(cmd)} (cwd={project_path})")
        try:
            proc = subprocess.run(
                cmd,
                cwd=project_path,
                capture_output=True, text=True, check=False,
                shell=False,
                timeout=toml.deb_timeout_s,
            )
        except FileNotFoundError as exc:
            return False, f"deb build failed for {version}: command not found {cmd[0]!r}: {exc}", []
        except subprocess.TimeoutExpired:
            return False, f"deb build timed out after {toml.deb_timeout_s}s", []
        if proc.returncode != 0:
            raw = (proc.stderr or proc.stdout or "").strip()
            err = raw if verbose else raw[-2000:]
            return False, f"deb build failed for {version}: {err}", []
        artifacts = self._collect_debs(project_path, outdir)
        if not artifacts:
            return False, f"deb build produced no .deb for {version} (cmd: {' '.join(cmd)})", []
        names = ", ".join(os.path.basename(a) for a in artifacts)
        return True, f"deb built {version}: {names}", artifacts
