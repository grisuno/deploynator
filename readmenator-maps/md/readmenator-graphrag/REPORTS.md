# GraphRAG Community Reports

Entities: 514 | Relationships: 1434 | Communities: 4 | Themes: 2 | Text units: 417

Query with `readmenator . ask "<question>"` (local: BM25 + Personalized PageRank; global: map-reduce over these reports) or the MCP tool `readmenator.graphrag`.

## Project overview (`root`, root, rating 7.0)

33 files in 4 communities and 2 themes. Highest-impact communities: deploynator: _mcp_server (7.0), deploynator: _platforms (5.6), deploynator: _pypi (3.0). God nodes: deploynator/_config.py, deploynator/_deploy.py, deploynator/_models.py, deploynator/_toml.py, deploynator/_app.py.

- [deploynator: _mcp_server] rating 7.0: `deploynator/_config.py` ranks 1 by PageRank, 64 importers, 6 symbols.
- [deploynator: _platforms] rating 5.6: `deploynator/_models.py` ranks 1 by PageRank, 24 importers, 27 symbols.
- [deploynator: _pypi] rating 3.0: `deploynator/_toml.py` ranks 1 by PageRank, 19 importers, 4 symbols.
- [unassigned files] rating 0.7: `deploy.sh` ranks 1 by PageRank, 0 importers, 1 symbols: one-liner deploy via deploynator (generic per-repo script).
- Key entities: file:deploynator/_mcp_server.py, file:deploynator/_config.py, file:tests/test_models.py, file:deploynator/_platforms.py, file:tests/test_pypi.py, file:tests/bdd_test_deploy.py
- Children: t0, t1
- Root rating = highest community rating.

## deploynator: _mcp_server + deploynator: _platforms +1 (`t0`, theme, rating 7.0)

Theme of 3 communities and 30 files: deploynator: _mcp_server (11 files, rating 7.0); deploynator: _platforms (11 files, rating 5.6); deploynator: _pypi (8 files, rating 3.0).

- [deploynator: _mcp_server] `deploynator/_config.py` ranks 1 by PageRank, 64 importers, 6 symbols.
- [deploynator: _mcp_server] `deploynator/__init__.py` ranks 2 by PageRank, 16 importers, 0 symbols.
- [deploynator: _platforms] `deploynator/_models.py` ranks 1 by PageRank, 24 importers, 27 symbols.
- [deploynator: _platforms] `deploynator/_app.py` ranks 2 by PageRank, 1 importers, 32 symbols: install_packages: pip install/upgrade packages (default: deploynator from PyPI).
- [deploynator: _pypi] `deploynator/_toml.py` ranks 1 by PageRank, 19 importers, 4 symbols.
- [deploynator: _pypi] `deploynator/_pypi.py` ranks 2 by PageRank, 16 importers, 8 symbols: prompt_for_credentials: Pide el token PyPI por input oculto solo si hay TTY.
- Key entities: file:deploynator/_mcp_server.py, file:deploynator/_config.py, file:tests/test_models.py, file:deploynator/_platforms.py, file:tests/test_pypi.py, file:tests/bdd_test_deploy.py
- Children: c0, c1, c2
- Theme rating = highest child community rating.

## unassigned files (`t1`, theme, rating 0.7)

Theme of 1 communities and 3 files: unassigned files (3 files, rating 0.7).

- [unassigned files] `deploy.sh` ranks 1 by PageRank, 0 importers, 1 symbols: one-liner deploy via deploynator (generic per-repo script).
- [unassigned files] `install.sh` ranks 2 by PageRank, 0 importers, 0 symbols.
- Key entities: file:deploy.sh, sym:deploy.sh::ensure_pkg@22
- Children: c3
- Theme rating = highest child community rating.

## deploynator: _mcp_server (`c0`, community, rating 7.0)

11 files under deploynator (py 11), mostly testing. Core file deploynator/_config.py (PageRank 0.2321, imported by 64 files). Key abstractions: Config, create, resolve_path, gh_authd, glab_authd, bb_authd. Depends on deploynator: _platforms (4), deploynator: _pypi (1). Used by deploynator: _pypi (35), deploynator: _platforms (17).

- `deploynator/_config.py` ranks 1 by PageRank, 64 importers, 6 symbols.
- `deploynator/__init__.py` ranks 2 by PageRank, 16 importers, 0 symbols.
- `deploynator/_mcp_server.py` ranks 3 by PageRank, 6 importers, 32 symbols: MCP (Model Context Protocol) stdio server for deploynator.
- Hotspot `deploynator/_config.py`: 6 symbols, 67 connections (score 0.49).
- Hotspot `deploynator/_mcp_server.py`: 32 symbols, 15 connections (score 0.39).
- Taint: 3 paths reach this group via subprocess.
- Dataflow: 2 INFERRED issues (first: UNCHECKED_ALLOC in test_deploy_sh_content_generic).
- Surprising bridge: app.py <-> test_models.py (4 hops across communities).
- Key entities: file:deploynator/_mcp_server.py, file:deploynator/_config.py, file:tests/test_install_example.py, file:tests/test_config.py, file:deploynator/_changelog.py, file:tests/test_cli_mcp.py, sym:deploynator/__main__.py::main@167, file:tests/test_changelog.py
- Rating 7.0/10 = 7 x PageRank share 1.00 + 3 x risk 0.00. Internal imports: 40.

## deploynator: _platforms (`c1`, community, rating 5.6)

11 files under deploynator (py 11), mostly testing. Core file deploynator/_models.py (PageRank 0.0971, imported by 24 files). Key abstractions: Platform, CommitType, PlatformConfig, VersionConfig, ProjectConfig, CommitMessage. Depends on deploynator: _mcp_server (17), deploynator: _pypi (5). Used by deploynator: _pypi (13), deploynator: _mcp_server (4).

- `deploynator/_models.py` ranks 1 by PageRank, 24 importers, 27 symbols.
- `deploynator/_app.py` ranks 2 by PageRank, 1 importers, 32 symbols: install_packages: pip install/upgrade packages (default: deploynator from PyPI).
- `deploynator/_deploy.py` ranks 3 by PageRank, 15 importers, 19 symbols: _gh_release_in_repo: Best-effort `gh release create` inferring repo from origin.
- Hotspot `deploynator/_app.py`: 32 symbols, 39 connections (score 0.55).
- Hotspot `deploynator/_deploy.py`: 19 symbols, 43 connections (score 0.45).
- Taint: 12 paths reach this group via subprocess.
- Surprising bridge: app.py <-> test_models.py (4 hops across communities).
- Key entities: file:tests/test_models.py, file:deploynator/_platforms.py, file:deploynator/_models.py, file:deploynator/_app.py, file:deploynator/_deploy.py, sym:deploynator/_deploy.py::deploy@97, file:deploynator/_git.py, file:deploynator/_semver.py
- Rating 5.6/10 = 7 x PageRank share 0.80 + 3 x risk 0.00. Internal imports: 39.

## deploynator: _pypi (`c2`, community, rating 3.0)

8 files under deploynator (py 8), mostly testing. Core file deploynator/_toml.py (PageRank 0.0640, imported by 19 files). Key abstractions: TomlConfig, load_toml_config, PyPIRunner, is_packaging_project, has_credentials, prompt_for_credentials. Depends on deploynator: _mcp_server (35), deploynator: _platforms (13). Used by deploynator: _platforms (5), deploynator: _mcp_server (1).

- `deploynator/_toml.py` ranks 1 by PageRank, 19 importers, 4 symbols.
- `deploynator/_pypi.py` ranks 2 by PageRank, 16 importers, 8 symbols: prompt_for_credentials: Pide el token PyPI por input oculto solo si hay TTY.
- `deploynator/_runner.py` ranks 3 by PageRank, 10 importers, 3 symbols.
- Hotspot `tests/test_pypi.py`: 25 symbols, 92 connections (score 0.83).
- Hotspot `tests/test_runner.py`: 15 symbols, 61 connections (score 0.53).
- Taint: 5 paths reach this group via subprocess.
- Surprising bridge: test_models.py <-> test_runner.py (4 hops across communities).
- Key entities: file:tests/test_pypi.py, file:tests/bdd_test_deploy.py, file:tests/test_runner.py, file:deploynator/_pypi.py, file:deploynator/_toml.py, sym:deploynator/_pypi.py::PyPIRunner@12, file:tests/test_toml.py, sym:deploynator/_toml.py::load_toml_config@46
- Rating 3.0/10 = 7 x PageRank share 0.43 + 3 x risk 0.00. Internal imports: 45.

## unassigned files (`c3`, community, rating 0.7)

3 files under root (sh 2, py 1), mostly utility. Core file deploy.sh (PageRank 0.0141, imported by 0 files): one-liner deploy via deploynator (generic per-repo script). Key abstractions: ensure_pkg.

- `deploy.sh` ranks 1 by PageRank, 0 importers, 1 symbols: one-liner deploy via deploynator (generic per-repo script).
- `install.sh` ranks 2 by PageRank, 0 importers, 0 symbols.
- `tests/__init__.py` ranks 3 by PageRank, 0 importers, 0 symbols.
- Hotspot `deploy.sh`: 1 symbols, 0 connections (score 0.01).
- Hotspot `install.sh`: 0 symbols, 0 connections (score 0.00).
- Key entities: file:deploy.sh, sym:deploy.sh::ensure_pkg@22, file:install.sh, file:tests/__init__.py
- Rating 0.7/10 = 7 x PageRank share 0.10 + 3 x risk 0.00. Internal imports: 0.
