"""
BDD-style tests for deploynator using behavior-driven patterns.

Feature: Multi-platform deployment
  As a developer
  I want to deploy my project to multiple git platforms
  So that I can release software consistently

Scenario: Create a release with correct version bumping
  Given a project configured for GitHub
  When I create a release of type "feat"
  Then the version should bump by "minor"

Scenario: Create a release of type fix
  Given a project configured for GitHub
  When I create a release of type "fix"
  Then the version should bump by "patch"

Scenario: Documentation changes don't bump version
  Given a project configured for GitHub
  When I create a release of type "docs"
  Then the version should NOT change
"""
import pytest
from deploynator._models import CommitType, VersionInfo


class TestBDDDeployScenarios:
    @pytest.fixture
    def project(self):
        return {
            "name": "my-app",
            "platforms": ["github"],
        }

    @pytest.mark.parametrize("commit_type,expected_bump,initial,final", [
        ("feat", "minor", "1.0.0", "1.1.0"),
        ("fix", "patch", "1.0.0", "1.0.1"),
        ("hotfix", "patch", "1.0.0", "1.0.1"),
        ("release", "major", "1.0.0", "2.0.0"),
        ("docs", None, "1.0.0", "1.0.0"),
        ("refactor", None, "1.0.0", "1.0.0"),
        ("style", None, "1.0.0", "1.0.0"),
        ("chore", None, "1.0.0", "1.0.0"),
    ])
    def test_version_bump_by_commit_type(self, project, commit_type, expected_bump, initial, final):
        ctype = CommitType.from_string(commit_type)
        strategy = ctype.bump_strategy()
        assert strategy == expected_bump

        current = VersionInfo.parse(initial)
        result = current.bump(strategy)
        assert str(result) == final

    def test_conventional_commit_parsing(self):
        from deploynator._models import CommitMessage
        cases = [
            ("feat: add login", "feat", "", "add login"),
            ("fix(api): timeout fix", "fix", "api", "timeout fix"),
            ("docs: readme update", "docs", "", "readme update"),
            ("release: v2.0", "release", "", "v2.0"),
        ]
        for raw, expected_type, expected_scope, expected_subject in cases:
            msg = CommitMessage.parse(raw)
            assert msg.commit_type.value == expected_type
            assert msg.scope == expected_scope
            assert msg.subject == expected_subject

    def test_commit_message_format_is_consistent(self):
        from deploynator._models import CommitMessage, CommitType
        msg = CommitMessage(
            commit_type=CommitType.FEAT,
            scope="core",
            subject="implement caching",
            body="Adds Redis-based caching layer",
            version="2.1.0",
        )
        formatted = msg.format()
        assert formatted.startswith("feat(core): implement caching")
        assert "Version: 2.1.0" in formatted
        assert "Redis-based caching" in formatted


class TestBDDPipeline:
    """
    Feature: Pipeline release con tests + docs + semver secuencial
      Como dev que jubila DEPLOY.sh
      Quiero tests que bloqueen, docs que no bloqueen y versión = max(file, tag)
      Para desplegar secuencialmente sin fragilidad
    """

    def test_tests_failure_blocks_release(self):
        """Given tests fallan, When deploy sin --no-test, Then abort sin tag."""
        import os
        import subprocess
        import tempfile
        from deploynator._config import Config
        from deploynator._deploy import DeployOrchestrator
        from deploynator._models import CommitType, ProjectConfig

        with tempfile.TemporaryDirectory() as tmp:
            subprocess.run(["git", "init", "-q", tmp], check=True)
            subprocess.run(["git", "-C", tmp, "config", "user.email", "t@t.t"], check=True)
            subprocess.run(["git", "-C", tmp, "config", "user.name", "t"], check=True)
            with open(os.path.join(tmp, "f.txt"), "w") as f:
                f.write("x")
            subprocess.run(["git", "-C", tmp, "add", "-A"], check=True)
            subprocess.run(["git", "-C", tmp, "commit", "-qm", "chore: init"], check=True)
            with open(os.path.join(tmp, "deploynator.toml"), "w") as f:
                f.write('[tests]\ncommands = ["false"]\n')
            orch = DeployOrchestrator(Config.create())
            res = orch.deploy(
                project=ProjectConfig(name="p", path=tmp),
                commit_type=CommitType.FIX, subject="x",
                dry_run=False, run_tests=True, run_docs=False,
            )
            assert res.success is False
            assert "Tests failed" in (res.error or "")

    def test_docs_failure_does_not_block_release(self):
        """Given docs fallan, When deploy, Then continúa (solo warning)."""
        import os
        import tempfile
        from deploynator._config import Config
        from deploynator._docs import DocsRunner
        from deploynator._toml import TomlConfig

        cfg = TomlConfig(
            project_name="p", version_file="version.json",
            test_commands=["true"], test_timeout_s=30, allow_no_tests=False,
            docs_auto=True, docs_command="false", docs_timeout_s=30,
            deploy_branch="main", deploy_remote="origin",
        )
        with tempfile.TemporaryDirectory() as tmp:
            assert DocsRunner(Config.create()).run(tmp, cfg) is False

    def test_force_bump_overrides_commit_type(self):
        """Given type fix (patch), When --bump major, Then 1.2.3 -> 2.0.0."""
        from deploynator._models import VersionInfo
        current = VersionInfo.parse("1.2.3")
        assert str(current.bump("major")) == "2.0.0"
        assert str(current.bump("patch")) == "1.2.4"

    def test_version_is_max_file_tag(self):
        """Given file 1.2.3 y tag 1.4.0, When current, Then 1.4.0."""
        import json
        import os
        import subprocess
        import tempfile
        from deploynator._config import Config
        from deploynator._semver import SemverManager

        with tempfile.TemporaryDirectory() as tmp:
            subprocess.run(["git", "init", "-q", tmp], check=True)
            subprocess.run(["git", "-C", tmp, "config", "user.email", "t@t.t"], check=True)
            subprocess.run(["git", "-C", tmp, "config", "user.name", "t"], check=True)
            with open(os.path.join(tmp, "f.txt"), "w") as f:
                f.write("x")
            subprocess.run(["git", "-C", tmp, "add", "-A"], check=True)
            subprocess.run(["git", "-C", tmp, "commit", "-qm", "chore: init"], check=True)
            with open(os.path.join(tmp, "version.json"), "w") as f:
                json.dump({"version": "1.2.3"}, f)
            subprocess.run(["git", "-C", tmp, "tag", "-a", "1.4.0", "-m", "v"], check=True)
            assert str(SemverManager(Config.create()).get_current_version(tmp)) == "1.4.0"
