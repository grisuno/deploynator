# GraphRAG Community Reports

Entities: 702 | Relationships: 2069 | Communities: 6 | Themes: 2 | Text units: 597

Query with `readmenator . ask "<question>"` (local: BM25 + Personalized PageRank; global: map-reduce over these reports) or the MCP tool `readmenator.graphrag`.

## Project overview (`root`, root, rating 7.0)

40 files in 6 communities and 2 themes. Highest-impact communities: deploynator: _changelog (7.0), deploynator: _toml (4.1), deploynator: _receipt (3.6). God nodes: deploynator/_config.py, deploynator/_deploy.py, deploynator/_models.py, deploynator/_toml.py, deploynator/_app.py.

- [deploynator: _changelog] rating 7.0: `deploynator/_config.py` ranks 1 by PageRank, 85 importers, 6 symbols.
- [deploynator: _toml] rating 4.1: `deploynator/_toml.py` ranks 1 by PageRank, 42 importers, 10 symbols: list_make_targets: Lee el Makefile y devuelve sus targets sin ejecutar nada.
- [deploynator: _receipt] rating 3.6: `deploynator/_app.py` ranks 1 by PageRank, 1 importers, 33 symbols: install_packages: pip install/upgrade packages (default: deploynator from PyPI).
- [deploynator: _models] rating 3.4: `deploynator/_models.py` ranks 1 by PageRank, 28 importers, 27 symbols.
- [deploynator: _mcp_server] rating 2.6: `deploynator/__init__.py` ranks 1 by PageRank, 16 importers, 0 symbols.
- [unassigned files] rating 0.7: `deploy.sh` ranks 1 by PageRank, 0 importers, 1 symbols: one-liner deploy via deploynator (generic per-repo script).
- Key entities: file:deploynator/_config.py, file:tests/test_config.py, file:tests/test_pypi.py, file:tests/test_deb.py, file:deploynator/_platforms.py, file:tests/test_receipt.py
- Children: t0, t1
- Root rating = highest community rating.

## deploynator: _changelog + deploynator: _toml +3 (`t0`, theme, rating 7.0)

Theme of 5 communities and 37 files: deploynator: _changelog (6 files, rating 7.0); deploynator: _toml (10 files, rating 4.1); deploynator: _receipt (7 files, rating 3.6); deploynator: _models (7 files, rating 3.4); deploynator: _mcp_server (7 files, rating 2.6).

- [deploynator: _changelog] `deploynator/_config.py` ranks 1 by PageRank, 85 importers, 6 symbols.
- [deploynator: _changelog] `deploynator/_changelog.py` ranks 2 by PageRank, 2 importers, 9 symbols.
- [deploynator: _toml] `deploynator/_toml.py` ranks 1 by PageRank, 42 importers, 10 symbols: list_make_targets: Lee el Makefile y devuelve sus targets sin ejecutar nada.
- [deploynator: _toml] `deploynator/_pypi.py` ranks 2 by PageRank, 16 importers, 8 symbols: prompt_for_credentials: Pide el token PyPI por input oculto solo si hay TTY.
- [deploynator: _receipt] `deploynator/_app.py` ranks 1 by PageRank, 1 importers, 33 symbols: install_packages: pip install/upgrade packages (default: deploynator from PyPI).
- [deploynator: _receipt] `deploynator/_deploy.py` ranks 2 by PageRank, 21 importers, 23 symbols: _gh_release_in_repo: Best-effort `gh release create` inferring repo from origin.
- [deploynator: _models] `deploynator/_models.py` ranks 1 by PageRank, 28 importers, 27 symbols.
- [deploynator: _models] `deploynator/_semver.py` ranks 2 by PageRank, 9 importers, 9 symbols.
- Key entities: file:deploynator/_config.py, file:tests/test_config.py, file:tests/test_pypi.py, file:tests/test_deb.py, file:deploynator/_platforms.py, file:tests/test_receipt.py, file:tests/test_models.py, file:deploynator/_models.py
- Children: c4, c0, c2, c3, c1
- Theme rating = highest child community rating.

## unassigned files (`t1`, theme, rating 0.7)

Theme of 1 communities and 3 files: unassigned files (3 files, rating 0.7).

- [unassigned files] `deploy.sh` ranks 1 by PageRank, 0 importers, 1 symbols: one-liner deploy via deploynator (generic per-repo script).
- [unassigned files] `install.sh` ranks 2 by PageRank, 0 importers, 0 symbols.
- Key entities: file:deploy.sh, sym:deploy.sh::ensure_pkg@22
- Children: c5
- Theme rating = highest child community rating.

## deploynator: _changelog (`c4`, community, rating 7.0)

6 files under deploynator (py 6), mostly testing. Core file deploynator/_config.py (PageRank 0.2542, imported by 85 files). Key abstractions: Config, create, resolve_path, gh_authd, glab_authd, bb_authd. Depends on deploynator: _models (1). Used by deploynator: _toml (51), deploynator: _mcp_server (12), deploynator: _models (10).

- `deploynator/_config.py` ranks 1 by PageRank, 85 importers, 6 symbols.
- `deploynator/_changelog.py` ranks 2 by PageRank, 2 importers, 9 symbols.
- `deploynator/_readme.py` ranks 3 by PageRank, 2 importers, 4 symbols: footer_block: Return the anchored deploy footer block.
- Hotspot `deploynator/_config.py`: 6 symbols, 88 connections (score 0.62).
- Hotspot `deploynator/_changelog.py`: 9 symbols, 10 connections (score 0.14).
- Taint: 4 paths reach this group via subprocess.
- Surprising bridge: test_config.py <-> test_models.py (4 hops across communities).
- Key entities: file:deploynator/_config.py, file:tests/test_config.py, file:deploynator/_changelog.py, file:tests/test_changelog.py, file:deploynator/_readme.py, file:tests/test_readme_footer.py, sym:deploynator/_readme.py::ensure_deployed_footer@48, sym:deploynator/_changelog.py::generate_from_messages@24
- Rating 7.0/10 = 7 x PageRank share 1.00 + 3 x risk 0.00. Internal imports: 7.

## deploynator: _toml (`c0`, community, rating 4.1)

10 files under deploynator (py 10), mostly testing. Core file deploynator/_toml.py (PageRank 0.0664, imported by 42 files): list_make_targets: Lee el Makefile y devuelve sus targets sin ejecutar nada. Key abstractions: TomlConfig, list_make_targets, looks_like_packaging_project, detect_test_commands, load_toml_config, PyPIRunner. Depends on deploynator: _changelog (51), deploynator: _models (12), deploynator: _receipt (7). Used by deploynator: _receipt (10), deploynator: _mcp_server (1).

- `deploynator/_toml.py` ranks 1 by PageRank, 42 importers, 10 symbols: list_make_targets: Lee el Makefile y devuelve sus targets sin ejecutar nada.
- `deploynator/_pypi.py` ranks 2 by PageRank, 16 importers, 8 symbols: prompt_for_credentials: Pide el token PyPI por input oculto solo si hay TTY.
- `deploynator/_deb.py` ranks 3 by PageRank, 13 importers, 9 symbols: DebRunner: Construye paquetes .deb desde fuentes C, espejo del flujo PyPI.
- Hotspot `tests/test_pypi.py`: 25 symbols, 92 connections (score 0.81).
- Hotspot `tests/test_deb.py`: 24 symbols, 74 connections (score 0.69).
- Taint: 5 paths reach this group via subprocess.
- Surprising bridge: test_models.py <-> test_runner.py (4 hops across communities).
- Key entities: file:tests/test_pypi.py, file:tests/test_deb.py, file:tests/test_toml.py, file:deploynator/_toml.py, file:tests/bdd_test_deploy.py, file:tests/test_runner.py, sym:deploynator/_toml.py::load_toml_config@217, file:deploynator/_pypi.py
- Rating 4.1/10 = 7 x PageRank share 0.59 + 3 x risk 0.00. Internal imports: 77.

## deploynator: _receipt (`c2`, community, rating 3.6)

7 files under deploynator (py 7), mostly utility. Core file deploynator/_app.py (PageRank 0.0459, imported by 1 files): install_packages: pip install/upgrade packages (default: deploynator from PyPI). Key abstractions: DeploynatorApp, auth_login, auth_status, init_project, start_branch, commit. Depends on deploynator: _toml (10), deploynator: _models (9), deploynator: _changelog (9). Used by deploynator: _models (8), deploynator: _toml (7), deploynator: _mcp_server (1).

- `deploynator/_app.py` ranks 1 by PageRank, 1 importers, 33 symbols: install_packages: pip install/upgrade packages (default: deploynator from PyPI).
- `deploynator/_deploy.py` ranks 2 by PageRank, 21 importers, 23 symbols: _gh_release_in_repo: Best-effort `gh release create` inferring repo from origin.
- `deploynator/_git.py` ranks 3 by PageRank, 6 importers, 25 symbols: is_behind: True si `ahead_branch` tiene commits que `behind_branch` no tiene (es decir, behind_branch esta por debajo de ahead_branch).
- Hotspot `deploynator/_app.py`: 33 symbols, 45 connections (score 0.57).
- Hotspot `deploynator/_deploy.py`: 23 symbols, 54 connections (score 0.55).
- Taint: 9 paths reach this group via subprocess.
- Key entities: file:deploynator/_platforms.py, file:tests/test_receipt.py, file:deploynator/_receipt.py, sym:deploynator/_receipt.py::write@438, file:deploynator/_deploy.py, sym:deploynator/_deploy.py::_deploy_impl@172, file:deploynator/_app.py, file:deploynator/_git.py
- Rating 3.6/10 = 7 x PageRank share 0.51 + 3 x risk 0.00. Internal imports: 17.

## deploynator: _models (`c3`, community, rating 3.4)

7 files under tests (py 7), mostly testing. Core file deploynator/_models.py (PageRank 0.0779, imported by 28 files). Key abstractions: Platform, CommitType, PlatformConfig, VersionConfig, ProjectConfig, CommitMessage. Depends on deploynator: _changelog (10), deploynator: _receipt (8), deploynator: _mcp_server (2). Used by deploynator: _toml (12), deploynator: _receipt (9), deploynator: _mcp_server (1).

- `deploynator/_models.py` ranks 1 by PageRank, 28 importers, 27 symbols.
- `deploynator/_semver.py` ranks 2 by PageRank, 9 importers, 9 symbols.
- `tests/test_deploy.py` ranks 3 by PageRank, 0 importers, 11 symbols.
- Hotspot `deploynator/_models.py`: 27 symbols, 33 connections (score 0.45).
- Hotspot `tests/test_models.py`: 44 symbols, 3 connections (score 0.39).
- Taint: 2 paths reach this group via subprocess.
- Surprising bridge: app.py <-> test_models.py (4 hops across communities).
- Key entities: file:tests/test_models.py, file:deploynator/_models.py, file:tests/test_pipeline.py, file:deploynator/_semver.py, file:tests/test_path_deploy.py, file:tests/test_semver.py, file:tests/test_deploy.py, sym:deploynator/_models.py::VersionInfo@207
- Rating 3.4/10 = 7 x PageRank share 0.49 + 3 x risk 0.00. Internal imports: 14.

## deploynator: _mcp_server (`c1`, community, rating 2.6)

7 files under deploynator (py 7), mostly utility. Core file deploynator/__init__.py (PageRank 0.0405, imported by 16 files). Key abstractions: MCPRequest, MCPTool, MCPResource, MCPServer, is_notification, response. Depends on deploynator: _changelog (12), deploynator: _toml (1), deploynator: _receipt (1). Used by deploynator: _models (2).

- `deploynator/__init__.py` ranks 1 by PageRank, 16 importers, 0 symbols.
- `deploynator/_mcp_server.py` ranks 2 by PageRank, 6 importers, 32 symbols: MCP (Model Context Protocol) stdio server for deploynator.
- `deploynator/__main__.py` ranks 3 by PageRank, 4 importers, 3 symbols.
- Hotspot `deploynator/_mcp_server.py`: 32 symbols, 16 connections (score 0.38).
- Hotspot `tests/test_init.py`: 6 symbols, 30 connections (score 0.25).
- Surprising bridge: app.py <-> test_models.py (4 hops across communities).
- Key entities: file:deploynator/_mcp_server.py, file:tests/test_install_example.py, file:tests/test_cli_mcp.py, sym:deploynator/__main__.py::main@185, file:tests/test_init.py, file:deploynator/__main__.py, sym:deploynator/_mcp_server.py::_register_all@181, sym:deploynator/__main__.py::build_parser@16
- Rating 2.6/10 = 7 x PageRank share 0.37 + 3 x risk 0.00. Internal imports: 24.

## unassigned files (`c5`, community, rating 0.7)

3 files under root (sh 2, py 1), mostly utility. Core file deploy.sh (PageRank 0.0115, imported by 0 files): one-liner deploy via deploynator (generic per-repo script). Key abstractions: ensure_pkg.

- `deploy.sh` ranks 1 by PageRank, 0 importers, 1 symbols: one-liner deploy via deploynator (generic per-repo script).
- `install.sh` ranks 2 by PageRank, 0 importers, 0 symbols.
- `tests/__init__.py` ranks 3 by PageRank, 0 importers, 0 symbols.
- Hotspot `deploy.sh`: 1 symbols, 0 connections (score 0.01).
- Hotspot `install.sh`: 0 symbols, 0 connections (score 0.00).
- Key entities: file:deploy.sh, sym:deploy.sh::ensure_pkg@22, file:install.sh, file:tests/__init__.py
- Rating 0.7/10 = 7 x PageRank share 0.11 + 3 x risk 0.00. Internal imports: 0.
