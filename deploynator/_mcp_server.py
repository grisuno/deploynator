"""MCP (Model Context Protocol) stdio server for deploynator.

Exposes headless deploy operations as MCP tools so AI harnesses
(claude code, codex, opencode) can release without interactive prompts.

Tools:
  deploynator.release  — full pipeline (tests gate, docs, semver, tag, push)
  deploynator.commit   — conventional commit only
  deploynator.status   — repo status JSON
  deploynator.projects — list discovered projects
  deploynator.docs     — regenerate docs via readmenator

Resources:
  deploynator://projects — discovered projects JSON
  deploynator://status   — status JSON

Rule: bare `deploynator` (no args) = interactive menu.
Any flags = headless. MCP tools always headless (dry_run supported).
"""

from __future__ import annotations

import json
import logging
import sys
from typing import Any, Callable, Dict, Optional

logger = logging.getLogger(__name__)

METHOD_NOT_FOUND = -32601
INVALID_PARAMS = -32602
INTERNAL_ERROR = -32603


class MCPRequest:
    def __init__(self, msg: Dict[str, Any]):
        self.jsonrpc = msg.get("jsonrpc", "2.0")
        self.id: Any = msg.get("id")
        self.method: str = msg.get("method", "")
        self.params: Any = msg.get("params", {})

    @property
    def is_notification(self) -> bool:
        return self.id is None

    def response(self, result: Any = None) -> Dict[str, Any]:
        return {"jsonrpc": "2.0", "id": self.id, "result": result}

    def error(self, code: int, message: str, data: Any = None) -> Dict[str, Any]:
        err: Dict[str, Any] = {"jsonrpc": "2.0", "id": self.id, "error": {"code": code, "message": message}}
        if data is not None:
            err["error"]["data"] = data
        return err


class MCPTool:
    def __init__(self, name: str, description: str, handler: Callable,
                 input_schema: Optional[Dict[str, Any]] = None):
        self.name = name
        self.description = description
        self.handler = handler
        self.input_schema = input_schema or {"type": "object", "properties": {}}

    def definition(self) -> Dict[str, Any]:
        return {"name": self.name, "description": self.description, "inputSchema": self.input_schema}

    def call(self, arguments: Dict[str, Any]) -> Any:
        return self.handler(**arguments)


class MCPResource:
    def __init__(self, uri: str, name: str, description: str, mime_type: str, handler: Callable):
        self.uri = uri
        self.name = name
        self.description = description
        self.mime_type = mime_type
        self.handler = handler

    def definition(self) -> Dict[str, Any]:
        return {"uri": self.uri, "name": self.name, "description": self.description, "mimeType": self.mime_type}

    def read(self) -> Any:
        return self.handler()


class MCPServer:
    def __init__(self, app: Any, target_dir: str):
        self._app = app
        self._target_dir = target_dir
        self._tools: Dict[str, MCPTool] = {}
        self._resources: Dict[str, MCPResource] = {}
        self._initialized = False

    def register_tool(self, tool: MCPTool) -> None:
        self._tools[tool.name] = tool

    def register_resource(self, resource: MCPResource) -> None:
        self._resources[resource.uri] = resource

    def _handle_initialize(self, req: MCPRequest) -> Dict[str, Any]:
        self._initialized = True
        return req.response({
            "protocolVersion": "2024-11-05",
            "serverInfo": {"name": "deploynator", "version": "1.0.0"},
            "capabilities": {"tools": {}, "resources": {}},
        })

    def _handle_list_tools(self, req: MCPRequest) -> Dict[str, Any]:
        return req.response({"tools": [t.definition() for t in self._tools.values()]})

    def _handle_call_tool(self, req: MCPRequest) -> Dict[str, Any]:
        name = req.params.get("name", "")
        arguments = req.params.get("arguments", {})
        tool = self._tools.get(name)
        if not tool:
            return req.error(METHOD_NOT_FOUND, f"Tool not found: {name}")
        try:
            result = tool.call(arguments or {})
            if not isinstance(result, str):
                result = json.dumps(result, indent=2, default=str)
            return req.response({"content": [{"type": "text", "text": result}], "isError": False})
        except TypeError as e:
            return req.error(INVALID_PARAMS, f"Invalid arguments: {e}")
        except Exception as e:
            logger.exception("Tool call failed: %s", name)
            return req.error(INTERNAL_ERROR, str(e))

    def _handle_list_resources(self, req: MCPRequest) -> Dict[str, Any]:
        return req.response({"resources": [r.definition() for r in self._resources.values()]})

    def _handle_read_resource(self, req: MCPRequest) -> Dict[str, Any]:
        uri = req.params.get("uri", "")
        resource = self._resources.get(uri)
        if not resource:
            return req.error(METHOD_NOT_FOUND, f"Resource not found: {uri}")
        try:
            content = resource.read()
            text = content if isinstance(content, str) else json.dumps(content, indent=2, default=str)
            return req.response({"contents": [{"uri": uri, "mimeType": resource.mime_type, "text": text}]})
        except Exception as e:
            logger.exception("Resource read failed: %s", uri)
            return req.error(INTERNAL_ERROR, str(e))

    def dispatch(self, req: MCPRequest) -> Optional[Dict[str, Any]]:
        if req.method == "initialize":
            return self._handle_initialize(req)
        if req.method == "notifications/initialized":
            return None
        if not self._initialized:
            return req.error(-32000, "Server not initialized")
        handlers = {
            "tools/list": self._handle_list_tools,
            "tools/call": self._handle_call_tool,
            "resources/list": self._handle_list_resources,
            "resources/read": self._handle_read_resource,
        }
        handler = handlers.get(req.method)
        if handler:
            return handler(req)
        return req.error(METHOD_NOT_FOUND, f"Method not found: {req.method}")

    def run(self) -> None:
        self._register_all()
        logger.info("deploynator MCP server started for: %s", self._target_dir)
        for line in sys.stdin:
            line = line.strip()
            if not line:
                continue
            try:
                req = MCPRequest(json.loads(line))
                response = self.dispatch(req)
                if response is not None:
                    sys.stdout.write(json.dumps(response) + "\n")
                    sys.stdout.flush()
            except json.JSONDecodeError:
                sys.stdout.write(json.dumps(
                    {"jsonrpc": "2.0", "id": None, "error": {"code": -32700, "message": "Parse error"}}) + "\n")
                sys.stdout.flush()

    def _register_all(self) -> None:
        self.register_tool(MCPTool(
            "deploynator.release",
            "Full headless release: tests gate, readmenator docs, semver bump, tag, push. "
            "Use dry_run=true to preview.",
            self._tool_release,
            {"type": "object", "properties": {
                "project": {"type": "string"}, "commit_type": {"type": "string", "default": "release"},
                "subject": {"type": "string", "default": ""}, "message": {"type": "string", "default": ""},
                "scope": {"type": "string", "default": ""},
                "body": {"type": "string", "default": ""}, "bump": {"type": "string", "default": ""},
                "dry_run": {"type": "boolean", "default": False},
                "no_test": {"type": "boolean", "default": False},
                "no_docs": {"type": "boolean", "default": False},
                "no_pypi": {"type": "boolean", "default": False},
            }},
        ))
        self.register_tool(MCPTool(
            "deploynator.commit",
            "Create a conventional commit (no version bump).",
            self._tool_commit,
            {"type": "object", "properties": {
                "project": {"type": "string", "default": ""}, "commit_type": {"type": "string"},
                "subject": {"type": "string"}, "scope": {"type": "string", "default": ""},
                "body": {"type": "string", "default": ""}, "dry_run": {"type": "boolean", "default": False},
            }, "required": ["commit_type", "subject"]},
        ))
        self.register_tool(MCPTool(
            "deploynator.status",
            "Repo status: branch, dirty, remote, projects count.",
            self._tool_status,
            {"type": "object", "properties": {"project": {"type": "string", "default": ""}}},
        ))
        self.register_tool(MCPTool(
            "deploynator.projects",
            "List discovered projects from projects/ + deploynator.yaml.",
            self._tool_projects,
            {"type": "object", "properties": {}},
        ))
        self.register_tool(MCPTool(
            "deploynator.docs",
            "Regenerate docs via readmenator.",
            self._tool_docs,
            {"type": "object", "properties": {"project": {"type": "string", "default": ""}}},
        ))
        self.register_resource(MCPResource(
            "deploynator://projects", "Projects", "Discovered projects JSON",
            "application/json", self._resource_projects,
        ))
        self.register_resource(MCPResource(
            "deploynator://status", "Status", "Status JSON",
            "application/json", lambda: self._app.status(),
        ))

    def _tool_release(self, project: str = "", commit_type: str = "release", subject: str = "",
                      message: str = "", scope: str = "", body: str = "", bump: str = "",
                      dry_run: bool = False, no_test: bool = False, no_docs: bool = False,
                      no_pypi: bool = False) -> str:
        results = self._app.release(
            commit_type=commit_type, subject=subject, message=message, scope=scope, body=body,
            project_name=project, bump=bump, dry_run=dry_run,
            all_projects=not project, no_test=no_test, no_docs=no_docs, no_pypi=no_pypi,
        )
        lines = []
        for r in results:
            lines.append(f"[{('OK' if r.success else 'FAIL')}] {r.project} v{r.version}"
                         + (f" error={r.error}" if r.error else ""))
        return "\n".join(lines) or "No projects found."

    def _tool_commit(self, commit_type: str, subject: str, project: str = "",
                     scope: str = "", body: str = "", dry_run: bool = False) -> str:
        return self._app.commit(commit_type, subject, scope, body, project_name=project, dry_run=dry_run)

    def _tool_status(self, project: str = "") -> str:
        return json.dumps(self._app.status(project_name=project), indent=2, default=str)

    def _tool_projects(self) -> str:
        projects = self._app.list_projects()
        return json.dumps([{"name": p.name, "path": p.path,
                            "platforms": [f"{c.platform.label()}/{c.repo}" for c in p.platforms if c.enabled]}
                           for p in projects], indent=2)

    def _tool_docs(self, project: str = "") -> str:
        ok = self._app.generate_docs(project_name=project)
        return "docs ok" if ok else "docs failed"

    def _resource_projects(self) -> str:
        return self._tool_projects()


def main() -> None:
    from deploynator._config import Config
    from deploynator import DeploynatorApp
    target = sys.argv[1] if len(sys.argv) > 1 else "."
    app = DeploynatorApp(Config.create(), workdir=target)
    MCPServer(app, target).run()


if __name__ == "__main__":
    main()
