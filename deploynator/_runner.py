from __future__ import annotations

import os
import shlex
import subprocess

from deploynator._config import Config
from deploynator._toml import TomlConfig


class TestRunner:
    def __init__(self, config: Config) -> None:
        self._config = config

    def run(self, project_path: str, toml: TomlConfig) -> tuple[bool, str]:
        commands = toml.test_commands or []
        if not commands:
            if toml.allow_no_tests or not os.path.isdir(os.path.join(project_path, "tests")):
                if toml.allow_no_tests:
                    return True, "No tests configured (allowed)"
                return False, "No tests configured: [tests] commands empty and tests/ missing"
            return False, "No tests configured: [tests] commands empty"
        outputs: list[str] = []
        for cmd_str in commands:
            if not cmd_str or not cmd_str.strip():
                return False, "Invalid test command: empty string"
            try:
                argv = shlex.split(cmd_str)
            except ValueError as exc:
                return False, f"Invalid test command {cmd_str!r}: {exc}"
            if not argv:
                return False, f"Invalid test command: {cmd_str!r}"
            try:
                result = subprocess.run(
                    argv,
                    cwd=project_path,
                    capture_output=True,
                    text=True,
                    check=False,
                    shell=False,
                    timeout=toml.test_timeout_s,
                )
            except FileNotFoundError as exc:
                return False, f"Test command not found {argv[0]!r}: {exc}"
            except subprocess.TimeoutExpired:
                return False, f"Test command timed out after {toml.test_timeout_s}s: {cmd_str}"
            combined = (result.stdout or "") + (result.stderr or "")
            outputs.append(f"$ {cmd_str}\n{combined}")
            if result.returncode != 0:
                return False, f"Tests failed: {cmd_str}\n{combined}".strip()
        return True, "\n".join(outputs)
