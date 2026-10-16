# deploynator: _platforms

*Community 0 | 11 files | cohesion 0.45*

## Definition

This community groups 11 file(s) rooted at `deploynator` with dominant language py (cohesion 0.45). Central symbols: `BitbucketCLI`, `ChangelogEntry`, `CommitMessage`, `CommitType`, `DeployOrchestrator`, `DeployResult`, `DeploynatorApp`, `GitHubCLI`. Core file: `tests/test_models.py` (44 symbols). Documented purpose: Path-direct deploy + tag prefijos + version_file toml (ReadMenator real)..

## Files

| File | Language | Layer | Symbols | Doc |
|------|----------|-------|---------|-----|
| `deploynator/_app.py` | py | utility | 32 | no |
| `deploynator/_deploy.py` | py | utility | 20 | no |
| `deploynator/_git.py` | py | utility | 21 | no |
| `deploynator/_models.py` | py | business_logic | 27 | no |
| `deploynator/_platforms.py` | py | utility | 34 | no |
| `deploynator/_semver.py` | py | utility | 9 | no |
| `tests/test_deploy.py` | py | testing | 11 | no |
| `tests/test_models.py` | py | testing | 44 | no |
| `tests/test_path_deploy.py` | py | testing | 10 | yes |
| `tests/test_pipeline.py` | py | testing | 12 | yes |
| `tests/test_semver.py` | py | testing | 11 | no |

## Key Symbols

- `DeploynatorApp` (class, `deploynator/_app.py:20`) `class DeploynatorApp`
- `__init__` (method, `deploynator/_app.py:21`) `def __init__(self, config, workdir)`
- `auth_login` (method, `deploynator/_app.py:31`) `def auth_login(self, platforms)`
- `auth_status` (method, `deploynator/_app.py:45`) `def auth_status(self)`
- `_auth_github` (method, `deploynator/_app.py:56`) `def _auth_github()`
- `_auth_gitlab` (method, `deploynator/_app.py:69`) `def _auth_gitlab()`
- `_auth_bitbucket` (method, `deploynator/_app.py:86`) `def _auth_bitbucket()`
- `init_project` (method, `deploynator/_app.py:170`) `def init_project(self, project_path, name)`
- `start_branch` (method, `deploynator/_app.py:247`) `def start_branch(self, commit_type, description, project_path, project_name, rem`
- `_is_path_like` (method, `deploynator/_app.py:265`) `def _is_path_like(value)`
- `_looks_like_path` (method, `deploynator/_app.py:269`) `def _looks_like_path(value)`
- `_resolve_project_path` (method, `deploynator/_app.py:276`) `def _resolve_project_path(self, project_name)`
- `_smart_prepare` (method, `deploynator/_app.py:290`) `def _smart_prepare(self, base, changelog_content, dry_run)`
- `commit` (method, `deploynator/_app.py:305`) `def commit(self, commit_type, subject, scope, body, project_path, project_name,`
- `release` (method, `deploynator/_app.py:345`) `def release(self, commit_type, subject, scope, body, project_name, bump, dry_run`
- `generate_docs` (method, `deploynator/_app.py:435`) `def generate_docs(self, project_path, project_name)`
- `status` (method, `deploynator/_app.py:441`) `def status(self, project_path, project_name)`
- `list_projects` (method, `deploynator/_app.py:461`) `def list_projects(self, search_path)`
- `generate_ci` (method, `deploynator/_app.py:466`) `def generate_ci(self, project_name, all_projects)`
- `install_deps` (method, `deploynator/_app.py:482`) `def install_deps(self, project_name)`
- `install_packages` (method, `deploynator/_app.py:493`) `def install_packages(self, packages)` - pip install/upgrade packages (default: deploynator from PyPI).
- `interactive_menu` (method, `deploynator/_app.py:521`) `def interactive_menu(self)`
- `_interactive_release` (method, `deploynator/_app.py:557`) `def _interactive_release(self)`
- `_interactive_commit` (method, `deploynator/_app.py:599`) `def _interactive_commit(self)`
- `_interactive_start` (method, `deploynator/_app.py:626`) `def _interactive_start(self)`
- `_interactive_auth` (method, `deploynator/_app.py:650`) `def _interactive_auth(self)`
- `_interactive_auth_status` (method, `deploynator/_app.py:673`) `def _interactive_auth_status(self)`
- `_interactive_docs` (method, `deploynator/_app.py:679`) `def _interactive_docs(self)`
- `_interactive_ci` (method, `deploynator/_app.py:686`) `def _interactive_ci(self)`
- `_interactive_status` (method, `deploynator/_app.py:695`) `def _interactive_status(self)`

## Internal vs External Edges

- Internal resolved imports (EXTRACTED): 39
- Cross-boundary resolved imports (EXTRACTED): 41

## Connections

- [EXTRACTED] depends_on community 2 <-> 0 (strength 0.9): Extracted import edge crosses communities: deploynator/__init__.py imports deploynator/_app.py.
- [EXTRACTED] depends_on community 0 <-> 3 (strength 0.9): Extracted import edge crosses communities: deploynator/_app.py imports deploynator/_config.py.
- [EXTRACTED] depends_on community 0 <-> 1 (strength 0.9): Extracted import edge crosses communities: deploynator/_app.py imports deploynator/_toml.py.
- [INFERRED] bridges community 2 <-> 0 (strength 0.6): Inferred cross-community bridge: app.py reaches tests/test_models.py in 4 hops.
- [INFERRED] bridges community 3 <-> 0 (strength 0.6): Inferred cross-community bridge: tests/test_config.py reaches tests/test_models.py in 4 hops.
- [INFERRED] bridges community 2 <-> 0 (strength 0.6): Inferred cross-community bridge: tests/test_init.py reaches tests/test_models.py in 4 hops.
- [INFERRED] bridges community 0 <-> 3 (strength 0.6): Inferred cross-community bridge: tests/test_models.py reaches tests/test_readme_footer.py in 4 hops.
- [INFERRED] bridges community 0 <-> 1 (strength 0.6): Inferred cross-community bridge: tests/test_models.py reaches tests/test_runner.py in 4 hops.

## Risks

- [taint high] `deploynator/_app.py` -> `deploynator/_app.py` via `subprocess` (0 hops)
- [taint high] `deploynator/_app.py` -> `deploynator/_models.py` via `subprocess` (1 hops)
- [taint high] `deploynator/_app.py` -> `deploynator/_deploy.py` via `subprocess` (1 hops)
- [taint high] `deploynator/_app.py` -> `deploynator/_platforms.py` via `subprocess` (1 hops)
- [taint high] `deploynator/_app.py` -> `deploynator/_config.py` via `subprocess` (1 hops)
- [taint high] `deploynator/_app.py` -> `deploynator/_git.py` via `subprocess` (1 hops)
- [taint high] `deploynator/_app.py` -> `deploynator/_toml.py` via `subprocess` (1 hops)
- [taint high] `deploynator/_app.py` -> `deploynator/_runner.py` via `subprocess` (2 hops)
- [taint high] `deploynator/_app.py` -> `deploynator/_readme.py` via `subprocess` (2 hops)
- [taint high] `deploynator/_app.py` -> `deploynator/_changelog.py` via `subprocess` (2 hops)
- [taint high] `deploynator/_app.py` -> `deploynator/_docs.py` via `subprocess` (2 hops)
- [taint high] `deploynator/_app.py` -> `deploynator/_semver.py` via `subprocess` (2 hops)
- [taint high] `deploynator/_app.py` -> `deploynator/_pypi.py` via `subprocess` (2 hops)
- [taint high] `deploynator/_app.py` -> `deploynator/_app.py` via `subprocess` (0 hops)
- [taint high] `deploynator/_app.py` -> `deploynator/_models.py` via `subprocess` (1 hops)

## Open Questions

- Why do 9 file(s) lack file-level docs (e.g. `deploynator/_app.py`)? What purpose do they serve?
- Is the dangerous import `subprocess` in `deploynator/_app.py` still required, or can it be isolated?
- What would break if the most connected file in deploynator: _platforms changed?
- Should deploynator: _platforms be split, given cohesion 0.45?

## Sources

- `deploynator/_app.py`
- `deploynator/_deploy.py`
- `deploynator/_git.py`
- `deploynator/_models.py`
- `deploynator/_platforms.py`
- `deploynator/_semver.py`
- `tests/test_deploy.py`
- `tests/test_models.py`
- `tests/test_path_deploy.py`
- `tests/test_pipeline.py`
- `tests/test_semver.py`
