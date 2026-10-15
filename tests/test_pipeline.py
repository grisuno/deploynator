"""RED: pipeline deploy — tests gate + docs non-blocking + bump override + max(file,tag)."""
import json
import os
import subprocess
import tempfile
import pytest
from deploynator._config import Config
from deploynator._models import CommitType, ProjectConfig, VersionInfo


def _git_init(tmp):
    subprocess.run(["git", "init", "-q", tmp], check=True)
    subprocess.run(["git", "-C", tmp, "config", "user.email", "t@t.t"], check=True)
    subprocess.run(["git", "-C", tmp, "config", "user.name", "t"], check=True)
    with open(os.path.join(tmp, "a.txt"), "w") as f:
        f.write("hi")
    subprocess.run(["git", "-C", tmp, "add", "-A"], check=True)
    subprocess.run(["git", "-C", tmp, "commit", "-qm", "chore: init"], check=True)


class TestSemverMax:
    def test_current_is_max_of_file_and_tag(self):
        from deploynator._semver import SemverManager
        m = SemverManager(Config.create())
        with tempfile.TemporaryDirectory() as tmp:
            _git_init(tmp)
            with open(os.path.join(tmp, "version.json"), "w") as f:
                json.dump({"version": "1.2.3"}, f)
            subprocess.run(["git", "-C", tmp, "tag", "-a", "1.4.0", "-m", "v"], check=True)
            cur = m.get_current_version(tmp)
            assert str(cur) == "1.4.0"

    def test_file_ahead_of_tag(self):
        from deploynator._semver import SemverManager
        m = SemverManager(Config.create())
        with tempfile.TemporaryDirectory() as tmp:
            _git_init(tmp)
            with open(os.path.join(tmp, "version.json"), "w") as f:
                json.dump({"version": "2.0.0"}, f)
            subprocess.run(["git", "-C", tmp, "tag", "-a", "1.9.9", "-m", "v"], check=True)
            cur = m.get_current_version(tmp)
            assert str(cur) == "2.0.0"

    def test_max_version_helper(self):
        from deploynator._semver import SemverManager
        m = SemverManager(Config.create())
        a = VersionInfo.parse("1.2.3")
        b = VersionInfo.parse("1.4.0")
        assert str(m.max_version(a, b)) == "1.4.0"
        assert str(m.max_version(b, a)) == "1.4.0"


class TestDeployPipeline:
    def _project(self, path):
        return ProjectConfig(
            name="p",
            description="",
            platforms=[],
            path=path,
        )

    def test_aborts_on_test_failure(self):
        from deploynator._deploy import DeployOrchestrator
        orch = DeployOrchestrator(Config.create())
        with tempfile.TemporaryDirectory() as tmp:
            _git_init(tmp)
            subprocess.run(["git", "-C", tmp, "tag", "-a", "0.1.0", "-m", "v"], check=True)
            with open(os.path.join(tmp, "deploynator.toml"), "w") as f:
                f.write('[tests]\ncommands = ["false"]\n')
            res = orch.deploy(
                project=self._project(tmp),
                commit_type=CommitType.FIX,
                subject="x",
                dry_run=False,
                run_tests=True,
                run_docs=False,
            )
            assert res.success is False
            assert "Tests failed" in (res.error or "")
            # sin mutar: no debe crear tag 0.1.1
            tags = subprocess.run(
                ["git", "-C", tmp, "tag", "--list"], capture_output=True, text=True
            ).stdout
            assert "0.1.1" not in tags

    def test_no_test_skips_failing_tests(self):
        from deploynator._deploy import DeployOrchestrator
        orch = DeployOrchestrator(Config.create())
        with tempfile.TemporaryDirectory() as tmp:
            _git_init(tmp)
            with open(os.path.join(tmp, "deploynator.toml"), "w") as f:
                f.write('[tests]\ncommands = ["false"]\n')
            res = orch.deploy(
                project=self._project(tmp),
                commit_type=CommitType.FIX,
                subject="x",
                dry_run=True,  # dry-run no muta pero valida gate
                run_tests=False,
                run_docs=False,
            )
            assert res.success is True or "remote" in (res.error or "").lower()

    def test_docs_failure_does_not_block(self):
        from deploynator._deploy import DeployOrchestrator
        orch = DeployOrchestrator(Config.create())
        with tempfile.TemporaryDirectory() as tmp:
            _git_init(tmp)
            with open(os.path.join(tmp, "deploynator.toml"), "w") as f:
                f.write('[tests]\ncommands = ["true"]\n[docs]\ncommand = "false"\n')
            res = orch.deploy(
                project=self._project(tmp),
                commit_type=CommitType.FIX,
                subject="x",
                dry_run=True,
                run_tests=True,
                run_docs=True,
            )
            # dry-run: docs fail solo warning, no abort por docs
            assert "Tests failed" not in (res.error or "")

    def test_force_bump_overrides(self):
        from deploynator._deploy import DeployOrchestrator
        orch = DeployOrchestrator(Config.create())
        with tempfile.TemporaryDirectory() as tmp:
            _git_init(tmp)
            with open(os.path.join(tmp, "version.json"), "w") as f:
                json.dump({"version": "1.2.3"}, f)
            subprocess.run(["git", "-C", tmp, "add", "-A"], check=True)
            subprocess.run(["git", "-C", tmp, "commit", "-qm", "chore: v"], check=True)
            subprocess.run(["git", "-C", tmp, "tag", "-a", "1.2.3", "-m", "v"], check=True)
            with open(os.path.join(tmp, "deploynator.toml"), "w") as f:
                f.write('[tests]\ncommands = ["true"]\n')
            res = orch.deploy(
                project=self._project(tmp),
                commit_type=CommitType.FIX,  # patch → 1.2.4
                subject="x",
                dry_run=True,
                run_tests=False,
                run_docs=False,
                force_bump="major",  # → 2.0.0
            )
            assert res.version == "2.0.0"

    def test_dry_run_prints_would(self, capsys):
        from deploynator._deploy import DeployOrchestrator
        orch = DeployOrchestrator(Config.create())
        with tempfile.TemporaryDirectory() as tmp:
            _git_init(tmp)
            res = orch.deploy(
                project=self._project(tmp),
                commit_type=CommitType.FEAT,
                subject="x",
                dry_run=True,
                run_tests=True,
                run_docs=True,
            )
            out = capsys.readouterr().out
            assert "DRY-RUN" in out or "Would" in out
