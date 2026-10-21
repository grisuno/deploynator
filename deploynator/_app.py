from __future__ import annotations

import os
import re
import sys

from deploynator._config import Config
from deploynator._deploy import DeployOrchestrator, ProjectDiscovery
from deploynator._models import (
    CommitType,
    DeployResult,
    Platform,
    ProjectConfig,
)
from deploynator._platforms import PlatformFactory


class DeploynatorApp:
    def __init__(self, config: Config | None = None, workdir: str = "") -> None:
        self._config = config or Config.create()
        self._workdir = workdir
        if workdir:
            self._config = Config.create({"_path": workdir})
        self._discovery = ProjectDiscovery(self._config)
        self._orchestrator = DeployOrchestrator(self._config)

    # ---- Auth ----

    def auth_login(self, platforms: list[str] | None = None) -> dict[str, bool]:
        results = {}

        if platforms is None or "github" in platforms:
            results["github"] = self._auth_github()

        if platforms is None or "gitlab" in platforms:
            results["gitlab"] = self._auth_gitlab()

        if platforms is None or "bitbucket" in platforms:
            results["bitbucket"] = self._auth_bitbucket()

        return results

    def auth_status(self) -> dict[str, bool]:
        status = {}
        for pname in ["github", "gitlab", "bitbucket"]:
            client = PlatformFactory.create(Platform.from_string(pname), self._config)
            try:
                status[pname] = client.is_authenticated()
            except (ValueError, RuntimeError):
                status[pname] = False
        return status

    @staticmethod
    def _auth_github() -> bool:
        import subprocess
        try:
            result = subprocess.run(
                ["gh", "auth", "login"],
                capture_output=False, text=True, check=False,
            )
            return result.returncode == 0
        except FileNotFoundError:
            print("[!] gh CLI not found. Install: https://cli.github.com")
            return False

    @staticmethod
    def _auth_gitlab() -> bool:
        import subprocess
        try:
            result = subprocess.run(
                ["glab", "auth", "login"],
                capture_output=False, text=True, check=False,
            )
            return result.returncode == 0
        except FileNotFoundError:
            env_token = os.environ.get("GITLAB_TOKEN")
            if env_token:
                return True
            print("[!] glab not found. Install: https://gitlab.com/gitlab-org/cli")
            print("    Or set GITLAB_TOKEN env var for token-based auth.")
            return False

    @staticmethod
    def _auth_bitbucket() -> bool:
        env_token = os.environ.get("BITBUCKET_TOKEN")
        if env_token:
            return True
        print("[!] BITBUCKET_TOKEN not set. Set BITBUCKET_TOKEN env var.")
        print("    Or install the Bitbucket CLI: https://bitbucket.org/")
        return False

    # ---- Init ----

    DEPLOY_SH_TEMPLATE = """#!/bin/bash
# deploy.sh -- one-liner deploy via deploynator (generic per-repo script).
# Deployed by deploynator: detects its own directory, ensures tooling,
# then releases this repo. Usage:
#   ./deploy.sh                    # patch release (smallest bump)
#   ./deploy.sh feat --dry-run     # preview a minor release
#   ./deploy.sh fix --no-test      # patch release skipping tests
set -euo pipefail

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TYPE="patch"
if [ $# -gt 0 ]; then
    TYPE="$1"
    shift
fi

PIP_BIN="pip"
command -v pip >/dev/null 2>&1 || PIP_BIN="pip3"

# Install or update one package (best effort: works offline with current versions,
# on PEP 668 systems, and before the PyPI upload via git fallback).
ensure_pkg() {
    if python3 -c "import $1" 2>/dev/null; then
        "$PIP_BIN" install -U "$2" 2>/dev/null || true
    else
        "$PIP_BIN" install "$2" 2>/dev/null \\
            || "$PIP_BIN" install "$3" 2>/dev/null \\
            || "$PIP_BIN" install --break-system-packages "$2" 2>/dev/null \\
            || "$PIP_BIN" install --break-system-packages "$3" 2>/dev/null \\
            || true
    fi
}

ensure_pkg deploynator deploynator "git+https://github.com/grisuno/deploynator.git"
ensure_pkg readmenator readmenator readmenator
ensure_pkg build build build
ensure_pkg twine twine twine

if ! python3 -c "import deploynator" 2>/dev/null; then
    echo "[!] deploynator not available and install failed (offline?)." >&2
    exit 1
fi

exec python3 -m deploynator release --type "$TYPE" --project "$DIR" "$@"
"""

    DEPLOY_TOML_TEMPLATE = """# deploynator.toml -- per-project deploy config (created by `deploynator init`).
# Docs: specify version file, tests, docs and PyPI behaviour for this repo.

[project]
name = "{name}"
version_file = "version.json"

[tests]
commands = ["python -m pytest tests/ -q"]
timeout_s = 300
allow_no_tests = false

[docs]
auto = true
command = "python -m readmenator . --rebuild"
timeout_s = 300

[deploy]
branch = "main"
remote = "origin"
# Default release message when CLI gives no --subject/--message
# nor trailing words (e.g. message = "chore: nightly sync").
# CLI always wins over this value.
message = ""

[pypi]
enabled = true
repo = "pypi"
clean_dist = true
timeout_s = 600

[deb]
# Proyectos C (Makefile): si hay debian/control o un target
# deb|package-deb|dist-deb|deb-package|package, construye el .deb
# y lo sube como asset del release (equivalente PyPI para apt/dpkg).
# build = "" -> auto (`make <target>` o dpkg-buildpackage).
# Ej. C explícito: build = "make deb".
enabled = true
build = ""
outdir = "dist-deb"
clean_dist = true
timeout_s = 600
upload_assets = true
"""

    def init_project(self, project_path: str = "", name: str = "") -> str:
        base = project_path or os.getcwd()
        project_name = name or os.path.basename(base)
        config_path = os.path.join(base, "deploynator.yaml")
        created = []

        if not os.path.isfile(config_path):
            content = f"""version: 1.0
name: {project_name}
description: "Project managed by deploynator"
platforms:
  github:
    repo: "user/{project_name}"
    enabled: true
  gitlab:
    repo: "group/{project_name}"
    enabled: false
  bitbucket:
    repo: "workspace/{project_name}"
    enabled: false
version:
  file: version.json
  file_type: json
"""
            with open(config_path, "w") as f:
                f.write(content)
            created.append(config_path)

        toml_path = os.path.join(base, "deploynator.toml")
        if not os.path.isfile(toml_path):
            from deploynator._toml import _has_python_tests, detect_test_commands
            inferred: list[str] | None = None
            try:
                detected = detect_test_commands(base)
                if detected is not None and not (
                    detected != ["make test-host"]
                    and detected[0].startswith("make")
                    and _has_python_tests(base)
                ):
                    inferred = detected
            except ValueError:
                inferred = None
            if inferred is not None:
                commands_repr = "[" + ", ".join(f'"{c}"' for c in inferred) + "]"
                timeout = 900
            else:
                commands_repr = '["python -m pytest tests/ -q"]'
                timeout = 300
            content = self.DEPLOY_TOML_TEMPLATE.format(name=project_name)
            content = content.replace(
                'commands = ["python -m pytest tests/ -q"]',
                f"commands = {commands_repr}",
            ).replace(
                "timeout_s = 300",
                f"timeout_s = {timeout}",
                1,
            )
            with open(toml_path, "w") as f:
                f.write(content)
            created.append(toml_path)

        script_path = os.path.join(base, "deploy.sh")
        if not os.path.isfile(script_path):
            with open(script_path, "w") as f:
                f.write(self.DEPLOY_SH_TEMPLATE)
            os.chmod(script_path, 0o755)
            created.append(script_path)

        projects_dir = os.path.join(base, self._config.projects_dir)
        os.makedirs(projects_dir, exist_ok=True)

        if not created:
            return f"deploynator already initialized at {base}"
        return "Initialized deploynator: " + ", ".join(created)

    # ---- Start ----

    def start_branch(self, commit_type: str, description: str, project_path: str = "",
                     project_name: str = "", remote: bool = False) -> str:
        from deploynator._git import GitOperations
        from deploynator._models import CommitType
        commit_type_enum = CommitType.from_string(commit_type)
        git = GitOperations(self._config)
        base = project_path or self._resolve_project_path(project_name)
        safe_desc = re.sub(r"[^a-zA-Z0-9_-]", "-", description)
        safe_desc = safe_desc.strip("-")
        branch_name = f"{commit_type_enum.value}/{safe_desc}"
        ok = git.create_branch(base, branch_name)
        if not ok:
            return f"Failed to create branch {branch_name}"
        if remote:
            git.push(base, self._config.default_remote, branch_name)
        return f"Created branch {branch_name}"

    @staticmethod
    def _is_path_like(value: str) -> bool:
        return bool(value) and (value.startswith(("/", "~", ".")) or os.sep in value or os.path.isdir(value))

    @staticmethod
    def _looks_like_path(value: str) -> bool:
        return bool(value) and (
            value.startswith(("/", "~", "."))
            or os.sep in value
            or os.path.isabs(os.path.expanduser(value))
        )

    def _resolve_project_path(self, project_name: str) -> str:
        if not project_name:
            return self._config._path or os.getcwd()
        project = self._discovery.find_by_name(project_name)
        if project:
            from deploynator._deploy import DeployOrchestrator
            return DeployOrchestrator._resolve_project_path(project, config=self._config)
        expanded = os.path.expanduser(project_name)
        if self._looks_like_path(project_name) and os.path.isdir(expanded):
            return os.path.abspath(expanded)
        return self._config._path or os.getcwd()

    def _smart_prepare(self, base: str, changelog_content: str = "", dry_run: bool = False) -> None:
        from deploynator._git import GitOperations
        git = GitOperations(self._config)

        if not dry_run:
            self._orchestrator.integrate_readmenator(base)

        if changelog_content and not dry_run:
            self._orchestrator._changelog.write_changelog(base, changelog_content)

        if not dry_run:
            git.add_all(base)

    # ---- Commit ----

    def commit(self, commit_type: str, subject: str, scope: str = "", body: str = "",
               project_path: str = "", project_name: str = "", dry_run: bool = False) -> str:
        from deploynator._git import GitOperations
        from deploynator._models import CommitMessage

        ctype = CommitType.from_string(commit_type)
        git = GitOperations(self._config)
        base = project_path or self._resolve_project_path(project_name)

        if not os.path.isdir(os.path.join(base, ".git")):
            return f"Not a git repository: {base}"

        scope_part = f"({scope})" if scope else ""
        commit_desc = f"{ctype.value}{scope_part}: {subject}"
        changelog = self._orchestrator._changelog.generate_from_messages(
            [commit_desc]
        ) if not dry_run else ""

        self._smart_prepare(base, changelog, dry_run)

        if not git.is_dirty(base) and not dry_run:
            return f"Nothing to commit. Working tree clean for {commit_desc}"

        commit_msg = CommitMessage(
            commit_type=ctype,
            scope=scope,
            subject=subject,
            body=body,
        )

        if dry_run:
            return f"[DRY-RUN] Would commit:\n{commit_msg.format()}"

        ok, msg = git.commit(base, commit_msg.format())
        if not ok:
            return f"Commit failed: {msg}"
        return f"Committed as {commit_desc}"

    # ---- Release ----

    @staticmethod
    def _parse_release_message(raw: str) -> tuple[str | None, str, str]:
        """Parsea `test(module): texto` o `test(module) texto` (colon opcional).

        Devuelve (commit_type|None, scope, subject). Si no hay prefijo
        convencional, devuelve (None, "", raw.strip()).
        """
        import re as _re

        from deploynator._models import CommitType as _CT
        text = (raw or "").strip()
        if not text:
            return None, "", ""
        types = "|".join(_CT.valid_types())
        m = _re.match(rf"^({types})(?:\(([^)]+)\))?\s*:?\s+(.+)$", text, _re.IGNORECASE)
        if m:
            return m.group(1).lower(), (m.group(2) or "").strip(), m.group(3).strip()
        return None, "", text

    def release(
        self,
        commit_type: str = "release",
        subject: str = "",
        scope: str = "",
        body: str = "",
        message: str = "",
        project_name: str = "",
        bump: str = "",
        dry_run: bool = False,
        platforms: list[str] | None = None,
        all_projects: bool = False,
        no_test: bool = False,
        no_docs: bool = False,
        no_pypi: bool = False,
        no_deb: bool = False,
        verbose: bool = False,
        receipt_path: str | None = None,
        trace: bool = False,
    ) -> list[DeployResult]:
        base = os.getcwd()
        ctype = CommitType.from_string(commit_type)
        results: list[DeployResult] = []

        if all_projects:
            projects = self._discovery.discover()
        elif project_name:
            project = self._discovery.find_by_name(project_name)
            if project:
                projects = [project]
            else:
                expanded = os.path.expanduser(project_name)
                if self._looks_like_path(project_name) and os.path.isdir(expanded):
                    from deploynator._models import ProjectConfig, VersionConfig
                    from deploynator._toml import load_toml_config
                    abs_path = os.path.abspath(expanded)
                    try:
                        toml_cfg = load_toml_config(abs_path)
                        version_file = toml_cfg.version_file
                    except ValueError:
                        version_file = "version.json"
                    projects = [ProjectConfig(
                        name=os.path.basename(abs_path),
                        description="",
                        platforms=[],
                        version=VersionConfig(file=version_file),
                        path=abs_path,
                    )]
                else:
                    projects = []
        else:
            projects = self._discovery.discover()
            if not projects:
                single = self._discovery._load_single(
                    os.path.join(base, "deploynator.yaml")
                ) if os.path.isfile(os.path.join(base, "deploynator.yaml")) else None
                projects = [single] if single else []

        if not projects:
            return [DeployResult(
                project=project_name or "unknown",
                version="",
                success=False,
                error="No projects found. Create a deploynator.yaml or projects/*.yaml"
            )]

        platform_objs = None
        if platforms:
            platform_objs = [Platform.from_string(p) for p in platforms]

        # Precedencia mensaje: CLI trailing/--message > --subject > [deploy] message > auto.
        cli_message = (message or "").strip()
        base_ctype = ctype
        if cli_message:
            p_type, p_scope, p_subject = self._parse_release_message(cli_message)
            if p_type:
                base_ctype = CommitType.from_string(p_type)
                base_scope = p_scope or scope
                base_subject = p_subject
            else:
                base_scope = scope
                base_subject = cli_message
            has_base_subject = True
        elif (subject or "").strip():
            base_scope = scope
            base_subject = subject.strip()
            has_base_subject = True
        else:
            base_scope = scope
            base_subject = ""
            has_base_subject = False

        for project in projects:
            if not project:
                continue
            proj_ctype = base_ctype
            proj_scope = base_scope
            if has_base_subject:
                subject_text = base_subject
            else:
                # Fallback per-proyecto: [deploy] message del deploynator.toml.
                toml_msg = ""
                try:
                    from deploynator._deploy import DeployOrchestrator as _DO
                    from deploynator._toml import load_toml_config as _load
                    toml_msg = (_load(_DO._resolve_project_path(project)).deploy_message or "").strip()
                except (ValueError, OSError):
                    toml_msg = ""
                if toml_msg:
                    t_type, t_scope, t_subject = self._parse_release_message(toml_msg)
                    if t_type:
                        proj_ctype = CommitType.from_string(t_type)
                        proj_scope = t_scope or scope
                        subject_text = t_subject
                    else:
                        subject_text = toml_msg
                else:
                    subject_text = f"{proj_ctype.value}: automated release"
            result = self._orchestrator.deploy(
                project=project,
                commit_type=proj_ctype,
                subject=subject_text,
                scope=proj_scope,
                body=body,
                dry_run=dry_run,
                platforms_override=platform_objs,
                run_tests=not no_test,
                run_docs=not no_docs,
                force_bump=bump or None,
                run_pypi=not no_pypi,
                run_deb=not no_deb,
                verbose=verbose,
                receipt_path=receipt_path,
                trace=trace,
            )
            results.append(result)
            self._print_result(result)

        return results

    # ---- Docs ----

    def generate_docs(self, project_path: str = "", project_name: str = "") -> bool:
        base = project_path or self._resolve_project_path(project_name)
        return self._orchestrator.integrate_readmenator(base)

    # ---- Status ----

    def status(self, project_path: str = "", project_name: str = "") -> dict:
        from deploynator._git import GitOperations
        git = GitOperations(self._config)
        base = project_path or self._resolve_project_path(project_name)
        info = {
            "path": base,
            "is_git_repo": os.path.isdir(os.path.join(base, ".git")),
            "current_branch": git.current_branch(base) if os.path.isdir(os.path.join(base, ".git")) else None,
            "is_dirty": git.is_dirty(base) if os.path.isdir(os.path.join(base, ".git")) else None,
            "has_remote": git.has_remote(base) if os.path.isdir(os.path.join(base, ".git")) else None,
            "has_deploynator_yaml": os.path.isfile(os.path.join(base, "deploynator.yaml")),
        }
        if os.path.isdir(os.path.join(base, self._config.projects_dir)):
            info["projects_count"] = len(self._discovery.discover())
        else:
            info["projects_count"] = 0
        return info

    # ---- Projects ----

    def list_projects(self, search_path: str = "") -> list[ProjectConfig]:
        return self._discovery.discover(search_path)

    # ---- Workflows ----

    def generate_ci(self, project_name: str = "", all_projects: bool = False) -> list[str]:
        created = []
        if all_projects:
            projects = self._discovery.discover()
        elif project_name:
            project = self._discovery.find_by_name(project_name)
            projects = [project] if project else []
        else:
            projects = self._discovery.discover()
        for project in projects:
            if project:
                created.extend(self._orchestrator.generate_workflows(project))
        return created

    # ---- Install ----

    def install_deps(self, project_name: str = "") -> dict[str, bool]:
        if project_name:
            project = self._discovery.find_by_name(project_name)
            if project:
                return self._orchestrator.install_dependencies(project)
            return {}
        all_deps = {}
        for project in self._discovery.discover():
            all_deps.update(self._orchestrator.install_dependencies(project))
        return all_deps

    def install_packages(self, packages: list[str] | None = None) -> dict[str, bool]:
        """pip install/upgrade packages (default: deploynator from PyPI)."""
        import subprocess
        targets = packages if packages is not None else ["deploynator"]
        results: dict[str, bool] = {}
        for pkg in targets:
            ok = False
            for cmd in (
                [sys.executable, "-m", "pip", "install", "-U", pkg],
                [sys.executable, "-m", "pip", "install", "-U", "--break-system-packages", pkg],
            ):
                try:
                    result = subprocess.run(
                        cmd, capture_output=True, text=True, check=False,
                        shell=False, timeout=300,
                    )
                    if result.returncode == 0:
                        ok = True
                        break
                except (FileNotFoundError, subprocess.TimeoutExpired):
                    continue
            results[pkg] = ok
            print(f"  {pkg}: {'installed' if ok else 'FAILED'}")
        return results

    # ---- Interactive ----

    def interactive_menu(self) -> None:
        options = {
            "1": ("Release", self._interactive_release),
            "2": ("Commit", self._interactive_commit),
            "3": ("Start branch", self._interactive_start),
            "4": ("Auth login", self._interactive_auth),
            "5": ("Auth status", self._interactive_auth_status),
            "6": ("Generate docs", self._interactive_docs),
            "7": ("Generate CI workflows", self._interactive_ci),
            "8": ("Status", self._interactive_status),
            "9": ("Init project", self._interactive_init),
            "0": ("Exit", None),
        }

        while True:
            print("\n=== deploynator interactive menu ===")
            for key, (label, _) in options.items():
                print(f"  {key}. {label}")
            print()
            try:
                choice = input("Select option: ").strip()
            except (EOFError, KeyboardInterrupt):
                print()
                break

            if choice == "0":
                break
            entry = options.get(choice)
            if entry and entry[1]:
                try:
                    entry[1]()
                except (OSError, ValueError, RuntimeError) as exc:
                    print(f"[!] Error: {exc}")
            else:
                print("[!] Invalid option")

    def _interactive_release(self) -> None:
        print("\nCommit types:")
        for i, ct in enumerate(CommitType.valid_types(), 1):
            print(f"  {i}. {ct}")
        try:
            choice = input("Select type (number): ").strip()
            types = CommitType.valid_types()
            idx = int(choice) - 1
            if idx < 0 or idx >= len(types):
                print("[!] Invalid type")
                return
            ctype = types[idx]
        except (ValueError, IndexError):
            print("[!] Invalid input")
            return

        subject = input("Subject (optional, press Enter for auto): ").strip()
        message = input("Message (optional, e.g. test(module) testing ...): ").strip()
        if message and not subject:
            subject = ""
        scope = input("Scope (optional): ").strip()
        body = input("Body (optional): ").strip()
        bump = input("Force bump (major/minor/patch or Enter for auto): ").strip()
        dry_run = input("Dry-run? (y/N): ").strip().lower() == "y"
        no_test = input("Skip tests? (--no-test) (y/N): ").strip().lower() == "y"
        no_docs = input("Skip docs? (--no-docs) (y/N): ").strip().lower() == "y"
        no_pypi = input("Skip PyPI? (--no-pypi) (y/N): ").strip().lower() == "y"
        no_deb = input("Skip .deb? (--no-deb) (y/N): ").strip().lower() == "y"
        all_proj = input("Deploy all projects? (y/N): ").strip().lower() == "y"

        results = self.release(
            commit_type=ctype,
            subject=subject,
            message=message,
            scope=scope,
            body=body,
            bump=bump,
            dry_run=dry_run,
            all_projects=all_proj,
            no_test=no_test,
            no_docs=no_docs,
            no_pypi=no_pypi,
            no_deb=no_deb,
        )

        for r in results:
            self._print_result(r)

    def _interactive_commit(self) -> None:
        print("\nCommit types:")
        for i, ct in enumerate(CommitType.valid_types(), 1):
            print(f"  {i}. {ct}")
        try:
            choice = input("Select type (number): ").strip()
            types = CommitType.valid_types()
            idx = int(choice) - 1
            if idx < 0 or idx >= len(types):
                print("[!] Invalid type")
                return
            ctype = types[idx]
        except (ValueError, IndexError):
            print("[!] Invalid input")
            return

        project_raw = input("Project (Enter for current dir): ").strip()
        subject = input("Subject: ").strip()
        scope = input("Scope (optional): ").strip()
        body = input("Body (optional): ").strip()
        dry_run = input("Dry-run? (y/N): ").strip().lower() == "y"
        if self._is_path_like(project_raw):
            result = self.commit(ctype, subject, scope, body, project_path=project_raw, dry_run=dry_run)
        else:
            result = self.commit(ctype, subject, scope, body, project_name=project_raw, dry_run=dry_run)
        print(result)

    def _interactive_start(self) -> None:
        print("\nBranch types:")
        for i, ct in enumerate(CommitType.valid_types(), 1):
            print(f"  {i}. {ct}")
        try:
            choice = input("Select type (number): ").strip()
            types = CommitType.valid_types()
            idx = int(choice) - 1
            if idx < 0 or idx >= len(types):
                print("[!] Invalid type")
                return
            ctype = types[idx]
        except (ValueError, IndexError):
            print("[!] Invalid input")
            return
        project_raw = input("Project (Enter for current dir): ").strip()
        desc = input("Description: ").strip()
        remote = input("Push to remote? (y/N): ").strip().lower() == "y"
        if self._is_path_like(project_raw):
            result = self.start_branch(ctype, desc, project_path=project_raw, remote=remote)
        else:
            result = self.start_branch(ctype, desc, project_name=project_raw, remote=remote)
        print(result)

    def _interactive_auth(self) -> None:
        print("\nPlatforms:")
        platforms = ["github", "gitlab", "bitbucket"]
        for i, p in enumerate(platforms, 1):
            print(f"  {i}. {p}")
        choice = input("Select platform (number or 'all'): ").strip()
        if choice.lower() == "all":
            results = self.auth_login()
        else:
            try:
                idx = int(choice) - 1
                if 0 <= idx < len(platforms):
                    results = self.auth_login([platforms[idx]])
                else:
                    print("[!] Invalid")
                    return
            except ValueError:
                print("[!] Invalid")
                return
        for platform, ok in results.items():
            status = "authenticated" if ok else "failed"
            print(f"  {platform}: {status}")

    def _interactive_auth_status(self) -> None:
        status = self.auth_status()
        for platform, ok in status.items():
            s = "authenticated" if ok else "not authenticated"
            print(f"  {platform}: {s}")

    def _interactive_docs(self) -> None:
        result = self.generate_docs()
        if result:
            print("[+] Documentation generated via ReadMenator")
        else:
            print("[!] Documentation generation failed")

    def _interactive_ci(self) -> None:
        all_proj = input("Generate for all projects? (y/N): ").strip().lower() == "y"
        created = self.generate_ci(all_projects=all_proj)
        if created:
            for path in created:
                print(f"[+] Created {path}")
        else:
            print("[!] No workflows created")

    def _interactive_status(self) -> None:
        info = self.status()
        for key, value in info.items():
            print(f"  {key}: {value}")

    def _interactive_init(self) -> None:
        name = input("Project name (Enter for dirname): ").strip()
        result = self.init_project(name=name)
        print(result)

    @staticmethod
    def _print_result(result: DeployResult) -> None:
        status = "OK" if result.success else "FAIL"
        platforms = ", ".join(result.platforms_pushed) or "none"
        releases = ", ".join(result.releases_created) or "none"
        print(f"[{status}] {result.project} v{result.version}")
        print(f"  Platforms pushed: {platforms}")
        print(f"  Releases created: {releases}")
        if result.error:
            print(f"  Error: {result.error}")
