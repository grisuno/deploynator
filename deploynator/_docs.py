from __future__ import annotations

import shlex
import subprocess

from deploynator._config import Config
from deploynator._toml import TomlConfig


class DocsRunner:
    def __init__(self, config: Config) -> None:
        self._config = config

    def run(self, project_path: str, toml: TomlConfig) -> bool:
        if not toml.docs_auto:
            return True
        cmd_str = (toml.docs_command or "").strip()
        if not cmd_str:
            print("[!] docs command empty, skipping")
            return True
        try:
            argv = shlex.split(cmd_str)
        except ValueError as exc:
            print(f"[!] invalid docs command: {exc}")
            return False
        if not argv:
            return True
        try:
            result = subprocess.run(
                argv,
                cwd=project_path,
                capture_output=True,
                text=True,
                check=False,
                shell=False,
                timeout=toml.docs_timeout_s,
            )
        except FileNotFoundError:
            print("[!] readmenator not available. Install: pip install readmenator")
            return False
        except subprocess.TimeoutExpired:
            print(f"[!] docs timed out after {toml.docs_timeout_s}s, continuing")
            return False
        if result.returncode != 0:
            err = (result.stderr or result.stdout or "").strip()[:500]
            print(f"[!] docs failed ({cmd_str}), continuing: {err}")
            return False
        print("[+] docs regenerated via readmenator")
        return True
