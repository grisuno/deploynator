# deploynator: _platforms

*Community 4 | 5 files | cohesion 0.24*

## Definition

This community groups 5 file(s) rooted at `deploynator` with dominant language py (cohesion 0.24). Central symbols: `BitbucketCLI`, `DeployOrchestrator`, `DeploynatorApp`, `GitHubCLI`, `GitLabCLI`, `GitOperations`, `PlatformClient`, `PlatformFactory`. Core file: `deploynator/_platforms.py` (34 symbols).

## Files

| File | Language | Layer | Symbols | Doc |
|------|----------|-------|---------|-----|
| `deploynator/_app.py` | py | utility | 33 | no |
| `deploynator/_deploy.py` | py | utility | 21 | no |
| `deploynator/_git.py` | py | utility | 24 | no |
| `deploynator/_platforms.py` | py | utility | 34 | no |
| `tests/test_git_sync.py` | py | testing | 6 | no |

## Key Symbols

- `DeploynatorApp` (class, `deploynator/_app.py:18`) `class DeploynatorApp`
- `__init__` (method, `deploynator/_app.py:19`) `def __init__(self, config, workdir)`
- `auth_login` (method, `deploynator/_app.py:29`) `def auth_login(self, platforms)`
- `auth_status` (method, `deploynator/_app.py:43`) `def auth_status(self)`
- `_auth_github` (method, `deploynator/_app.py:54`) `def _auth_github()`
- `_auth_gitlab` (method, `deploynator/_app.py:67`) `def _auth_gitlab()`
- `_auth_bitbucket` (method, `deploynator/_app.py:84`) `def _auth_bitbucket()`
- `init_project` (method, `deploynator/_app.py:172`) `def init_project(self, project_path, name)`
- `start_branch` (method, `deploynator/_app.py:249`) `def start_branch(self, commit_type, description, project_path, project_name, rem`
- `_is_path_like` (method, `deploynator/_app.py:267`) `def _is_path_like(value)`
- `_looks_like_path` (method, `deploynator/_app.py:271`) `def _looks_like_path(value)`
- `_resolve_project_path` (method, `deploynator/_app.py:278`) `def _resolve_project_path(self, project_name)`
- `_smart_prepare` (method, `deploynator/_app.py:292`) `def _smart_prepare(self, base, changelog_content, dry_run)`
- `commit` (method, `deploynator/_app.py:307`) `def commit(self, commit_type, subject, scope, body, project_path, project_name,`
- `_parse_release_message` (method, `deploynator/_app.py:348`) `def _parse_release_message(raw)` - Parsea `test(module): texto` o `test(module) texto` (colon opcional).
- `release` (method, `deploynator/_app.py:366`) `def release(self, commit_type, subject, scope, body, message, project_name, bump`
- `generate_docs` (method, `deploynator/_app.py:502`) `def generate_docs(self, project_path, project_name)`
- `status` (method, `deploynator/_app.py:508`) `def status(self, project_path, project_name)`
- `list_projects` (method, `deploynator/_app.py:528`) `def list_projects(self, search_path)`
- `generate_ci` (method, `deploynator/_app.py:533`) `def generate_ci(self, project_name, all_projects)`
- `install_deps` (method, `deploynator/_app.py:549`) `def install_deps(self, project_name)`
- `install_packages` (method, `deploynator/_app.py:560`) `def install_packages(self, packages)` - pip install/upgrade packages (default: deploynator from PyPI).
- `interactive_menu` (method, `deploynator/_app.py:587`) `def interactive_menu(self)`
- `_interactive_release` (method, `deploynator/_app.py:623`) `def _interactive_release(self)`
- `_interactive_commit` (method, `deploynator/_app.py:669`) `def _interactive_commit(self)`
- `_interactive_start` (method, `deploynator/_app.py:696`) `def _interactive_start(self)`
- `_interactive_auth` (method, `deploynator/_app.py:720`) `def _interactive_auth(self)`
- `_interactive_auth_status` (method, `deploynator/_app.py:743`) `def _interactive_auth_status(self)`
- `_interactive_docs` (method, `deploynator/_app.py:749`) `def _interactive_docs(self)`
- `_interactive_ci` (method, `deploynator/_app.py:756`) `def _interactive_ci(self)`

## Internal vs External Edges

- Internal resolved imports (EXTRACTED): 13
- Cross-boundary resolved imports (EXTRACTED): 35

## Connections

- [EXTRACTED] depends_on community 1 <-> 4 (strength 0.9): Extracted import edge crosses communities: deploynator/__init__.py imports deploynator/_app.py.
- [EXTRACTED] depends_on community 4 <-> 3 (strength 0.9): Extracted import edge crosses communities: deploynator/_app.py imports deploynator/_config.py.
- [EXTRACTED] depends_on community 4 <-> 2 (strength 0.9): Extracted import edge crosses communities: deploynator/_app.py imports deploynator/_models.py.
- [EXTRACTED] depends_on community 4 <-> 0 (strength 0.9): Extracted import edge crosses communities: deploynator/_app.py imports deploynator/_toml.py.
- [INFERRED] shares_context community 4 <-> 5 (strength 0.5): Inferred shared context (layer utility) with no import path between community 4 (deploynator: _platforms) and community 5 (orphans).

## Risks

- [taint high] `deploynator/_app.py` -> `deploynator/_app.py` via `subprocess` (0 hops)
- [taint high] `deploynator/_app.py` -> `deploynator/_toml.py` via `subprocess` (1 hops)
- [taint high] `deploynator/_app.py` -> `deploynator/_deploy.py` via `subprocess` (1 hops)
- [taint high] `deploynator/_app.py` -> `deploynator/_platforms.py` via `subprocess` (1 hops)
- [taint high] `deploynator/_app.py` -> `deploynator/_config.py` via `subprocess` (1 hops)
- [taint high] `deploynator/_app.py` -> `deploynator/_models.py` via `subprocess` (1 hops)
- [taint high] `deploynator/_app.py` -> `deploynator/_git.py` via `subprocess` (1 hops)
- [taint high] `deploynator/_app.py` -> `deploynator/_runner.py` via `subprocess` (2 hops)
- [taint high] `deploynator/_app.py` -> `deploynator/_semver.py` via `subprocess` (2 hops)
- [taint high] `deploynator/_app.py` -> `deploynator/_pypi.py` via `subprocess` (2 hops)
- [taint high] `deploynator/_app.py` -> `deploynator/_docs.py` via `subprocess` (2 hops)
- [taint high] `deploynator/_app.py` -> `deploynator/_changelog.py` via `subprocess` (2 hops)
- [taint high] `deploynator/_app.py` -> `deploynator/_readme.py` via `subprocess` (2 hops)
- [taint high] `deploynator/_app.py` -> `deploynator/_app.py` via `subprocess` (0 hops)
- [taint high] `deploynator/_app.py` -> `deploynator/_toml.py` via `subprocess` (1 hops)

## Open Questions

- Why do 5 file(s) lack file-level docs (e.g. `deploynator/_app.py`)? What purpose do they serve?
- Is the dangerous import `subprocess` in `deploynator/_app.py` still required, or can it be isolated?
- What would break if the most connected file in deploynator: _platforms changed?
- Should deploynator: _platforms be split, given cohesion 0.24?

## Sources

- `deploynator/_app.py`
- `deploynator/_deploy.py`
- `deploynator/_git.py`
- `deploynator/_platforms.py`
- `tests/test_git_sync.py`
