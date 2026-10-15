"""Path-direct deploy + tag prefijos + version_file toml (ReadMenator real)."""
import json
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


class TestTagPrefixes:
    def test_release_v_prefix(self):
        from deploynator._semver import SemverManager
        from deploynator._config import Config
        m = SemverManager(Config.create())
        with tempfile.TemporaryDirectory() as tmp:
            _git_init(tmp)
            subprocess.run(["git", "-C", tmp, "tag", "-a", "release/v1.3.4", "-m", "v"], check=True)
            assert str(m.get_current_version(tmp)) == "1.3.4"

    def test_v_prefix(self):
        from deploynator._semver import SemverManager
        from deploynator._config import Config
        m = SemverManager(Config.create())
        with tempfile.TemporaryDirectory() as tmp:
            _git_init(tmp)
            subprocess.run(["git", "-C", tmp, "tag", "-a", "v2.0.1", "-m", "v"], check=True)
            assert str(m.get_current_version(tmp)) == "2.0.1"


class TestTomlVersionFile:
    def test_write_pyproject_toml(self):
        from deploynator._semver import SemverManager
        from deploynator._config import Config
        from deploynator._models import VersionInfo
        m = SemverManager(Config.create())
        with tempfile.TemporaryDirectory() as tmp:
            with open(os.path.join(tmp, "pyproject.toml"), "w") as f:
                f.write('[project]\nname = "x"\nversion = "1.3.5"\n')
            assert str(m.get_current_version(tmp, "pyproject.toml")) == "1.3.5"
            m.write_version_file(tmp, VersionInfo.parse("1.4.0"), "pyproject.toml")
            assert str(m.get_current_version(tmp, "pyproject.toml")) == "1.4.0"


class TestPathDirectRelease:
    def test_release_by_path_dry_run(self):
        from deploynator import DeploynatorApp
        from deploynator._config import Config
        with tempfile.TemporaryDirectory() as tmp:
            _git_init(tmp)
            app = DeploynatorApp(Config.create())
            res = app.release(commit_type="feat", project_name=tmp, dry_run=True,
                              no_test=True, no_docs=True)
            assert len(res) == 1
            assert res[0].version == "0.2.0"  # 0.1.0 default + minor

    def test_no_platforms_pushes_to_origin(self):
        from deploynator._deploy import DeployOrchestrator
        from deploynator._config import Config
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
            subprocess.run(["git", "-C", work, "add", "-A"], check=True)
            subprocess.run(["git", "-C", work, "commit", "-qm", "chore: init"], check=True)
            subprocess.run(["git", "-C", work, "remote", "add", "origin", origin], check=True)
            subprocess.run(["git", "-C", work, "branch", "-M", "main"], check=True)
            with open(os.path.join(work, "deploynator.toml"), "w") as f:
                f.write('[tests]\ncommands = ["true"]\n[docs]\nauto = false\n')
            orch = DeployOrchestrator(Config.create())
            res = orch.deploy(
                project=ProjectConfig(name="p", path=work),
                commit_type=CommitType.FIX, subject="x",
                dry_run=False, run_tests=True, run_docs=False,
            )
            assert res.success is True
            assert any("origin" in p for p in res.platforms_pushed)
            tags = subprocess.run(["git", "--git-dir", origin, "tag", "--list"],
                                  capture_output=True, text=True).stdout
            assert res.version in tags
