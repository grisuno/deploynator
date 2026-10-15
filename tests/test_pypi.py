"""RED: PyPI runner — detecta packaging, build limpio, upload twine."""
import os
import subprocess
import tempfile

import pytest


@pytest.fixture(autouse=True)
def _isolated_home(tmp_path, monkeypatch):
    """Aísla ~/.pypirc real: los tests nunca ven ni tocan credenciales del operador."""
    monkeypatch.setenv("HOME", str(tmp_path))


def _git_init(tmp):
    subprocess.run(["git", "init", "-q", tmp], check=True)
    subprocess.run(["git", "-C", tmp, "config", "user.email", "t@t.t"], check=True)
    subprocess.run(["git", "-C", tmp, "config", "user.name", "t"], check=True)
    with open(os.path.join(tmp, "f.txt"), "w") as f:
        f.write("x")
    subprocess.run(["git", "-C", tmp, "add", "-A"], check=True)
    subprocess.run(["git", "-C", tmp, "commit", "-qm", "chore: init"], check=True)


class TestDetect:
    def test_pyproject_with_project_table(self):
        from deploynator._pypi import PyPIRunner
        from deploynator._config import Config
        with tempfile.TemporaryDirectory() as tmp:
            with open(os.path.join(tmp, "pyproject.toml"), "w") as f:
                f.write('[build-system]\nrequires=["hatchling"]\n[project]\nname="x"\nversion="0.1.0"\n')
            assert PyPIRunner(Config.create()).is_packaging_project(tmp) is True

    def test_empty_dir_no_packaging(self):
        from deploynator._pypi import PyPIRunner
        from deploynator._config import Config
        with tempfile.TemporaryDirectory() as tmp:
            assert PyPIRunner(Config.create()).is_packaging_project(tmp) is False

    def test_setup_py_counts(self):
        from deploynator._pypi import PyPIRunner
        from deploynator._config import Config
        with tempfile.TemporaryDirectory() as tmp:
            with open(os.path.join(tmp, "setup.py"), "w") as f:
                f.write("from setuptools import setup\nsetup(name='x')\n")
            assert PyPIRunner(Config.create()).is_packaging_project(tmp) is True

    def test_credentials_from_env(self, monkeypatch):
        from deploynator._pypi import PyPIRunner
        from deploynator._config import Config
        r = PyPIRunner(Config.create())
        monkeypatch.delenv("TWINE_PASSWORD", raising=False)
        monkeypatch.delenv("PYPI_TOKEN", raising=False)
        assert r.has_credentials() is False
        monkeypatch.setenv("PYPI_TOKEN", "pypi-fake")
        assert r.has_credentials() is True

    def test_no_shell_in_runner(self):
        import inspect
        import deploynator._pypi as mod
        assert "shell=True" not in inspect.getsource(mod)


class TestPromptCredentials:
    def test_no_tty_returns_none(self, monkeypatch):
        import sys
        from deploynator._pypi import PyPIRunner
        from deploynator._config import Config
        monkeypatch.setattr(sys.stdin, "isatty", lambda: False)
        assert PyPIRunner(Config.create()).prompt_for_credentials() is None

    def test_prompt_returns_token_without_save(self, monkeypatch):
        import sys
        from deploynator._pypi import PyPIRunner
        from deploynator._config import Config
        monkeypatch.setattr(sys.stdin, "isatty", lambda: True)
        monkeypatch.setattr("getpass.getpass", lambda *a, **k: "pypi-fake-token")
        monkeypatch.setattr("builtins.input", lambda *a, **k: "n")
        assert PyPIRunner(Config.create()).prompt_for_credentials() == "pypi-fake-token"

    def test_prompt_empty_token_returns_none(self, monkeypatch):
        import sys
        from deploynator._pypi import PyPIRunner
        from deploynator._config import Config
        monkeypatch.setattr(sys.stdin, "isatty", lambda: True)
        monkeypatch.setattr("getpass.getpass", lambda *a, **k: "   ")
        assert PyPIRunner(Config.create()).prompt_for_credentials() is None

    def test_prompt_default_is_no_save(self, monkeypatch):
        """Enter (vacío) NO guarda: el default es NO."""
        import sys
        from deploynator._pypi import PyPIRunner
        from deploynator._config import Config
        monkeypatch.setattr(sys.stdin, "isatty", lambda: True)
        monkeypatch.setattr("getpass.getpass", lambda *a, **k: "pypi-fake-token")
        monkeypatch.setattr("builtins.input", lambda *a, **k: "")
        saved = []
        monkeypatch.setattr(PyPIRunner, "save_pypirc",
                            lambda self, token, path=None: saved.append(token))
        assert PyPIRunner(Config.create()).prompt_for_credentials() == "pypi-fake-token"
        assert saved == []

    def test_prompt_yes_saves(self, monkeypatch):
        import sys
        from deploynator._pypi import PyPIRunner
        from deploynator._config import Config
        monkeypatch.setattr(sys.stdin, "isatty", lambda: True)
        monkeypatch.setattr("getpass.getpass", lambda *a, **k: "pypi-fake-token")
        monkeypatch.setattr("builtins.input", lambda *a, **k: "y")
        saved = []
        monkeypatch.setattr(PyPIRunner, "save_pypirc",
                            lambda self, token, path=None: saved.append(token) or "/tmp/x")
        assert PyPIRunner(Config.create()).prompt_for_credentials() == "pypi-fake-token"
        assert saved == ["pypi-fake-token"]

    def test_save_pypirc_roundtrip(self):
        import configparser
        from deploynator._pypi import PyPIRunner
        from deploynator._config import Config
        import tempfile
        with tempfile.TemporaryDirectory() as tmp:
            target = os.path.join(tmp, ".pypirc")
            PyPIRunner(Config.create()).save_pypirc("pypi-secret", path=target)
            assert (os.stat(target).st_mode & 0o777) == 0o600
            cfg = configparser.ConfigParser()
            cfg.read(target)
            assert cfg["pypi"]["username"] == "__token__"
            assert cfg["pypi"]["password"] == "pypi-secret"

    def test_save_pypirc_rejects_symlink(self):
        from deploynator._pypi import PyPIRunner
        from deploynator._config import Config
        import tempfile
        import pytest
        with tempfile.TemporaryDirectory() as tmp:
            real = os.path.join(tmp, "real")
            with open(real, "w") as f:
                f.write("x")
            link = os.path.join(tmp, "link")
            os.symlink(real, link)
            with pytest.raises(ValueError):
                PyPIRunner(Config.create()).save_pypirc("t", path=link)

    def test_prompted_token_used_for_upload(self, monkeypatch):
        from deploynator._deploy import DeployOrchestrator
        from deploynator._config import Config
        from deploynator._models import CommitType, ProjectConfig
        monkeypatch.delenv("TWINE_PASSWORD", raising=False)
        monkeypatch.delenv("PYPI_TOKEN", raising=False)
        monkeypatch.setattr(
            "deploynator._pypi.PyPIRunner.prompt_for_credentials",
            lambda self: "pypi-fake",
        )
        with tempfile.TemporaryDirectory() as tmp:
            origin = os.path.join(tmp, "origin.git")
            work = os.path.join(tmp, "work")
            subprocess.run(["git", "init", "--bare", "-q", origin], check=True)
            subprocess.run(["git", "init", "-q", work], check=True)
            subprocess.run(["git", "-C", work, "config", "user.email", "t@t.t"], check=True)
            subprocess.run(["git", "-C", work, "config", "user.name", "t"], check=True)
            with open(os.path.join(work, "f.txt"), "w") as f:
                f.write("x")
            with open(os.path.join(work, "pyproject.toml"), "w") as f:
                f.write('[build-system]\nrequires=["no-such-backend-xyz"]\n'
                        'build-backend="nope"\n[project]\nname="x"\nversion="0.1.0"\n')
            subprocess.run(["git", "-C", work, "add", "-A"], check=True)
            subprocess.run(["git", "-C", work, "commit", "-qm", "chore: init"], check=True)
            subprocess.run(["git", "-C", work, "remote", "add", "origin", origin], check=True)
            subprocess.run(["git", "-C", work, "branch", "-M", "main"], check=True)
            with open(os.path.join(work, "deploynator.toml"), "w") as f:
                f.write('[tests]\ncommands = ["true"]\n[docs]\nauto = false\n')
            res = DeployOrchestrator(Config.create()).deploy(
                project=ProjectConfig(name="p", path=work),
                commit_type=CommitType.FIX, subject="x",
                dry_run=False, run_tests=True, run_docs=False, run_pypi=True,
            )
            assert res.success is False
            assert "pypi" in (res.error or "").lower()


class TestCleanAndRun:
    def _toml(self, **kw):
        from deploynator._toml import TomlConfig
        base = dict(project_name="t", version_file="version.json",
                    test_commands=["true"], test_timeout_s=30, allow_no_tests=False,
                    docs_auto=False, docs_command="true", docs_timeout_s=30,
                    deploy_branch="main", deploy_remote="origin")
        base.update(kw)
        return TomlConfig(**base)

    def test_clean_removes_dist(self):
        from deploynator._pypi import PyPIRunner
        from deploynator._config import Config
        with tempfile.TemporaryDirectory() as tmp:
            d = os.path.join(tmp, "dist")
            os.makedirs(d)
            with open(os.path.join(d, "old.whl"), "w") as f:
                f.write("stale")
            r = PyPIRunner(Config.create())
            r.clean(tmp, self._toml())
            assert not os.path.exists(os.path.join(d, "old.whl"))

    def test_run_fails_on_broken_build(self, monkeypatch):
        from deploynator._pypi import PyPIRunner
        from deploynator._config import Config
        monkeypatch.setenv("PYPI_TOKEN", "pypi-fake")
        with tempfile.TemporaryDirectory() as tmp:
            with open(os.path.join(tmp, "pyproject.toml"), "w") as f:
                f.write('[build-system]\nrequires=["no-such-backend-xyz"]\n'
                        'build-backend="nope"\n[project]\nname="x"\nversion="0.1.0"\n')
            ok, msg = PyPIRunner(Config.create()).run(tmp, self._toml(), "0.1.0")
            assert ok is False

    def test_run_skips_without_packaging(self):
        from deploynator._pypi import PyPIRunner
        from deploynator._config import Config
        with tempfile.TemporaryDirectory() as tmp:
            ok, msg = PyPIRunner(Config.create()).run(tmp, self._toml(), "0.1.0")
            assert ok is True
            assert "skip" in msg.lower() or "no packaging" in msg.lower()


class TestPipelinePyPI:
    def test_pypi_failure_aborts_with_error(self, monkeypatch):
        from deploynator._deploy import DeployOrchestrator
        from deploynator._config import Config
        from deploynator._models import CommitType, ProjectConfig
        monkeypatch.setenv("PYPI_TOKEN", "pypi-fake")
        with tempfile.TemporaryDirectory() as tmp:
            origin = os.path.join(tmp, "origin.git")
            work = os.path.join(tmp, "work")
            subprocess.run(["git", "init", "--bare", "-q", origin], check=True)
            subprocess.run(["git", "init", "-q", work], check=True)
            subprocess.run(["git", "-C", work, "config", "user.email", "t@t.t"], check=True)
            subprocess.run(["git", "-C", work, "config", "user.name", "t"], check=True)
            with open(os.path.join(work, "f.txt"), "w") as f:
                f.write("x")
            with open(os.path.join(work, "pyproject.toml"), "w") as f:
                f.write('[build-system]\nrequires=["no-such-backend-xyz"]\n'
                        'build-backend="nope"\n[project]\nname="x"\nversion="0.1.0"\n')
            subprocess.run(["git", "-C", work, "add", "-A"], check=True)
            subprocess.run(["git", "-C", work, "commit", "-qm", "chore: init"], check=True)
            subprocess.run(["git", "-C", work, "remote", "add", "origin", origin], check=True)
            subprocess.run(["git", "-C", work, "branch", "-M", "main"], check=True)
            with open(os.path.join(work, "deploynator.toml"), "w") as f:
                f.write('[tests]\ncommands = ["true"]\n[docs]\nauto = false\n')
            res = DeployOrchestrator(Config.create()).deploy(
                project=ProjectConfig(name="p", path=work),
                commit_type=CommitType.FIX, subject="x",
                dry_run=False, run_tests=True, run_docs=False, run_pypi=True,
            )
            assert res.success is False
            assert "pypi" in (res.error or "").lower()
            assert any("origin" in p for p in res.platforms_pushed)

    def test_no_credentials_skips_pypi(self, monkeypatch):
        from deploynator._deploy import DeployOrchestrator
        from deploynator._config import Config
        from deploynator._models import CommitType, ProjectConfig
        monkeypatch.delenv("TWINE_PASSWORD", raising=False)
        monkeypatch.delenv("PYPI_TOKEN", raising=False)
        with tempfile.TemporaryDirectory() as tmp:
            origin = os.path.join(tmp, "origin.git")
            work = os.path.join(tmp, "work")
            subprocess.run(["git", "init", "--bare", "-q", origin], check=True)
            subprocess.run(["git", "init", "-q", work], check=True)
            subprocess.run(["git", "-C", work, "config", "user.email", "t@t.t"], check=True)
            subprocess.run(["git", "-C", work, "config", "user.name", "t"], check=True)
            with open(os.path.join(work, "f.txt"), "w") as f:
                f.write("x")
            with open(os.path.join(work, "setup.py"), "w") as f:
                f.write("from setuptools import setup\nsetup(name='x')\n")
            subprocess.run(["git", "-C", work, "add", "-A"], check=True)
            subprocess.run(["git", "-C", work, "commit", "-qm", "chore: init"], check=True)
            subprocess.run(["git", "-C", work, "remote", "add", "origin", origin], check=True)
            subprocess.run(["git", "-C", work, "branch", "-M", "main"], check=True)
            with open(os.path.join(work, "deploynator.toml"), "w") as f:
                f.write('[tests]\ncommands = ["true"]\n[docs]\nauto = false\n')
            res = DeployOrchestrator(Config.create()).deploy(
                project=ProjectConfig(name="p", path=work),
                commit_type=CommitType.FIX, subject="x",
                dry_run=False, run_tests=True, run_docs=False, run_pypi=True,
            )
            assert res.success is True
