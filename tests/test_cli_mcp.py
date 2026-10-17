"""RED: bare = interactive, flags = headless + MCP server."""


class TestCliMode:
    def test_bare_invokes_interactive(self, monkeypatch):
        from deploynator import __main__ as m
        called = {}
        monkeypatch.setattr(
            "deploynator._app.DeploynatorApp.interactive_menu",
            lambda self: called.setdefault("hit", True),
        )
        m.main([])
        assert called.get("hit") is True

    def test_explicit_interactive_still_works(self):
        from deploynator.__main__ import build_parser
        args = build_parser().parse_args(["interactive"])
        assert args.command == "interactive"

    def test_release_flags_headless(self):
        from deploynator.__main__ import build_parser
        args = build_parser().parse_args(
            ["release", "--type", "feat", "--project", "X", "--no-test", "--dry-run"]
        )
        assert args.command == "release"
        assert args.no_test is True
        assert args.dry_run is True

    def test_serve_command_exists(self):
        from deploynator.__main__ import build_parser
        args = build_parser().parse_args(["serve", "/tmp"])
        assert args.command == "serve"


class TestMCPServer:
    def _server(self, tmp):
        from deploynator import DeploynatorApp
        from deploynator._config import Config
        from deploynator._mcp_server import MCPServer
        app = DeploynatorApp(Config.create(), workdir=tmp)
        return MCPServer(app, tmp)

    def test_initialize_and_list(self, tmp_path):
        from deploynator._mcp_server import MCPRequest
        s = self._server(str(tmp_path))
        s._register_all()
        r = s.dispatch(MCPRequest({"jsonrpc": "2.0", "id": 1, "method": "initialize"}))
        assert "result" in r
        r = s.dispatch(MCPRequest({"jsonrpc": "2.0", "id": 2, "method": "tools/list"}))
        names = [t["name"] for t in r["result"]["tools"]]
        assert "deploynator.release" in names
        assert "deploynator.status" in names
        assert "deploynator.projects" in names

    def test_call_status_and_projects(self, tmp_path):
        from deploynator._mcp_server import MCPRequest
        s = self._server(str(tmp_path))
        s._register_all()
        s.dispatch(MCPRequest({"jsonrpc": "2.0", "id": 1, "method": "initialize"}))
        r = s.dispatch(MCPRequest({
            "jsonrpc": "2.0", "id": 2, "method": "tools/call",
            "params": {"name": "deploynator.projects", "arguments": {}},
        }))
        assert r["result"]["isError"] is False
        r = s.dispatch(MCPRequest({
            "jsonrpc": "2.0", "id": 3, "method": "tools/call",
            "params": {"name": "deploynator.status", "arguments": {}},
        }))
        assert r["result"]["isError"] is False

    def test_unknown_tool_errors(self, tmp_path):
        from deploynator._mcp_server import MCPRequest
        s = self._server(str(tmp_path))
        s._register_all()
        s.dispatch(MCPRequest({"jsonrpc": "2.0", "id": 1, "method": "initialize"}))
        r = s.dispatch(MCPRequest({
            "jsonrpc": "2.0", "id": 2, "method": "tools/call",
            "params": {"name": "nope", "arguments": {}},
        }))
        assert "error" in r

    def test_resources_list(self, tmp_path):
        from deploynator._mcp_server import MCPRequest
        s = self._server(str(tmp_path))
        s._register_all()
        s.dispatch(MCPRequest({"jsonrpc": "2.0", "id": 1, "method": "initialize"}))
        r = s.dispatch(MCPRequest({"jsonrpc": "2.0", "id": 2, "method": "resources/list"}))
        uris = [x["uri"] for x in r["result"]["resources"]]
        assert "deploynator://projects" in uris
