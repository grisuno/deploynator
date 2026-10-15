# deploynator: _changelog

*Community 0 | 6 files | cohesion 0.22*

## Definition

This community groups 6 file(s) rooted at `deploynator` with dominant language py (cohesion 0.22). Central symbols: `ChangelogGenerator`, `Config`, `PyPIRunner`, `TestChangelogGenerator`, `TestCleanAndRun`, `TestConfigContract`, `TestDetect`, `TestPipelinePyPI`. Core file: `tests/test_pypi.py` (22 symbols). Documented purpose: RED: PyPI runner — detecta packaging, build limpio, upload twine..

## Files

| File | Language | Layer | Symbols | Doc |
|------|----------|-------|---------|-----|
| `deploynator/_changelog.py` | py | utility | 9 | no |
| `deploynator/_config.py` | py | infrastructure | 6 | no |
| `deploynator/_pypi.py` | py | utility | 8 | no |
| `tests/test_changelog.py` | py | testing | 8 | no |
| `tests/test_config.py` | py | testing | 10 | no |
| `tests/test_pypi.py` | py | testing | 22 | yes |

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
- `PyPIRunner` (class, `deploynator/_pypi.py:12`) `class PyPIRunner`
- `__init__` (method, `deploynator/_pypi.py:13`) `def __init__(self, config)`
- `is_packaging_project` (method, `deploynator/_pypi.py:16`) `def is_packaging_project(self, project_path)`
- `has_credentials` (method, `deploynator/_pypi.py:33`) `def has_credentials(self)`
- `prompt_for_credentials` (method, `deploynator/_pypi.py:39`) `def prompt_for_credentials(self)` - Pide el token PyPI por input oculto solo si hay TTY.
- `save_pypirc` (method, `deploynator/_pypi.py:72`) `def save_pypirc(self, token, path)` - Guarda el token en ~/.pypirc (username __token__, modo 600).
- `clean` (method, `deploynator/_pypi.py:90`) `def clean(self, project_path, toml)`
- `run` (method, `deploynator/_pypi.py:107`) `def run(self, project_path, toml, version, token)`
- `TestChangelogGenerator` (class, `tests/test_changelog.py:7`) `class TestChangelogGenerator`
- `generator` (method, `tests/test_changelog.py:9`) `def generator(self)`
- `test_generate_header` (method, `tests/test_changelog.py:13`) `def test_generate_header(self, generator)`
- `test_generate_from_messages` (method, `tests/test_changelog.py:17`) `def test_generate_from_messages(self, generator)`
- `test_generate_from_messages_organizes_by_type` (method, `tests/test_changelog.py:32`) `def test_generate_from_messages_organizes_by_type(self, generator)`
- `test_generate_empty` (method, `tests/test_changelog.py:43`) `def test_generate_empty(self, generator)`
- `test_format_for_release_short` (method, `tests/test_changelog.py:47`) `def test_format_for_release_short(self, generator)`

## Internal vs External Edges

- Internal resolved imports (EXTRACTED): 33
- Cross-boundary resolved imports (EXTRACTED): 46

## Connections

- [EXTRACTED] depends_on community 4 <-> 0 (strength 0.9): Extracted import edge crosses communities: deploynator/__main__.py imports deploynator/_config.py.
- [EXTRACTED] depends_on community 3 <-> 0 (strength 0.9): Extracted import edge crosses communities: deploynator/_app.py imports deploynator/_config.py.
- [EXTRACTED] depends_on community 0 <-> 2 (strength 0.9): Extracted import edge crosses communities: deploynator/_changelog.py imports deploynator/_models.py.
- [EXTRACTED] depends_on community 1 <-> 0 (strength 0.9): Extracted import edge crosses communities: deploynator/_docs.py imports deploynator/_config.py.
- [INFERRED] bridges community 4 <-> 0 (strength 0.7): Inferred cross-community bridge: deploynator/__init__.py reaches deploynator/_changelog.py in 3 hops.
- [INFERRED] bridges community 0 <-> 2 (strength 0.6): Inferred cross-community bridge: tests/test_config.py reaches tests/test_models.py in 4 hops.
- [INFERRED] shares_context community 0 <-> 5 (strength 0.5): Inferred shared context (language py) with no import path between community 0 (deploynator: _changelog) and community 5 (orphans).

## Risks

- [taint high] `deploynator/_app.py` -> `deploynator/_config.py` via `subprocess` (1 hops)
- [taint high] `deploynator/_app.py` -> `deploynator/_pypi.py` via `subprocess` (2 hops)
- [taint high] `deploynator/_app.py` -> `deploynator/_changelog.py` via `subprocess` (2 hops)
- [taint high] `deploynator/_app.py` -> `deploynator/_config.py` via `subprocess` (1 hops)

## Open Questions

- Why do 5 file(s) lack file-level docs (e.g. `deploynator/_changelog.py`)? What purpose do they serve?
- What would break if the most connected file in deploynator: _changelog changed?
- Should deploynator: _changelog be split, given cohesion 0.22?

## Sources

- `deploynator/_changelog.py`
- `deploynator/_config.py`
- `deploynator/_pypi.py`
- `tests/test_changelog.py`
- `tests/test_config.py`
- `tests/test_pypi.py`
