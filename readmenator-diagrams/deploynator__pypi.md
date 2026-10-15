# deploynator: _pypi

deploynator: _pypi groups 8 files (py) around TomlConfig, __post_init__, _clamp_timeout, load_toml_config, PyPIRunner. prompt_for_credentials: Pide el token PyPI por input oculto solo si hay TTY.

```mermaid
graph LR
    deploynator["deploynator"]
    tests["tests"]
    tests -- "calls into" --> deploynator
```

## deploynator (3.1)

deploynator groups 4 files (py) around TomlConfig, __post_init__, _clamp_timeout, load_toml_config, PyPIRunner. prompt_for_credentials: Pide el token PyPI por input oculto solo si hay TTY.

## tests (3.2)

tests groups 4 files (py) around TestBDDDeployScenarios, project, test_version_bump_by_commit_type, test_conventional_commit_parsing, test_commit_message_format_is_consistent. BDD-style tests for deploynator using behavior-driven patterns.

**Files**:

- deploynator/_docs.py
- deploynator/_pypi.py
- deploynator/_runner.py
- deploynator/_toml.py
- tests/bdd_test_deploy.py
- tests/test_pypi.py
- tests/test_runner.py
- tests/test_toml.py
