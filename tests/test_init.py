"""RED: init deja deploy.sh genérico + deploynator.toml starter."""
import os
import stat
import subprocess


class TestInitScript:
    def test_init_creates_files(self):
        import tempfile

        from deploynator import DeploynatorApp
        from deploynator._config import Config
        with tempfile.TemporaryDirectory() as tmp:
            msg = DeploynatorApp(Config.create()).init_project(project_path=tmp, name="demo")
            assert os.path.isfile(os.path.join(tmp, "deploynator.yaml"))
            assert os.path.isfile(os.path.join(tmp, "deploy.sh"))
            assert os.path.isfile(os.path.join(tmp, "deploynator.toml"))
            assert "deploy.sh" in msg and "deploynator.toml" in msg

    def test_deploy_sh_executable_and_valid_bash(self):
        import tempfile

        from deploynator import DeploynatorApp
        from deploynator._config import Config
        with tempfile.TemporaryDirectory() as tmp:
            DeploynatorApp(Config.create()).init_project(project_path=tmp, name="demo")
            path = os.path.join(tmp, "deploy.sh")
            assert os.stat(path).st_mode & stat.S_IXUSR
            r = subprocess.run(["bash", "-n", path], capture_output=True, text=True, check=False)
            assert r.returncode == 0, r.stderr

    def test_deploy_sh_content_generic(self):
        import tempfile

        from deploynator import DeploynatorApp
        from deploynator._config import Config
        with tempfile.TemporaryDirectory() as tmp:
            DeploynatorApp(Config.create()).init_project(project_path=tmp, name="demo")
            with open(os.path.join(tmp, "deploy.sh")) as f:
                content = f.read()
            assert "dirname" in content  # autodetecta su directorio
            assert "PIP_BIN" in content and "install" in content  # instala/actualiza tooling
            assert "break-system-packages" in content  # PEP 668 (Kali)
            assert "ensure_pkg" in content
            assert "deploynator" in content and "readmenator" in content
            assert "--project" in content  # one-liner con path detectado
            assert "grisuno/deploynator" in content  # fallback git
            assert "demo" not in content  # genérico: sin nombre hardcodeado

    def test_init_no_overwrite(self):
        import tempfile

        from deploynator import DeploynatorApp
        from deploynator._config import Config
        with tempfile.TemporaryDirectory() as tmp:
            app = DeploynatorApp(Config.create())
            app.init_project(project_path=tmp, name="demo")
            with open(os.path.join(tmp, "deploy.sh"), "w") as f:
                f.write("# custom\n")
            app.init_project(project_path=tmp, name="demo")
            with open(os.path.join(tmp, "deploy.sh")) as f:
                assert f.read() == "# custom\n"

    def test_toml_starter_parseable(self):
        import tempfile

        from deploynator import DeploynatorApp
        from deploynator._config import Config
        from deploynator._toml import load_toml_config
        with tempfile.TemporaryDirectory() as tmp:
            DeploynatorApp(Config.create()).init_project(project_path=tmp, name="demo")
            cfg = load_toml_config(tmp)
            assert cfg.project_name == "demo"
            assert cfg.test_commands == ["python -m pytest tests/ -q"]
