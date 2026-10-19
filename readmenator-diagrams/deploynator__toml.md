# deploynator: _toml

deploynator: _toml groups 8 files (py) around _target_regex, list_make_targets, _has_python_tests, looks_like_packaging_project, detect_test_commands. DebRunner: Construye paquetes .deb desde fuentes C, espejo del flujo PyPI.

```mermaid
graph LR
    deploynator["deploynator"]
    tests["tests"]
    tests -- "calls into" --> deploynator
```

## deploynator (1.1)

deploynator groups 4 files (py) around _target_regex, list_make_targets, _has_python_tests, looks_like_packaging_project, detect_test_commands. DebRunner: Construye paquetes .deb desde fuentes C, espejo del flujo PyPI.

## tests (1.2)

tests groups 4 files (py) around TestBDDDeployScenarios, project, test_version_bump_by_commit_type, test_conventional_commit_parsing, test_commit_message_format_is_consistent. BDD-style tests for deploynator using behavior-driven patterns.

**Files**:

- deploynator/_deb.py
- deploynator/_docs.py
- deploynator/_runner.py
- deploynator/_toml.py
- tests/bdd_test_deploy.py
- tests/test_deb.py
- tests/test_runner.py
- tests/test_toml.py
