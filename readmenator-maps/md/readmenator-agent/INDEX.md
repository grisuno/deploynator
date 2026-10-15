# Index

| File | Purpose | Subsystem | Symbols | Used by |
|------|---------|-----------|---------|---------|
| `app.py` | example: use deploynator programmatically as a library. | root | 1 | 0 |
| `deploy.sh` | one-liner deploy via deploynator (generic per-repo script). | root | 1 | 0 |
| `deploynator/__init__.py` | - | deploynator | 0 | 7 |
| `deploynator/__main__.py` | - | deploynator | 3 | 2 |
| `deploynator/_app.py` | install_packages: pip install/upgrade packages (default: deploynator from PyPI). | deploynator | 32 | 1 |
| `deploynator/_changelog.py` | - | deploynator | 9 | 2 |
| `deploynator/_config.py` | - | deploynator | 6 | 25 |
| `deploynator/_deploy.py` | _gh_release_in_repo: Best-effort `gh release create` inferring repo from origin. | deploynator | 19 | 6 |
| `deploynator/_docs.py` | - | deploynator | 3 | 3 |
| `deploynator/_git.py` | - | deploynator | 21 | 2 |
| `deploynator/_mcp_server.py` | MCP (Model Context Protocol) stdio server for deploynator. | deploynator | 32 | 2 |
| `deploynator/_models.py` | - | deploynator | 27 | 14 |
| `deploynator/_platforms.py` | - | deploynator | 34 | 2 |
| `deploynator/_pypi.py` | prompt_for_credentials: Pide el token PyPI por input oculto solo si hay TTY. | deploynator | 8 | 2 |
| `deploynator/_runner.py` | - | deploynator | 3 | 2 |
| `deploynator/_semver.py` | - | deploynator | 9 | 5 |
| `deploynator/_toml.py` | - | deploynator | 4 | 10 |
| `install.sh` | - | root | 0 | 0 |
| `tests/__init__.py` | - | tests | 0 | 0 |
| `tests/bdd_test_deploy.py` | BDD-style tests for deploynator using behavior-driven patterns. | tests | 10 | 0 |
| `tests/test_changelog.py` | - | tests | 8 | 0 |
| `tests/test_cli_mcp.py` | RED: bare = interactive, flags = headless + MCP server. | tests | 11 | 0 |
| `tests/test_config.py` | - | tests | 10 | 0 |
| `tests/test_deploy.py` | - | tests | 11 | 0 |
| `tests/test_init.py` | RED: init deja deploy.sh genérico + deploynator.toml starter. | tests | 6 | 0 |
| `tests/test_install_example.py` | RED: install como pip install + app.py ejemplo de librería. | tests | 12 | 0 |
| `tests/test_models.py` | - | tests | 44 | 0 |
| `tests/test_path_deploy.py` | Path-direct deploy + tag prefijos + version_file toml (ReadMenator real). | tests | 10 | 0 |
| `tests/test_pipeline.py` | RED: pipeline deploy — tests gate + docs non-blocking + bump override + max(file,tag). | tests | 12 | 0 |
| `tests/test_pypi.py` | RED: PyPI runner — detecta packaging, build limpio, upload twine. | tests | 24 | 0 |
| `tests/test_runner.py` | RED: TestRunner + DocsRunner contracts. | tests | 15 | 0 |
| `tests/test_semver.py` | - | tests | 11 | 0 |
| `tests/test_toml.py` | RED: TomlConfig contract — deploynator.toml per-project. | tests | 8 | 0 |
