from __future__ import annotations

import os
import shutil
import subprocess
import tempfile
from typing import Optional

from deploynator._config import Config
from deploynator._models import (
    Platform,
    PlatformConfig,
    ProjectConfig,
    CommitType,
    CommitMessage,
    VersionInfo,
    ReleaseInfo,
    DeployResult,
    ChangelogEntry,
)
from deploynator._git import GitOperations
from deploynator._semver import SemverManager
from deploynator._changelog import ChangelogGenerator
from deploynator._platforms import PlatformFactory, PlatformClient
from deploynator._toml import load_toml_config
from deploynator._runner import TestRunner
from deploynator._docs import DocsRunner
from deploynator._pypi import PyPIRunner


class ProjectDiscovery:
    def __init__(self, config: Config) -> None:
        self._config = config

    def discover(self, search_path: str = "") -> list[ProjectConfig]:
        base = search_path or self._config._path or os.getcwd()
        projects_dir = os.path.join(base, self._config.projects_dir)

        if not os.path.isdir(projects_dir):
            project_yaml = os.path.join(base, "deploynator.yaml")
            if os.path.isfile(project_yaml):
                return [self._load_single(project_yaml)]
            return []

        projects = []
        for entry in sorted(os.listdir(projects_dir)):
            if entry.endswith((".yaml", ".yml")):
                yaml_path = os.path.join(projects_dir, entry)
                try:
                    project = self._load_single(yaml_path)
                    projects.append(project)
                except (ValueError, KeyError, OSError) as exc:
                    continue
        return projects

    def find_by_name(self, name: str, search_path: str = "") -> Optional[ProjectConfig]:
        for project in self.discover(search_path):
            if project.name == name:
                return project
        return None

    @staticmethod
    def _load_single(yaml_path: str) -> ProjectConfig:
        import yaml
        if os.path.islink(yaml_path):
            raise ValueError(f"Symlink rejected: {yaml_path}")
        if os.path.getsize(yaml_path) > Config.create().max_file_size_bytes:
            raise ValueError(f"File too large: {yaml_path}")
        with open(yaml_path, "r") as f:
            data = yaml.safe_load(f)
        if not data or "name" not in data:
            raise ValueError(f"Invalid project config: {yaml_path}")
        return ProjectConfig.from_dict(data)


class DeployOrchestrator:
    def __init__(self, config: Config) -> None:
        self._config = config
        self._git = GitOperations(config)
        self._semver = SemverManager(config)
        self._changelog = ChangelogGenerator(config)
        self._discovery = ProjectDiscovery(config)
        self._tests = TestRunner(config)
        self._docs = DocsRunner(config)
        self._pypi = PyPIRunner(config)

    @staticmethod
    def _resolve_project_path(project: ProjectConfig) -> str:
        if not project.path:
            return os.getcwd()
        if os.path.isabs(project.path):
            return project.path
        base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        resolved = os.path.join(base, project.path)
        return os.path.abspath(resolved)

    def deploy(
        self,
        project: ProjectConfig,
        commit_type: CommitType,
        subject: str,
        scope: str = "",
        body: str = "",
        dry_run: bool = False,
        platforms_override: Optional[list[Platform]] = None,
        run_tests: bool = True,
        run_docs: bool = True,
        force_bump: Optional[str] = None,
        run_pypi: bool = True,
    ) -> DeployResult:
        repo_path = self._resolve_project_path(project)

        if force_bump not in (None, "", "major", "minor", "patch"):
            return DeployResult(
                project=project.name,
                version="",
                success=False,
                error=f"Invalid bump: {force_bump}. Valid: major, minor, patch",
            )

        try:
            toml_cfg = load_toml_config(repo_path)
        except ValueError as exc:
            return DeployResult(
                project=project.name,
                version="",
                success=False,
                error=f"Invalid deploynator.toml: {exc}",
            )

        if dry_run:
            print(f"[DRY-RUN] Would deploy {project.name} with type={commit_type.value}")
            if run_tests:
                print(f"[DRY-RUN] Would run tests: {toml_cfg.test_commands}")
            if run_docs:
                print(f"[DRY-RUN] Would run docs: {toml_cfg.docs_command}")

        current_version = self._semver.get_current_version(repo_path, project.version.file, project.version.pattern)
        strategy = force_bump or self._semver.determine_bump(commit_type)
        new_version = self._semver.calculate_next_version(current_version, strategy)

        if run_tests and not dry_run:
            ok, output = self._tests.run(repo_path, toml_cfg)
            if not ok:
                return DeployResult(
                    project=project.name,
                    version=str(new_version),
                    success=False,
                    error=f"Tests failed: {output[:2000]}",
                )
            print(f"[+] tests passed for {project.name}")

        if run_docs and not dry_run:
            docs_ok = self._docs.run(repo_path, toml_cfg)
            if not docs_ok:
                print(f"[!] docs step failed for {project.name}, continuing deploy")

        if not dry_run and not self._git.has_remote(repo_path):
            return DeployResult(
                project=project.name,
                version=str(new_version),
                success=False,
                error="No git remote configured",
            )

        start_ref = self._git.get_start_ref(repo_path)
        if not start_ref:
            return DeployResult(
                project=project.name,
                version=str(new_version),
                success=False,
                error="No starting ref (tag or initial commit) found",
            )

        if not dry_run:
            self._semver.write_version_file(repo_path, new_version, project.version.file)
            self._git.add_all(repo_path)

        changelog_content = self._changelog.generate_from_log(repo_path, start_ref)

        changed_files = self._git.get_changed_files(repo_path, start_ref)
        listfiles_parts = []
        if changed_files["modified"]:
            listfiles_parts.append("Modified file(s):\n" + "\n".join(f"- {f}" for f in changed_files["modified"]))
        if changed_files["deleted"]:
            listfiles_parts.append("Deleted file(s):\n" + "\n".join(f"- {f}" for f in changed_files["deleted"]))
        if changed_files["created"]:
            listfiles_parts.append("Created file(s):\n" + "\n".join(f"- {f}" for f in changed_files["created"]))
        listfiles_str = "\n".join(listfiles_parts)

        footer = (
            f"Deployed with deploynator ({self._config.deploynator_badge_url})\n"
            f"Platforms: {', '.join(p.platform.label() for p in project.platforms if p.enabled)}"
        )

        commit_msg = CommitMessage(
            commit_type=commit_type,
            scope=scope,
            subject=subject,
            body=body,
            footer=f"{footer}\n\n{listfiles_str}",
            version=str(new_version),
        )

        if not dry_run:
            self._changelog.write_changelog(repo_path, changelog_content)
            self._git.add_all(repo_path)

            ok_commit, commit_err = self._git.commit(repo_path, commit_msg.format())
            if not ok_commit:
                return DeployResult(
                    project=project.name,
                    version=str(new_version),
                    success=False,
                    error=f"Commit failed: {commit_err}",
                )

            tag_name = str(new_version)
            while self._git.tag_exists(repo_path, tag_name):
                current_ver = VersionInfo.parse(tag_name)
                tag_name = str(VersionInfo(current_ver.major, current_ver.minor, current_ver.patch + 1))

            if not self._git.tag(repo_path, tag_name, f"Version {tag_name}"):
                return DeployResult(
                    project=project.name,
                    version=tag_name,
                    success=False,
                    error="Tag creation failed",
                )

            new_version_str = tag_name
        else:
            new_version_str = str(new_version)

        platforms_to_deploy: list[PlatformConfig] = []
        for pc in project.platforms:
            if platforms_override and pc.platform not in platforms_override:
                continue
            if pc.enabled:
                platforms_to_deploy.append(pc)

        platforms_pushed = []
        releases_created = []
        overall_success = True

        if not platforms_to_deploy and dry_run:
            print(f"[DRY-RUN] Would push to {toml_cfg.deploy_remote}/"
                  f"{self._git.current_branch(repo_path) or toml_cfg.deploy_branch} --follow-tags")

        if not platforms_to_deploy and not dry_run:
            # Sin plataformas (ej. deploy por ruta): fallback estilo DEPLOY.sh —
            # push al remoto propio + release con gh si disponible.
            branch = self._git.current_branch(repo_path) or toml_cfg.deploy_branch
            if self._git.push(repo_path, toml_cfg.deploy_remote, branch):
                platforms_pushed.append(f"{toml_cfg.deploy_remote}/{branch}")
            else:
                overall_success = False
            release_notes = self._changelog.format_for_release(changelog_content)
            if self._gh_release_in_repo(repo_path, project.name, new_version_str,
                                        release_notes, branch):
                releases_created.append("github")

        for pc in platforms_to_deploy:
            if dry_run:
                print(f"[DRY-RUN] Would push to {pc.platform.label()}/{pc.repo}")
                platforms_pushed.append(pc.platform.label())
                continue

            try:
                client = PlatformFactory.create(pc.platform, self._config)
            except ValueError:
                overall_success = False
                continue

            if not client.is_authenticated():
                print(f"[!] {pc.platform.label()} not authenticated. Skipping.")
                continue

            remote_url = self._get_remote_url(repo_path, pc)
            branch = self._git.current_branch(repo_path) or self._config.default_branch

            if remote_url:
                temp_remote = f"deploynator-{pc.platform.name}"
                self._add_temp_remote(repo_path, temp_remote, remote_url)
                push_ok = self._git.push(repo_path, temp_remote, branch)
                self._remove_temp_remote(repo_path, temp_remote)
            else:
                push_ok = self._git.push(repo_path, self._config.default_remote, branch)

            if push_ok:
                platforms_pushed.append(pc.platform.label())
            else:
                overall_success = False
                continue

            release_notes = self._changelog.format_for_release(changelog_content)
            release = ReleaseInfo(
                version=new_version_str,
                title=f"{project.name} {new_version_str}",
                notes=release_notes,
                target_branch=self._config.release_branch,
            )

            if client.create_release(pc.repo, release):
                releases_created.append(pc.platform.label())
            else:
                overall_success = False

        if run_pypi and toml_cfg.pypi_enabled and self._pypi.is_packaging_project(repo_path):
            if dry_run:
                print(f"[DRY-RUN] Would build+upload to PyPI ({toml_cfg.pypi_repo}) version {new_version_str}")
            elif not self._pypi.has_credentials():
                token = self._pypi.prompt_for_credentials()
                if not token:
                    print("[!] PyPI packaging detected but no credentials "
                          "(TWINE_PASSWORD/PYPI_TOKEN/~/.pypirc). Skipping upload.")
                else:
                    ok, msg = self._pypi.run(repo_path, toml_cfg, new_version_str, token=token)
                    print(f"[{'OK' if ok else 'FAIL'}] {msg}")
                    if not ok:
                        return DeployResult(
                            project=project.name,
                            version=new_version_str,
                            success=False,
                            platforms_pushed=platforms_pushed,
                            releases_created=releases_created,
                            error=msg[:2000],
                        )
            else:
                ok, msg = self._pypi.run(repo_path, toml_cfg, new_version_str)
                print(f"[{'OK' if ok else 'FAIL'}] {msg}")
                if not ok:
                    return DeployResult(
                        project=project.name,
                        version=new_version_str,
                        success=False,
                        platforms_pushed=platforms_pushed,
                        releases_created=releases_created,
                        error=msg[:2000],
                    )

        return DeployResult(
            project=project.name,
            version=new_version_str,
            success=overall_success,
            platforms_pushed=platforms_pushed,
            releases_created=releases_created,
            error=None if overall_success else "Some platforms failed",
        )

    def _gh_release_in_repo(self, repo_path: str, project_name: str, version: str,
                            notes: str, branch: str) -> bool:
        """Best-effort `gh release create` inferring repo from origin. Never raises."""
        if shutil.which(self._config.gh_cli) is None:
            print("[!] gh CLI not found. Push done, create the release manually.")
            return False
        notes_file: Optional[str] = None
        try:
            with tempfile.NamedTemporaryFile(mode="w", suffix=".md", delete=False) as nf:
                nf.write(notes[:self._config.max_release_chars])
                notes_file = nf.name
            result = subprocess.run(
                [self._config.gh_cli, "release", "create", version,
                 "--title", f"{project_name} {version}",
                 "--notes-file", notes_file,
                 "--target", branch],
                cwd=repo_path,
                capture_output=True, text=True, check=False,
            )
            if result.returncode != 0:
                print(f"[!] gh release failed: {(result.stderr or result.stdout).strip()[:300]}")
                return False
            return True
        except (subprocess.SubprocessError, OSError) as exc:
            print(f"[!] gh release failed: {exc}")
            return False
        finally:
            if notes_file:
                try:
                    os.unlink(notes_file)
                except OSError:
                    pass

    def _add_temp_remote(self, repo_path: str, name: str, url: str) -> None:
        try:
            subprocess.run(
                ["git", "-C", repo_path, "remote", "add", name, url],
                capture_output=True, text=True, check=False,
            )
        except FileNotFoundError:
            pass

    def _remove_temp_remote(self, repo_path: str, name: str) -> None:
        try:
            subprocess.run(
                ["git", "-C", repo_path, "remote", "remove", name],
                capture_output=True, text=True, check=False,
            )
        except FileNotFoundError:
            pass

    @staticmethod
    def _get_remote_url(repo_path: str, pc: PlatformConfig) -> Optional[str]:
        if pc.platform == Platform.GITHUB:
            return f"https://github.com/{pc.repo}.git"
        elif pc.platform == Platform.GITLAB:
            return f"https://gitlab.com/{pc.repo}.git"
        elif pc.platform == Platform.BITBUCKET:
            return f"https://bitbucket.org/{pc.repo}.git"
        return None

    def generate_workflows(self, project: ProjectConfig, output_dir: str = ".github/workflows") -> list[str]:
        created = []
        base_dir = os.path.join(project.path or os.getcwd(), output_dir)
        os.makedirs(base_dir, exist_ok=True)

        ci_yml = os.path.join(base_dir, "deploynator-ci.yml")
        if not os.path.isfile(ci_yml):
            with open(ci_yml, "w") as f:
                f.write(self._ci_workflow_content(project))
            created.append(ci_yml)

        release_yml = os.path.join(base_dir, "deploynator-release.yml")
        if not os.path.isfile(release_yml):
            with open(release_yml, "w") as f:
                f.write(self._release_workflow_content(project))
            created.append(release_yml)

        return created

    def _ci_workflow_content(self, project: ProjectConfig) -> str:
        return f"""name: deploynator CI

on:
  push:
    branches: ["**"]
  pull_request:
    branches: [main]

jobs:
  quality:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Run deploynator docs
        run: |
          pip install readmenator
          python -m readmenator .
        continue-on-error: true
"""

    def _release_workflow_content(self, project: ProjectConfig) -> str:
        platforms_gh = any(p.platform == Platform.GITHUB for p in project.platforms if p.enabled)
        return f"""name: deploynator Release

on:
  push:
    tags: ["v*"]

jobs:
  release:
    runs-on: ubuntu-latest
    permissions:
      contents: write
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0
      - name: Generate changelog
        run: |
          echo "# Changelog" > CHANGELOG.md
          git log --pretty=format:"%s" $(git describe --tags --abbrev=0 HEAD^^ 2>/dev/null || git rev-list --max-parents=0 HEAD)..HEAD >> CHANGELOG.md || true
      - name: Create Release
        uses: softprops/action-gh-release@v2
        with:
          body_path: CHANGELOG.md
          generate_release_notes: true
"""

    def install_dependencies(self, project: ProjectConfig) -> dict[str, bool]:
        status = {}
        for pc in project.platforms:
            if not pc.enabled:
                continue
            client = PlatformFactory.create(pc.platform, self._config)
            available = client.is_available()
            status[pc.platform.label()] = available
        return status

    def integrate_readmenator(self, project_path: str) -> bool:
        try:
            toml_cfg = load_toml_config(project_path)
        except ValueError:
            toml_cfg = None
        if toml_cfg is not None:
            return self._docs.run(project_path, toml_cfg)
        try:
            import readmenator
            result = subprocess.run(
                ["python", "-m", "readmenator", project_path, "--rebuild"],
                capture_output=True, text=True, check=False,
            )
            return result.returncode == 0
        except ImportError:
            for cmd in (
                ["pip", "install", "readmenator"],
                ["pip", "install", "--break-system-packages", "readmenator"],
                ["pip3", "install", "readmenator"],
                ["pip3", "install", "--break-system-packages", "readmenator"],
            ):
                try:
                    result = subprocess.run(cmd, capture_output=True, text=True, check=False)
                    if result.returncode == 0:
                        result = subprocess.run(
                            ["python", "-m", "readmenator", project_path, "--rebuild"],
                            capture_output=True, text=True, check=False,
                        )
                        return result.returncode == 0
                except FileNotFoundError:
                    continue
            print("[!] readmenator not available. Install: pip install readmenator")
            return False

    def install_lazygit(self) -> bool:
        try:
            result = subprocess.run(
                ["which", "lazygit"],
                capture_output=True, text=True, check=False,
            )
            if result.returncode == 0:
                return True
            install_methods = [
                ["brew", "install", "lazygit"],
                ["npm", "install", "-g", "lazygit"],
            ]
            for method in install_methods:
                try:
                    result = subprocess.run(method, capture_output=True, text=True, check=False)
                    if result.returncode == 0:
                        return True
                except FileNotFoundError:
                    continue
        except FileNotFoundError:
            pass
        return False
