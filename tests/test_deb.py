"""RED: DebRunner — detecta packaging C, build .deb, upload como asset (espejo PyPI)."""
import os
import subprocess
import tempfile


def _git_init(tmp):
    subprocess.run(["git", "init", "-q", tmp], check=True)
    subprocess.run(["git", "-C", tmp, "config", "user.email", "t@t.t"], check=True)
    subprocess.run(["git", "-C", tmp, "config", "user.name", "t"], check=True)
    with open(os.path.join(tmp, "f.txt"), "w") as f:
        f.write("x")
    subprocess.run(["git", "-C", tmp, "add", "-A"], check=True)
    subprocess.run(["git", "-C", tmp, "commit", "-qm", "chore: init"], check=True)


def _toml(**kw):
    from deploynator._toml import TomlConfig
    base = {"project_name": "t", "version_file": "version.json",
            "test_commands": ["true"], "test_timeout_s": 30, "allow_no_tests": False,
            "docs_auto": False, "docs_command": "true", "docs_timeout_s": 30,
            "deploy_branch": "main", "deploy_remote": "origin"}
    base.update(kw)
    return TomlConfig(**base)


class TestDetect:
    def test_empty_dir_no_deb(self):
        from deploynator._config import Config
        from deploynator._deb import DebRunner
        with tempfile.TemporaryDirectory() as tmp:
            assert DebRunner(Config.create()).is_deb_project(tmp) is False

    def test_debian_control_counts(self):
        from deploynator._config import Config
        from deploynator._deb import DebRunner
        with tempfile.TemporaryDirectory() as tmp:
            os.makedirs(os.path.join(tmp, "debian"))
            with open(os.path.join(tmp, "debian", "control"), "w") as f:
                f.write("Source: x\n")
            assert DebRunner(Config.create()).is_deb_project(tmp) is True

    def test_makefile_deb_target_counts(self):
        from deploynator._config import Config
        from deploynator._deb import DebRunner
        with tempfile.TemporaryDirectory() as tmp:
            with open(os.path.join(tmp, "Makefile"), "w") as f:
                f.write("all:\n\techo hi\ndeb:\n\techo deb\n")
            r = DebRunner(Config.create())
            assert r.is_deb_project(tmp) is True
            assert r.deb_make_target(tmp) == "deb"

    def test_makefile_without_deb_no_project(self):
        from deploynator._config import Config
        from deploynator._deb import DebRunner
        with tempfile.TemporaryDirectory() as tmp:
            with open(os.path.join(tmp, "Makefile"), "w") as f:
                f.write("all:\n\techo hi\ntest:\n\techo t\n")
            assert DebRunner(Config.create()).is_deb_project(tmp) is False

    def test_no_shell_in_runner(self):
        import inspect

        import deploynator._deb as mod
        assert "shell=True" not in inspect.getsource(mod)


class TestBuildCommand:
    def test_custom_build_shlex(self):
        from deploynator._config import Config
        from deploynator._deb import DebRunner
        with tempfile.TemporaryDirectory() as tmp:
            r = DebRunner(Config.create())
            cmd = r.build_command(tmp, _toml(deb_build="make deb VERSION=1.0"))
            assert cmd == ["make", "deb", "VERSION=1.0"]

    def test_make_target_preferred(self):
        from deploynator._config import Config
        from deploynator._deb import DebRunner
        with tempfile.TemporaryDirectory() as tmp:
            with open(os.path.join(tmp, "Makefile"), "w") as f:
                f.write("deb:\n\techo deb\n")
            assert DebRunner(Config.create()).build_command(tmp, _toml()) == ["make", "deb"]

    def test_dpkg_buildpackage_fallback(self):
        from deploynator._config import Config
        from deploynator._deb import DebRunner
        with tempfile.TemporaryDirectory() as tmp:
            os.makedirs(os.path.join(tmp, "debian"))
            with open(os.path.join(tmp, "debian", "control"), "w") as f:
                f.write("Source: x\n")
            cmd = DebRunner(Config.create()).build_command(tmp, _toml())
            assert cmd is not None and cmd[0] == "dpkg-buildpackage"


class TestCleanAndRun:
    def test_clean_removes_outdir(self):
        from deploynator._config import Config
        from deploynator._deb import DebRunner
        with tempfile.TemporaryDirectory() as tmp:
            d = os.path.join(tmp, "dist-deb")
            os.makedirs(d)
            with open(os.path.join(d, "old.deb"), "w") as f:
                f.write("stale")
            DebRunner(Config.create()).clean(tmp, _toml())
            assert not os.path.exists(os.path.join(d, "old.deb"))

    def test_run_skips_without_packaging(self):
        from deploynator._config import Config
        from deploynator._deb import DebRunner
        with tempfile.TemporaryDirectory() as tmp:
            ok, msg, arts = DebRunner(Config.create()).run(tmp, _toml(), "0.1.0")
            assert ok is True and arts == []
            assert "skip" in msg.lower()

    def test_run_fails_on_broken_build(self):
        from deploynator._config import Config
        from deploynator._deb import DebRunner
        with tempfile.TemporaryDirectory() as tmp:
            with open(os.path.join(tmp, "Makefile"), "w") as f:
                f.write("deb:\n\tfalse\n")
            ok, _msg, _arts = DebRunner(Config.create()).run(tmp, _toml(), "0.1.0")
            assert ok is False

    def test_run_builds_fake_deb_via_make(self):
        from deploynator._config import Config
        from deploynator._deb import DebRunner
        with tempfile.TemporaryDirectory() as tmp:
            with open(os.path.join(tmp, "Makefile"), "w") as f:
                f.write("deb:\n\tmkdir -p dist-deb\n\ttouch dist-deb/myapp_0.1.0_amd64.deb\n")
            ok, _msg, arts = DebRunner(Config.create()).run(tmp, _toml(), "0.1.0")
            assert ok is True
            assert len(arts) == 1 and arts[0].endswith(".deb")
            assert os.path.isfile(arts[0])


class TestTomlDeb:
    def test_deb_section_parsed(self):
        from deploynator._toml import load_toml_config
        with tempfile.TemporaryDirectory() as tmp:
            with open(os.path.join(tmp, "deploynator.toml"), "w") as f:
                f.write('[deb]\nenabled = false\nbuild = "make deb"\n'
                        'outdir = "out"\ntimeout_s = 60\nupload_assets = false\n')
            cfg = load_toml_config(tmp)
            assert cfg.deb_enabled is False
            assert cfg.deb_build == "make deb"
            assert cfg.deb_outdir == "out"
            assert cfg.deb_timeout_s == 60
            assert cfg.deb_upload_assets is False

    def test_deb_defaults(self):
        from deploynator._toml import load_toml_config
        with tempfile.TemporaryDirectory() as tmp:
            cfg = load_toml_config(tmp)
            assert cfg.deb_enabled is True
            assert cfg.deb_outdir == "dist-deb"
            assert cfg.deb_upload_assets is True


class TestPipelineDeb:
    def test_deb_failure_aborts_with_error(self):
        from deploynator._config import Config
        from deploynator._deploy import DeployOrchestrator
        from deploynator._models import CommitType, ProjectConfig
        with tempfile.TemporaryDirectory() as tmp:
            origin = os.path.join(tmp, "origin.git")
            work = os.path.join(tmp, "work")
            subprocess.run(["git", "init", "--bare", "-q", origin], check=True)
            subprocess.run(["git", "init", "-q", work], check=True)
            subprocess.run(["git", "-C", work, "config", "user.email", "t@t.t"], check=True)
            subprocess.run(["git", "-C", work, "config", "user.name", "t"], check=True)
            with open(os.path.join(work, "f.txt"), "w") as f:
                f.write("x")
            with open(os.path.join(work, "Makefile"), "w") as f:
                f.write("test:\n\ttrue\ndeb:\n\tfalse\n")
            subprocess.run(["git", "-C", work, "add", "-A"], check=True)
            subprocess.run(["git", "-C", work, "commit", "-qm", "chore: init"], check=True)
            subprocess.run(["git", "-C", work, "remote", "add", "origin", origin], check=True)
            subprocess.run(["git", "-C", work, "branch", "-M", "main"], check=True)
            with open(os.path.join(work, "deploynator.toml"), "w") as f:
                f.write('[tests]\ncommands = ["true"]\n[docs]\nauto = false\n')
            res = DeployOrchestrator(Config.create()).deploy(
                project=ProjectConfig(name="p", path=work),
                commit_type=CommitType.FIX, subject="x",
                dry_run=False, run_tests=True, run_docs=False,
                run_pypi=False, run_deb=True,
            )
            assert res.success is False
            assert "deb" in (res.error or "").lower()

    def test_deb_success_does_not_break_deploy(self):
        from deploynator._config import Config
        from deploynator._deploy import DeployOrchestrator
        from deploynator._models import CommitType, ProjectConfig
        with tempfile.TemporaryDirectory() as tmp:
            origin = os.path.join(tmp, "origin.git")
            work = os.path.join(tmp, "work")
            subprocess.run(["git", "init", "--bare", "-q", origin], check=True)
            subprocess.run(["git", "init", "-q", work], check=True)
            subprocess.run(["git", "-C", work, "config", "user.email", "t@t.t"], check=True)
            subprocess.run(["git", "-C", work, "config", "user.name", "t"], check=True)
            with open(os.path.join(work, "f.txt"), "w") as f:
                f.write("x")
            with open(os.path.join(work, "Makefile"), "w") as f:
                f.write("test:\n\ttrue\ndeb:\n\tmkdir -p dist-deb\n\ttouch dist-deb/myapp_0.0.1_amd64.deb\n")
            subprocess.run(["git", "-C", work, "add", "-A"], check=True)
            subprocess.run(["git", "-C", work, "commit", "-qm", "chore: init"], check=True)
            subprocess.run(["git", "-C", work, "remote", "add", "origin", origin], check=True)
            subprocess.run(["git", "-C", work, "branch", "-M", "main"], check=True)
            with open(os.path.join(work, "deploynator.toml"), "w") as f:
                f.write('[tests]\ncommands = ["true"]\n[docs]\nauto = false\n')
            res = DeployOrchestrator(Config.create()).deploy(
                project=ProjectConfig(name="p", path=work),
                commit_type=CommitType.FIX, subject="x",
                dry_run=False, run_tests=True, run_docs=False,
                run_pypi=False, run_deb=True,
            )
            assert res.success is True

    def test_no_deb_flag_skips_build(self):
        from deploynator._config import Config
        from deploynator._deploy import DeployOrchestrator
        from deploynator._models import CommitType, ProjectConfig
        with tempfile.TemporaryDirectory() as tmp:
            origin = os.path.join(tmp, "origin.git")
            work = os.path.join(tmp, "work")
            subprocess.run(["git", "init", "--bare", "-q", origin], check=True)
            subprocess.run(["git", "init", "-q", work], check=True)
            subprocess.run(["git", "-C", work, "config", "user.email", "t@t.t"], check=True)
            subprocess.run(["git", "-C", work, "config", "user.name", "t"], check=True)
            with open(os.path.join(work, "f.txt"), "w") as f:
                f.write("x")
            with open(os.path.join(work, "Makefile"), "w") as f:
                f.write("test:\n\ttrue\ndeb:\n\tfalse\n")
            subprocess.run(["git", "-C", work, "add", "-A"], check=True)
            subprocess.run(["git", "-C", work, "commit", "-qm", "chore: init"], check=True)
            subprocess.run(["git", "-C", work, "remote", "add", "origin", origin], check=True)
            subprocess.run(["git", "-C", work, "branch", "-M", "main"], check=True)
            with open(os.path.join(work, "deploynator.toml"), "w") as f:
                f.write('[tests]\ncommands = ["true"]\n[docs]\nauto = false\n')
            res = DeployOrchestrator(Config.create()).deploy(
                project=ProjectConfig(name="p", path=work),
                commit_type=CommitType.FIX, subject="x",
                dry_run=False, run_tests=True, run_docs=False,
                run_pypi=False, run_deb=False,
            )
            assert res.success is True
