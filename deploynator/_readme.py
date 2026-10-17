from __future__ import annotations

from pathlib import Path

from deploynator._config import Config

FOOTER_START = "<!-- deploynator-footer -->"
FOOTER_END = "<!-- /deploynator-footer -->"

README_CANDIDATES = (
    "README.md",
    "README.rst",
    "Readme.md",
    "readme.md",
)


def footer_block(config: Config) -> str:
    """Return the anchored deploy footer block.

    Args:
        config: Centralized configuration with badge URL and text.

    Returns:
        Anchored footer text in English without emojis.
    """
    line = f"Deployed with [deploynator]({config.deploynator_badge_url})"
    return f"{FOOTER_START}\n\n---\n\n{line}\n\n{FOOTER_END}"


def _find_readme(repo_path: str) -> Path | None:
    """Return the first README candidate in the repository.

    Args:
        repo_path: Repository root directory.

    Returns:
        README path or None when no candidate exists.
    """
    root = Path(repo_path)
    for name in README_CANDIDATES:
        candidate = root / name
        if candidate.is_file() and not candidate.is_symlink():
            return candidate
    return None


def ensure_deployed_footer(repo_path: str, config: Config | None = None) -> bool:
    """Append or refresh the deploy footer in the repository README.

    Args:
        repo_path: Repository root directory holding the README.
        config: Optional configuration override.

    Returns:
        True when the README was created or modified, False otherwise.
    """
    cfg = config or Config.create()
    readme = _find_readme(repo_path)
    if readme is None:
        return False
    try:
        content = readme.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return False
    block = footer_block(cfg)
    plain_line = f"Deployed with [deploynator]({cfg.deploynator_badge_url})"
    if FOOTER_START in content and FOOTER_END in content:
        start = content.find(FOOTER_START)
        end = content.find(FOOTER_END) + len(FOOTER_END)
        current = content[start:end]
        if current.strip() == block.strip():
            return False
        updated = content[:start].rstrip("\n") + "\n\n" + block + "\n" + content[end:].lstrip("\n")
        try:
            readme.write_text(updated.rstrip("\n") + "\n", encoding="utf-8")
        except OSError:
            return False
        return True
    if plain_line in content:
        updated = content.replace(plain_line, block, 1)
        try:
            readme.write_text(updated.rstrip("\n") + "\n", encoding="utf-8")
        except OSError:
            return False
        return True
    updated = content.rstrip("\n") + "\n\n" + block + "\n"
    try:
        readme.write_text(updated, encoding="utf-8")
    except OSError:
        return False
    return True


def footer_line(config: Config | None = None) -> str:
    """Return the plain deploy footer line.

    Args:
        config: Optional configuration override.

    Returns:
        English footer line without emojis.
    """
    cfg = config or Config.create()
    return f"Deployed with [deploynator]({cfg.deploynator_badge_url})"
