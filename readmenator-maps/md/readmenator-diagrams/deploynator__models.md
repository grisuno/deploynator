# deploynator: _models

deploynator: _models groups 7 files (py) around Platform, from_string, label, cli_name, auth_env_var.

```mermaid
graph LR
    deploynator["deploynator"]
    tests["tests"]
    tests -- "calls into" --> deploynator
```

## deploynator (3.1)

deploynator groups 2 files (py) around Platform, from_string, label, cli_name, auth_env_var.

## tests (3.2)

tests groups 5 files (py) around TestProjectDiscovery, discovery, test_discover_empty_dir, test_discover_single_yaml, test_discover_multiple_yamls. Path-direct deploy + tag prefijos + version_file toml (ReadMenator real).

**Files**:

- deploynator/_models.py
- deploynator/_semver.py
- tests/test_deploy.py
- tests/test_models.py
- tests/test_path_deploy.py
- tests/test_pipeline.py
- tests/test_semver.py
