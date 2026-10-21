# deploynator: _receipt

*Community 2 | 7 files | cohesion 0.26*

## Definition

This community groups 7 file(s) rooted at `deploynator` with dominant language py (cohesion 0.26). Central symbols: `BitbucketCLI`, `CommandRecord`, `DeployOrchestrator`, `DeploynatorApp`, `EdgeRecord`, `GitHubCLI`, `GitLabCLI`, `GitOperations`. Core file: `tests/test_receipt.py` (47 symbols). Documented purpose: Receipt contract: operational trace of a deploynator release.  Evidence hierarchy (golden rule): Fact      = step observed at runtime (exit_code recorded)      .

## Files

| File | Language | Layer | Symbols | Doc |
|------|----------|-------|---------|-----|
| `deploynator/_app.py` | py | utility | 33 | no |
| `deploynator/_deploy.py` | py | utility | 23 | no |
| `deploynator/_git.py` | py | utility | 25 | no |
| `deploynator/_platforms.py` | py | utility | 36 | no |
| `deploynator/_receipt.py` | py | utility | 43 | yes |
| `tests/test_git_sync.py` | py | testing | 6 | no |
| `tests/test_receipt.py` | py | testing | 47 | no |

## Key Symbols

- `DeploynatorApp` (class, `deploynator/_app.py:18`) `class DeploynatorApp`
- `__init__` (method, `deploynator/_app.py:19`) `def __init__(self, config, workdir)`
- `auth_login` (method, `deploynator/_app.py:29`) `def auth_login(self, platforms)`
- `auth_status` (method, `deploynator/_app.py:43`) `def auth_status(self)`
- `_auth_github` (method, `deploynator/_app.py:54`) `def _auth_github()`
- `_auth_gitlab` (method, `deploynator/_app.py:67`) `def _auth_gitlab()`
- `_auth_bitbucket` (method, `deploynator/_app.py:84`) `def _auth_bitbucket()`
- `init_project` (method, `deploynator/_app.py:185`) `def init_project(self, project_path, name)`
- `start_branch` (method, `deploynator/_app.py:262`) `def start_branch(self, commit_type, description, project_path, project_name, rem`
- `_is_path_like` (method, `deploynator/_app.py:280`) `def _is_path_like(value)`
- `_looks_like_path` (method, `deploynator/_app.py:284`) `def _looks_like_path(value)`
- `_resolve_project_path` (method, `deploynator/_app.py:291`) `def _resolve_project_path(self, project_name)`
- `_smart_prepare` (method, `deploynator/_app.py:303`) `def _smart_prepare(self, base, changelog_content, dry_run)`
- `commit` (method, `deploynator/_app.py:318`) `def commit(self, commit_type, subject, scope, body, project_path, project_name,`
- `_parse_release_message` (method, `deploynator/_app.py:359`) `def _parse_release_message(raw)` - Parsea `test(module): texto` o `test(module) texto` (colon opcional).
- `release` (method, `deploynator/_app.py:377`) `def release(self, commit_type, subject, scope, body, message, project_name, bump`
- `generate_docs` (method, `deploynator/_app.py:519`) `def generate_docs(self, project_path, project_name)`
- `status` (method, `deploynator/_app.py:525`) `def status(self, project_path, project_name)`
- `list_projects` (method, `deploynator/_app.py:545`) `def list_projects(self, search_path)`
- `generate_ci` (method, `deploynator/_app.py:550`) `def generate_ci(self, project_name, all_projects)`
- `install_deps` (method, `deploynator/_app.py:566`) `def install_deps(self, project_name)`
- `install_packages` (method, `deploynator/_app.py:577`) `def install_packages(self, packages)` - pip install/upgrade packages (default: deploynator from PyPI).
- `interactive_menu` (method, `deploynator/_app.py:604`) `def interactive_menu(self)`
- `_interactive_release` (method, `deploynator/_app.py:640`) `def _interactive_release(self)`
- `_interactive_commit` (method, `deploynator/_app.py:688`) `def _interactive_commit(self)`
- `_interactive_start` (method, `deploynator/_app.py:715`) `def _interactive_start(self)`
- `_interactive_auth` (method, `deploynator/_app.py:739`) `def _interactive_auth(self)`
- `_interactive_auth_status` (method, `deploynator/_app.py:762`) `def _interactive_auth_status(self)`
- `_interactive_docs` (method, `deploynator/_app.py:768`) `def _interactive_docs(self)`
- `_interactive_ci` (method, `deploynator/_app.py:775`) `def _interactive_ci(self)`

## Internal vs External Edges

- Internal resolved imports (EXTRACTED): 16
- Cross-boundary resolved imports (EXTRACTED): 44

## Connections

- [EXTRACTED] depends_on community 1 <-> 2 (strength 0.9): Extracted import edge crosses communities: deploynator/__init__.py imports deploynator/_app.py.
- [EXTRACTED] depends_on community 2 <-> 4 (strength 0.9): Extracted import edge crosses communities: deploynator/_app.py imports deploynator/_config.py.
- [EXTRACTED] depends_on community 2 <-> 3 (strength 0.9): Extracted import edge crosses communities: deploynator/_app.py imports deploynator/_models.py.
- [EXTRACTED] depends_on community 2 <-> 0 (strength 0.9): Extracted import edge crosses communities: deploynator/_app.py imports deploynator/_toml.py.
- [INFERRED] shares_context community 2 <-> 5 (strength 0.5): Inferred shared context (layer utility) with no import path between community 2 (deploynator: _receipt) and community 5 (orphans).

## Risks

- [taint high] `deploynator/_app.py` -> `deploynator/_app.py` via `subprocess` (0 hops)
- [taint high] `deploynator/_app.py` -> `deploynator/_models.py` via `subprocess` (1 hops)
- [taint high] `deploynator/_app.py` -> `deploynator/_deploy.py` via `subprocess` (1 hops)
- [taint high] `deploynator/_app.py` -> `deploynator/_config.py` via `subprocess` (1 hops)
- [taint high] `deploynator/_app.py` -> `deploynator/_toml.py` via `subprocess` (1 hops)
- [taint high] `deploynator/_app.py` -> `deploynator/_git.py` via `subprocess` (1 hops)
- [taint high] `deploynator/_app.py` -> `deploynator/_platforms.py` via `subprocess` (1 hops)
- [taint high] `deploynator/_app.py` -> `deploynator/_pypi.py` via `subprocess` (2 hops)
- [taint high] `deploynator/_app.py` -> `deploynator/_changelog.py` via `subprocess` (2 hops)
- [taint high] `deploynator/_app.py` -> `deploynator/_runner.py` via `subprocess` (2 hops)
- [taint high] `deploynator/_app.py` -> `deploynator/_docs.py` via `subprocess` (2 hops)
- [taint high] `deploynator/_app.py` -> `deploynator/_receipt.py` via `subprocess` (2 hops)
- [taint high] `deploynator/_app.py` -> `deploynator/_deb.py` via `subprocess` (2 hops)
- [taint high] `deploynator/_app.py` -> `deploynator/_readme.py` via `subprocess` (2 hops)
- [taint high] `deploynator/_app.py` -> `deploynator/_semver.py` via `subprocess` (2 hops)

## Open Questions

- Why do 6 file(s) lack file-level docs (e.g. `deploynator/_app.py`)? What purpose do they serve?
- Is the dangerous import `subprocess` in `deploynator/_app.py` still required, or can it be isolated?
- What would break if the most connected file in deploynator: _receipt changed?
- Should deploynator: _receipt be split, given cohesion 0.26?

## Sources

- `deploynator/_app.py`
- `deploynator/_deploy.py`
- `deploynator/_git.py`
- `deploynator/_platforms.py`
- `deploynator/_receipt.py`
- `tests/test_git_sync.py`
- `tests/test_receipt.py`
