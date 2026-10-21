from __future__ import annotations

import os
import shutil
import subprocess
import tempfile

from deploynator._changelog import ChangelogGenerator
from deploynator._config import Config
from deploynator._deb import DebRunner
from deploynator._docs import DocsRunner
from deploynator._git import GitOperations
from deploynator._models import (
    CommitMessage,
    CommitType,
    DeployResult,
    Platform,
    PlatformConfig,
    ProjectConfig,
    ReleaseInfo,
    VersionInfo,
)
from deploynator._platforms import PlatformFactory
from deploynator._pypi import PyPIRunner
from deploynator._receipt import (
    MODE_PLAN,
    MODE_RUN,
    ReceiptCollector,
    build_plan,
    build_receipt_from_result,
    default_receipt_path,
)
from deploynator._runner import TestRunner
from deploynator._semver import SemverManager
from deploynator._toml import load_toml_config


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
                except (ValueError, KeyError, OSError):
                    continue
        return projects

    def find_by_name(self, name: str, search_path: str = "") -> ProjectConfig | None:
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
        self._deb = DebRunner(config)

    @staticmethod
    def _resolve_project_path(project: ProjectConfig,
                              config: Config | None = None) -> str:
        if not project.path:
            return os.getcwd()
        if os.path.isabs(project.path):
            return project.path
        candidates: list[str] = []
        if config is not None:
            scan_base = getattr(config, "_path", "") or os.getcwd()
            candidates.append(os.path.join(scan_base, project.path))
        legacy_base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        candidates.append(os.path.join(legacy_base, project.path))
        for resolved in candidates:
            if os.path.isdir(resolved):
                return os.path.abspath(resolved)
        return os.path.abspath(candidates[-1])

    def deploy(
        self,
        project: ProjectConfig,
        commit_type: CommitType,
        subject: str,
        scope: str = "",
        body: str = "",
        dry_run: bool = False,
        platforms_override: list[Platform] | None = None,
        run_tests: bool = True,
        run_docs: bool = True,
        force_bump: str | None = None,
        run_pypi: bool = True,
        run_deb: bool = True,
        verbose: bool = False,
        receipt_path: str | None = None,
        trace: bool = False,
    ) -> DeployResult:
        collector = ReceiptCollector(
            project=project.name,
            mode=(MODE_RUN if not dry_run else MODE_PLAN),
            dry_run=dry_run,
            trace=trace,
            flags={
                "bump": force_bump or "",
                "no_test": not run_tests,
                "no_docs": not run_docs,
                "no_pypi": not run_pypi,
                "no_deb": not run_deb,
                "platforms": [p.label() for p in (platforms_override or [])],
                "verbose": verbose,
            },
            tail_chars=self._config.receipt_tail_chars,
        )
        self._collector = collector
        error = ""
        try:
            with collector.capture():
                result = self._deploy_impl(
                    project, commit_type, subject, scope, body, dry_run,
                    platforms_override, run_tests, run_docs, force_bump,
                    run_pypi, run_deb, verbose,
                )
        except Exception as exc:  # noqa: BLE001 -- contract boundary: receipt on crash
            error = f"{type(exc).__name__}: {exc}"
            result = DeployResult(
                project=project.name,
                version=collector.receipt.version_to or collector.receipt.version_from,
                success=False,
                error=error[:2000],
            )
        build_receipt_from_result(collector.receipt, result, error)
        collector.finalize(collector.receipt.status)
        written = None
        if trace or receipt_path is not None:
            target = receipt_path or default_receipt_path(
                os.getcwd(), result.project, collector.receipt.mode,
                collector.receipt.status, result.version or collector.receipt.version_from,
            )
            try:
                written = collector.write(target)
                print(f"[+] receipt: {written}")
            except (OSError, ValueError) as exc:
                print(f"[!] receipt write failed: {exc}")
        result.receipt_path = written
        return result

    def _deploy_impl(
        self,
        project: ProjectConfig,
        commit_type: CommitType,
        subject: str,
        scope: str = "",
        body: str = "",
        dry_run: bool = False,
        platforms_override: list[Platform] | None = None,
        run_tests: bool = True,
        run_docs: bool = True,
        force_bump: str | None = None,
        run_pypi: bool = True,
        run_deb: bool = True,
        verbose: bool = False,
    ) -> DeployResult:
        collector = getattr(self, "_collector", None)
        if collector is None:
            collector = ReceiptCollector(project=project.name, dry_run=dry_run)
            self._collector = collector
        repo_path = self._resolve_project_path(project, config=self._config)

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
            collector.mark_failure("toml_load", str(exc), "load_toml_config")
            return DeployResult(
                project=project.name,
                version="",
                success=False,
                error=f"Invalid deploynator.toml: {exc}",
            )

        if dry_run:
            _scope = f"({scope})" if scope else ""
            print(f"[DRY-RUN] Would deploy {project.name} with type={commit_type.value}")
            print(f"[DRY-RUN] Would commit: {commit_type.value}{_scope}: {subject}")
            if run_tests:
                print(f"[DRY-RUN] Would run tests: {toml_cfg.test_commands}")
            if run_docs:
                print(f"[DRY-RUN] Would run docs: {toml_cfg.docs_command}")

        current_version = self._semver.get_current_version(repo_path, project.version.file, project.version.pattern)
        strategy = force_bump or self._semver.determine_bump(commit_type)
        new_version = self._semver.calculate_next_version(current_version, strategy)

        if collector is not None:
            collector.set_run_context(
                str(current_version), str(new_version),
                branch=self._git.current_branch(repo_path) or "",
            )
            for pc_cfg in project.platforms:
                will_deploy = bool(pc_cfg.enabled) and (
                    not platforms_override or pc_cfg.platform in platforms_override
                )
                collector.note_platform(pc_cfg.platform.label(), pc_cfg.repo, will_deploy)
            if collector.receipt.trace:
                plan_edges, plan_commands = build_plan(
                    self._config, project, toml_cfg, platforms_override,
                    run_tests, run_docs, run_pypi, run_deb,
                    version=str(new_version),
                )
                collector.add_edges(plan_edges)
                collector.add_commands(plan_commands)

        if run_tests and not dry_run:
            with collector.stage("tests", caller="TestRunner.run") as tests_stage:
                ok, output = self._tests.run(repo_path, toml_cfg)
                if not ok:
                    tests_stage.fail(f"Tests failed: {output[:2000]}")
                    return DeployResult(
                        project=project.name,
                        version=str(new_version),
                        success=False,
                        error=f"Tests failed: {output[:2000]}",
                    )
            collector.observe_edge("DeployOrchestrator.deploy", "TestRunner.run", "step:tests")
            print(f"[+] tests passed for {project.name}")

        if run_docs and not dry_run:
            with collector.stage("docs", caller="DocsRunner.run") as docs_stage:
                docs_ok = self._docs.run(repo_path, toml_cfg)
                if not docs_ok:
                    docs_stage.fail("docs step failed")
            collector.observe_edge("DeployOrchestrator.deploy", "DocsRunner.run", "step:docs")
            if not docs_ok:
                print(f"[!] docs step failed for {project.name}, continuing deploy")

        if not dry_run:
            try:
                from deploynator._readme import ensure_deployed_footer
            except (OSError, ValueError) as exc:
                print(f"[!] deploy footer skipped for {project.name}: {exc}")
                collector.mark_failure("footer", str(exc), "ensure_deployed_footer")
            else:
                with collector.stage("footer", caller="ensure_deployed_footer"):
                    if ensure_deployed_footer(repo_path, self._config):
                        print(f"[+] deploy footer ensured for {project.name}")

        if not dry_run and not self._git.has_remote(repo_path):
            collector.mark_failure("remote_check", "No git remote configured", "GitOperations.has_remote")
            return DeployResult(
                project=project.name,
                version=str(new_version),
                success=False,
                error="No git remote configured",
            )

        start_ref = self._git.get_start_ref(repo_path)
        if not start_ref:
            collector.mark_failure("start_ref", "No starting ref (tag or initial commit) found",
                                   "GitOperations.get_start_ref")
            return DeployResult(
                project=project.name,
                version=str(new_version),
                success=False,
                error="No starting ref (tag or initial commit) found",
            )

        if not dry_run:
            with collector.stage("version_write", caller="SemverManager.write_version_file"):
                self._semver.write_version_file(repo_path, new_version, project.version.file)
                self._git.add_all(repo_path)

        changelog_content = self._changelog.generate_from_log(repo_path, start_ref)

        changed_files = self._git.get_changed_files(repo_path, start_ref)
        listfiles_parts = []
        # Cap each section: full file lists can exceed MAX_ARG_STRLEN
        # (E2BIG) when passed via `git commit -m`. Counts stay exact.
        _MAX_LISTED = 50

        def _listed(files: list) -> str:
            shown = [f"- {f}" for f in files[:_MAX_LISTED]]
            if len(files) > _MAX_LISTED:
                shown.append(f"- ... and {len(files) - _MAX_LISTED} more")
            return "\n".join(shown)

        if changed_files["modified"]:
            listfiles_parts.append(f"Modified file(s) [{len(changed_files['modified'])}]:\n" + _listed(changed_files["modified"]))
        if changed_files["deleted"]:
            listfiles_parts.append(f"Deleted file(s) [{len(changed_files['deleted'])}]:\n" + _listed(changed_files["deleted"]))
        if changed_files["created"]:
            listfiles_parts.append(f"Created file(s) [{len(changed_files['created'])}]:\n" + _listed(changed_files["created"]))
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

            with collector.stage("commit", caller="GitOperations.commit") as commit_stage:
                ok_commit, commit_err = self._git.commit(repo_path, commit_msg.format())
                if not ok_commit:
                    commit_stage.fail(f"Commit failed: {commit_err}")
                    return DeployResult(
                        project=project.name,
                        version=str(new_version),
                        success=False,
                        error=f"Commit failed: {commit_err}",
                    )
            collector.set_commit(self._git.head_commit(repo_path))
            collector.observe_edge("DeployOrchestrator.deploy", "GitOperations.commit",
                                   f"commit:{self._git.head_commit(repo_path)}")

            tag_name = str(new_version)
            while self._git.tag_exists(repo_path, tag_name):
                current_ver = VersionInfo.parse(tag_name)
                tag_name = str(VersionInfo(current_ver.major, current_ver.minor, current_ver.patch + 1))

            with collector.stage("tag", caller="GitOperations.tag") as tag_stage:
                if not self._git.tag(repo_path, tag_name, f"Version {tag_name}"):
                    tag_stage.fail("Tag creation failed")
                    return DeployResult(
                        project=project.name,
                        version=tag_name,
                        success=False,
                        error="Tag creation failed",
                    )
            collector.set_tag(tag_name)
            collector.observe_edge("DeployOrchestrator.deploy", "GitOperations.tag",
                                   f"tag:{tag_name}")

            new_version_str = tag_name
        else:
            new_version_str = str(new_version)

        # Mantenimiento: antes de empujar a main, si dev existe y esta por
        # debajo, fuerza main sobre dev para que dev quede igual que main.
        if not dry_run:
            with collector.stage("sync_dev", caller="DeployOrchestrator._sync_dev_to_main"):
                self._sync_dev_to_main(repo_path)

        platforms_to_deploy: list[PlatformConfig] = []
        for pc in project.platforms:
            if platforms_override and pc.platform not in platforms_override:
                continue
            if pc.enabled:
                platforms_to_deploy.append(pc)

        platforms_pushed = []
        releases_created = []
        overall_success = True
        deb_artifacts: list[str] = []

        # Build .deb ANTES de crear releases: los assets se suben justo
        # después de cada `create_release` (espejo PyPI pero como asset
        # descargable en vez de upload a un índice).
        if run_deb and toml_cfg.deb_enabled and (
            toml_cfg.deb_build.strip() or self._deb.is_deb_project(repo_path)
        ):
            if dry_run:
                print(f"[DRY-RUN] Would build .deb (outdir={toml_cfg.deb_outdir}) version {new_version_str}")
                if toml_cfg.deb_upload_assets:
                    print(f"[DRY-RUN] Would upload *.deb as release assets version {new_version_str}")
            else:
                with collector.stage("deb", caller="DebRunner.run") as deb_stage:
                    ok, msg, artifacts = self._deb.run(
                        repo_path, toml_cfg, new_version_str, verbose=verbose
                    )
                    if not ok:
                        deb_stage.fail(msg if verbose else msg[:2000])
                        return DeployResult(
                            project=project.name,
                            version=new_version_str,
                            success=False,
                            platforms_pushed=platforms_pushed,
                            releases_created=releases_created,
                            error=msg if verbose else msg[:2000],
                        )
                print(f"[{'OK' if ok else 'FAIL'}] {msg}")
                collector.observe_edge("DeployOrchestrator.deploy", "DebRunner.run",
                                       "step:deb")
                deb_artifacts = artifacts

        if not platforms_to_deploy and dry_run:
            print(f"[DRY-RUN] Would push to {toml_cfg.deploy_remote}/"
                  f"{self._git.current_branch(repo_path) or toml_cfg.deploy_branch} --follow-tags")

        if not platforms_to_deploy and not dry_run:
            # Sin plataformas (ej. deploy por ruta): fallback estilo DEPLOY.sh —
            # push al remoto propio + release con gh si disponible.
            branch = self._git.current_branch(repo_path) or toml_cfg.deploy_branch
            with collector.stage("push:origin", caller="GitOperations.push") as push_stage:
                push_ok = self._git.push(repo_path, toml_cfg.deploy_remote, branch)
                if not push_ok:
                    push_stage.fail(f"push failed: {toml_cfg.deploy_remote}/{branch}")
            if push_ok:
                platforms_pushed.append(f"{toml_cfg.deploy_remote}/{branch}")
                collector.observe_edge("DeployOrchestrator.deploy", "GitOperations.push",
                                       f"platform:origin/{branch}")
            else:
                overall_success = False
            release_notes = self._changelog.format_for_release(changelog_content)
            with collector.stage("gh_release", caller="DeployOrchestrator._gh_release_in_repo") as gh_stage:
                gh_ok = self._gh_release_in_repo(repo_path, project.name, new_version_str,
                                                 release_notes, branch)
                if not gh_ok:
                    gh_stage.fail("gh release create failed")
            if gh_ok:
                releases_created.append("github")
                collector.observe_edge("DeployOrchestrator.deploy",
                                       "DeployOrchestrator._gh_release_in_repo",
                                       f"platform:github/{new_version_str}")
                if deb_artifacts and toml_cfg.deb_upload_assets and not dry_run:
                    if self._gh_upload_assets(repo_path, new_version_str, deb_artifacts):
                        print(f"[OK] deb assets uploaded: {', '.join(deb_artifacts)}")
                    else:
                        print("[!] deb assets upload failed (gh release upload)")
                        overall_success = False

        for pc in platforms_to_deploy:
            if dry_run:
                print(f"[DRY-RUN] Would push to {pc.platform.label()}/{pc.repo}")
                platforms_pushed.append(pc.platform.label())
                continue

            label = pc.platform.label()
            try:
                client = PlatformFactory.create(pc.platform, self._config)
            except ValueError:
                collector.mark_failure(f"factory:{label}", f"Platform unavailable: {pc.platform.name}",
                                       "PlatformFactory.create")
                overall_success = False
                continue

            if not client.is_authenticated():
                print(f"[!] {pc.platform.label()} not authenticated. Skipping.")
                collector.mark_failure(f"auth:{label}", "not authenticated",
                                       "PlatformClient.is_authenticated")
                collector.note_platform(label, pc.repo, True, error="not authenticated")
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
                collector.observe_edge("DeployOrchestrator.deploy", "GitOperations.push",
                                       f"platform:{label}/{branch}")
                collector.note_platform(label, pc.repo, True, pushed=True)
            else:
                overall_success = False
                collector.note_platform(label, pc.repo, True, pushed=False, error="push failed")
                continue

            release_notes = self._changelog.format_for_release(changelog_content)
            release = ReleaseInfo(
                version=new_version_str,
                title=f"{project.name} {new_version_str}",
                notes=release_notes,
                target_branch=self._config.release_branch,
                assets=list(deb_artifacts),
            )

            client_class = client.__class__.__name__
            with collector.stage(f"release:{label}",
                                 caller=f"{client_class}.create_release") as rel_stage:
                rel_ok = client.create_release(pc.repo, release)
                if not rel_ok:
                    rel_stage.fail("create_release failed")
            if rel_ok:
                releases_created.append(label)
                collector.note_platform(label, pc.repo, True, released=True)
                collector.observe_edge("Platform.create_release",
                                       f"{client_class}.create_release",
                                       f"platform:{label}/{new_version_str}")
                if deb_artifacts and toml_cfg.deb_upload_assets:
                    with collector.stage(f"assets:{label}",
                                         caller=f"{client_class}.upload_release_assets") as ast_stage:
                        assets_ok = client.upload_release_assets(pc.repo, new_version_str,
                                                                 deb_artifacts)
                        if not assets_ok:
                            ast_stage.fail("deb assets upload failed")
                    if assets_ok:
                        collector.observe_edge("Platform.upload_release_assets",
                                               f"{client_class}.upload_release_assets",
                                               f"platform:{label}/{new_version_str}")
                        print(f"[OK] deb assets uploaded to {pc.platform.label()}: "
                              f"{', '.join(deb_artifacts)}")
                    else:
                        print(f"[!] deb assets upload failed for {pc.platform.label()}")
                        overall_success = False
            else:
                overall_success = False
                collector.note_platform(label, pc.repo, True, released=False,
                                        error="create_release failed")

        if run_pypi and toml_cfg.pypi_enabled and self._pypi.is_packaging_project(repo_path):
            if dry_run:
                print(f"[DRY-RUN] Would build+upload to PyPI ({toml_cfg.pypi_repo}) version {new_version_str}")
            elif not self._pypi.has_credentials():
                token = self._pypi.prompt_for_credentials()
                if not token:
                    print("[!] PyPI packaging detected but no credentials "
                          "(TWINE_PASSWORD/PYPI_TOKEN/~/.pypirc). Skipping upload.")
                    collector.mark_failure("pypi", "no credentials; skipped upload",
                                           "PyPIRunner.has_credentials")
                else:
                    with collector.stage("pypi", caller="PyPIRunner.run") as pypi_stage:
                        ok, msg = self._pypi.run(repo_path, toml_cfg, new_version_str, token=token,
                                                 verbose=verbose)
                        if not ok:
                            pypi_stage.fail(msg if verbose else msg[:2000])
                            return DeployResult(
                                project=project.name,
                                version=new_version_str,
                                success=False,
                                platforms_pushed=platforms_pushed,
                                releases_created=releases_created,
                                error=msg if verbose else msg[:2000],
                            )
                    print(f"[{'OK' if ok else 'FAIL'}] {msg}")
                    if ok:
                        collector.observe_edge("DeployOrchestrator.deploy", "PyPIRunner.run",
                                               f"step:pypi/{new_version_str}")
            else:
                with collector.stage("pypi", caller="PyPIRunner.run") as pypi_stage:
                    ok, msg = self._pypi.run(repo_path, toml_cfg, new_version_str, verbose=verbose)
                    if not ok:
                        pypi_stage.fail(msg if verbose else msg[:2000])
                        return DeployResult(
                            project=project.name,
                            version=new_version_str,
                            success=False,
                            platforms_pushed=platforms_pushed,
                            releases_created=releases_created,
                            error=msg if verbose else msg[:2000],
                        )
                print(f"[{'OK' if ok else 'FAIL'}] {msg}")
                if ok:
                    collector.observe_edge("DeployOrchestrator.deploy", "PyPIRunner.run",
                                           f"step:pypi/{new_version_str}")

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
        notes_file: str | None = None
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

    def _gh_upload_assets(self, repo_path: str, version: str, assets: list[str]) -> bool:
        """Best-effort `gh release upload <tag> <debs> --clobber`. Never raises."""
        files = [a for a in assets if a and os.path.isfile(a) and not os.path.islink(a)]
        if not files or shutil.which(self._config.gh_cli) is None:
            return False
        try:
            result = subprocess.run(
                [self._config.gh_cli, "release", "upload", version, *files, "--clobber"],
                cwd=repo_path,
                capture_output=True, text=True, check=False,
            )
            return result.returncode == 0
        except (subprocess.SubprocessError, OSError):
            return False

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

    def _sync_dev_to_main(self, repo_path: str) -> None:
        """Sincroniza dev con main antes del push.

        Si la rama dev existe, esta por debajo de main y hay diferencias,
        empuja main sobre dev con force (+main:dev) para que dev quede
        igual de actualizado que main. Nunca falla el despliegue si el
        sync no se puede completar.
        """
        main = self._config.default_branch
        dev = self._config.dev_branch
        remote = self._config.default_remote

        if not self._git.branch_exists(repo_path, dev):
            return
        if not self._git.branch_exists(repo_path, main):
            return
        if not self._git.is_behind(repo_path, dev, main):
            return
        if not self._git.has_remote(repo_path, remote):
            return

        ok = self._git.push_force(repo_path, remote, main, dev)
        if ok:
            print(f"[+] dev sincronizado con main (force): {main} -> {dev}")
        else:
            print(f"[!] No se pudo sincronizar dev con main: {main} -> {dev}")

    @staticmethod
    def _get_remote_url(repo_path: str, pc: PlatformConfig) -> str | None:
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
        return """name: deploynator CI

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
        return """name: deploynator Release

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
            import importlib.util
            if importlib.util.find_spec("readmenator") is None:
                raise ImportError("readmenator not installed")
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
