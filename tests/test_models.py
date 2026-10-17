
import pytest

from deploynator._models import (
    ChangelogEntry,
    CommitMessage,
    CommitType,
    DeployResult,
    Platform,
    PlatformConfig,
    ProjectConfig,
    ReleaseInfo,
    VersionConfig,
    VersionInfo,
)


class TestPlatformContract:
    def test_platform_from_string(self):
        assert Platform.from_string("github") == Platform.GITHUB
        assert Platform.from_string("gitlab") == Platform.GITLAB
        assert Platform.from_string("bitbucket") == Platform.BITBUCKET

    def test_platform_from_string_case(self):
        assert Platform.from_string("GitHub") == Platform.GITHUB
        assert Platform.from_string("GITLAB") == Platform.GITLAB

    def test_platform_from_string_invalid(self):
        with pytest.raises(ValueError):
            Platform.from_string("invalid")

    def test_platform_cli_name(self):
        assert Platform.GITHUB.cli_name() == "gh"
        assert Platform.GITLAB.cli_name() == "glab"
        assert Platform.BITBUCKET.cli_name() == "bb"

    def test_platform_auth_env(self):
        assert Platform.GITHUB.auth_env_var() == "GITHUB_TOKEN"
        assert Platform.GITLAB.auth_env_var() == "GITLAB_TOKEN"


class TestCommitTypeContract:
    def test_commit_type_from_string(self):
        assert CommitType.from_string("feat") == CommitType.FEAT
        assert CommitType.from_string("fix") == CommitType.FIX
        assert CommitType.from_string("HOTFIX") == CommitType.HOTFIX

    def test_commit_type_invalid(self):
        with pytest.raises(ValueError):
            CommitType.from_string("invalid")

    def test_commit_type_valid_types(self):
        types = CommitType.valid_types()
        assert "feat" in types
        assert "fix" in types
        assert "release" in types
        assert len(types) == 10

    def test_bump_strategy(self):
        assert CommitType.FEAT.bump_strategy() == "minor"
        assert CommitType.FIX.bump_strategy() == "patch"
        assert CommitType.HOTFIX.bump_strategy() == "patch"
        assert CommitType.RELEASE.bump_strategy() == "major"
        assert CommitType.DOCS.bump_strategy() is None
        assert CommitType.REFACTOR.bump_strategy() is None

    def test_section_header(self):
        assert CommitType.FEAT.section_header() == "Features"
        assert CommitType.FIX.section_header() == "Bug Fixes"
        assert CommitType.DOCS.section_header() == "Documentation"


class TestCommitMessageContract:
    def test_format_basic(self):
        msg = CommitMessage(commit_type=CommitType.FEAT, scope="auth", subject="add login")
        formatted = msg.format()
        assert "feat(auth): add login" in formatted

    def test_format_with_version(self):
        msg = CommitMessage(
            commit_type=CommitType.FIX, scope="", subject="fix crash",
            version="1.2.3",
        )
        formatted = msg.format()
        assert "fix: fix crash" in formatted
        assert "Version: 1.2.3" in formatted

    def test_format_with_body_and_footer(self):
        msg = CommitMessage(
            commit_type=CommitType.FEAT, scope="api", subject="new endpoint",
            body="Added /api/v2/users", footer="BREAKING CHANGE",
        )
        formatted = msg.format()
        assert "feat(api): new endpoint" in formatted
        assert "/api/v2/users" in formatted
        assert "BREAKING CHANGE" in formatted

    def test_parse_valid(self):
        msg = CommitMessage.parse("feat(auth): add login with OAuth")
        assert msg.commit_type == CommitType.FEAT
        assert msg.scope == "auth"
        assert msg.subject == "add login with OAuth"

    def test_parse_no_scope(self):
        msg = CommitMessage.parse("fix: resolve timeout")
        assert msg.commit_type == CommitType.FIX
        assert msg.scope == ""
        assert msg.subject == "resolve timeout"

    def test_parse_invalid(self):
        with pytest.raises(ValueError):
            CommitMessage.parse("invalid message format")


class TestVersionInfoContract:
    def test_parse(self):
        v = VersionInfo.parse("1.2.3")
        assert v.major == 1
        assert v.minor == 2
        assert v.patch == 3

    def test_str(self):
        v = VersionInfo(2, 1, 0)
        assert str(v) == "2.1.0"

    def test_bump_major(self):
        v = VersionInfo(1, 2, 3)
        bumped = v.bump("major")
        assert str(bumped) == "2.0.0"

    def test_bump_minor(self):
        v = VersionInfo(1, 2, 3)
        bumped = v.bump("minor")
        assert str(bumped) == "1.3.0"

    def test_bump_patch(self):
        v = VersionInfo(1, 2, 3)
        bumped = v.bump("patch")
        assert str(bumped) == "1.2.4"

    def test_bump_none(self):
        v = VersionInfo(1, 2, 3)
        bumped = v.bump(None)
        assert str(bumped) == "1.2.3"

    def test_parse_invalid(self):
        with pytest.raises(ValueError):
            VersionInfo.parse("not-a-version")
        with pytest.raises(ValueError):
            VersionInfo.parse("1.2")


class TestPlatformConfigContract:
    def test_from_dict_full(self):
        data = {"platform": "github", "repo": "user/repo", "enabled": True}
        pc = PlatformConfig.from_dict(data)
        assert pc.platform == Platform.GITHUB
        assert pc.repo == "user/repo"
        assert pc.enabled is True

    def test_from_dict_defaults(self):
        data = {"platform": "gitlab", "repo": "user/repo"}
        pc = PlatformConfig.from_dict(data)
        assert pc.enabled is True
        assert pc.auth_env is None


class TestProjectConfigContract:
    def test_from_dict_minimal(self):
        data = {"name": "test-proj"}
        pc = ProjectConfig.from_dict(data)
        assert pc.name == "test-proj"
        assert pc.description == ""
        assert pc.platforms == []
        assert isinstance(pc.version, VersionConfig)

    def test_from_dict_full(self):
        data = {
            "name": "my-app",
            "description": "Test app",
            "platforms": {
                "github": {"repo": "user/my-app", "enabled": True},
                "gitlab": "user/my-app",
            },
            "version": {"file": "VERSION", "file_type": "text"},
        }
        pc = ProjectConfig.from_dict(data)
        assert pc.name == "my-app"
        assert pc.description == "Test app"
        assert len(pc.platforms) == 2
        assert pc.version.file == "VERSION"

    def test_from_dict_platform_string(self):
        data = {
            "name": "test",
            "platforms": {"github": "user/repo"},
        }
        pc = ProjectConfig.from_dict(data)
        assert len(pc.platforms) == 1
        assert pc.platforms[0].repo == "user/repo"
        assert pc.platforms[0].enabled is True


class TestChangelogEntryContract:
    def test_from_git_log_line(self):
        entry = ChangelogEntry.from_git_log_line("feat: new feature", author="dev", sha="abc123")
        assert entry.commit_type == CommitType.FEAT
        assert entry.message == "feat: new feature"
        assert entry.author == "dev"
        assert entry.sha == "abc123"

    def test_from_git_log_line_unparseable(self):
        entry = ChangelogEntry.from_git_log_line("random commit message")
        assert entry.commit_type == CommitType.CHORE

    def test_from_git_log_line_scope(self):
        entry = ChangelogEntry.from_git_log_line("fix(api): timeout issue")
        assert entry.commit_type == CommitType.FIX


class TestReleaseInfoContract:
    def test_defaults(self):
        r = ReleaseInfo(version="1.0.0", title="v1.0.0", notes="First release")
        assert r.target_branch == "main"
        assert r.prerelease is False
        assert r.draft is False

    def test_custom(self):
        r = ReleaseInfo(
            version="2.0.0-beta", title="Beta", notes="Beta release",
            target_branch="develop", prerelease=True, draft=True,
        )
        assert r.prerelease is True
        assert r.draft is True
        assert r.target_branch == "develop"


class TestDeployResultContract:
    def test_defaults(self):
        r = DeployResult(project="test", version="1.0", success=True)
        assert r.project == "test"
        assert r.success is True
        assert r.platforms_pushed == []
        assert r.releases_created == []
        assert r.error is None

    def test_with_data(self):
        r = DeployResult(
            project="app", version="2.0", success=False,
            platforms_pushed=["github"], releases_created=[],
            error="Push failed",
        )
        assert r.error == "Push failed"
        assert not r.success
