import pytest
from deploynator._config import Config
from deploynator._changelog import ChangelogGenerator
from deploynator._models import CommitType, CommitMessage, ChangelogEntry


class TestChangelogGenerator:
    @pytest.fixture
    def generator(self):
        config = Config.create()
        return ChangelogGenerator(config)

    def test_generate_header(self, generator):
        header = generator.generate_header()
        assert header.startswith("# Changelog")

    def test_generate_from_messages(self, generator):
        messages = [
            "feat(auth): add OAuth2 login",
            "fix(api): handle timeout gracefully",
            "docs: update README",
            "random message without type",
        ]
        result = generator.generate_from_messages(messages)
        assert "# Changelog" in result
        assert "feat(auth): add OAuth2 login" in result
        assert "fix(api): handle timeout gracefully" in result
        assert "docs: update README" in result
        assert "random message without type" in result
        assert "deploynator" in result

    def test_generate_from_messages_organizes_by_type(self, generator):
        messages = [
            "fix: bug one",
            "feat: feature one",
            "fix: bug two",
            "feat: feature two",
        ]
        result = generator.generate_from_messages(messages)
        assert "### Bug Fixes" in result
        assert "### Features" in result

    def test_generate_empty(self, generator):
        result = generator.generate_from_messages([])
        assert "No changes recorded" in result

    def test_format_for_release_short(self, generator):
        short = "short content"
        result = generator.format_for_release(short)
        assert result == short

    def test_format_for_release_truncated(self, generator):
        long_content = "x" * (Config.create().max_release_chars + 1000)
        result = generator.format_for_release(long_content)
        assert len(result) <= Config.create().max_release_chars + 200
        assert "truncated" in result
