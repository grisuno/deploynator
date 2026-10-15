# deploynator: _models

*Community 2 | 6 files | cohesion 0.31*

## Definition

This community groups 6 file(s) rooted at `tests` with dominant language py (cohesion 0.31). Central symbols: `ChangelogEntry`, `CommitMessage`, `CommitType`, `DeployResult`, `Platform`, `PlatformConfig`, `ProjectConfig`, `ReleaseInfo`. Core file: `tests/test_models.py` (44 symbols). Documented purpose: Path-direct deploy + tag prefijos + version_file toml (ReadMenator real)..

## Files

| File | Language | Layer | Symbols | Doc |
|------|----------|-------|---------|-----|
| `deploynator/_models.py` | py | business_logic | 27 | no |
| `deploynator/_semver.py` | py | utility | 9 | no |
| `tests/test_models.py` | py | testing | 44 | no |
| `tests/test_path_deploy.py` | py | testing | 10 | yes |
| `tests/test_pipeline.py` | py | testing | 12 | yes |
| `tests/test_semver.py` | py | testing | 11 | no |

## Key Symbols

- `Platform` (class, `deploynator/_models.py:10`) `class Platform(Enum)`
- `from_string` (method, `deploynator/_models.py:16`) `def from_string(cls, name)`
- `label` (method, `deploynator/_models.py:27`) `def label(self)`
- `cli_name` (method, `deploynator/_models.py:30`) `def cli_name(self)`
- `auth_env_var` (method, `deploynator/_models.py:37`) `def auth_env_var(self)`
- `CommitType` (class, `deploynator/_models.py:45`) `class CommitType(Enum)`
- `from_string` (method, `deploynator/_models.py:58`) `def from_string(cls, value)`
- `valid_types` (method, `deploynator/_models.py:65`) `def valid_types(cls)`
- `bump_strategy` (method, `deploynator/_models.py:68`) `def bump_strategy(self)`
- `section_header` (method, `deploynator/_models.py:82`) `def section_header(self)`
- `PlatformConfig` (class, `deploynator/_models.py:98`) `class PlatformConfig`
- `from_dict` (method, `deploynator/_models.py:105`) `def from_dict(cls, data)`
- `VersionConfig` (class, `deploynator/_models.py:115`) `class VersionConfig`
- `from_dict` (method, `deploynator/_models.py:121`) `def from_dict(cls, data)`
- `ProjectConfig` (class, `deploynator/_models.py:130`) `class ProjectConfig`
- `from_dict` (method, `deploynator/_models.py:139`) `def from_dict(cls, data)`
- `CommitMessage` (class, `deploynator/_models.py:175`) `class CommitMessage`
- `format` (method, `deploynator/_models.py:183`) `def format(self)`
- `parse` (method, `deploynator/_models.py:195`) `def parse(cls, raw)`
- `VersionInfo` (class, `deploynator/_models.py:208`) `class VersionInfo`
- `__str__` (method, `deploynator/_models.py:213`) `def __str__(self)`
- `parse` (method, `deploynator/_models.py:217`) `def parse(cls, version_str)`
- `bump` (method, `deploynator/_models.py:228`) `def bump(self, strategy)`
- `ChangelogEntry` (class, `deploynator/_models.py:239`) `class ChangelogEntry`
- `from_git_log_line` (method, `deploynator/_models.py:247`) `def from_git_log_line(cls, line, author, sha)`
- `ReleaseInfo` (class, `deploynator/_models.py:266`) `class ReleaseInfo`
- `DeployResult` (class, `deploynator/_models.py:276`) `class DeployResult`
- `SemverManager` (class, `deploynator/_semver.py:12`) `class SemverManager`
- `__init__` (method, `deploynator/_semver.py:13`) `def __init__(self, config)`
- `max_version` (method, `deploynator/_semver.py:16`) `def max_version(self, a, b)`

## Internal vs External Edges

- Internal resolved imports (EXTRACTED): 13
- Cross-boundary resolved imports (EXTRACTED): 37

## Connections

- [EXTRACTED] depends_on community 3 <-> 2 (strength 0.9): Extracted import edge crosses communities: deploynator/__main__.py imports deploynator/_models.py.
- [EXTRACTED] depends_on community 4 <-> 2 (strength 0.9): Extracted import edge crosses communities: deploynator/_app.py imports deploynator/_models.py.
- [EXTRACTED] depends_on community 0 <-> 2 (strength 0.9): Extracted import edge crosses communities: deploynator/_changelog.py imports deploynator/_models.py.
- [EXTRACTED] depends_on community 1 <-> 2 (strength 0.9): Extracted import edge crosses communities: tests/bdd_test_deploy.py imports deploynator/_models.py.
- [INFERRED] bridges community 0 <-> 2 (strength 0.6): Inferred cross-community bridge: tests/test_config.py reaches tests/test_models.py in 4 hops.
- [INFERRED] bridges community 3 <-> 2 (strength 0.6): Inferred cross-community bridge: tests/test_init.py reaches tests/test_models.py in 4 hops.
- [INFERRED] bridges community 2 <-> 1 (strength 0.6): Inferred cross-community bridge: tests/test_models.py reaches tests/test_runner.py in 4 hops.
- [INFERRED] bridges community 2 <-> 1 (strength 0.6): Inferred cross-community bridge: tests/test_models.py reaches tests/test_toml.py in 4 hops.
- [INFERRED] shares_context community 2 <-> 5 (strength 0.5): Inferred shared context (language py) with no import path between community 2 (deploynator: _models) and community 5 (orphans).

## Risks

- [taint high] `deploynator/_app.py` -> `deploynator/_models.py` via `subprocess` (1 hops)
- [taint high] `deploynator/_app.py` -> `deploynator/_semver.py` via `subprocess` (2 hops)
- [taint high] `deploynator/_app.py` -> `deploynator/_models.py` via `subprocess` (1 hops)

## Open Questions

- Why do 4 file(s) lack file-level docs (e.g. `deploynator/_models.py`)? What purpose do they serve?
- What would break if the most connected file in deploynator: _models changed?
- Should deploynator: _models be split, given cohesion 0.31?

## Sources

- `deploynator/_models.py`
- `deploynator/_semver.py`
- `tests/test_models.py`
- `tests/test_path_deploy.py`
- `tests/test_pipeline.py`
- `tests/test_semver.py`
