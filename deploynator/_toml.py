from __future__ import annotations

import os
from dataclasses import dataclass

from deploynator._config import Config

TOML_FILENAME = "deploynator.toml"
DEFAULT_TEST_COMMANDS: list[str] = ["python -m pytest tests/ -q"]
DEFAULT_DOCS_COMMAND = "python -m readmenator . --rebuild"


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

    commands = tests_raw.get("commands", list(DEFAULT_TEST_COMMANDS))
    if commands is None:
        commands = list(DEFAULT_TEST_COMMANDS)
    if not isinstance(commands, list) or not all(isinstance(c, str) for c in commands):
        raise ValueError(f"Invalid {TOML_FILENAME}: [tests] commands must be list[str]")

    return TomlConfig(
        project_name=str(project_raw.get("name", "") or os.path.basename(os.path.abspath(project_path))),
        version_file=str(project_raw.get("version_file", "version.json")),
        test_commands=list(commands),
        test_timeout_s=_clamp_timeout(tests_raw.get("timeout_s", 300)),
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
