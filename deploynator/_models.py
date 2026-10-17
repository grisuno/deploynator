from __future__ import annotations

import re
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum, auto


class Platform(Enum):
    GITHUB = auto()
    GITLAB = auto()
    BITBUCKET = auto()

    @classmethod
    def from_string(cls, name: str) -> Platform:
        mapping = {
            "github": cls.GITHUB,
            "gitlab": cls.GITLAB,
            "bitbucket": cls.BITBUCKET,
        }
        normalized = name.strip().lower()
        if normalized not in mapping:
            raise ValueError(f"Unknown platform: {name}. Valid: {list(mapping.keys())}")
        return mapping[normalized]

    def label(self) -> str:
        return self.name.lower()

    def cli_name(self) -> str:
        return {
            Platform.GITHUB: "gh",
            Platform.GITLAB: "glab",
            Platform.BITBUCKET: "bb",
        }[self]

    def auth_env_var(self) -> str:
        return {
            Platform.GITHUB: "GITHUB_TOKEN",
            Platform.GITLAB: "GITLAB_TOKEN",
            Platform.BITBUCKET: "BITBUCKET_TOKEN",
        }[self]


class CommitType(Enum):
    FEAT = "feat"
    FIX = "fix"
    HOTFIX = "hotfix"
    DOCS = "docs"
    REFACTOR = "refactor"
    STYLE = "style"
    CHORE = "chore"
    TEST = "test"
    RELEASE = "release"
    PATCH = "patch"

    @classmethod
    def from_string(cls, value: str) -> CommitType:
        for member in cls:
            if member.value == value.lower():
                return member
        raise ValueError(f"Unknown commit type: {value}")

    @classmethod
    def valid_types(cls) -> list[str]:
        return [m.value for m in cls]

    def bump_strategy(self) -> str | None:
        return {
            CommitType.FEAT: "minor",
            CommitType.FIX: "patch",
            CommitType.HOTFIX: "patch",
            CommitType.DOCS: None,
            CommitType.REFACTOR: None,
            CommitType.STYLE: None,
            CommitType.CHORE: None,
            CommitType.TEST: None,
            CommitType.RELEASE: "major",
            CommitType.PATCH: "patch",
        }[self]

    def section_header(self) -> str:
        return {
            CommitType.FEAT: "Features",
            CommitType.FIX: "Bug Fixes",
            CommitType.HOTFIX: "Hotfixes",
            CommitType.DOCS: "Documentation",
            CommitType.REFACTOR: "Code Refactoring",
            CommitType.STYLE: "Style Changes",
            CommitType.CHORE: "Chores",
            CommitType.TEST: "Tests",
            CommitType.RELEASE: "Releases",
            CommitType.PATCH: "Patches",
        }[self]


@dataclass(frozen=True)
class PlatformConfig:
    platform: Platform
    repo: str
    enabled: bool = True
    auth_env: str | None = None

    @classmethod
    def from_dict(cls, data: dict) -> PlatformConfig:
        return cls(
            platform=Platform.from_string(data.get("platform", "")),
            repo=data.get("repo", ""),
            enabled=data.get("enabled", True),
            auth_env=data.get("auth_env"),
        )


@dataclass(frozen=True)
class VersionConfig:
    file: str = "version.json"
    file_type: str = "json"
    pattern: str = r"(\d+)\.(\d+)\.(\d+)"

    @classmethod
    def from_dict(cls, data: dict) -> VersionConfig:
        return cls(
            file=data.get("file", "version.json"),
            file_type=data.get("file_type", "json"),
            pattern=data.get("pattern", r"(\d+)\.(\d+)\.(\d+)"),
        )


@dataclass(frozen=True)
class ProjectConfig:
    name: str
    description: str = ""
    platforms: list[PlatformConfig] = field(default_factory=list)
    version: VersionConfig = field(default_factory=VersionConfig)
    path: str = ""
    repo_url: str = ""

    @classmethod
    def from_dict(cls, data: dict) -> ProjectConfig:
        platforms_raw = data.get("platforms", {})
        platforms = []
        for pname, pinfo in platforms_raw.items():
            if isinstance(pinfo, dict):
                platforms.append(
                    PlatformConfig(
                        platform=Platform.from_string(pname),
                        repo=pinfo.get("repo", ""),
                        enabled=pinfo.get("enabled", True),
                        auth_env=pinfo.get("auth_env"),
                    )
                )
            elif isinstance(pinfo, str):
                platforms.append(
                    PlatformConfig(
                        platform=Platform.from_string(pname),
                        repo=pinfo,
                    )
                )
        version_raw = data.get("version", {})
        if isinstance(version_raw, dict):
            version = VersionConfig.from_dict(version_raw)
        else:
            version = VersionConfig()
        return cls(
            name=data.get("name", ""),
            description=data.get("description", ""),
            platforms=platforms,
            version=version,
            path=data.get("path", ""),
            repo_url=data.get("repo_url", ""),
        )


@dataclass(frozen=True)
class CommitMessage:
    commit_type: CommitType
    scope: str
    subject: str
    body: str = ""
    footer: str = ""
    version: str = ""

    def format(self) -> str:
        scope_part = f"({self.scope})" if self.scope else ""
        lines = [f"{self.commit_type.value}{scope_part}: {self.subject}"]
        if self.version:
            lines.append(f"\nVersion: {self.version}")
        if self.body:
            lines.append(f"\n{self.body}")
        if self.footer:
            lines.append(f"\n{self.footer}")
        return "\n".join(lines)

    @classmethod
    def parse(cls, raw: str) -> CommitMessage:
        pattern = r"^(feat|fix|hotfix|docs|refactor|style|chore|test|release|patch)(\(([^)]*)\))?:\s(.+)$"
        match = re.match(pattern, raw.strip())
        if not match:
            raise ValueError(f"Cannot parse commit message: {raw}")
        return cls(
            commit_type=CommitType.from_string(match.group(1)),
            scope=match.group(3) or "",
            subject=match.group(4),
        )


@dataclass(frozen=True)
class VersionInfo:
    major: int
    minor: int
    patch: int

    def __str__(self) -> str:
        return f"{self.major}.{self.minor}.{self.patch}"

    @classmethod
    def parse(cls, version_str: str) -> VersionInfo:
        pattern = r"^(\d+)\.(\d+)\.(\d+)$"
        match = re.match(pattern, version_str.strip())
        if not match:
            raise ValueError(f"Invalid version string: {version_str}")
        return cls(
            major=int(match.group(1)),
            minor=int(match.group(2)),
            patch=int(match.group(3)),
        )

    def bump(self, strategy: str | None) -> VersionInfo:
        if strategy == "major":
            return VersionInfo(self.major + 1, 0, 0)
        elif strategy == "minor":
            return VersionInfo(self.major, self.minor + 1, 0)
        elif strategy == "patch":
            return VersionInfo(self.major, self.minor, self.patch + 1)
        return self


@dataclass(frozen=True)
class ChangelogEntry:
    commit_type: CommitType
    message: str
    author: str = ""
    date: datetime = field(default_factory=datetime.now)
    sha: str = ""

    @classmethod
    def from_git_log_line(cls, line: str, author: str = "", sha: str = "") -> ChangelogEntry:
        try:
            parsed = CommitMessage.parse(line)
            return cls(
                commit_type=parsed.commit_type,
                message=line,
                author=author,
                sha=sha,
            )
        except ValueError:
            return cls(
                commit_type=CommitType.CHORE,
                message=line,
                author=author,
                sha=sha,
            )


@dataclass(frozen=True)
class ReleaseInfo:
    version: str
    title: str
    notes: str
    target_branch: str = "main"
    prerelease: bool = False
    draft: bool = False


@dataclass
class DeployResult:
    project: str
    version: str
    success: bool
    platforms_pushed: list[str] = field(default_factory=list)
    releases_created: list[str] = field(default_factory=list)
    error: str | None = None
