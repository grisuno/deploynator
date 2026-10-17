#!/usr/bin/env python3
"""app.py -- example: use deploynator programmatically as a library.

Install first:  pip install deploynator
Run:            python app.py            # safe: everything below is dry-run
"""

from deploynator import DeploynatorApp
from deploynator._config import Config


def main() -> None:
    app = DeploynatorApp(Config.create())

    # 1. Discover configured projects (projects/*.yaml)
    print("== projects ==")
    for p in app.list_projects():
        print(f"  {p.name}: {p.path or '(cwd)'}")

    # 2. Repo status (accepts a project name or a filesystem path)
    print("== status ==")
    for key, value in app.status().items():
        print(f"  {key}: {value}")

    # 3. Preview a release (no mutations: tests/docs/push simulated)
    print("== release preview ==")
    for result in app.release(
        commit_type="patch",
        subject="example preview",
        dry_run=True,
        no_pypi=True,
    ):
        print(f"  [{('OK' if result.success else 'FAIL')}] "
              f"{result.project} v{result.version} {result.error or ''}")

    # 4. Real release (uncomment to actually deploy):
    # results = app.release(commit_type="feat", subject="add login")
    # for r in results:
    #     print(r)

    # 5. Docs via readmenator / conventional commit / branch (dry-run):
    # app.generate_docs()
    # print(app.commit("feat", "add login", scope="auth", dry_run=True))
    # print(app.start_branch("feat", "add-login"))


if __name__ == "__main__":
    main()
