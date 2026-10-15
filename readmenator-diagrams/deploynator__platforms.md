# deploynator: _platforms

deploynator: _platforms groups 11 files (py) around Platform, from_string, label, cli_name, auth_env_var. install_packages: pip install/upgrade packages (default: deploynator from PyPI).

```mermaid
graph LR
    deploynator["deploynator"]
    tests["tests"]
    tests -- "calls into" --> deploynator
```

## deploynator (1.1)

deploynator groups 6 files (py) around Platform, from_string, label, cli_name, auth_env_var. install_packages: pip install/upgrade packages (default: deploynator from PyPI).

## tests (1.2)

tests groups 5 files (py) around TestProjectDiscovery, discovery, test_discover_empty_dir, test_discover_single_yaml, test_discover_multiple_yamls. Path-direct deploy + tag prefijos + version_file toml (ReadMenator real).

**Files**:

- deploynator/_app.py
- deploynator/_deploy.py
- deploynator/_git.py
- deploynator/_models.py
- deploynator/_platforms.py
- deploynator/_semver.py
- tests/test_deploy.py
- tests/test_models.py
- tests/test_path_deploy.py
- tests/test_pipeline.py
- tests/test_semver.py
