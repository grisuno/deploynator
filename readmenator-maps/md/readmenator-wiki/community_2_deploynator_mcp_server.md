# deploynator: _mcp_server

*Community 2 | 7 files | cohesion 0.50*

## Definition

This community groups 7 file(s) rooted at `deploynator` with dominant language py (cohesion 0.50). Central symbols: `MCPRequest`, `MCPResource`, `MCPServer`, `MCPTool`, `R`, `TestAppExample`, `TestCliMode`, `TestInitScript`. Core file: `deploynator/_mcp_server.py` (32 symbols). Documented purpose: example: use deploynator programmatically as a library.  Install first:  pip install deploynator Run:            python app.py            # safe: everything bel.

## Files

| File | Language | Layer | Symbols | Doc |
|------|----------|-------|---------|-----|
| `app.py` | py | utility | 1 | yes |
| `deploynator/__init__.py` | py | utility | 0 | no |
| `deploynator/__main__.py` | py | utility | 3 | no |
| `deploynator/_mcp_server.py` | py | utility | 32 | yes |
| `tests/test_cli_mcp.py` | py | testing | 11 | yes |
| `tests/test_init.py` | py | testing | 6 | yes |
| `tests/test_install_example.py` | py | testing | 12 | yes |

## Key Symbols

- `main` (function, `app.py:12`) `def main()`
- `build_parser` (function, `deploynator/__main__.py:17`) `def build_parser()`
- `preprocess_argv` (function, `deploynator/__main__.py:133`) `def preprocess_argv(argv)`
- `main` (function, `deploynator/__main__.py:167`) `def main(argv)`
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
- `definition` (method, `deploynator/_mcp_server.py:79`) `def definition(self)`
- `read` (method, `deploynator/_mcp_server.py:82`) `def read(self)`
- `MCPServer` (class, `deploynator/_mcp_server.py:86`) `class MCPServer`
- `__init__` (method, `deploynator/_mcp_server.py:87`) `def __init__(self, app, target_dir)`
- `register_tool` (method, `deploynator/_mcp_server.py:94`) `def register_tool(self, tool)`
- `register_resource` (method, `deploynator/_mcp_server.py:97`) `def register_resource(self, resource)`
- `_handle_initialize` (method, `deploynator/_mcp_server.py:100`) `def _handle_initialize(self, req)`
- `_handle_list_tools` (method, `deploynator/_mcp_server.py:108`) `def _handle_list_tools(self, req)`
- `_handle_call_tool` (method, `deploynator/_mcp_server.py:111`) `def _handle_call_tool(self, req)`
- `_handle_list_resources` (method, `deploynator/_mcp_server.py:128`) `def _handle_list_resources(self, req)`
- `_handle_read_resource` (method, `deploynator/_mcp_server.py:131`) `def _handle_read_resource(self, req)`
- `dispatch` (method, `deploynator/_mcp_server.py:144`) `def dispatch(self, req)`
- `run` (method, `deploynator/_mcp_server.py:162`) `def run(self)`
- `_register_all` (method, `deploynator/_mcp_server.py:180`) `def _register_all(self)`
- `_tool_release` (method, `deploynator/_mcp_server.py:233`) `def _tool_release(self, project, commit_type, subject, scope, body, bump, dry_ru`

## Internal vs External Edges

- Internal resolved imports (EXTRACTED): 24
- Cross-boundary resolved imports (EXTRACTED): 17

## Connections

- [EXTRACTED] depends_on community 2 <-> 3 (strength 0.9): Extracted import edge crosses communities: app.py imports deploynator/_config.py.
- [EXTRACTED] depends_on community 2 <-> 0 (strength 0.9): Extracted import edge crosses communities: deploynator/__init__.py imports deploynator/_app.py.
- [EXTRACTED] depends_on community 2 <-> 1 (strength 0.9): Extracted import edge crosses communities: tests/test_init.py imports deploynator/_toml.py.
- [INFERRED] bridges community 2 <-> 0 (strength 0.6): Inferred cross-community bridge: app.py reaches tests/test_models.py in 4 hops.
- [INFERRED] bridges community 2 <-> 0 (strength 0.6): Inferred cross-community bridge: tests/test_init.py reaches tests/test_models.py in 4 hops.
- [INFERRED] shares_context community 2 <-> 4 (strength 0.5): Inferred shared context (layer utility) with no import path between community 2 (deploynator: _mcp_server) and community 4 (orphans).

## Risks

- [dataflow UNCHECKED_ALLOC] `tests/test_init.py:36` `test_deploy_sh_content_generic` `content`: Result of allocator stored in `content` is never checked against NULL.
- [dataflow UNCHECKED_ALLOC] `tests/test_install_example.py:65` `test_example_uses_library` `content`: Result of allocator stored in `content` is never checked against NULL.

## Open Questions

- Why do 2 file(s) lack file-level docs (e.g. `deploynator/__init__.py`)? What purpose do they serve?
- What would break if the most connected file in deploynator: _mcp_server changed?
- Should deploynator: _mcp_server be split, given cohesion 0.50?

## Sources

- `app.py`
- `deploynator/__init__.py`
- `deploynator/__main__.py`
- `deploynator/_mcp_server.py`
- `tests/test_cli_mcp.py`
- `tests/test_init.py`
- `tests/test_install_example.py`
