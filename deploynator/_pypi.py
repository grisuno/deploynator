from __future__ import annotations

import os
import shutil
import subprocess
import sys

from deploynator._config import Config
from deploynator._toml import TomlConfig


class PyPIRunner:
    def __init__(self, config: Config) -> None:
        self._config = config

    def is_packaging_project(self, project_path: str) -> bool:
        pyproject = os.path.join(project_path, "pyproject.toml")
        if os.path.isfile(pyproject) and not os.path.islink(pyproject):
            try:
                import tomllib
                with open(pyproject, "rb") as f:
                    data = tomllib.load(f)
                project = data.get("project", {})
                if isinstance(project, dict) and project.get("name"):
                    return True
            except (OSError, ValueError):
                pass
        for candidate in ("setup.py", "setup.cfg"):
            if os.path.isfile(os.path.join(project_path, candidate)):
                return True
        return False

    def has_credentials(self) -> bool:
        if os.environ.get("TWINE_PASSWORD") or os.environ.get("PYPI_TOKEN"):
            return True
        pypirc = os.path.expanduser("~/.pypirc")
        return os.path.isfile(pypirc)

    def prompt_for_credentials(self) -> str | None:
        """Pide el token PyPI por input oculto solo si hay TTY.

        Sin TTY (harness, CI, MCP) devuelve None para no bloquear.
        Pregunta si guardar en ~/.pypirc (modo 600, fuera de git).
        """
        import sys
        try:
            if not sys.stdin.isatty():
                return None
        except (ValueError, OSError):
            return None
        import getpass
        try:
            token = getpass.getpass("PyPI API token (pypi-...): ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            return None
        if not token:
            return None
        try:
            save = input("Save token to ~/.pypirc (mode 600)? (y/N): ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            print()
            return token
        if save in ("y", "yes", "s", "si"):
            try:
                self.save_pypirc(token)
                print("[+] Token saved to ~/.pypirc")
            except (ValueError, OSError) as exc:
                print(f"[!] Could not save ~/.pypirc: {exc}")
        return token

    def save_pypirc(self, token: str, path: str | None = None) -> str:
        """Guarda el token en ~/.pypirc (username __token__, modo 600)."""
        import configparser
        target = path or os.path.expanduser("~/.pypirc")
        if os.path.islink(target):
            raise ValueError(f"Symlink rejected: {target}")
        cfg = configparser.ConfigParser()
        if os.path.isfile(target):
            cfg.read(target)
        if "pypi" not in cfg:
            cfg["pypi"] = {}
        cfg["pypi"]["username"] = "__token__"
        cfg["pypi"]["password"] = token
        with open(target, "w") as f:
            cfg.write(f)
        os.chmod(target, 0o600)
        return target

    def clean(self, project_path: str, toml: TomlConfig) -> None:
        if not toml.pypi_clean_dist:
            return
        for entry in ("dist", "build"):
            target = os.path.join(project_path, entry)
            if os.path.islink(target):
                raise ValueError(f"Symlink rejected: {target}")
            if os.path.isdir(target):
                shutil.rmtree(target)
        for entry in sorted(os.listdir(project_path)):
            if entry.endswith(".egg-info"):
                target = os.path.join(project_path, entry)
                if os.path.islink(target):
                    raise ValueError(f"Symlink rejected: {target}")
                if os.path.isdir(target):
                    shutil.rmtree(target)

    def run(self, project_path: str, toml: TomlConfig, version: str,
            token: str | None = None, verbose: bool = False) -> tuple[bool, str]:
        if not self.is_packaging_project(project_path):
            return True, "PyPI skipped: no packaging files"
        try:
            self.clean(project_path, toml)
        except (ValueError, OSError) as exc:
            return False, f"PyPI clean failed: {exc}"
        build = subprocess.run(
            [sys.executable, "-m", "build", "--outdir", "dist/"],
            cwd=project_path,
            capture_output=True, text=True, check=False,
            shell=False,
            timeout=toml.pypi_timeout_s,
        )
        if build.returncode != 0:
            raw = (build.stderr or build.stdout or "").strip()
            if verbose and raw:
                print(raw)
            err = raw if verbose else raw[-2000:]
            hint = "" if "build" not in err.lower() else " (pip install build)"
            return False, f"PyPI build failed for {version}{hint}: {err}"
        dist_dir = os.path.join(project_path, "dist")
        artifacts = sorted(os.listdir(dist_dir)) if os.path.isdir(dist_dir) else []
        if not artifacts:
            return False, f"PyPI build produced no artifacts for {version}"
        cmd = [sys.executable, "-m", "twine", "upload", "--non-interactive"]
        if verbose:
            cmd += ["--verbose"]
        if toml.pypi_repo == "testpypi":
            cmd += ["--repository", "testpypi"]
        elif toml.pypi_repo not in ("pypi", "testpypi"):
            cmd += ["--repository-url", toml.pypi_repo]
        cmd += [os.path.join("dist", a) for a in artifacts]
        if verbose:
            print(f"[...] {subprocess.list2cmdline(cmd)} (cwd={project_path})")
        env = dict(os.environ)
        token = token or os.environ.get("PYPI_TOKEN")
        if token and not os.environ.get("TWINE_PASSWORD"):
            env["TWINE_USERNAME"] = "__token__"
            env["TWINE_PASSWORD"] = token
        try:
            upload = subprocess.run(
                cmd,
                cwd=project_path,
                capture_output=True, text=True, check=False,
                shell=False,
                timeout=toml.pypi_timeout_s,
                env=env,
            )
        except subprocess.TimeoutExpired:
            return False, f"PyPI upload timed out after {toml.pypi_timeout_s}s"
        if upload.returncode != 0:
            raw = (upload.stderr or upload.stdout or "").strip()
            if verbose and raw:
                print(raw)
            err = raw if verbose else raw[-2000:]
            return False, f"PyPI upload failed for {version}: {err}"
        return True, f"PyPI uploaded {version}: {', '.join(artifacts)}"
