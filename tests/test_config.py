import pytest
from deploynator._config import Config


class TestConfigContract:
    def test_default_config_creation(self):
        config = Config.create()
        assert config.changelog_file == "CHANGELOG.md"
        assert config.version_file == "version.json"
        assert config.default_branch == "main"
        assert config.max_release_chars == 120000

    def test_config_with_overrides(self):
        config = Config.create({"changelog_file": "HISTORY.md", "default_branch": "master"})
        assert config.changelog_file == "HISTORY.md"
        assert config.default_branch == "master"
        assert config.version_file == "version.json"

    def test_config_frozen(self):
        config = Config.create()
        with pytest.raises(Exception):
            config.changelog_file = "new.md"

    def test_config_immutability(self):
        config1 = Config.create({"default_branch": "develop"})
        config2 = Config.create()
        assert config1.default_branch == "develop"
        assert config2.default_branch == "main"

    def test_resolve_path(self):
        config = Config.create({"_path": "/tmp/test"})
        assert config.resolve_path("subdir", "file.txt") == "/tmp/test/subdir/file.txt"

    def test_auth_checks(self, monkeypatch):
        config = Config.create()
        monkeypatch.setenv("GITHUB_TOKEN", "test-token")
        assert config.gh_authd is True
        assert config.glab_authd is False

    def test_conventional_types_contains_all(self):
        config = Config.create()
        expected = {"feat", "fix", "hotfix", "docs", "refactor", "style", "chore", "test", "release", "patch"}
        assert set(config.conventional_types.keys()) == expected

    def test_semver_pattern_valid(self):
        import re
        config = Config.create()
        assert bool(re.match(config.semver_pattern, "1.2.3"))
        assert not bool(re.match(config.semver_pattern, "1.2"))
        assert not bool(re.match(config.semver_pattern, "version-1.2.3"))

    def test_commit_type_pattern_valid(self):
        import re
        config = Config.create()
        assert bool(re.match(config.commit_type_pattern, "feat: add login"))
        assert bool(re.match(config.commit_type_pattern, "fix(auth): handle timeout"))
        assert not bool(re.match(config.commit_type_pattern, "invalid: message"))
