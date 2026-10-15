from __future__ import annotations

import json
import os
import re
from typing import Optional

from deploynator._config import Config
from deploynator._models import VersionInfo, CommitType


class SemverManager:
    def __init__(self, config: Config) -> None:
        self._config = config

    def max_version(self, a: VersionInfo, b: VersionInfo) -> VersionInfo:
        if (a.major, a.minor, a.patch) >= (b.major, b.minor, b.patch):
            return a
        return b

    def get_current_version(self, project_path: str, version_file: str = "version.json",
                            version_pattern: str = r"(\d+)\.(\d+)\.(\d+)") -> VersionInfo:
        file_version: VersionInfo | None = None
        vfile = os.path.join(project_path, version_file)
        if os.path.isfile(vfile) and not os.path.islink(vfile):
            try:
                if version_file.endswith(".json"):
                    with open(vfile, "r") as f:
                        data = json.load(f)
                    raw = data.get("version", "")
                    if raw:
                        file_version = VersionInfo.parse(str(raw).strip().lstrip("v"))
                else:
                    with open(vfile, "r") as f:
                        content = f.read()
                    match = re.search(version_pattern, content)
                    if match:
                        file_version = VersionInfo(int(match.group(1)), int(match.group(2)), int(match.group(3)))
            except (OSError, ValueError):
                file_version = None
        tag_version: VersionInfo | None = None
        tag = self._get_latest_tag(project_path)
        if tag:
            try:
                last = tag.strip().split("/")[-1].strip()
                if last.lower().startswith("release-"):
                    last = last[len("release-"):]
                if last.lower().startswith("release"):
                    last = last[len("release"):].lstrip("-_v")
                last = last.lstrip("vV")
                tag_version = VersionInfo.parse(last)
            except ValueError:
                match = re.search(r"(\d+)\.(\d+)\.(\d+)", tag)
                if match:
                    tag_version = VersionInfo(int(match.group(1)), int(match.group(2)), int(match.group(3)))
                else:
                    tag_version = None
        if file_version and tag_version:
            return self.max_version(file_version, tag_version)
        if file_version:
            return file_version
        if tag_version:
            return tag_version
        return VersionInfo(0, 1, 0)

    def write_version_file(self, project_path: str, version: VersionInfo, version_file: str = "version.json") -> str:
        vfile = os.path.join(project_path, version_file)
        if os.path.islink(vfile):
            raise OSError(f"Symlink rejected: {vfile}")
        if version_file.endswith(".json"):
            with open(vfile, "w") as f:
                json.dump({"version": str(version)}, f, indent=2)
        elif version_file.endswith(".py"):
            with open(vfile, "r") as f:
                content = f.read()
            content = re.sub(
                r'__version__\s*=\s*"(\d+)\.(\d+)\.(\d+)"',
                f'__version__ = "{version}"',
                content,
            )
            with open(vfile, "w") as f:
                f.write(content)
        elif version_file.endswith(".toml"):
            with open(vfile, "r") as f:
                content = f.read()
            new_content, n = re.subn(
                r'version\s*=\s*"(\d+)\.(\d+)\.(\d+)"',
                f'version = "{version}"',
                content,
                count=1,
            )
            if n == 0:
                raise ValueError(f"No version found in {version_file}")
            with open(vfile, "w") as f:
                f.write(new_content)
        else:
            with open(vfile, "r") as f:
                content = f.read()
            new_content, n = re.subn(
                r"(\d+)\.(\d+)\.(\d+)",
                str(version),
                content,
                count=1,
            )
            if n == 0:
                raise ValueError(f"No version found in {version_file}")
            with open(vfile, "w") as f:
                f.write(new_content)
        return vfile

    def determine_bump(self, commit_type: CommitType) -> Optional[str]:
        return commit_type.bump_strategy()

    def calculate_next_version(self, current: VersionInfo, strategy: Optional[str]) -> VersionInfo:
        return current.bump(strategy)

    @staticmethod
    def is_valid_version(version_str: str) -> bool:
        pattern = r"^\d+\.\d+\.\d+$"
        return bool(re.match(pattern, version_str.strip()))

    def _get_latest_tag(self, project_path: str) -> Optional[str]:
        import subprocess
        try:
            result = subprocess.run(
                ["git", "-C", project_path, "describe", "--tags", "--abbrev=0"],
                capture_output=True,
                text=True,
                check=False,
            )
            if result.returncode == 0:
                return result.stdout.strip()
        except (subprocess.SubprocessError, FileNotFoundError):
            pass
        return None
