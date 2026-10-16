# deploynator: _changelog

*Community 3 | 6 files | cohesion 0.21*

## Definition

This community groups 6 file(s) rooted at `deploynator` with dominant language py (cohesion 0.21). Central symbols: `ChangelogGenerator`, `Config`, `TestChangelogGenerator`, `TestConfigContract`, `__init__`, `_collect_entries`, `_find_readme`, `_format_entries`. Core file: `tests/test_config.py` (10 symbols). Documented purpose: Tests for the deploy README footer injector..

## Files

| File | Language | Layer | Symbols | Doc |
|------|----------|-------|---------|-----|
| `deploynator/_changelog.py` | py | utility | 9 | no |
| `deploynator/_config.py` | py | infrastructure | 6 | no |
| `deploynator/_readme.py` | py | utility | 4 | no |
| `tests/test_changelog.py` | py | testing | 8 | no |
| `tests/test_config.py` | py | testing | 10 | no |
| `tests/test_readme_footer.py` | py | testing | 6 | yes |

## Key Symbols

- `ChangelogGenerator` (class, `deploynator/_changelog.py:12`) `class ChangelogGenerator`
- `__init__` (method, `deploynator/_changelog.py:13`) `def __init__(self, config)`
- `generate_from_log` (method, `deploynator/_changelog.py:16`) `def generate_from_log(self, repo_path, from_ref, to_ref)`
- `generate_from_messages` (method, `deploynator/_changelog.py:25`) `def generate_from_messages(self, messages)`
- `generate_header` (method, `deploynator/_changelog.py:45`) `def generate_header(self)`
- `_collect_entries` (method, `deploynator/_changelog.py:48`) `def _collect_entries(self, repo_path, from_ref, to_ref)`
- `_format_entries` (method, `deploynator/_changelog.py:69`) `def _format_entries(self, entries)`
- `write_changelog` (method, `deploynator/_changelog.py:100`) `def write_changelog(self, repo_path, content, filename)`
- `format_for_release` (method, `deploynator/_changelog.py:110`) `def format_for_release(self, changelog_content, max_chars)`
- `Config` (class, `deploynator/_config.py:8`) `class Config`
- `create` (method, `deploynator/_config.py:79`) `def create(overrides)`
- `resolve_path` (method, `deploynator/_config.py:85`) `def resolve_path(self)`
- `gh_authd` (method, `deploynator/_config.py:91`) `def gh_authd(self)`
- `glab_authd` (method, `deploynator/_config.py:95`) `def glab_authd(self)`
- `bb_authd` (method, `deploynator/_config.py:99`) `def bb_authd(self)`
- `footer_block` (function, `deploynator/_readme.py:19`) `def footer_block(config)` - Return the anchored deploy footer block.
- `_find_readme` (function, `deploynator/_readme.py:32`) `def _find_readme(repo_path)` - Return the first README candidate in the repository.
- `ensure_deployed_footer` (function, `deploynator/_readme.py:49`) `def ensure_deployed_footer(repo_path, config)` - Append or refresh the deploy footer in the repository README.
- `footer_line` (function, `deploynator/_readme.py:96`) `def footer_line(config)` - Return the plain deploy footer line.
- `TestChangelogGenerator` (class, `tests/test_changelog.py:7`) `class TestChangelogGenerator`
- `generator` (method, `tests/test_changelog.py:9`) `def generator(self)`
- `test_generate_header` (method, `tests/test_changelog.py:13`) `def test_generate_header(self, generator)`
- `test_generate_from_messages` (method, `tests/test_changelog.py:17`) `def test_generate_from_messages(self, generator)`
- `test_generate_from_messages_organizes_by_type` (method, `tests/test_changelog.py:32`) `def test_generate_from_messages_organizes_by_type(self, generator)`
- `test_generate_empty` (method, `tests/test_changelog.py:43`) `def test_generate_empty(self, generator)`
- `test_format_for_release_short` (method, `tests/test_changelog.py:47`) `def test_format_for_release_short(self, generator)`
- `test_format_for_release_truncated` (method, `tests/test_changelog.py:52`) `def test_format_for_release_truncated(self, generator)`
- `TestConfigContract` (class, `tests/test_config.py:5`) `class TestConfigContract`
- `test_default_config_creation` (method, `tests/test_config.py:6`) `def test_default_config_creation(self)`
- `test_config_with_overrides` (method, `tests/test_config.py:13`) `def test_config_with_overrides(self)`

## Internal vs External Edges

- Internal resolved imports (EXTRACTED): 7
- Cross-boundary resolved imports (EXTRACTED): 66

## Connections

- [EXTRACTED] depends_on community 2 <-> 3 (strength 0.9): Extracted import edge crosses communities: app.py imports deploynator/_config.py.
- [EXTRACTED] depends_on community 0 <-> 3 (strength 0.9): Extracted import edge crosses communities: deploynator/_app.py imports deploynator/_config.py.
- [EXTRACTED] depends_on community 1 <-> 3 (strength 0.9): Extracted import edge crosses communities: deploynator/_docs.py imports deploynator/_config.py.
- [INFERRED] bridges community 3 <-> 0 (strength 0.6): Inferred cross-community bridge: tests/test_config.py reaches tests/test_models.py in 4 hops.
- [INFERRED] bridges community 0 <-> 3 (strength 0.6): Inferred cross-community bridge: tests/test_models.py reaches tests/test_readme_footer.py in 4 hops.

## Risks

- [taint high] `deploynator/_app.py` -> `deploynator/_config.py` via `subprocess` (1 hops)
- [taint high] `deploynator/_app.py` -> `deploynator/_readme.py` via `subprocess` (2 hops)
- [taint high] `deploynator/_app.py` -> `deploynator/_changelog.py` via `subprocess` (2 hops)
- [taint high] `deploynator/_app.py` -> `deploynator/_config.py` via `subprocess` (1 hops)

## Open Questions

- Why do 5 file(s) lack file-level docs (e.g. `deploynator/_changelog.py`)? What purpose do they serve?
- What would break if the most connected file in deploynator: _changelog changed?
- Should deploynator: _changelog be split, given cohesion 0.21?

## Sources

- `deploynator/_changelog.py`
- `deploynator/_config.py`
- `deploynator/_readme.py`
- `tests/test_changelog.py`
- `tests/test_config.py`
- `tests/test_readme_footer.py`
