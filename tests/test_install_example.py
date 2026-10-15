"""RED: install como pip install + app.py ejemplo de librería."""
import os


class TestInstallPackages:
    def test_empty_is_noop(self):
        from deploynator import DeploynatorApp
        from deploynator._config import Config
        assert DeploynatorApp(Config.create()).install_packages([]) == {}

    def test_default_targets_deploynator(self, monkeypatch):
        from deploynator import DeploynatorApp
        from deploynator._config import Config
        calls = []
        import subprocess

        def fake_run(cmd, **kw):
            calls.append(cmd)
            class R:
                returncode = 0
                stdout = "ok"
                stderr = ""
            return R()
        monkeypatch.setattr(subprocess, "run", fake_run)
        res = DeploynatorApp(Config.create()).install_packages(None)
        assert res == {"deploynator": True}
        assert any("deploynator" in c for c in calls)

    def test_failure_reported(self, monkeypatch):
        from deploynator import DeploynatorApp
        from deploynator._config import Config
        import subprocess

        def fake_run(cmd, **kw):
            raise FileNotFoundError("no pip")
        monkeypatch.setattr(subprocess, "run", fake_run)
        assert DeploynatorApp(Config.create()).install_packages(["x"]) == {"x": False}

    def test_no_shell(self):
        import inspect
        from deploynator import _app
        src = inspect.getsource(_app.DeploynatorApp.install_packages)
        assert "shell=True" not in src

    def test_cli_install_parses_packages(self):
        from deploynator.__main__ import build_parser
        args = build_parser().parse_args(["install", "readmenator"])
        assert args.command == "install"
        assert "readmenator" in args.packages
        args = build_parser().parse_args(["install"])
        assert args.packages == []


class TestAppExample:
    def test_example_exists_and_compiles(self):
        import py_compile
        path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                            "app.py")
        assert os.path.isfile(path), "app.py example missing at repo root"
        py_compile.compile(path, doraise=True)

    def test_example_uses_library(self):
        path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                            "app.py")
        content = open(path).read()
        assert "from deploynator import DeploynatorApp" in content
        assert "dry_run" in content
