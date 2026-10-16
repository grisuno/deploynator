# GraphRAG Community Reports

Entities: 554 | Relationships: 1550 | Communities: 5 | Themes: 2 | Text units: 455

Query with `readmenator . ask "<question>"` (local: BM25 + Personalized PageRank; global: map-reduce over these reports) or the MCP tool `readmenator.graphrag`.

## Project overview (`root`, root, rating 7.0)

35 files in 5 communities and 2 themes. Highest-impact communities: deploynator: _changelog (7.0), deploynator: _platforms (6.9), deploynator: _toml (3.8). God nodes: deploynator/_config.py, deploynator/_deploy.py, deploynator/_models.py, deploynator/_toml.py, deploynator/_app.py.

- [deploynator: _changelog] rating 7.0: `deploynator/_config.py` ranks 1 by PageRank, 67 importers, 6 symbols.
- [deploynator: _platforms] rating 6.9: `deploynator/_models.py` ranks 1 by PageRank, 24 importers, 27 symbols.
- [deploynator: _toml] rating 3.8: `deploynator/_toml.py` ranks 1 by PageRank, 35 importers, 10 symbols: list_make_targets: Lee el Makefile y devuelve sus targets sin ejecutar nada.
- [deploynator: _mcp_server] rating 3.0: `deploynator/__init__.py` ranks 1 by PageRank, 16 importers, 0 symbols.
- [unassigned files] rating 0.9: `deploy.sh` ranks 1 by PageRank, 0 importers, 1 symbols: one-liner deploy via deploynator (generic per-repo script).
- Key entities: file:deploynator/_config.py, file:tests/test_config.py, file:tests/test_models.py, file:deploynator/_platforms.py, file:tests/test_pypi.py, file:tests/test_toml.py
- Children: t0, t1
- Root rating = highest community rating.

## deploynator: _changelog + deploynator: _platforms +2 (`t0`, theme, rating 7.0)

Theme of 4 communities and 32 files: deploynator: _changelog (6 files, rating 7.0); deploynator: _platforms (11 files, rating 6.9); deploynator: _toml (8 files, rating 3.8); deploynator: _mcp_server (7 files, rating 3.0).

- [deploynator: _changelog] `deploynator/_config.py` ranks 1 by PageRank, 67 importers, 6 symbols.
- [deploynator: _changelog] `deploynator/_readme.py` ranks 2 by PageRank, 2 importers, 4 symbols: footer_block: Return the anchored deploy footer block.
- [deploynator: _platforms] `deploynator/_models.py` ranks 1 by PageRank, 24 importers, 27 symbols.
- [deploynator: _platforms] `deploynator/_app.py` ranks 2 by PageRank, 1 importers, 32 symbols: install_packages: pip install/upgrade packages (default: deploynator from PyPI).
- [deploynator: _toml] `deploynator/_toml.py` ranks 1 by PageRank, 35 importers, 10 symbols: list_make_targets: Lee el Makefile y devuelve sus targets sin ejecutar nada.
- [deploynator: _toml] `deploynator/_pypi.py` ranks 2 by PageRank, 16 importers, 8 symbols: prompt_for_credentials: Pide el token PyPI por input oculto solo si hay TTY.
- [deploynator: _mcp_server] `deploynator/__init__.py` ranks 1 by PageRank, 16 importers, 0 symbols.
- [deploynator: _mcp_server] `deploynator/_mcp_server.py` ranks 2 by PageRank, 6 importers, 32 symbols: MCP (Model Context Protocol) stdio server for deploynator.
- Key entities: file:deploynator/_config.py, file:tests/test_config.py, file:tests/test_models.py, file:deploynator/_platforms.py, file:tests/test_pypi.py, file:tests/test_toml.py, file:deploynator/_mcp_server.py, file:tests/test_install_example.py
- Children: c3, c0, c1, c2
- Theme rating = highest child community rating.

## unassigned files (`t1`, theme, rating 0.9)

Theme of 1 communities and 3 files: unassigned files (3 files, rating 0.9).

- [unassigned files] `deploy.sh` ranks 1 by PageRank, 0 importers, 1 symbols: one-liner deploy via deploynator (generic per-repo script).
- [unassigned files] `install.sh` ranks 2 by PageRank, 0 importers, 0 symbols.
- Key entities: file:deploy.sh, sym:deploy.sh::ensure_pkg@22
- Children: c4
- Theme rating = highest child community rating.

## deploynator: _changelog (`c3`, community, rating 7.0)

6 files under deploynator (py 6), mostly testing. Core file deploynator/_config.py (PageRank 0.2428, imported by 67 files). Key abstractions: Config, create, resolve_path, gh_authd, glab_authd, bb_authd. Depends on deploynator: _platforms (2). Used by deploynator: _toml (36), deploynator: _platforms (16), deploynator: _mcp_server (12).

- `deploynator/_config.py` ranks 1 by PageRank, 67 importers, 6 symbols.
- `deploynator/_readme.py` ranks 2 by PageRank, 2 importers, 4 symbols: footer_block: Return the anchored deploy footer block.
- `deploynator/_changelog.py` ranks 3 by PageRank, 2 importers, 9 symbols.
- Hotspot `deploynator/_config.py`: 6 symbols, 70 connections (score 0.51).
- Hotspot `deploynator/_changelog.py`: 9 symbols, 12 connections (score 0.16).
- Taint: 4 paths reach this group via subprocess.
- Surprising bridge: test_config.py <-> test_models.py (4 hops across communities).
- Key entities: file:deploynator/_config.py, file:tests/test_config.py, file:deploynator/_changelog.py, file:tests/test_changelog.py, file:deploynator/_readme.py, file:tests/test_readme_footer.py, sym:deploynator/_readme.py::ensure_deployed_footer@49, sym:deploynator/_changelog.py::generate_from_messages@25
- Rating 7.0/10 = 7 x PageRank share 1.00 + 3 x risk 0.00. Internal imports: 7.

## deploynator: _platforms (`c0`, community, rating 6.9)

11 files under deploynator (py 11), mostly testing. Core file deploynator/_models.py (PageRank 0.0900, imported by 24 files). Key abstractions: Platform, CommitType, PlatformConfig, VersionConfig, ProjectConfig, CommitMessage. Depends on deploynator: _changelog (16), deploynator: _toml (6), deploynator: _mcp_server (2). Used by deploynator: _toml (13), deploynator: _mcp_server (2), deploynator: _changelog (2).

- `deploynator/_models.py` ranks 1 by PageRank, 24 importers, 27 symbols.
- `deploynator/_app.py` ranks 2 by PageRank, 1 importers, 32 symbols: install_packages: pip install/upgrade packages (default: deploynator from PyPI).
- `deploynator/_deploy.py` ranks 3 by PageRank, 15 importers, 20 symbols: _gh_release_in_repo: Best-effort `gh release create` inferring repo from origin.
- Hotspot `deploynator/_app.py`: 32 symbols, 41 connections (score 0.56).
- Hotspot `deploynator/_deploy.py`: 20 symbols, 45 connections (score 0.48).
- Taint: 11 paths reach this group via subprocess.
- Surprising bridge: app.py <-> test_models.py (4 hops across communities).
- Key entities: file:tests/test_models.py, file:deploynator/_platforms.py, file:deploynator/_models.py, file:deploynator/_deploy.py, file:deploynator/_app.py, sym:deploynator/_deploy.py::deploy@97, file:deploynator/_git.py, file:tests/test_pipeline.py
- Rating 6.9/10 = 7 x PageRank share 0.99 + 3 x risk 0.00. Internal imports: 39.

## deploynator: _toml (`c1`, community, rating 3.8)

8 files under deploynator (py 8), mostly testing. Core file deploynator/_toml.py (PageRank 0.0624, imported by 35 files): list_make_targets: Lee el Makefile y devuelve sus targets sin ejecutar nada. Key abstractions: TomlConfig, list_make_targets, looks_like_packaging_project, detect_test_commands, load_toml_config, PyPIRunner. Depends on deploynator: _changelog (36), deploynator: _platforms (13). Used by deploynator: _platforms (6), deploynator: _mcp_server (1).

- `deploynator/_toml.py` ranks 1 by PageRank, 35 importers, 10 symbols: list_make_targets: Lee el Makefile y devuelve sus targets sin ejecutar nada.
- `deploynator/_pypi.py` ranks 2 by PageRank, 16 importers, 8 symbols: prompt_for_credentials: Pide el token PyPI por input oculto solo si hay TTY.
- `deploynator/_runner.py` ranks 3 by PageRank, 11 importers, 3 symbols.
- Hotspot `tests/test_pypi.py`: 25 symbols, 92 connections (score 0.83).
- Hotspot `tests/test_runner.py`: 16 symbols, 66 connections (score 0.58).
- Taint: 5 paths reach this group via subprocess.
- Surprising bridge: test_models.py <-> test_runner.py (4 hops across communities).
- Key entities: file:tests/test_pypi.py, file:tests/test_toml.py, file:tests/bdd_test_deploy.py, file:deploynator/_toml.py, file:tests/test_runner.py, sym:deploynator/_toml.py::load_toml_config@211, file:deploynator/_pypi.py, sym:deploynator/_pypi.py::PyPIRunner@12
- Rating 3.8/10 = 7 x PageRank share 0.54 + 3 x risk 0.00. Internal imports: 61.

## deploynator: _mcp_server (`c2`, community, rating 3.0)

7 files under deploynator (py 7), mostly utility. Core file deploynator/__init__.py (PageRank 0.0468, imported by 16 files). Key abstractions: MCPRequest, MCPTool, MCPResource, MCPServer, is_notification, response. Depends on deploynator: _changelog (12), deploynator: _platforms (2), deploynator: _toml (1). Used by deploynator: _platforms (2).

- `deploynator/__init__.py` ranks 1 by PageRank, 16 importers, 0 symbols.
- `deploynator/_mcp_server.py` ranks 2 by PageRank, 6 importers, 32 symbols: MCP (Model Context Protocol) stdio server for deploynator.
- `deploynator/__main__.py` ranks 3 by PageRank, 4 importers, 3 symbols.
- Hotspot `deploynator/_mcp_server.py`: 32 symbols, 15 connections (score 0.39).
- Hotspot `tests/test_init.py`: 6 symbols, 30 connections (score 0.25).
- Dataflow: 2 INFERRED issues (first: UNCHECKED_ALLOC in test_deploy_sh_content_generic).
- Surprising bridge: app.py <-> test_models.py (4 hops across communities).
- Key entities: file:deploynator/_mcp_server.py, file:tests/test_install_example.py, file:tests/test_cli_mcp.py, sym:deploynator/__main__.py::main@171, file:tests/test_init.py, file:deploynator/__main__.py, sym:deploynator/_mcp_server.py::_register_all@180, sym:deploynator/_mcp_server.py::read@82
- Rating 3.0/10 = 7 x PageRank share 0.43 + 3 x risk 0.00. Internal imports: 24.

## unassigned files (`c4`, community, rating 0.9)

3 files under root (sh 2, py 1), mostly utility. Core file deploy.sh (PageRank 0.0133, imported by 0 files): one-liner deploy via deploynator (generic per-repo script). Key abstractions: ensure_pkg.

- `deploy.sh` ranks 1 by PageRank, 0 importers, 1 symbols: one-liner deploy via deploynator (generic per-repo script).
- `install.sh` ranks 2 by PageRank, 0 importers, 0 symbols.
- `tests/__init__.py` ranks 3 by PageRank, 0 importers, 0 symbols.
- Hotspot `deploy.sh`: 1 symbols, 0 connections (score 0.01).
- Hotspot `install.sh`: 0 symbols, 0 connections (score 0.00).
- Key entities: file:deploy.sh, sym:deploy.sh::ensure_pkg@22, file:install.sh, file:tests/__init__.py
- Rating 0.9/10 = 7 x PageRank share 0.12 + 3 x risk 0.00. Internal imports: 0.
