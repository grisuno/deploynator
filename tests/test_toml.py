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


class TestCMakefileDetection:
    def _mk(self, tmp, content="all:\n\techo hi\ntest-host:\n\techo host\ntest:\n\techo t\n"):
        with open(os.path.join(tmp, "Makefile"), "w") as f:
            f.write(content)

    def test_list_targets_ignores_recipes(self):
        from deploynator._toml import list_make_targets
        with tempfile.TemporaryDirectory() as tmp:
            self._mk(tmp, "all:\n\techo hi\ntest-host:\n\techo host\n")
            targets = list_make_targets(tmp)
            assert "all" in targets
            assert "test-host" in targets
            assert "echo hi" not in targets

    def test_detect_prefers_test_host(self):
        from deploynator._toml import detect_test_commands
        with tempfile.TemporaryDirectory() as tmp:
            self._mk(tmp)
            assert detect_test_commands(tmp) == ["make test-host"]

    def test_detect_falls_back_to_test(self):
        from deploynator._toml import detect_test_commands
        with tempfile.TemporaryDirectory() as tmp:
            self._mk(tmp, "all:\n\techo hi\ntest:\n\techo t\n")
            assert detect_test_commands(tmp) == ["make test"]

    def test_detect_falls_back_to_check(self):
        from deploynator._toml import detect_test_commands
        with tempfile.TemporaryDirectory() as tmp:
            self._mk(tmp, "all:\n\techo hi\ncheck:\n\techo c\n")
            assert detect_test_commands(tmp) == ["make check"]

    def test_detect_cmake(self):
        from deploynator._toml import detect_test_commands
        with tempfile.TemporaryDirectory() as tmp:
            with open(os.path.join(tmp, "CMakeLists.txt"), "w") as f:
                f.write("cmake_minimum_required(VERSION 3.10)\n")
            cmds = detect_test_commands(tmp)
            assert cmds is not None and any("ctest" in c for c in cmds)

    def test_load_missing_makefile_uses_make(self):
        from deploynator._toml import load_toml_config
        with tempfile.TemporaryDirectory() as tmp:
            self._mk(tmp, "test-host:\n\techo host\n")
            cfg = load_toml_config(tmp)
            assert cfg.test_commands == ["make test-host"]
            assert cfg.test_timeout_s == 900
            assert cfg.pypi_enabled is False

    def test_python_with_aux_makefile_keeps_pytest(self):
        from deploynator._toml import load_toml_config
        with tempfile.TemporaryDirectory() as tmp:
            self._mk(tmp, "test:\n\techo t\n")
            os.makedirs(os.path.join(tmp, "tests"))
            with open(os.path.join(tmp, "tests", "test_x.py"), "w") as f:
                f.write("def test_x(): pass\n")
            cfg = load_toml_config(tmp)
            assert cfg.test_commands == ["python -m pytest tests/ -q"]

    def test_test_host_wins_over_python_tests(self):
        from deploynator._toml import load_toml_config
        with tempfile.TemporaryDirectory() as tmp:
            self._mk(tmp, "test-host:\n\techo host\ntest:\n\techo t\n")
            os.makedirs(os.path.join(tmp, "tests"))
            with open(os.path.join(tmp, "tests", "test_x.py"), "w") as f:
                f.write("def test_x(): pass\n")
            cfg = load_toml_config(tmp)
            assert cfg.test_commands == ["make test-host"]

    def test_makefile_symlink_rejected(self):
        from deploynator._toml import list_make_targets
        with tempfile.TemporaryDirectory() as tmp:
            real = os.path.join(tmp, "RealMakefile")
            with open(real, "w") as f:
                f.write("test:\n\techo t\n")
            os.symlink(real, os.path.join(tmp, "Makefile"))
            with pytest.raises(ValueError, match="Symlink"):
                list_make_targets(tmp)


class TestMultiTargetAndPyPIInference:
    """Runtime multi-proyecto: todos los targets test en una invocación
    y pypi_enabled inferido de los ficheros de packaging."""

    def _mk(self, tmp, content):
        with open(os.path.join(tmp, "Makefile"), "w") as f:
            f.write(content)

    def test_detect_combines_test_targets(self):
        from deploynator._toml import detect_test_commands
        with tempfile.TemporaryDirectory() as tmp:
            self._mk(tmp, "test:\n\techo t\ntest-dsp:\n\techo d\n"
                          "test-transport:\n\techo r\ntests:\n\tmkdir -p tests\n")
            assert detect_test_commands(tmp) == ["make test test-dsp test-transport"]

    def test_detect_test_host_alone_wins(self):
        from deploynator._toml import detect_test_commands
        with tempfile.TemporaryDirectory() as tmp:
            self._mk(tmp, "test-host:\n\techo h\ntest:\n\techo t\n"
                          "test-dsp:\n\techo d\n")
            assert detect_test_commands(tmp) == ["make test-host"]

    def test_detect_bare_tests_alone_kept(self):
        from deploynator._toml import detect_test_commands
        with tempfile.TemporaryDirectory() as tmp:
            self._mk(tmp, "tests:\n\techo t\n")
            assert detect_test_commands(tmp) == ["make tests"]

    def test_auto_pypi_enabled_for_packaging(self):
        from deploynator._toml import load_toml_config
        with tempfile.TemporaryDirectory() as tmp:
            self._mk(tmp, "test:\n\techo t\n")
            with open(os.path.join(tmp, "pyproject.toml"), "w") as f:
                f.write('[project]\nname = "x"\nversion = "0.1.0"\n')
            cfg = load_toml_config(tmp)
            assert cfg.test_commands == ["make test"]
            assert cfg.pypi_enabled is True

    def test_auto_pypi_disabled_for_plain_c(self):
        from deploynator._toml import load_toml_config
        with tempfile.TemporaryDirectory() as tmp:
            self._mk(tmp, "test:\n\techo t\n")
            cfg = load_toml_config(tmp)
            assert cfg.test_commands == ["make test"]
            assert cfg.pypi_enabled is False

    def test_looks_like_packaging_setup_py(self):
        from deploynator._toml import looks_like_packaging_project
        with tempfile.TemporaryDirectory() as tmp:
            assert looks_like_packaging_project(tmp) is False
            with open(os.path.join(tmp, "setup.py"), "w") as f:
                f.write("from setuptools import setup\nsetup(name='x')\n")
            assert looks_like_packaging_project(tmp) is True
