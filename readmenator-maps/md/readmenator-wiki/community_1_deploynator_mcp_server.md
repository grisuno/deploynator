# deploynator: _mcp_server

*Community 1 | 7 files | cohesion 0.50*

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
- `build_parser` (function, `deploynator/__main__.py:16`) `def build_parser()`
- `preprocess_argv` (function, `deploynator/__main__.py:144`) `def preprocess_argv(argv)`
- `main` (function, `deploynator/__main__.py:178`) `def main(argv)`
- `MCPRequest` (class, `deploynator/_mcp_server.py:36`) `class MCPRequest`
- `__init__` (method, `deploynator/_mcp_server.py:37`) `def __init__(self, msg)`
- `is_notification` (method, `deploynator/_mcp_server.py:44`) `def is_notification(self)`
- `response` (method, `deploynator/_mcp_server.py:47`) `def response(self, result)`
- `error` (method, `deploynator/_mcp_server.py:50`) `def error(self, code, message, data)`
- `MCPTool` (class, `deploynator/_mcp_server.py:57`) `class MCPTool`
- `__init__` (method, `deploynator/_mcp_server.py:58`) `def __init__(self, name, description, handler, input_schema)`
- `definition` (method, `deploynator/_mcp_server.py:65`) `def definition(self)`
- `call` (method, `deploynator/_mcp_server.py:68`) `def call(self, arguments)`
- `MCPResource` (class, `deploynator/_mcp_server.py:72`) `class MCPResource`
- `__init__` (method, `deploynator/_mcp_server.py:73`) `def __init__(self, uri, name, description, mime_type, handler)`
- `definition` (method, `deploynator/_mcp_server.py:80`) `def definition(self)`
- `read` (method, `deploynator/_mcp_server.py:83`) `def read(self)`
- `MCPServer` (class, `deploynator/_mcp_server.py:87`) `class MCPServer`
- `__init__` (method, `deploynator/_mcp_server.py:88`) `def __init__(self, app, target_dir)`
- `register_tool` (method, `deploynator/_mcp_server.py:95`) `def register_tool(self, tool)`
- `register_resource` (method, `deploynator/_mcp_server.py:98`) `def register_resource(self, resource)`
- `_handle_initialize` (method, `deploynator/_mcp_server.py:101`) `def _handle_initialize(self, req)`
- `_handle_list_tools` (method, `deploynator/_mcp_server.py:109`) `def _handle_list_tools(self, req)`
- `_handle_call_tool` (method, `deploynator/_mcp_server.py:112`) `def _handle_call_tool(self, req)`
- `_handle_list_resources` (method, `deploynator/_mcp_server.py:129`) `def _handle_list_resources(self, req)`
- `_handle_read_resource` (method, `deploynator/_mcp_server.py:132`) `def _handle_read_resource(self, req)`
- `dispatch` (method, `deploynator/_mcp_server.py:145`) `def dispatch(self, req)`
- `run` (method, `deploynator/_mcp_server.py:163`) `def run(self)`
- `_register_all` (method, `deploynator/_mcp_server.py:181`) `def _register_all(self)`
- `_tool_release` (method, `deploynator/_mcp_server.py:235`) `def _tool_release(self, project, commit_type, subject, message, scope, body, bum`

## Internal vs External Edges

- Internal resolved imports (EXTRACTED): 24
- Cross-boundary resolved imports (EXTRACTED): 17

## Connections

- [EXTRACTED] depends_on community 1 <-> 3 (strength 0.9): Extracted import edge crosses communities: app.py imports deploynator/_config.py.
- [EXTRACTED] depends_on community 1 <-> 4 (strength 0.9): Extracted import edge crosses communities: deploynator/__init__.py imports deploynator/_app.py.
- [EXTRACTED] depends_on community 1 <-> 2 (strength 0.9): Extracted import edge crosses communities: deploynator/__main__.py imports deploynator/_models.py.
- [EXTRACTED] depends_on community 1 <-> 0 (strength 0.9): Extracted import edge crosses communities: tests/test_init.py imports deploynator/_toml.py.
- [INFERRED] bridges community 1 <-> 2 (strength 0.6): Inferred cross-community bridge: app.py reaches tests/test_models.py in 4 hops.
- [INFERRED] bridges community 1 <-> 2 (strength 0.6): Inferred cross-community bridge: tests/test_init.py reaches tests/test_models.py in 4 hops.
- [INFERRED] shares_context community 1 <-> 5 (strength 0.5): Inferred shared context (layer utility) with no import path between community 1 (deploynator: _mcp_server) and community 5 (orphans).

## Risks

- No scoped security, taint, cycle, or layer risks.

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
