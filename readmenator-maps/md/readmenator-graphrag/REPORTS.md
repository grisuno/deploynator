# GraphRAG Community Reports

Entities: 485 | Relationships: 1333 | Communities: 6 | Themes: 2 | Text units: 390

Query with `readmenator . ask "<question>"` (local: BM25 + Personalized PageRank; global: map-reduce over these reports) or the MCP tool `readmenator.graphrag`.

## Project overview (`root`, root, rating 7.0)

30 files in 6 communities and 2 themes. Highest-impact communities: deploynator: _changelog (7.0), deploynator: _models (4.2), deploynator: _toml (3.5). God nodes: deploynator/_config.py, deploynator/_deploy.py, deploynator/_models.py, deploynator/_toml.py, deploynator/_app.py.

- [deploynator: _changelog] rating 7.0: `deploynator/_config.py` ranks 1 by PageRank, 53 importers, 6 symbols.
- [deploynator: _models] rating 4.2: `deploynator/_models.py` ranks 1 by PageRank, 24 importers, 27 symbols.
- [deploynator: _toml] rating 3.5: `deploynator/_toml.py` ranks 1 by PageRank, 18 importers, 4 symbols.
- [deploynator: _platforms] rating 3.3: `deploynator/_app.py` ranks 1 by PageRank, 1 importers, 31 symbols.
- [deploynator: _mcp_server] rating 2.1: `deploynator/__init__.py` ranks 1 by PageRank, 6 importers, 0 symbols.
- [unassigned files] rating 1.0: `app.py` ranks 1 by PageRank, 0 importers, 0 symbols: Autor: Gris Iscomeback Correo electrónico: grisiscomeback[at]gmail[dot]com Fecha de creación: xx/xx/xxxx Licencia: GPL v3  Descripción:
- Key entities: file:tests/test_pypi.py, file:deploynator/_config.py, file:tests/test_models.py, file:deploynator/_models.py, file:tests/bdd_test_deploy.py, file:tests/test_runner.py
- Children: t0, t1
- Root rating = highest community rating.

## deploynator: _changelog + deploynator: _models +3 (`t0`, theme, rating 7.0)

Theme of 5 communities and 27 files: deploynator: _changelog (6 files, rating 7.0); deploynator: _models (6 files, rating 4.2); deploynator: _toml (6 files, rating 3.5); deploynator: _platforms (5 files, rating 3.3); deploynator: _mcp_server (4 files, rating 2.1).

- [deploynator: _changelog] `deploynator/_config.py` ranks 1 by PageRank, 53 importers, 6 symbols.
- [deploynator: _changelog] `deploynator/_pypi.py` ranks 2 by PageRank, 14 importers, 8 symbols: prompt_for_credentials: Pide el token PyPI por input oculto solo si hay TTY.
- [deploynator: _models] `deploynator/_models.py` ranks 1 by PageRank, 24 importers, 27 symbols.
- [deploynator: _models] `deploynator/_semver.py` ranks 2 by PageRank, 9 importers, 9 symbols.
- [deploynator: _toml] `deploynator/_toml.py` ranks 1 by PageRank, 18 importers, 4 symbols.
- [deploynator: _toml] `deploynator/_runner.py` ranks 2 by PageRank, 10 importers, 3 symbols.
- [deploynator: _platforms] `deploynator/_app.py` ranks 1 by PageRank, 1 importers, 31 symbols.
- [deploynator: _platforms] `deploynator/_deploy.py` ranks 2 by PageRank, 15 importers, 19 symbols: _gh_release_in_repo: Best-effort `gh release create` inferring repo from origin.
- Key entities: file:tests/test_pypi.py, file:deploynator/_config.py, file:tests/test_models.py, file:deploynator/_models.py, file:tests/bdd_test_deploy.py, file:tests/test_runner.py, file:deploynator/_platforms.py, file:deploynator/_app.py
- Children: c0, c2, c1, c3, c4
- Theme rating = highest child community rating.

## unassigned files (`t1`, theme, rating 1.0)

Theme of 1 communities and 3 files: unassigned files (3 files, rating 1.0).

- [unassigned files] `app.py` ranks 1 by PageRank, 0 importers, 0 symbols: Autor: Gris Iscomeback Correo electrónico: grisiscomeback[at]gmail[dot]com Fecha de creación: xx/xx/xxxx Licencia: GPL v3  Descripción:
- [unassigned files] `install.sh` ranks 2 by PageRank, 0 importers, 0 symbols.
- Key entities: file:install.sh, file:app.py
- Children: c5
- Theme rating = highest child community rating.

## deploynator: _changelog (`c0`, community, rating 7.0)

6 files under deploynator (py 6), mostly testing. Core file deploynator/_config.py (PageRank 0.2357, imported by 53 files). Key abstractions: Config, create, resolve_path, gh_authd, glab_authd, bb_authd. Depends on deploynator: _models (5), deploynator: _platforms (3), deploynator: _toml (2). Used by deploynator: _toml (17), deploynator: _models (9), deploynator: _platforms (7).

- `deploynator/_config.py` ranks 1 by PageRank, 53 importers, 6 symbols.
- `deploynator/_pypi.py` ranks 2 by PageRank, 14 importers, 8 symbols: prompt_for_credentials: Pide el token PyPI por input oculto solo si hay TTY.
- `deploynator/_changelog.py` ranks 3 by PageRank, 2 importers, 9 symbols.
- Hotspot `tests/test_pypi.py`: 22 symbols, 81 connections (score 0.80).
- Hotspot `deploynator/_config.py`: 6 symbols, 56 connections (score 0.47).
- Taint: 4 paths reach this group via subprocess.
- Surprising bridge: test_config.py <-> test_models.py (4 hops across communities).
- Key entities: file:tests/test_pypi.py, file:deploynator/_config.py, file:tests/test_config.py, file:deploynator/_pypi.py, file:deploynator/_changelog.py, file:tests/test_changelog.py, sym:deploynator/_pypi.py::PyPIRunner@12, sym:deploynator/_changelog.py::generate_from_messages@25
- Rating 7.0/10 = 7 x PageRank share 1.00 + 3 x risk 0.00. Internal imports: 33.

## deploynator: _models (`c2`, community, rating 4.2)

6 files under tests (py 6), mostly testing. Core file deploynator/_models.py (PageRank 0.1046, imported by 24 files). Key abstractions: Platform, CommitType, PlatformConfig, VersionConfig, ProjectConfig, CommitMessage. Depends on deploynator: _changelog (9), deploynator: _platforms (6), deploynator: _mcp_server (2). Used by deploynator: _platforms (8), deploynator: _toml (6), deploynator: _changelog (5).

- `deploynator/_models.py` ranks 1 by PageRank, 24 importers, 27 symbols.
- `deploynator/_semver.py` ranks 2 by PageRank, 9 importers, 9 symbols.
- `tests/test_models.py` ranks 3 by PageRank, 0 importers, 44 symbols.
- Hotspot `deploynator/_models.py`: 27 symbols, 30 connections (score 0.47).
- Hotspot `tests/test_models.py`: 44 symbols, 4 connections (score 0.43).
- Taint: 3 paths reach this group via subprocess.
- Surprising bridge: test_config.py <-> test_models.py (4 hops across communities).
- Key entities: file:tests/test_models.py, file:deploynator/_models.py, file:deploynator/_semver.py, file:tests/test_pipeline.py, file:tests/test_path_deploy.py, file:tests/test_semver.py, sym:deploynator/_models.py::VersionInfo@208, sym:deploynator/_semver.py::get_current_version@21
- Rating 4.2/10 = 7 x PageRank share 0.60 + 3 x risk 0.00. Internal imports: 13.

## deploynator: _toml (`c1`, community, rating 3.5)

6 files under deploynator (py 6), mostly testing. Core file deploynator/_toml.py (PageRank 0.0696, imported by 18 files). Key abstractions: TomlConfig, load_toml_config, TestRunner, run, DocsRunner, run. Depends on deploynator: _changelog (17), deploynator: _models (6), deploynator: _platforms (1). Used by deploynator: _platforms (4), deploynator: _changelog (2).

- `deploynator/_toml.py` ranks 1 by PageRank, 18 importers, 4 symbols.
- `deploynator/_runner.py` ranks 2 by PageRank, 10 importers, 3 symbols.
- `deploynator/_docs.py` ranks 3 by PageRank, 6 importers, 3 symbols.
- Hotspot `tests/test_runner.py`: 15 symbols, 61 connections (score 0.59).
- Hotspot `tests/bdd_test_deploy.py`: 10 symbols, 34 connections (score 0.34).
- Taint: 5 paths reach this group via subprocess.
- Surprising bridge: test_models.py <-> test_runner.py (4 hops across communities).
- Key entities: file:tests/bdd_test_deploy.py, file:tests/test_runner.py, file:deploynator/_toml.py, file:tests/test_toml.py, sym:deploynator/_toml.py::load_toml_config@46, file:deploynator/_docs.py, file:deploynator/_runner.py, sym:tests/test_runner.py::_toml@7
- Rating 3.5/10 = 7 x PageRank share 0.49 + 3 x risk 0.00. Internal imports: 28.

## deploynator: _platforms (`c3`, community, rating 3.3)

5 files under deploynator (py 5), mostly utility. Core file deploynator/_app.py (PageRank 0.0464, imported by 1 files). Key abstractions: DeploynatorApp, auth_login, auth_status, init_project, start_branch, commit. Depends on deploynator: _models (8), deploynator: _changelog (7), deploynator: _toml (4). Used by deploynator: _models (6), deploynator: _changelog (3), deploynator: _toml (1).

- `deploynator/_app.py` ranks 1 by PageRank, 1 importers, 31 symbols.
- `deploynator/_deploy.py` ranks 2 by PageRank, 15 importers, 19 symbols: _gh_release_in_repo: Best-effort `gh release create` inferring repo from origin.
- `deploynator/_git.py` ranks 3 by PageRank, 5 importers, 21 symbols.
- Hotspot `deploynator/_app.py`: 31 symbols, 37 connections (score 0.56).
- Hotspot `deploynator/_deploy.py`: 19 symbols, 43 connections (score 0.49).
- Taint: 8 paths reach this group via subprocess.
- Key entities: file:deploynator/_platforms.py, file:deploynator/_app.py, file:deploynator/_deploy.py, sym:deploynator/_deploy.py::deploy@97, file:deploynator/_git.py, file:tests/test_deploy.py, sym:deploynator/_app.py::release@229, sym:deploynator/_deploy.py::discover@35
- Rating 3.3/10 = 7 x PageRank share 0.47 + 3 x risk 0.00. Internal imports: 12.

## deploynator: _mcp_server (`c4`, community, rating 2.1)

4 files under deploynator (py 4), mostly utility. Core file deploynator/__init__.py (PageRank 0.0358, imported by 6 files). Key abstractions: MCPRequest, MCPTool, MCPResource, MCPServer, is_notification, response. Depends on deploynator: _changelog (3), deploynator: _models (1), deploynator: _platforms (1). Used by deploynator: _models (2).

- `deploynator/__init__.py` ranks 1 by PageRank, 6 importers, 0 symbols.
- `deploynator/_mcp_server.py` ranks 2 by PageRank, 6 importers, 32 symbols: MCP (Model Context Protocol) stdio server for deploynator.
- `deploynator/__main__.py` ranks 3 by PageRank, 3 importers, 3 symbols.
- Hotspot `deploynator/_mcp_server.py`: 32 symbols, 15 connections (score 0.40).
- Hotspot `tests/test_cli_mcp.py`: 11 symbols, 23 connections (score 0.27).
- Surprising bridge: __init__.py <-> _changelog.py (3 hops across communities).
- Key entities: file:deploynator/_mcp_server.py, file:tests/test_cli_mcp.py, sym:deploynator/__main__.py::main@164, file:deploynator/__main__.py, sym:deploynator/_mcp_server.py::_register_all@180, sym:deploynator/_mcp_server.py::dispatch@144, sym:deploynator/__main__.py::build_parser@17, sym:tests/test_cli_mcp.py::_server@37
- Rating 2.1/10 = 7 x PageRank share 0.29 + 3 x risk 0.00. Internal imports: 13.

## unassigned files (`c5`, community, rating 1.0)

3 files under root (py 2, sh 1), mostly utility. Core file app.py (PageRank 0.0160, imported by 0 files): Autor: Gris Iscomeback Correo electrónico: grisiscomeback[at]gmail[dot]com Fecha de creación: xx/xx/xxxx Licencia: GPL v3  Descripción:

- `app.py` ranks 1 by PageRank, 0 importers, 0 symbols: Autor: Gris Iscomeback Correo electrónico: grisiscomeback[at]gmail[dot]com Fecha de creación: xx/xx/xxxx Licencia: GPL v3  Descripción:
- `install.sh` ranks 2 by PageRank, 0 importers, 0 symbols.
- `tests/__init__.py` ranks 3 by PageRank, 0 importers, 0 symbols.
- Hotspot `app.py`: 0 symbols, 0 connections (score 0.00).
- Hotspot `install.sh`: 0 symbols, 0 connections (score 0.00).
- Key entities: file:install.sh, file:app.py, file:tests/__init__.py
- Rating 1.0/10 = 7 x PageRank share 0.14 + 3 x risk 0.00. Internal imports: 0.
