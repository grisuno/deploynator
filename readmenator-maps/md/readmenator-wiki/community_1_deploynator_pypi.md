# deploynator: _pypi

*Community 1 | 8 files | cohesion 0.38*

## Definition

This community groups 8 file(s) rooted at `deploynator` with dominant language py (cohesion 0.38). Central symbols: `DocsRunner`, `PyPIRunner`, `TestBDDDeployScenarios`, `TestBDDPipeline`, `TestCleanAndRun`, `TestDetect`, `TestDocsRunner`, `TestPipelinePyPI`. Core file: `tests/test_pypi.py` (25 symbols). Documented purpose: BDD-style tests for deploynator using behavior-driven patterns.  Feature: Multi-platform deployment As a developer I want to deploy my project to multiple git p.

## Files

| File | Language | Layer | Symbols | Doc |
|------|----------|-------|---------|-----|
| `deploynator/_docs.py` | py | utility | 3 | no |
| `deploynator/_pypi.py` | py | utility | 8 | no |
| `deploynator/_runner.py` | py | utility | 3 | no |
| `deploynator/_toml.py` | py | utility | 4 | no |
| `tests/bdd_test_deploy.py` | py | testing | 10 | yes |
| `tests/test_pypi.py` | py | testing | 25 | yes |
| `tests/test_runner.py` | py | testing | 15 | yes |
| `tests/test_toml.py` | py | testing | 8 | yes |

## Key Symbols

- `DocsRunner` (class, `deploynator/_docs.py:10`) `class DocsRunner`
- `__init__` (method, `deploynator/_docs.py:11`) `def __init__(self, config)`
- `run` (method, `deploynator/_docs.py:14`) `def run(self, project_path, toml)`
- `PyPIRunner` (class, `deploynator/_pypi.py:12`) `class PyPIRunner`
- `__init__` (method, `deploynator/_pypi.py:13`) `def __init__(self, config)`
- `is_packaging_project` (method, `deploynator/_pypi.py:16`) `def is_packaging_project(self, project_path)`
- `has_credentials` (method, `deploynator/_pypi.py:33`) `def has_credentials(self)`
- `prompt_for_credentials` (method, `deploynator/_pypi.py:39`) `def prompt_for_credentials(self)` - Pide el token PyPI por input oculto solo si hay TTY.
- `save_pypirc` (method, `deploynator/_pypi.py:72`) `def save_pypirc(self, token, path)` - Guarda el token en ~/.pypirc (username __token__, modo 600).
- `clean` (method, `deploynator/_pypi.py:90`) `def clean(self, project_path, toml)`
- `run` (method, `deploynator/_pypi.py:107`) `def run(self, project_path, toml, version, token)`
- `TestRunner` (class, `deploynator/_runner.py:11`) `class TestRunner`
- `__init__` (method, `deploynator/_runner.py:12`) `def __init__(self, config)`
- `run` (method, `deploynator/_runner.py:15`) `def run(self, project_path, toml)`
- `TomlConfig` (class, `deploynator/_toml.py:14`) `class TomlConfig`
- `__post_init__` (method, `deploynator/_toml.py:30`) `def __post_init__(self)`
- `_clamp_timeout` (function, `deploynator/_toml.py:38`) `def _clamp_timeout(value)`
- `load_toml_config` (function, `deploynator/_toml.py:46`) `def load_toml_config(project_path)`
- `TestBDDDeployScenarios` (class, `tests/bdd_test_deploy.py:28`) `class TestBDDDeployScenarios`
- `project` (method, `tests/bdd_test_deploy.py:30`) `def project(self)`
- `test_version_bump_by_commit_type` (method, `tests/bdd_test_deploy.py:46`) `def test_version_bump_by_commit_type(self, project, commit_type, expected_bump,`
- `test_conventional_commit_parsing` (method, `tests/bdd_test_deploy.py:55`) `def test_conventional_commit_parsing(self)`
- `test_commit_message_format_is_consistent` (method, `tests/bdd_test_deploy.py:69`) `def test_commit_message_format_is_consistent(self)`
- `TestBDDPipeline` (class, `tests/bdd_test_deploy.py:84`) `class TestBDDPipeline` - Feature: Pipeline release con tests + docs + semver secuencial
- `test_tests_failure_blocks_release` (method, `tests/bdd_test_deploy.py:92`) `def test_tests_failure_blocks_release(self)` - Given tests fallan, When deploy sin --no-test, Then abort sin tag.
- `test_docs_failure_does_not_block_release` (method, `tests/bdd_test_deploy.py:120`) `def test_docs_failure_does_not_block_release(self)` - Given docs fallan, When deploy, Then continúa (solo warning).
- `test_force_bump_overrides_commit_type` (method, `tests/bdd_test_deploy.py:137`) `def test_force_bump_overrides_commit_type(self)` - Given type fix (patch), When --bump major, Then 1.2.3 -> 2.0.0.
- `test_version_is_max_file_tag` (method, `tests/bdd_test_deploy.py:144`) `def test_version_is_max_file_tag(self)` - Given file 1.2.3 y tag 1.4.0, When current, Then 1.4.0.
- `_isolated_home` (function, `tests/test_pypi.py:10`) `def _isolated_home(tmp_path, monkeypatch)` - Aísla ~/.pypirc real: los tests nunca ven ni tocan credenciales del operador.
- `_git_init` (function, `tests/test_pypi.py:15`) `def _git_init(tmp)`

## Internal vs External Edges

- Internal resolved imports (EXTRACTED): 45
- Cross-boundary resolved imports (EXTRACTED): 54

## Connections

- [EXTRACTED] depends_on community 0 <-> 1 (strength 0.9): Extracted import edge crosses communities: deploynator/_app.py imports deploynator/_toml.py.
- [EXTRACTED] depends_on community 1 <-> 3 (strength 0.9): Extracted import edge crosses communities: deploynator/_docs.py imports deploynator/_config.py.
- [EXTRACTED] depends_on community 2 <-> 1 (strength 0.9): Extracted import edge crosses communities: tests/test_init.py imports deploynator/_toml.py.
- [INFERRED] bridges community 0 <-> 1 (strength 0.6): Inferred cross-community bridge: tests/test_models.py reaches tests/test_runner.py in 4 hops.

## Risks

- [taint high] `deploynator/_app.py` -> `deploynator/_toml.py` via `subprocess` (1 hops)
- [taint high] `deploynator/_app.py` -> `deploynator/_runner.py` via `subprocess` (2 hops)
- [taint high] `deploynator/_app.py` -> `deploynator/_docs.py` via `subprocess` (2 hops)
- [taint high] `deploynator/_app.py` -> `deploynator/_pypi.py` via `subprocess` (2 hops)
- [taint high] `deploynator/_app.py` -> `deploynator/_toml.py` via `subprocess` (1 hops)

## Open Questions

- Why do 4 file(s) lack file-level docs (e.g. `deploynator/_docs.py`)? What purpose do they serve?
- What would break if the most connected file in deploynator: _pypi changed?
- Should deploynator: _pypi be split, given cohesion 0.38?

## Sources

- `deploynator/_docs.py`
- `deploynator/_pypi.py`
- `deploynator/_runner.py`
- `deploynator/_toml.py`
- `tests/bdd_test_deploy.py`
- `tests/test_pypi.py`
- `tests/test_runner.py`
- `tests/test_toml.py`
