from __future__ import annotations

import os
import subprocess
import tempfile
from abc import ABC, abstractmethod
from typing import ClassVar

from deploynator._config import Config
from deploynator._models import Platform, ReleaseInfo


class PlatformClient(ABC):
    def __init__(self, config: Config) -> None:
        self._config = config

    @abstractmethod
    def name(self) -> str:
        ...

    @abstractmethod
    def is_available(self) -> bool:
        ...

    @abstractmethod
    def is_authenticated(self) -> bool:
        ...

    @abstractmethod
    def create_release(self, repo: str, release: ReleaseInfo) -> bool:
        ...

    @abstractmethod
    def create_pull_request(self, repo: str, title: str, body: str, head: str, base: str) -> str | None:
        ...

    @abstractmethod
    def push_changes(self, repo_path: str, remote: str, branch: str, tags: bool) -> bool:
        ...

    def upload_release_assets(self, repo: str, version: str, assets: list[str]) -> bool:
        """Sube ficheros como assets del release. Default: no soportado."""
        return False

    def _run(self, cmd: list[str], cwd: str | None = None, check: bool = False) -> subprocess.CompletedProcess:
        try:
            return subprocess.run(cmd, capture_output=True, text=True, check=check, cwd=cwd)
        except subprocess.SubprocessError as exc:
            raise RuntimeError(f"Command failed: {' '.join(cmd)}: {exc}") from exc


class GitHubCLI(PlatformClient):
    def name(self) -> str:
        return "github"

    def is_available(self) -> bool:
        try:
            result = self._run([self._config.gh_cli, "--version"], check=False)
            return result.returncode == 0
        except (FileNotFoundError, RuntimeError):
            return False

    def is_authenticated(self) -> bool:
        try:
            result = self._run([self._config.gh_cli, "auth", "status"], check=False)
            return result.returncode == 0 or self._config.gh_authd
        except (FileNotFoundError, RuntimeError):
            return False

    def create_release(self, repo: str, release: ReleaseInfo) -> bool:
        cmd = [
            self._config.gh_cli, "release", "create", release.version,
            "--repo", repo,
            "--title", release.title,
            "--target", release.target_branch,
        ]
        if release.prerelease:
            cmd.append("--prerelease")
        if release.draft:
            cmd.append("--draft")
        if release.notes:
            with tempfile.NamedTemporaryFile(mode="w", suffix=".md", delete=False) as nf:
                nf.write(release.notes[:self._config.max_release_chars])
                notes_file = nf.name
            cmd.extend(["--notes-file", notes_file])
            try:
                result = self._run(cmd, check=False)
                return result.returncode == 0
            finally:
                os.unlink(notes_file)
        result = self._run(cmd, check=False)
        return result.returncode == 0

    def create_pull_request(self, repo: str, title: str, body: str, head: str, base: str) -> str | None:
        cmd = [
            self._config.gh_cli, "pr", "create",
            "--repo", repo,
            "--title", title,
            "--body", body,
            "--head", head,
            "--base", base,
        ]
        result = self._run(cmd, check=False)
        if result.returncode == 0:
            return result.stdout.strip()
        return None

    def upload_release_assets(self, repo: str, version: str, assets: list[str]) -> bool:
        """`gh release upload <tag> <files> --repo <repo> --clobber` (shell=False)."""
        files = [a for a in assets if a and os.path.isfile(a) and not os.path.islink(a)]
        if not files:
            return False
        cmd = [
            self._config.gh_cli, "release", "upload", version,
            *files,
            "--repo", repo,
            "--clobber",
        ]
        try:
            result = self._run(cmd, check=False)
            return result.returncode == 0
        except (FileNotFoundError, RuntimeError):
            return False

    def push_changes(self, repo_path: str, remote: str, branch: str, tags: bool) -> bool:
        cmd = ["git", "-C", repo_path, "push", remote, branch]
        if tags:
            cmd.append("--follow-tags")
        result = self._run(cmd, check=False)
        return result.returncode == 0


class GitLabCLI(PlatformClient):
    def name(self) -> str:
        return "gitlab"

    def is_available(self) -> bool:
        try:
            result = self._run([self._config.glab_cli, "--version"], check=False)
            return result.returncode == 0
        except (FileNotFoundError, RuntimeError):
            return False

    def is_authenticated(self) -> bool:
        try:
            result = self._run([self._config.glab_cli, "auth", "status"], check=False)
            return result.returncode == 0 or self._config.glab_authd
        except (FileNotFoundError, RuntimeError):
            return False

    def create_release(self, repo: str, release: ReleaseInfo) -> bool:
        cmd = [
            self._config.glab_cli, "release", "create", release.version,
            "--repo", repo,
            "--name", release.title,
        ]
        if release.notes:
            cmd.extend(["--description", release.notes[:self._config.max_release_chars]])
        result = self._run(cmd, check=False)
        return result.returncode == 0

    def create_pull_request(self, repo: str, title: str, body: str, head: str, base: str) -> str | None:
        cmd = [
            self._config.glab_cli, "mr", "create",
            "--repo", repo,
            "--title", title,
            "--description", body,
            "--source-branch", head,
            "--target-branch", base,
        ]
        result = self._run(cmd, check=False)
        if result.returncode == 0:
            return result.stdout.strip()
        return None

    def push_changes(self, repo_path: str, remote: str, branch: str, tags: bool) -> bool:
        cmd = ["git", "-C", repo_path, "push", remote, branch]
        if tags:
            cmd.append("--follow-tags")
        result = self._run(cmd, check=False)
        return result.returncode == 0


class BitbucketCLI(PlatformClient):
    def name(self) -> str:
        return "bitbucket"

    def is_available(self) -> bool:
        for candidate in [self._config.bb_cli, "bitbucket", "atlassian"]:
            try:
                result = self._run([candidate, "--version"], check=False)
                if result.returncode == 0:
                    return True
            except (FileNotFoundError, RuntimeError):
                continue
        return False

    def is_authenticated(self) -> bool:
        return self._config.bb_authd

    def create_release(self, repo: str, release: ReleaseInfo) -> bool:
        cmd = [
            self._config.bb_cli, "release", "create",
            "--repo", repo,
            "--tag", release.version,
            "--title", release.title,
        ]
        if release.notes:
            with tempfile.NamedTemporaryFile(mode="w", suffix=".md", delete=False) as nf:
                nf.write(release.notes[:self._config.max_release_chars])
                notes_file = nf.name
            cmd.extend(["--description-file", notes_file])
            try:
                result = self._run(cmd, check=False)
                return result.returncode == 0
            finally:
                os.unlink(notes_file)
        result = self._run(cmd, check=False)
        return result.returncode == 0

    def create_pull_request(self, repo: str, title: str, body: str, head: str, base: str) -> str | None:
        cmd = [
            self._config.bb_cli, "pr", "create",
            "--repo", repo,
            "--title", title,
            "--description", body,
            "--source", head,
            "--destination", base,
        ]
        result = self._run(cmd, check=False)
        if result.returncode == 0:
            return result.stdout.strip()
        return None

    def push_changes(self, repo_path: str, remote: str, branch: str, tags: bool) -> bool:
        cmd = ["git", "-C", repo_path, "push", remote, branch]
        if tags:
            cmd.append("--follow-tags")
        result = self._run(cmd, check=False)
        return result.returncode == 0


class PlatformFactory:
    _registry: ClassVar[dict[Platform, type[PlatformClient]]] = {
        Platform.GITHUB: GitHubCLI,
        Platform.GITLAB: GitLabCLI,
        Platform.BITBUCKET: BitbucketCLI,
    }

    @classmethod
    def register(cls, platform: Platform, client_class: type[PlatformClient]) -> None:
        cls._registry[platform] = client_class

    @classmethod
    def create(cls, platform: Platform, config: Config) -> PlatformClient:
        client_class = cls._registry.get(platform)
        if not client_class:
            raise ValueError(f"No client registered for platform: {platform}")
        return client_class(config)

    @classmethod
    def create_all_available(cls, config: Config) -> list[PlatformClient]:
        clients = []
        for client_class in cls._registry.values():
            try:
                client = client_class(config)
                if client.is_available():
                    clients.append(client)
            except (FileNotFoundError, RuntimeError):
                continue
        return clients
