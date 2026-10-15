"""RED: TomlConfig contract — deploynator.toml per-project."""
import os
import tempfile
import pytest


class TestTomlConfig:
    def test_load_missing_returns_defaults(self):
        from deploynator._toml import load_toml_config
        with tempfile.TemporaryDirectory() as tmp:
            cfg = load_toml_config(tmp)
            assert cfg.project_name == os.path.basename(tmp) or cfg.project_name == ""
            assert cfg.test_commands == ["python -m pytest tests/ -q"]
            assert cfg.test_timeout_s == 300
            assert cfg.docs_auto is True
            assert "readmenator" in cfg.docs_command

    def test_load_valid_toml(self):
        from deploynator._toml import load_toml_config
        with tempfile.TemporaryDirectory() as tmp:
            with open(os.path.join(tmp, "deploynator.toml"), "w") as f:
                f.write(
                    '[project]\nname = "my-app"\nversion_file = "VERSION"\n\n'
                    '[tests]\ncommands = ["pytest -q", "ruff check ."]\ntimeout_s = 60\n'
                    '[docs]\nauto = false\n'
                    '[deploy]\nbranch = "develop"\nremote = "upstream"\n'
                )
            cfg = load_toml_config(tmp)
            assert cfg.project_name == "my-app"
            assert cfg.version_file == "VERSION"
            assert cfg.test_commands == ["pytest -q", "ruff check ."]
            assert cfg.test_timeout_s == 60
            assert cfg.docs_auto is False
            assert cfg.deploy_branch == "develop"
            assert cfg.deploy_remote == "upstream"

    def test_symlink_rejected(self):
        from deploynator._toml import load_toml_config
        with tempfile.TemporaryDirectory() as tmp:
            real = os.path.join(tmp, "real.toml")
            with open(real, "w") as f:
                f.write('[project]\nname="x"\n')
            link = os.path.join(tmp, "deploynator.toml")
            os.symlink(real, link)
            with pytest.raises(ValueError, match="Symlink"):
                load_toml_config(tmp)

    def test_oversize_rejected(self):
        from deploynator._toml import load_toml_config
        with tempfile.TemporaryDirectory() as tmp:
            with open(os.path.join(tmp, "deploynator.toml"), "w") as f:
                f.write("#" * (10_485_760 + 1))
            with pytest.raises(ValueError, match="too large"):
                load_toml_config(tmp)

    def test_malformed_toml_raises(self):
        from deploynator._toml import load_toml_config
        with tempfile.TemporaryDirectory() as tmp:
            with open(os.path.join(tmp, "deploynator.toml"), "w") as f:
                f.write("[tests\ncommands = [[[invalid")
            with pytest.raises(ValueError):
                load_toml_config(tmp)

    def test_timeout_clamped(self):
        from deploynator._toml import load_toml_config
        with tempfile.TemporaryDirectory() as tmp:
            with open(os.path.join(tmp, "deploynator.toml"), "w") as f:
                f.write("[tests]\ntimeout_s = 999999\n")
            cfg = load_toml_config(tmp)
            assert cfg.test_timeout_s <= 3600
            with open(os.path.join(tmp, "deploynator.toml"), "w") as f:
                f.write("[tests]\ntimeout_s = 0\n")
            cfg = load_toml_config(tmp)
            assert cfg.test_timeout_s >= 1

    def test_frozen(self):
        from deploynator._toml import load_toml_config
        with tempfile.TemporaryDirectory() as tmp:
            cfg = load_toml_config(tmp)
            with pytest.raises(Exception):
                cfg.project_name = "mutated"
