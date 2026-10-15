# deploynator: _mcp_server

*Community 0 | 11 files | cohesion 0.47*

## Definition

This community groups 11 file(s) rooted at `deploynator` with dominant language py (cohesion 0.47). Central symbols: `ChangelogGenerator`, `Config`, `MCPRequest`, `MCPResource`, `MCPServer`, `MCPTool`, `R`, `TestAppExample`. Core file: `deploynator/_mcp_server.py` (32 symbols). Documented purpose: example: use deploynator programmatically as a library.  Install first:  pip install deploynator Run:            python app.py            # safe: everything bel.

## Files

| File | Language | Layer | Symbols | Doc |
|------|----------|-------|---------|-----|
| `app.py` | py | utility | 1 | yes |
| `deploynator/__init__.py` | py | utility | 0 | no |
| `deploynator/__main__.py` | py | utility | 3 | no |
| `deploynator/_changelog.py` | py | utility | 9 | no |
| `deploynator/_config.py` | py | infrastructure | 6 | no |
| `deploynator/_mcp_server.py` | py | utility | 32 | yes |
| `tests/test_changelog.py` | py | testing | 8 | no |
| `tests/test_cli_mcp.py` | py | testing | 11 | yes |
| `tests/test_config.py` | py | testing | 10 | no |
| `tests/test_init.py` | py | testing | 6 | yes |
| `tests/test_install_example.py` | py | testing | 12 | yes |

## Key Symbols

- `main` (function, `app.py:12`) `def main()`
- `build_parser` (function, `deploynator/__main__.py:17`) `def build_parser()`
- `preprocess_argv` (function, `deploynator/__main__.py:133`) `def preprocess_argv(argv)`
- `main` (function, `deploynator/__main__.py:167`) `def main(argv)`
- `ChangelogGenerator` (class, `deploynator/_changelog.py:12`) `class ChangelogGenerator`
- `__init__` (method, `deploynator/_changelog.py:13`) `def __init__(self, config)`
- `generate_from_log` (method, `deploynator/_changelog.py:16`) `def generate_from_log(self, repo_path, from_ref, to_ref)`
- `generate_from_messages` (method, `deploynator/_changelog.py:25`) `def generate_from_messages(self, messages)`
- `generate_header` (method, `deploynator/_changelog.py:45`) `def generate_header(self)`
- `_collect_entries` (method, `deploynator/_changelog.py:48`) `def _collect_entries(self, repo_path, from_ref, to_ref)`
- `_format_entries` (method, `deploynator/_changelog.py:69`) `def _format_entries(self, entries)`
- `write_changelog` (method, `deploynator/_changelog.py:100`) `def write_changelog(self, repo_path, content, filename)`
- `format_for_release` (method, `deploynator/_changelog.py:110`) `def format_for_release(self, changelog_content, max_chars)`
- `Config` (class, `deploynator/_config.py:8`) `class Config`
- `create` (method, `deploynator/_config.py:79`) `def create(overrides)`
- `resolve_path` (method, `deploynator/_config.py:85`) `def resolve_path(self)`
- `gh_authd` (method, `deploynator/_config.py:91`) `def gh_authd(self)`
- `glab_authd` (method, `deploynator/_config.py:95`) `def glab_authd(self)`
- `bb_authd` (method, `deploynator/_config.py:99`) `def bb_authd(self)`
- `MCPRequest` (class, `deploynator/_mcp_server.py:35`) `class MCPRequest`
- `__init__` (method, `deploynator/_mcp_server.py:36`) `def __init__(self, msg)`
- `is_notification` (method, `deploynator/_mcp_server.py:43`) `def is_notification(self)`
- `response` (method, `deploynator/_mcp_server.py:46`) `def response(self, result)`
- `error` (method, `deploynator/_mcp_server.py:49`) `def error(self, code, message, data)`
- `MCPTool` (class, `deploynator/_mcp_server.py:56`) `class MCPTool`
- `__init__` (method, `deploynator/_mcp_server.py:57`) `def __init__(self, name, description, handler, input_schema)`
- `definition` (method, `deploynator/_mcp_server.py:64`) `def definition(self)`
- `call` (method, `deploynator/_mcp_server.py:67`) `def call(self, arguments)`
- `MCPResource` (class, `deploynator/_mcp_server.py:71`) `class MCPResource`
- `__init__` (method, `deploynator/_mcp_server.py:72`) `def __init__(self, uri, name, description, mime_type, handler)`

## Internal vs External Edges

- Internal resolved imports (EXTRACTED): 40
- Cross-boundary resolved imports (EXTRACTED): 57

## Connections

- [EXTRACTED] depends_on community 0 <-> 1 (strength 0.9): Extracted import edge crosses communities: deploynator/__init__.py imports deploynator/_app.py.
- [EXTRACTED] depends_on community 2 <-> 0 (strength 0.9): Extracted import edge crosses communities: deploynator/_docs.py imports deploynator/_config.py.
- [INFERRED] bridges community 0 <-> 1 (strength 0.6): Inferred cross-community bridge: app.py reaches tests/test_models.py in 4 hops.
- [INFERRED] bridges community 0 <-> 1 (strength 0.6): Inferred cross-community bridge: tests/test_config.py reaches tests/test_models.py in 4 hops.
- [INFERRED] bridges community 0 <-> 1 (strength 0.6): Inferred cross-community bridge: tests/test_init.py reaches tests/test_models.py in 4 hops.

## Risks

- [taint high] `deploynator/_app.py` -> `deploynator/_config.py` via `subprocess` (1 hops)
- [taint high] `deploynator/_app.py` -> `deploynator/_changelog.py` via `subprocess` (2 hops)
- [taint high] `deploynator/_app.py` -> `deploynator/_config.py` via `subprocess` (1 hops)
- [dataflow UNCHECKED_ALLOC] `tests/test_init.py:36` `test_deploy_sh_content_generic` `content`: Result of allocator stored in `content` is never checked against NULL.
- [dataflow UNCHECKED_ALLOC] `tests/test_install_example.py:65` `test_example_uses_library` `content`: Result of allocator stored in `content` is never checked against NULL.

## Open Questions

- Why do 6 file(s) lack file-level docs (e.g. `deploynator/__init__.py`)? What purpose do they serve?
- What would break if the most connected file in deploynator: _mcp_server changed?
- Should deploynator: _mcp_server be split, given cohesion 0.47?

## Sources

- `app.py`
- `deploynator/__init__.py`
- `deploynator/__main__.py`
- `deploynator/_changelog.py`
- `deploynator/_config.py`
- `deploynator/_mcp_server.py`
- `tests/test_changelog.py`
- `tests/test_cli_mcp.py`
- `tests/test_config.py`
- `tests/test_init.py`
- `tests/test_install_example.py`
