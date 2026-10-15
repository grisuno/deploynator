"""Tests for the deploy README footer injector."""

from __future__ import annotations

from deploynator._config import Config
from deploynator._readme import (
    FOOTER_END,
    FOOTER_START,
    ensure_deployed_footer,
    footer_block,
    footer_line,
)


def test_footer_line_is_english_without_emoji() -> None:
    """Footer line stays English prose with the badge URL."""
    line = footer_line(Config.create())
    assert line == "Deployed with [deploynator](https://github.com/grisuno/deploynator)"
    assert line.isascii()


def test_footer_block_is_anchored() -> None:
    """Footer block carries anchors for idempotent refresh."""
    block = footer_block(Config.create())
    assert block.startswith(FOOTER_START)
    assert block.endswith(FOOTER_END)
    assert "Deployed with [deploynator]" in block


def test_ensure_footer_appends_when_missing(tmp_path) -> None:
    """Missing footer is appended to the README."""
    readme = tmp_path / "README.md"
    readme.write_text("# Demo\n", encoding="utf-8")
    assert ensure_deployed_footer(str(tmp_path), Config.create()) is True
    content = readme.read_text(encoding="utf-8")
    assert FOOTER_START in content and FOOTER_END in content
    assert "Deployed with [deploynator]" in content


def test_ensure_footer_is_idempotent(tmp_path) -> None:
    """Second run reports no change when footer is current."""
    readme = tmp_path / "README.md"
    readme.write_text("# Demo\n", encoding="utf-8")
    assert ensure_deployed_footer(str(tmp_path), Config.create()) is True
    assert ensure_deployed_footer(str(tmp_path), Config.create()) is False


def test_ensure_footer_wraps_plain_line(tmp_path) -> None:
    """Legacy plain footer line is wrapped with anchors."""
    readme = tmp_path / "README.md"
    readme.write_text("# Demo\n\nDeployed with [deploynator](https://github.com/grisuno/deploynator)\n", encoding="utf-8")
    assert ensure_deployed_footer(str(tmp_path), Config.create()) is True
    content = readme.read_text(encoding="utf-8")
    assert content.count("Deployed with [deploynator]") == 1
    assert FOOTER_START in content


def test_ensure_footer_missing_readme(tmp_path) -> None:
    """No README means no change and no error."""
    assert ensure_deployed_footer(str(tmp_path / "empty"), Config.create()) is False
