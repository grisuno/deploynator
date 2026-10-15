from __future__ import annotations

import os
from dataclasses import dataclass, field


@dataclass(frozen=True)
class Config:
    changelog_file: str = "CHANGELOG.md"
    changelog_html: str = "docs/CHANGELOG.html"
    version_file: str = "version.json"
    readme_file: str = "README.md"
    knowledge_base: str = "KNOWLEDGE_BASE.md"

    projects_dir: str = "projects"
    modules_dir: str = "modules"
    workflows_dir: str = ".github/workflows"

    default_branch: str = "main"
    default_remote: str = "origin"
    release_branch: str = "main"

    max_release_chars: int = 120000
    max_file_size_bytes: int = 10_485_760
    max_dir_depth: int = 20

    changelog_header: str = "# Changelog"

    deploynator_badge_url: str = "https://github.com/grisuno/deploynator"
    deploynator_badge_text: str = "Deployed with deploynator"

    lazygit_config_key: str = "deploynator.lazygit.enabled"

    gh_cli: str = "gh"
    glab_cli: str = "glab"
    bb_cli: str = "bb"
    lazygit_cli: str = "lazygit"
    jq_cli: str = "jq"
    pandoc_cli: str = "pandoc"
    sponge_cli: str = "sponge"

    gpg_signing_key_env: str = "GPG_SIGNING_KEY"
    github_token_env: str = "GITHUB_TOKEN"
    gitlab_token_env: str = "GITLAB_TOKEN"
    bitbucket_token_env: str = "BITBUCKET_TOKEN"

    semver_pattern: str = r"^\d+\.\d+\.\d+$"
    commit_type_pattern: str = r"^(feat|fix|hotfix|docs|refactor|style|chore|test|release|patch)(\(.+\))?: .+"

    _path: str = field(default="", compare=False)

    conventional_types: dict[str, str] = field(default_factory=lambda: {
        "feat": "Features",
        "fix": "Bug Fixes",
        "hotfix": "Hotfixes",
        "docs": "Documentation",
        "refactor": "Code Refactoring",
        "style": "Style Changes",
        "chore": "Chores",
        "test": "Tests",
        "release": "Releases",
        "patch": "Patches",
    })

    version_bump_map: dict[str, str] = field(default_factory=lambda: {
        "feat": "minor",
        "fix": "patch",
        "hotfix": "patch",
        "docs": None,
        "refactor": None,
        "style": None,
        "chore": None,
        "test": None,
        "release": "major",
        "patch": "patch",
    })

    @staticmethod
    def create(overrides: dict | None = None) -> Config:
        base = Config()
        if not overrides:
            return base
        return Config(**{**{f.name: getattr(base, f.name) for f in Config.__dataclass_fields__.values()}, **overrides})

    def resolve_path(self, *parts: str) -> str:
        if self._path:
            return os.path.join(self._path, *parts)
        return os.path.join(*parts)

    @property
    def gh_authd(self) -> bool:
        return os.environ.get(self.github_token_env) is not None

    @property
    def glab_authd(self) -> bool:
        return os.environ.get(self.gitlab_token_env) is not None

    @property
    def bb_authd(self) -> bool:
        return os.environ.get(self.bitbucket_token_env) is not None
