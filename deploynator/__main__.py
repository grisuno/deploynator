from __future__ import annotations

import argparse
import sys
from typing import NoReturn

from deploynator import DeploynatorApp
from deploynator._config import Config
from deploynator._models import CommitType

KNOWN_COMMANDS = {
    "release", "commit", "start", "auth", "docs", "init",
    "status", "projects", "workflow", "install", "interactive", "serve",
}


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="deploynator",
        description="Multi-platform deployer for GitHub, GitLab, and Bitbucket.",
        epilog="Deployed with deploynator (https://github.com/grisuno/deploynator)",
    )
    parser.add_argument(
        "--version", action="version",
        version=f"deploynator {__import__('deploynator').__version__}",
    )
    parser.add_argument(
        "--workdir", type=str, default="",
        help="Working directory (default: current dir)",
    )

    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # release
    release_p = subparsers.add_parser("release", help="Create a release")
    release_p.add_argument(
        "--type", dest="commit_type", default="release",
        choices=CommitType.valid_types(),
        help="Commit type (default: release)",
    )
    release_p.add_argument("--subject", type=str, default="", help="Commit subject")
    release_p.add_argument("--scope", type=str, default="", help="Commit scope")
    release_p.add_argument("--body", type=str, default="", help="Commit body")
    release_p.add_argument("--project", "-p", type=str, default="", help="Project name from projects/")
    release_p.add_argument("--bump", type=str, default="", choices=["major", "minor", "patch", ""],
                           help="Force version bump")
    release_p.add_argument("--dry-run", action="store_true", help="Simulate without changes")
    release_p.add_argument("--no-test", dest="no_test", action="store_true",
                           help="Skip tests (like DEPLOY.sh --no-test)")
    release_p.add_argument("--no-docs", dest="no_docs", action="store_true",
                           help="Skip readmenator docs regeneration")
    release_p.add_argument("--no-pypi", dest="no_pypi", action="store_true",
                           help="Skip PyPI build+upload")
    release_p.add_argument("--platforms", type=str, nargs="*",
                           choices=["github", "gitlab", "bitbucket"],
                           help="Platforms to deploy to")
    release_p.add_argument("--all", dest="all_projects", action="store_true",
                           help="Deploy all discovered projects")

    # commit
    commit_p = subparsers.add_parser("commit", help="Create a conventional commit")
    commit_p.add_argument(
        "--type", dest="commit_type", required=True,
        choices=CommitType.valid_types(),
        help="Commit type",
    )
    commit_p.add_argument("--subject", type=str, required=True, help="Commit subject")
    commit_p.add_argument("--scope", type=str, default="", help="Commit scope")
    commit_p.add_argument("--body", type=str, default="", help="Commit body")
    commit_p.add_argument("--project", "-p", type=str, default="", help="Project name from projects/")
    commit_p.add_argument("--dry-run", action="store_true", help="Simulate without changes")

    # start
    start_p = subparsers.add_parser("start", help="Create a feature/bug branch")
    start_p.add_argument(
        "--type", dest="commit_type", required=True,
        choices=CommitType.valid_types(),
        help="Branch type",
    )
    start_p.add_argument("--desc", type=str, required=True, help="Branch description")
    start_p.add_argument("--project", "-p", type=str, default="", help="Project name from projects/")
    start_p.add_argument("--remote", action="store_true", help="Push branch to remote")

    # auth
    auth_p = subparsers.add_parser("auth", help="Authentication commands")
    auth_sub = auth_p.add_subparsers(dest="auth_command", help="Auth subcommands")
    auth_login_p = auth_sub.add_parser("login", help="Login to platforms")
    auth_login_p.add_argument(
        "--platforms", type=str, nargs="*",
        choices=["github", "gitlab", "bitbucket"],
        help="Platforms to authenticate (default: all)",
    )
    auth_sub.add_parser("status", help="Show authentication status")

    # docs
    docs_p = subparsers.add_parser("docs", help="Generate documentation via ReadMenator")
    docs_p.add_argument("--project", "-p", type=str, default="", help="Project name from projects/")

    # init
    init_p = subparsers.add_parser("init", help="Initialize deploynator in project")
    init_p.add_argument("--name", type=str, default="", help="Project name")

    # status
    status_p = subparsers.add_parser("status", help="Show project status")
    status_p.add_argument("--project", "-p", type=str, default="", help="Project name from projects/")

    # projects
    subparsers.add_parser("projects", help="List discovered projects")

    # workflow
    workflow_p = subparsers.add_parser("workflow", help="Generate CI/CD workflows")
    workflow_p.add_argument("--project", "-p", type=str, default="", help="Specific project")
    workflow_p.add_argument("--all", action="store_true", help="All projects")

    # install (pip packages from PyPI; --project keeps legacy platform CLI check)
    install_p = subparsers.add_parser("install", help="pip install packages (default: deploynator)")
    install_p.add_argument("packages", type=str, nargs="*", default=[],
                           help="Packages to install (default: deploynator)")
    install_p.add_argument("--project", "-p", type=str, default="",
                           help="Check platform CLI availability for a project instead")

    # interactive (no args/flags — bare mode menu)
    subparsers.add_parser("interactive", help="Start interactive menu (also default with no args)")

    # serve (MCP stdio server for agent harnesses)
    serve_p = subparsers.add_parser("serve", help="Start MCP stdio server")
    serve_p.add_argument("path", type=str, nargs="?", default=".",
                         help="Target directory (default: .)")

    return parser


def preprocess_argv(argv: list[str]) -> tuple[argparse.Namespace, str]:
    parser = build_parser()
    extracted_project = ""

    if not argv or argv[0] in ("--help", "-h", "--version"):
        return parser.parse_args(argv), extracted_project

    # Scan past global flags (--workdir, etc.) to find first positional token
    first_pos = None
    first_pos_idx = None
    i = 0
    while i < len(argv):
        arg = argv[i]
        if not arg.startswith("-"):
            first_pos = arg
            first_pos_idx = i
            break
        if arg in ("--workdir",):
            i += 2
        else:
            i += 1

    if first_pos is not None and first_pos not in KNOWN_COMMANDS:
        extracted_project = first_pos
        argv = argv[:first_pos_idx] + argv[first_pos_idx + 1:]

    args = parser.parse_args(argv)

    if hasattr(args, "project") and not args.project and extracted_project:
        args.project = extracted_project

    return args, extracted_project


def main(argv: list[str] | None = None) -> NoReturn | None:
    raw_argv = list(argv) if argv is not None else sys.argv[1:]

    # Bare `deploynator` (no args) = interactive menu. Flags = headless.
    if not raw_argv:
        config = Config.create()
        DeploynatorApp(config).interactive_menu()
        return

    args, project_pos = preprocess_argv(raw_argv)

    config = Config.create()
    app = DeploynatorApp(config, workdir=args.workdir if hasattr(args, "workdir") else "")

    if not args.command:
        parser = build_parser()
        parser.print_help()
        return

    project = getattr(args, "project", "") or project_pos

    if args.command == "release":
        results = app.release(
            commit_type=args.commit_type,
            subject=args.subject,
            scope=args.scope,
            body=args.body,
            project_name=project,
            bump=args.bump if hasattr(args, "bump") else "",
            dry_run=args.dry_run,
            platforms=args.platforms if hasattr(args, "platforms") else None,
            all_projects=args.all_projects if hasattr(args, "all_projects") else False,
            no_test=getattr(args, "no_test", False),
            no_docs=getattr(args, "no_docs", False),
            no_pypi=getattr(args, "no_pypi", False),
        )
        sys.exit(0 if all(r.success for r in results) else 1)

    elif args.command == "commit":
        result = app.commit(
            commit_type=args.commit_type,
            subject=args.subject,
            scope=args.scope,
            body=args.body,
            project_name=project,
            dry_run=args.dry_run,
        )
        print(result)

    elif args.command == "start":
        result = app.start_branch(
            commit_type=args.commit_type,
            description=args.desc,
            project_name=project,
            remote=args.remote,
        )
        print(result)

    elif args.command == "auth":
        if args.auth_command == "login":
            platforms = getattr(args, "platforms", None)
            results = app.auth_login(platforms)
            for p, ok in results.items():
                print(f"  {p}: {'OK' if ok else 'FAIL'}")
        elif args.auth_command == "status":
            status = app.auth_status()
            for p, ok in status.items():
                print(f"  {p}: {'authenticated' if ok else 'not authenticated'}")
        else:
            build_parser().parse_args(["auth", "--help"])

    elif args.command == "docs":
        ok = app.generate_docs(project_name=project)
        print("[+] Documentation generated" if ok else "[!] Documentation failed")

    elif args.command == "init":
        result = app.init_project(name=args.name)
        print(result)

    elif args.command == "status":
        info = app.status(project_name=project)
        for k, v in info.items():
            print(f"  {k}: {v}")

    elif args.command == "projects":
        projects = app.list_projects()
        if not projects:
            print("No projects found.")
            return
        for p in projects:
            platforms = ", ".join(
                f"{pc.platform.label()}/{pc.repo}" for pc in p.platforms if pc.enabled
            )
            print(f"  {p.name}: {platforms}" if platforms else f"  {p.name}")

    elif args.command == "workflow":
        created = app.generate_ci(
            project_name=project,
            all_projects=getattr(args, "all", False),
        )
        for path in created:
            print(f"[+] Created {path}")

    elif args.command == "install":
        if project:
            deps = app.install_deps(project_name=project)
            for p, ok in deps.items():
                print(f"  {p}: {'available' if ok else 'not found'}")
        else:
            results = app.install_packages(getattr(args, "packages", []) or None)
            if not all(results.values()):
                sys.exit(1)

    elif args.command == "interactive":
        app.interactive_menu()

    elif args.command == "serve":
        from deploynator._mcp_server import MCPServer
        target = getattr(args, "path", ".") or "."
        MCPServer(app, target).run()


if __name__ == "__main__":
    main()
