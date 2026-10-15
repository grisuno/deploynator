# deploynator: _toml

*Community 1 | 6 files | cohesion 0.35*

## Definition

This community groups 6 file(s) rooted at `deploynator` with dominant language py (cohesion 0.35). Central symbols: `DocsRunner`, `TestBDDDeployScenarios`, `TestBDDPipeline`, `TestDocsRunner`, `TestRunner`, `TestTestRunner`, `TestTomlConfig`, `TomlConfig`. Core file: `tests/test_runner.py` (15 symbols). Documented purpose: BDD-style tests for deploynator using behavior-driven patterns.  Feature: Multi-platform deployment As a developer I want to deploy my project to multiple git p.

## Files

| File | Language | Layer | Symbols | Doc |
|------|----------|-------|---------|-----|
| `deploynator/_docs.py` | py | utility | 3 | no |
| `deploynator/_runner.py` | py | utility | 3 | no |
| `deploynator/_toml.py` | py | utility | 4 | no |
| `tests/bdd_test_deploy.py` | py | testing | 10 | yes |
| `tests/test_runner.py` | py | testing | 15 | yes |
| `tests/test_toml.py` | py | testing | 8 | yes |

## Key Symbols

- `DocsRunner` (class, `deploynator/_docs.py:10`) `class DocsRunner`
- `__init__` (method, `deploynator/_docs.py:11`) `def __init__(self, config)`
- `run` (method, `deploynator/_docs.py:14`) `def run(self, project_path, toml)`
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
- `_toml` (function, `tests/test_runner.py:7`) `def _toml(commands, timeout)`
- `TestTestRunner` (class, `tests/test_runner.py:23`) `class TestTestRunner`
- `test_passing_command` (method, `tests/test_runner.py:24`) `def test_passing_command(self)`
- `test_failing_command` (method, `tests/test_runner.py:32`) `def test_failing_command(self)`
- `test_multiple_commands_stop_on_first_failure` (method, `tests/test_runner.py:41`) `def test_multiple_commands_stop_on_first_failure(self)`
- `test_empty_commands_no_tests_dir_fails` (method, `tests/test_runner.py:49`) `def test_empty_commands_no_tests_dir_fails(self)`
- `test_empty_commands_allow_no_tests_passes` (method, `tests/test_runner.py:58`) `def test_empty_commands_allow_no_tests_passes(self)`
- `test_no_shell_injection` (method, `tests/test_runner.py:73`) `def test_no_shell_injection(self)`
- `test_timeout_fails` (method, `tests/test_runner.py:87`) `def test_timeout_fails(self)`
- `test_empty_string_command_rejected` (method, `tests/test_runner.py:96`) `def test_empty_string_command_rejected(self)`

## Internal vs External Edges

- Internal resolved imports (EXTRACTED): 28
- Cross-boundary resolved imports (EXTRACTED): 31

## Connections

- [EXTRACTED] depends_on community 4 <-> 1 (strength 0.9): Extracted import edge crosses communities: deploynator/_app.py imports deploynator/_toml.py.
- [EXTRACTED] depends_on community 1 <-> 0 (strength 0.9): Extracted import edge crosses communities: deploynator/_docs.py imports deploynator/_config.py.
- [EXTRACTED] depends_on community 1 <-> 2 (strength 0.9): Extracted import edge crosses communities: tests/bdd_test_deploy.py imports deploynator/_models.py.
- [EXTRACTED] depends_on community 3 <-> 1 (strength 0.9): Extracted import edge crosses communities: tests/test_init.py imports deploynator/_toml.py.
- [INFERRED] bridges community 2 <-> 1 (strength 0.6): Inferred cross-community bridge: tests/test_models.py reaches tests/test_runner.py in 4 hops.
- [INFERRED] bridges community 2 <-> 1 (strength 0.6): Inferred cross-community bridge: tests/test_models.py reaches tests/test_toml.py in 4 hops.
- [INFERRED] shares_context community 1 <-> 5 (strength 0.5): Inferred shared context (language py and layer utility) with no import path between community 1 (deploynator: _toml) and community 5 (orphans).

## Risks

- [taint high] `deploynator/_app.py` -> `deploynator/_toml.py` via `subprocess` (1 hops)
- [taint high] `deploynator/_app.py` -> `deploynator/_runner.py` via `subprocess` (2 hops)
- [taint high] `deploynator/_app.py` -> `deploynator/_docs.py` via `subprocess` (2 hops)
- [taint high] `deploynator/_app.py` -> `deploynator/_toml.py` via `subprocess` (1 hops)
- [taint high] `deploynator/_app.py` -> `deploynator/_runner.py` via `subprocess` (2 hops)

## Open Questions

- Why do 3 file(s) lack file-level docs (e.g. `deploynator/_docs.py`)? What purpose do they serve?
- What would break if the most connected file in deploynator: _toml changed?
- Should deploynator: _toml be split, given cohesion 0.35?

## Sources

- `deploynator/_docs.py`
- `deploynator/_runner.py`
- `deploynator/_toml.py`
- `tests/bdd_test_deploy.py`
- `tests/test_runner.py`
- `tests/test_toml.py`
