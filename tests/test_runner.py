"""RED: TestRunner + DocsRunner contracts."""
import os
import tempfile

import pytest


def _toml(commands=None, timeout=30):
    from deploynator._toml import TomlConfig
    return TomlConfig(
        project_name="t",
        version_file="version.json",
        test_commands=commands if commands is not None else ["true"],
        test_timeout_s=timeout,
        allow_no_tests=False,
        docs_auto=True,
        docs_command="true",
        docs_timeout_s=timeout,
        deploy_branch="main",
        deploy_remote="origin",
    )


class TestTestRunner:
    def test_passing_command(self):
        from deploynator._config import Config
        from deploynator._runner import TestRunner
        r = TestRunner(Config.create())
        with tempfile.TemporaryDirectory() as tmp:
            ok, _out = r.run(tmp, _toml(["true"]))
            assert ok is True

    def test_failing_command(self):
        from deploynator._config import Config
        from deploynator._runner import TestRunner
        r = TestRunner(Config.create())
        with tempfile.TemporaryDirectory() as tmp:
            ok, out = r.run(tmp, _toml(["false"]))
            assert ok is False
            assert out != ""

    def test_multiple_commands_stop_on_first_failure(self):
        from deploynator._config import Config
        from deploynator._runner import TestRunner
        r = TestRunner(Config.create())
        with tempfile.TemporaryDirectory() as tmp:
            ok, _ = r.run(tmp, _toml(["true", "false", "true"]))
            assert ok is False

    def test_empty_commands_no_tests_dir_fails(self):
        from deploynator._config import Config
        from deploynator._runner import TestRunner
        r = TestRunner(Config.create())
        with tempfile.TemporaryDirectory() as tmp:
            ok, out = r.run(tmp, _toml([]))
            assert ok is False
            assert "No tests" in out

    def test_empty_commands_allow_no_tests_passes(self):
        from deploynator._config import Config
        from deploynator._runner import TestRunner
        from deploynator._toml import TomlConfig
        r = TestRunner(Config.create())
        with tempfile.TemporaryDirectory() as tmp:
            cfg = TomlConfig(
                project_name="t", version_file="version.json",
                test_commands=[], test_timeout_s=30, allow_no_tests=True,
                docs_auto=True, docs_command="true", docs_timeout_s=30,
                deploy_branch="main", deploy_remote="origin",
            )
            ok, _ = r.run(tmp, cfg)
            assert ok is True

    def test_no_shell_injection(self):
        import inspect

        import deploynator._runner as mod
        from deploynator._config import Config
        from deploynator._runner import TestRunner
        src = inspect.getsource(mod)
        assert "shell=True" not in src
        # intento de inyección no debe crear archivo vía shell
        r = TestRunner(Config.create())
        with tempfile.TemporaryDirectory() as tmp:
            marker = os.path.join(tmp, "pwned")
            r.run(tmp, _toml([f"echo hi; touch {marker}"]))
            assert not os.path.exists(marker)

    def test_timeout_fails(self):
        from deploynator._config import Config
        from deploynator._runner import TestRunner
        r = TestRunner(Config.create())
        with tempfile.TemporaryDirectory() as tmp:
            ok, out = r.run(tmp, _toml(["sleep 5"], timeout=1))
            assert ok is False
            assert "timeout" in out.lower() or "timed out" in out.lower()

    def test_empty_string_command_rejected(self):
        from deploynator._config import Config
        from deploynator._runner import TestRunner
        r = TestRunner(Config.create())
        with tempfile.TemporaryDirectory() as tmp:
            ok, _out = r.run(tmp, _toml([""]))
            assert ok is False

    def test_make_target_runs(self):
        import shutil

        from deploynator._config import Config
        from deploynator._runner import TestRunner
        if shutil.which("make") is None:
            pytest.skip("make not available")
        r = TestRunner(Config.create())
        with tempfile.TemporaryDirectory() as tmp:
            with open(os.path.join(tmp, "Makefile"), "w") as f:
                f.write("test-host:\n\techo host-ok\n")
            ok, out = r.run(tmp, _toml(["make test-host"]))
            assert ok is True
            assert "host-ok" in out


class TestDocsRunner:
    def test_passing_docs(self):
        from deploynator._config import Config
        from deploynator._docs import DocsRunner
        r = DocsRunner(Config.create())
        with tempfile.TemporaryDirectory() as tmp:
            assert r.run(tmp, _toml()) is True

    def test_failing_docs_returns_false(self):
        from deploynator._config import Config
        from deploynator._docs import DocsRunner
        from deploynator._toml import TomlConfig
        r = DocsRunner(Config.create())
        cfg = TomlConfig(
            project_name="t", version_file="version.json",
            test_commands=["true"], test_timeout_s=30, allow_no_tests=False,
            docs_auto=True, docs_command="false", docs_timeout_s=30,
            deploy_branch="main", deploy_remote="origin",
        )
        with tempfile.TemporaryDirectory() as tmp:
            assert r.run(tmp, cfg) is False

    def test_auto_false_skips(self):
        from deploynator._config import Config
        from deploynator._docs import DocsRunner
        from deploynator._toml import TomlConfig
        r = DocsRunner(Config.create())
        cfg = TomlConfig(
            project_name="t", version_file="version.json",
            test_commands=["true"], test_timeout_s=30, allow_no_tests=False,
            docs_auto=False, docs_command="false", docs_timeout_s=30,
            deploy_branch="main", deploy_remote="origin",
        )
        with tempfile.TemporaryDirectory() as tmp:
            assert r.run(tmp, cfg) is True

    def test_no_shell_injection(self):
        import inspect

        import deploynator._docs as mod
        assert "shell=True" not in inspect.getsource(mod)
