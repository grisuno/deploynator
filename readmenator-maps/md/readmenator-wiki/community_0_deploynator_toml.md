# deploynator: _toml

*Community 0 | 8 files | cohesion 0.35*

## Definition

This community groups 8 file(s) rooted at `deploynator` with dominant language py (cohesion 0.35). Central symbols: `DebRunner`, `DocsRunner`, `TestBDDDeployScenarios`, `TestBDDPipeline`, `TestBuildCommand`, `TestCMakefileDetection`, `TestCleanAndRun`, `TestDetect`. Core file: `tests/test_toml.py` (27 symbols). Documented purpose: BDD-style tests for deploynator using behavior-driven patterns.  Feature: Multi-platform deployment As a developer I want to deploy my project to multiple git p.

## Files

| File | Language | Layer | Symbols | Doc |
|------|----------|-------|---------|-----|
| `deploynator/_deb.py` | py | utility | 9 | no |
| `deploynator/_docs.py` | py | utility | 3 | no |
| `deploynator/_runner.py` | py | utility | 3 | no |
| `deploynator/_toml.py` | py | utility | 10 | no |
| `tests/bdd_test_deploy.py` | py | testing | 10 | yes |
| `tests/test_deb.py` | py | testing | 24 | yes |
| `tests/test_runner.py` | py | testing | 16 | yes |
| `tests/test_toml.py` | py | testing | 27 | yes |

## Key Symbols

- `DebRunner` (class, `deploynator/_deb.py:12`) `class DebRunner` - Construye paquetes .deb desde fuentes C, espejo del flujo PyPI.
- `__init__` (method, `deploynator/_deb.py:35`) `def __init__(self, config)`
- `deb_make_target` (method, `deploynator/_deb.py:38`) `def deb_make_target(self, project_path)`
- `is_deb_project` (method, `deploynator/_deb.py:48`) `def is_deb_project(self, project_path)`
- `_outdir` (method, `deploynator/_deb.py:54`) `def _outdir(self, project_path, toml)`
- `clean` (method, `deploynator/_deb.py:62`) `def clean(self, project_path, toml)`
- `_collect_debs` (method, `deploynator/_deb.py:71`) `def _collect_debs(self, project_path, outdir)` - Busca *.deb en outdir, raíz del proyecto y dir padre.
- `build_command` (method, `deploynator/_deb.py:110`) `def build_command(self, project_path, toml)`
- `run` (method, `deploynator/_deb.py:126`) `def run(self, project_path, toml, version, verbose)`
- `DocsRunner` (class, `deploynator/_docs.py:10`) `class DocsRunner`
- `__init__` (method, `deploynator/_docs.py:11`) `def __init__(self, config)`
- `run` (method, `deploynator/_docs.py:14`) `def run(self, project_path, toml)`
- `TestRunner` (class, `deploynator/_runner.py:11`) `class TestRunner`
- `__init__` (method, `deploynator/_runner.py:12`) `def __init__(self, config)`
- `run` (method, `deploynator/_runner.py:15`) `def run(self, project_path, toml)`
- `_target_regex` (function, `deploynator/_toml.py:23`) `def _target_regex()`
- `list_make_targets` (function, `deploynator/_toml.py:31`) `def list_make_targets(project_path)` - Lee el Makefile y devuelve sus targets sin ejecutar nada.
- `_has_python_tests` (function, `deploynator/_toml.py:63`) `def _has_python_tests(project_path)`
- `looks_like_packaging_project` (function, `deploynator/_toml.py:75`) `def looks_like_packaging_project(project_path)` - Inferencia runtime (multi-proyecto): ¿es un paquete PyPI?
- `detect_test_commands` (function, `deploynator/_toml.py:101`) `def detect_test_commands(project_path)` - Detecta comandos de test para proyectos C/autotools sin toml.
- `_auto_toml_config` (function, `deploynator/_toml.py:150`) `def _auto_toml_config(project_path)` - Config auto para proyectos sin deploynator.toml (C primero).
- `TomlConfig` (class, `deploynator/_toml.py:177`) `class TomlConfig`
- `__post_init__` (method, `deploynator/_toml.py:200`) `def __post_init__(self)`
- `_clamp_timeout` (function, `deploynator/_toml.py:209`) `def _clamp_timeout(value)`
- `load_toml_config` (function, `deploynator/_toml.py:217`) `def load_toml_config(project_path)`
- `TestBDDDeployScenarios` (class, `tests/bdd_test_deploy.py:29`) `class TestBDDDeployScenarios`
- `project` (method, `tests/bdd_test_deploy.py:31`) `def project(self)`
- `test_version_bump_by_commit_type` (method, `tests/bdd_test_deploy.py:47`) `def test_version_bump_by_commit_type(self, project, commit_type, expected_bump,`
- `test_conventional_commit_parsing` (method, `tests/bdd_test_deploy.py:56`) `def test_conventional_commit_parsing(self)`
- `test_commit_message_format_is_consistent` (method, `tests/bdd_test_deploy.py:70`) `def test_commit_message_format_is_consistent(self)`

## Internal vs External Edges

- Internal resolved imports (EXTRACTED): 60
- Cross-boundary resolved imports (EXTRACTED): 56

## Connections

- [EXTRACTED] depends_on community 2 <-> 0 (strength 0.9): Extracted import edge crosses communities: deploynator/_app.py imports deploynator/_toml.py.
- [EXTRACTED] depends_on community 0 <-> 4 (strength 0.9): Extracted import edge crosses communities: deploynator/_deb.py imports deploynator/_config.py.
- [EXTRACTED] depends_on community 0 <-> 3 (strength 0.9): Extracted import edge crosses communities: tests/bdd_test_deploy.py imports deploynator/_models.py.
- [EXTRACTED] depends_on community 1 <-> 0 (strength 0.9): Extracted import edge crosses communities: tests/test_init.py imports deploynator/_toml.py.
- [INFERRED] bridges community 3 <-> 0 (strength 0.6): Inferred cross-community bridge: tests/test_models.py reaches tests/test_runner.py in 4 hops.
- [INFERRED] shares_context community 0 <-> 5 (strength 0.5): Inferred shared context (layer utility) with no import path between community 0 (deploynator: _toml) and community 5 (orphans).

## Risks

- [taint high] `deploynator/_app.py` -> `deploynator/_toml.py` via `subprocess` (1 hops)
- [taint high] `deploynator/_app.py` -> `deploynator/_deb.py` via `subprocess` (2 hops)
- [taint high] `deploynator/_app.py` -> `deploynator/_docs.py` via `subprocess` (2 hops)
- [taint high] `deploynator/_app.py` -> `deploynator/_runner.py` via `subprocess` (2 hops)

## Open Questions

- Why do 4 file(s) lack file-level docs (e.g. `deploynator/_deb.py`)? What purpose do they serve?
- What would break if the most connected file in deploynator: _toml changed?
- Should deploynator: _toml be split, given cohesion 0.35?

## Sources

- `deploynator/_deb.py`
- `deploynator/_docs.py`
- `deploynator/_runner.py`
- `deploynator/_toml.py`
- `tests/bdd_test_deploy.py`
- `tests/test_deb.py`
- `tests/test_runner.py`
- `tests/test_toml.py`
