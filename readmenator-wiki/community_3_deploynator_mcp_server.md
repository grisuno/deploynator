# deploynator: _mcp_server

*Community 3 | 5 files | cohesion 0.47*

## Definition

This community groups 5 file(s) rooted at `deploynator` with dominant language py (cohesion 0.47). Central symbols: `MCPRequest`, `MCPResource`, `MCPServer`, `MCPTool`, `TestCliMode`, `TestInitScript`, `TestMCPServer`, `__init__`. Core file: `deploynator/_mcp_server.py` (32 symbols). Documented purpose: MCP (Model Context Protocol) stdio server for deploynator.  Exposes headless deploy operations as MCP tools so AI harnesses (claude code, codex, opencode) can r.

## Files

| File | Language | Layer | Symbols | Doc |
|------|----------|-------|---------|-----|
| `deploynator/__init__.py` | py | utility | 0 | no |
| `deploynator/__main__.py` | py | utility | 3 | no |
| `deploynator/_mcp_server.py` | py | utility | 32 | yes |
| `tests/test_cli_mcp.py` | py | testing | 11 | yes |
| `tests/test_init.py` | py | testing | 6 | yes |

## Key Symbols

- `build_parser` (function, `deploynator/__main__.py:17`) `def build_parser()`
- `preprocess_argv` (function, `deploynator/__main__.py:130`) `def preprocess_argv(argv)`
- `main` (function, `deploynator/__main__.py:164`) `def main(argv)`
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
- `_tool_commit` (method, `deploynator/_mcp_server.py:248`) `def _tool_commit(self, commit_type, subject, project, scope, body, dry_run)`

## Internal vs External Edges

- Internal resolved imports (EXTRACTED): 18
- Cross-boundary resolved imports (EXTRACTED): 13

## Connections

- [EXTRACTED] depends_on community 3 <-> 4 (strength 0.9): Extracted import edge crosses communities: deploynator/__init__.py imports deploynator/_app.py.
- [EXTRACTED] depends_on community 3 <-> 0 (strength 0.9): Extracted import edge crosses communities: deploynator/__main__.py imports deploynator/_config.py.
- [EXTRACTED] depends_on community 3 <-> 2 (strength 0.9): Extracted import edge crosses communities: deploynator/__main__.py imports deploynator/_models.py.
- [EXTRACTED] depends_on community 3 <-> 1 (strength 0.9): Extracted import edge crosses communities: tests/test_init.py imports deploynator/_toml.py.
- [INFERRED] bridges community 3 <-> 0 (strength 0.7): Inferred cross-community bridge: deploynator/__init__.py reaches deploynator/_changelog.py in 3 hops.
- [INFERRED] bridges community 3 <-> 2 (strength 0.6): Inferred cross-community bridge: tests/test_init.py reaches tests/test_models.py in 4 hops.
- [INFERRED] shares_context community 3 <-> 5 (strength 0.5): Inferred shared context (language py and layer utility) with no import path between community 3 (deploynator: _mcp_server) and community 5 (orphans).

## Risks

- [dataflow UNCHECKED_ALLOC] `tests/test_init.py:36` `test_deploy_sh_content_generic` `content`: Result of allocator stored in `content` is never checked against NULL.

## Open Questions

- Why do 2 file(s) lack file-level docs (e.g. `deploynator/__init__.py`)? What purpose do they serve?
- What would break if the most connected file in deploynator: _mcp_server changed?
- Should deploynator: _mcp_server be split, given cohesion 0.47?

## Sources

- `deploynator/__init__.py`
- `deploynator/__main__.py`
- `deploynator/_mcp_server.py`
- `tests/test_cli_mcp.py`
- `tests/test_init.py`
