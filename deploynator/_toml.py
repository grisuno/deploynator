from __future__ import annotations

import os
from dataclasses import dataclass

from deploynator._config import Config

TOML_FILENAME = "deploynator.toml"
DEFAULT_TEST_COMMANDS: list[str] = ["python -m pytest tests/ -q"]
DEFAULT_DOCS_COMMAND = "python -m readmenator . --rebuild"

# Auto-detección C: nombres de Makefile y targets preferidos.
# `test-host` va primero porque en proyectos como miniOS `test`
# requiere QEMU/imagen (lento), mientras `test-host` corre las
# suites unitarias rápidas en el host (contrato CI).
MAKEFILE_NAMES: tuple[str, ...] = ("Makefile", "makefile", "GNUmakefile")
MAKE_TEST_PRIORITY: list[str] = ["test-host", "test", "check", "tests"]
C_TEST_TIMEOUT_S: int = 900

_TARGET_RE = None


def _target_regex():  # type: ignore[no-untyped-def]
    global _TARGET_RE
    if _TARGET_RE is None:
        import re
        _TARGET_RE = re.compile(r"^([A-Za-z0-9_][A-Za-z0-9_.\-]*)\s*:(?!=)")
    return _TARGET_RE


def list_make_targets(project_path: str) -> list[str]:
    """Lee el Makefile y devuelve sus targets sin ejecutar nada.

    Seguro: rechaza symlinks, limita tamaño (Config.max_file_size_bytes).
    """
    makefile = ""
    for name in MAKEFILE_NAMES:
        candidate = os.path.join(project_path, name)
        if os.path.islink(candidate):
            raise ValueError(f"Symlink rejected: {candidate}")
        if os.path.isfile(candidate):
            makefile = candidate
            break
    if not makefile:
        return []
    if os.path.getsize(makefile) > Config.create().max_file_size_bytes:
        raise ValueError(f"File too large: {makefile}")
    targets: list[str] = []
    try:
        with open(makefile, "r", errors="replace") as f:
            for line in f:
                # Solo targets al inicio de línea (sin indentación = no receta).
                if line[:1] in (" ", "\t"):
                    continue
                m = _target_regex().match(line.strip())
                if m and m.group(1) not in targets:
                    if not m.group(1).startswith("."):
                        targets.append(m.group(1))
    except OSError as exc:
        raise ValueError(f"Cannot read Makefile: {exc}") from exc
    return targets


def _has_python_tests(project_path: str) -> bool:
    tests_dir = os.path.join(project_path, "tests")
    if not os.path.isdir(tests_dir):
        return False
    try:
        for entry in os.listdir(tests_dir):
            if entry.endswith(".py"):
                return True
    except OSError:
        return False


def looks_like_packaging_project(project_path: str) -> bool:
    """Inferencia runtime (multi-proyecto): ¿es un paquete PyPI?

    Espejo liviano de PyPIRunner.is_packaging_project sin importar
    _pypi (evita ciclo). El gate final sigue en PyPIRunner al
    desplegar; aquí solo se usa para el default de pypi_enabled.
    """
    pyproject = os.path.join(project_path, "pyproject.toml")
    if os.path.isfile(pyproject) and not os.path.islink(pyproject):
        try:
            import tomllib
            with open(pyproject, "rb") as f:
                data = tomllib.load(f)
            project = data.get("project", {})
            if isinstance(project, dict) and project.get("name"):
                return True
        except Exception:
            pass
    for candidate in ("setup.py", "setup.cfg"):
        candidate_path = os.path.join(project_path, candidate)
        if os.path.isfile(candidate_path) and not os.path.islink(candidate_path):
            return True
    return False
    return False


def detect_test_commands(project_path: str) -> list[str] | None:
    """Detecta comandos de test para proyectos C/autotools sin toml.

    Runtime multi-proyecto, sin hardcodear nombres de proyecto:
    Makefile (test-host canónico solo; si no, TODOS los targets de
    test en una sola invocación `make test test-* ...`, p. ej.
    `make test test-dsp test-transport`) → CMake (build+ctest) →
    meson (setup+test).
    Devuelve None si no hay nada detectable (caller usa pytest default).
    """
    try:
        targets = list_make_targets(project_path)
    except ValueError:
        targets = []
    if targets:
        # `test-host` es la suite canónica (drivers internos propios):
        # va sola, manda sobre todo (incluso sobre tests/*.py).
        if "test-host" in targets:
            return ["make test-host"]
        combined: list[str] = []
        for preferred in MAKE_TEST_PRIORITY[1:]:
            # `tests` desnudo suele ser helper mkdir (dependencia order-only
            # `| tests`), no runner: se excluye si hay otro target de test.
            if preferred == "tests" and any(
                t in targets for t in ("test", "check")
            ):
                continue
            if preferred in targets and preferred not in combined:
                combined.append(preferred)
        for extra in sorted(t for t in targets
                            if (t.startswith("test-") or t.startswith("test_"))
                            and t not in combined):
            combined.append(extra)
        if combined:
            return [f"make {' '.join(combined)}"]
        # Makefile sin target de test: al menos verifica que compila.
        if "all" in targets:
            return ["make"]
        return ["make"]
    if os.path.isfile(os.path.join(project_path, "CMakeLists.txt")):
        return [
            "cmake -S . -B build",
            "cmake --build build",
            "ctest --test-dir build",
        ]
    if os.path.isfile(os.path.join(project_path, "meson.build")):
        return ["meson setup build", "meson test -C build"]
    return None


def _auto_toml_config(project_path: str) -> TomlConfig | None:
    """Config auto para proyectos sin deploynator.toml (C primero).

    Multi-proyecto: pypi_enabled se infiere al vuelo de los ficheros
    de packaging (pyproject/setup.py/setup.cfg); el gate final sigue
    en PyPIRunner.is_packaging_project al desplegar.
    """
    detected = detect_test_commands(project_path)
    if detected is None:
        return None
    # `make test-host` es la suite canónica C (incluye sus propios
    # drivers python internos): manda incluso si hay tests/*.py.
    # Para el resto, si hay tests Python reales se conserva pytest
    # (evita romper proyectos Python con Makefile auxiliar).
    if detected != ["make test-host"] and detected[0].startswith("make") and _has_python_tests(project_path):
        return None
    name = os.path.basename(os.path.abspath(project_path))
    return TomlConfig(
        project_name=name,
        test_commands=detected,
        test_timeout_s=C_TEST_TIMEOUT_S,
        docs_auto=True,
        pypi_enabled=looks_like_packaging_project(project_path),
    )


@dataclass(frozen=True)
class TomlConfig:
    project_name: str = ""
    version_file: str = "version.json"
    test_commands: list[str] = None  # type: ignore[assignment]
    test_timeout_s: int = 300
    allow_no_tests: bool = False
    docs_auto: bool = True
    docs_command: str = DEFAULT_DOCS_COMMAND
    docs_timeout_s: int = 300
    deploy_branch: str = "main"
    deploy_remote: str = "origin"
    pypi_enabled: bool = True
    pypi_repo: str = "pypi"
    pypi_clean_dist: bool = True
    pypi_timeout_s: int = 600

    def __post_init__(self) -> None:
        if self.test_commands is None:
            object.__setattr__(self, "test_commands", list(DEFAULT_TEST_COMMANDS))
        object.__setattr__(self, "test_timeout_s", _clamp_timeout(self.test_timeout_s))
        object.__setattr__(self, "docs_timeout_s", _clamp_timeout(self.docs_timeout_s))
        object.__setattr__(self, "pypi_timeout_s", _clamp_timeout(self.pypi_timeout_s))


def _clamp_timeout(value: int) -> int:
    try:
        v = int(value)
    except (TypeError, ValueError):
        return 300
    return max(1, min(3600, v))


def load_toml_config(project_path: str) -> TomlConfig:
    toml_path = os.path.join(project_path, TOML_FILENAME)
    if os.path.islink(toml_path):
        raise ValueError(f"Symlink rejected: {toml_path}")
    if not os.path.isfile(toml_path):
        auto = _auto_toml_config(project_path)
        if auto is not None:
            return auto
        return TomlConfig(project_name=os.path.basename(os.path.abspath(project_path)))
    if os.path.getsize(toml_path) > Config.create().max_file_size_bytes:
        raise ValueError(f"File too large: {toml_path}")
    try:
        import tomllib
    except ImportError as exc:
        raise ValueError(f"tomllib unavailable: {exc}") from exc
    try:
        with open(toml_path, "rb") as f:
            data = tomllib.load(f)
    except Exception as exc:
        raise ValueError(f"Invalid {TOML_FILENAME}: {exc}") from exc
    if not isinstance(data, dict):
        raise ValueError(f"Invalid {TOML_FILENAME}: root must be a table")

    project_raw = data.get("project", {}) or {}
    tests_raw = data.get("tests", {}) or {}
    docs_raw = data.get("docs", {}) or {}
    deploy_raw = data.get("deploy", {}) or {}
    pypi_raw = data.get("pypi", {}) or {}

    if not isinstance(project_raw, dict) or not isinstance(tests_raw, dict):
        raise ValueError(f"Invalid {TOML_FILENAME}: bad sections")
    if not isinstance(docs_raw, dict) or not isinstance(deploy_raw, dict):
        raise ValueError(f"Invalid {TOML_FILENAME}: bad sections")
    if not isinstance(pypi_raw, dict):
        raise ValueError(f"Invalid {TOML_FILENAME}: bad sections")

    _sentinel: list[str] = []  # type: ignore[assignment]
    commands = tests_raw.get("commands", _sentinel)
    if commands is _sentinel:
        # Sin [tests]commands explícito: auto-detect C, si no pytest.
        detected = detect_test_commands(project_path)
        if detected is not None and not (
            detected != ["make test-host"]
            and detected[0].startswith("make")
            and _has_python_tests(project_path)
        ):
            commands = detected
            default_timeout = C_TEST_TIMEOUT_S
        else:
            commands = list(DEFAULT_TEST_COMMANDS)
            default_timeout = 300
    elif commands is None:
        commands = list(DEFAULT_TEST_COMMANDS)
        default_timeout = 300
    else:
        default_timeout = 300
    if not isinstance(commands, list) or not all(isinstance(c, str) for c in commands):
        raise ValueError(f"Invalid {TOML_FILENAME}: [tests] commands must be list[str]")

    raw_timeout = tests_raw.get("timeout_s", default_timeout)

    return TomlConfig(
        project_name=str(project_raw.get("name", "") or os.path.basename(os.path.abspath(project_path))),
        version_file=str(project_raw.get("version_file", "version.json")),
        test_commands=list(commands),
        test_timeout_s=_clamp_timeout(raw_timeout),
        allow_no_tests=bool(tests_raw.get("allow_no_tests", False)),
        docs_auto=bool(docs_raw.get("auto", True)),
        docs_command=str(docs_raw.get("command", DEFAULT_DOCS_COMMAND)),
        docs_timeout_s=_clamp_timeout(docs_raw.get("timeout_s", 300)),
        deploy_branch=str(deploy_raw.get("branch", "main")),
        deploy_remote=str(deploy_raw.get("remote", "origin")),
        pypi_enabled=bool(pypi_raw.get("enabled", True)),
        pypi_repo=str(pypi_raw.get("repo", "pypi")),
        pypi_clean_dist=bool(pypi_raw.get("clean_dist", True)),
        pypi_timeout_s=_clamp_timeout(pypi_raw.get("timeout_s", 600)),
    )
