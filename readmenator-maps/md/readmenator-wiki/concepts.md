# Concepts

Second-brain semantic layer: nouns map atomically to file sets (EXTRACTED); verbs aggregate structural edges (INFERRED).

| Concept | Files | Mentions | Top Files |
|---------|-------|----------|-----------|
| `deploynator` | 20 | 31 | `deploy.sh`, `deploynator/__init__.py`, `deploynator/__main__.py`, `deploynator/_app.py`, `deploynator/_changelog.py` |
| `release` | 12 | 33 | `deploy.sh`, `deploynator/_app.py`, `deploynator/_changelog.py`, `deploynator/_deploy.py`, `deploynator/_mcp_server.py` |
| `deploy` | 10 | 31 | `deploy.sh`, `deploynator/_deploy.py`, `deploynator/_mcp_server.py`, `deploynator/_models.py`, `tests/bdd_test_deploy.py` |
| `project` | 10 | 16 | `deploynator/_app.py`, `deploynator/_deploy.py`, `deploynator/_models.py`, `deploynator/_pypi.py`, `tests/bdd_test_deploy.py` |
| `git` | 9 | 17 | `deploynator/_git.py`, `deploynator/_models.py`, `deploynator/_platforms.py`, `deploynator/_pypi.py`, `tests/bdd_test_deploy.py` |
| `run` | 9 | 12 | `deploy.sh`, `deploynator/_docs.py`, `deploynator/_mcp_server.py`, `deploynator/_platforms.py`, `deploynator/_pypi.py` |
| `version` | 7 | 27 | `deploynator/_models.py`, `deploynator/_semver.py`, `tests/bdd_test_deploy.py`, `tests/test_models.py`, `tests/test_path_deploy.py` |
| `bump` | 7 | 18 | `deploy.sh`, `deploynator/_models.py`, `deploynator/_semver.py`, `tests/bdd_test_deploy.py`, `tests/test_models.py` |
| `commit` | 7 | 18 | `deploynator/_app.py`, `deploynator/_git.py`, `deploynator/_mcp_server.py`, `deploynator/_models.py`, `tests/bdd_test_deploy.py` |
| `valid` | 7 | 9 | `deploynator/_models.py`, `deploynator/_semver.py`, `tests/test_config.py`, `tests/test_init.py`, `tests/test_models.py` |
| `docs` | 6 | 20 | `deploynator/_app.py`, `deploynator/_docs.py`, `deploynator/_mcp_server.py`, `tests/bdd_test_deploy.py`, `tests/test_pipeline.py` |
| `config` | 6 | 19 | `deploynator/_config.py`, `deploynator/_models.py`, `deploynator/_toml.py`, `tests/test_config.py`, `tests/test_models.py` |
| `toml` | 6 | 18 | `deploynator/_toml.py`, `tests/test_init.py`, `tests/test_path_deploy.py`, `tests/test_pypi.py`, `tests/test_runner.py` |
| `tag` | 6 | 14 | `deploynator/_git.py`, `deploynator/_mcp_server.py`, `deploynator/_semver.py`, `tests/bdd_test_deploy.py`, `tests/test_path_deploy.py` |
| `file` | 6 | 13 | `deploynator/_semver.py`, `tests/bdd_test_deploy.py`, `tests/test_deploy.py`, `tests/test_path_deploy.py`, `tests/test_pipeline.py` |
| `semver` | 6 | 10 | `deploynator/_mcp_server.py`, `deploynator/_semver.py`, `tests/bdd_test_deploy.py`, `tests/test_config.py`, `tests/test_pipeline.py` |
| `name` | 6 | 9 | `deploynator/_deploy.py`, `deploynator/_models.py`, `deploynator/_platforms.py`, `tests/test_deploy.py`, `tests/test_models.py` |
| `red` | 6 | 6 | `tests/test_cli_mcp.py`, `tests/test_init.py`, `tests/test_pipeline.py`, `tests/test_pypi.py`, `tests/test_runner.py` |
| `create` | 5 | 18 | `deploynator/_config.py`, `deploynator/_deploy.py`, `deploynator/_git.py`, `deploynator/_platforms.py`, `tests/bdd_test_deploy.py` |
| `type` | 5 | 14 | `deploynator/_models.py`, `tests/bdd_test_deploy.py`, `tests/test_changelog.py`, `tests/test_config.py`, `tests/test_models.py` |
| `path` | 5 | 11 | `deploynator/_app.py`, `deploynator/_config.py`, `deploynator/_deploy.py`, `tests/test_config.py`, `tests/test_path_deploy.py` |
| `format` | 5 | 9 | `deploynator/_changelog.py`, `deploynator/_models.py`, `tests/bdd_test_deploy.py`, `tests/test_changelog.py`, `tests/test_models.py` |
| `current` | 5 | 6 | `deploynator/_git.py`, `deploynator/_semver.py`, `tests/bdd_test_deploy.py`, `tests/test_pipeline.py`, `tests/test_semver.py` |
| `platform` | 4 | 13 | `deploynator/_models.py`, `deploynator/_platforms.py`, `tests/bdd_test_deploy.py`, `tests/test_models.py` |
| `runner` | 4 | 12 | `deploynator/_docs.py`, `deploynator/_runner.py`, `tests/test_pypi.py`, `tests/test_runner.py` |
| `auth` | 4 | 10 | `deploynator/_app.py`, `deploynator/_models.py`, `tests/test_config.py`, `tests/test_models.py` |
| `generate` | 4 | 10 | `deploynator/_app.py`, `deploynator/_changelog.py`, `deploynator/_deploy.py`, `tests/test_changelog.py` |
| `changelog` | 4 | 9 | `deploynator/_changelog.py`, `deploynator/_models.py`, `tests/test_changelog.py`, `tests/test_models.py` |
| `cli` | 4 | 8 | `deploynator/_models.py`, `deploynator/_platforms.py`, `tests/test_cli_mcp.py`, `tests/test_models.py` |
| `get` | 4 | 8 | `deploynator/_deploy.py`, `deploynator/_git.py`, `deploynator/_semver.py`, `tests/test_semver.py` |
| `empty` | 4 | 7 | `tests/test_changelog.py`, `tests/test_deploy.py`, `tests/test_pypi.py`, `tests/test_runner.py` |
| `pipeline` | 4 | 7 | `deploynator/_mcp_server.py`, `tests/bdd_test_deploy.py`, `tests/test_pipeline.py`, `tests/test_pypi.py` |
| `failure` | 4 | 6 | `tests/bdd_test_deploy.py`, `tests/test_pipeline.py`, `tests/test_pypi.py`, `tests/test_runner.py` |
| `install` | 4 | 6 | `deploynator/_app.py`, `deploynator/_deploy.py`, `install.sh`, `tests/test_deploy.py` |
| `load` | 4 | 6 | `deploynator/_deploy.py`, `deploynator/_toml.py`, `tests/test_deploy.py`, `tests/test_toml.py` |
| `log` | 4 | 6 | `deploynator/_changelog.py`, `deploynator/_git.py`, `deploynator/_models.py`, `tests/test_models.py` |
| `patch` | 4 | 6 | `deploy.sh`, `tests/bdd_test_deploy.py`, `tests/test_models.py`, `tests/test_semver.py` |
| `none` | 4 | 5 | `deploynator/_pypi.py`, `tests/test_models.py`, `tests/test_pypi.py`, `tests/test_semver.py` |
| `all` | 4 | 4 | `deploynator/_git.py`, `deploynator/_mcp_server.py`, `deploynator/_platforms.py`, `tests/test_config.py` |
| `dry` | 4 | 4 | `deploy.sh`, `deploynator/_mcp_server.py`, `tests/test_path_deploy.py`, `tests/test_pipeline.py` |
| `header` | 4 | 4 | `deploynator/_changelog.py`, `deploynator/_models.py`, `tests/test_changelog.py`, `tests/test_models.py` |
| `minor` | 4 | 4 | `deploy.sh`, `tests/bdd_test_deploy.py`, `tests/test_models.py`, `tests/test_semver.py` |
| `resolve` | 4 | 4 | `deploynator/_app.py`, `deploynator/_config.py`, `deploynator/_deploy.py`, `tests/test_config.py` |
| `write` | 4 | 4 | `deploynator/_changelog.py`, `deploynator/_semver.py`, `tests/test_path_deploy.py`, `tests/test_semver.py` |
| `interactive` | 3 | 15 | `deploynator/_app.py`, `deploynator/_mcp_server.py`, `tests/test_cli_mcp.py` |
| `contract` | 3 | 11 | `tests/test_config.py`, `tests/test_models.py`, `tests/test_toml.py` |
| `status` | 3 | 10 | `deploynator/_app.py`, `deploynator/_mcp_server.py`, `tests/test_cli_mcp.py` |
| `mcp` | 3 | 9 | `deploynator/_mcp_server.py`, `deploynator/_pypi.py`, `tests/test_cli_mcp.py` |
| `projects` | 3 | 8 | `deploynator/_app.py`, `deploynator/_mcp_server.py`, `tests/test_cli_mcp.py` |
| `string` | 3 | 8 | `deploynator/_models.py`, `tests/test_models.py`, `tests/test_runner.py` |

## Verb Edges

| Source | Verb | Target | Strength |
|--------|------|--------|----------|
| `release` | `depends_on` | `deploynator` | 1.00 |
| `project` | `depends_on` | `deploynator` | 0.93 |
| `deploy` | `depends_on` | `deploynator` | 0.83 |
| `deploynator` | `depends_on` | `config` | 0.76 |
| `git` | `depends_on` | `deploynator` | 0.63 |
| `docs` | `depends_on` | `deploynator` | 0.59 |
| `run` | `depends_on` | `deploynator` | 0.59 |
| `file` | `depends_on` | `deploynator` | 0.56 |
| `deploynator` | `depends_on` | `create` | 0.54 |
| `path` | `depends_on` | `deploynator` | 0.54 |
| `generate` | `depends_on` | `deploynator` | 0.51 |
| `name` | `depends_on` | `deploynator` | 0.51 |
| `red` | `depends_on` | `deploynator` | 0.51 |
| `version` | `depends_on` | `deploynator` | 0.51 |
| `project` | `depends_on` | `config` | 0.49 |
| `release` | `depends_on` | `config` | 0.49 |
| `tag` | `depends_on` | `deploynator` | 0.49 |
| `create` | `depends_on` | `deploynator` | 0.46 |
| `deploynator` | `depends_on` | `path` | 0.46 |
| `deploynator` | `depends_on` | `resolve` | 0.46 |
| `failure` | `depends_on` | `deploynator` | 0.46 |
| `install` | `depends_on` | `deploynator` | 0.46 |
| `toml` | `depends_on` | `deploynator` | 0.46 |
| `semver` | `depends_on` | `deploynator` | 0.44 |
| `commit` | `depends_on` | `deploynator` | 0.41 |
| `pipeline` | `depends_on` | `deploynator` | 0.41 |
| `resolve` | `depends_on` | `deploynator` | 0.41 |
| `bump` | `depends_on` | `deploynator` | 0.39 |
| `current` | `depends_on` | `deploynator` | 0.39 |
| `deploy` | `depends_on` | `config` | 0.39 |
| `deploynator` | `depends_on` | `release` | 0.39 |
| `get` | `depends_on` | `deploynator` | 0.39 |
| `git` | `depends_on` | `config` | 0.39 |
| `project` | `depends_on` | `create` | 0.39 |
| `release` | `depends_on` | `create` | 0.39 |
| `run` | `depends_on` | `config` | 0.39 |
| `empty` | `depends_on` | `deploynator` | 0.37 |
| `load` | `depends_on` | `deploynator` | 0.37 |
| `project` | `depends_on` | `release` | 0.37 |
| `project` | `depends_on` | `name` | 0.34 |
| `deploy` | `depends_on` | `create` | 0.32 |
| `deploynator` | `depends_on` | `git` | 0.32 |
| `deploynator` | `depends_on` | `name` | 0.32 |
| `deploynator` | `depends_on` | `project` | 0.32 |
| `docs` | `depends_on` | `config` | 0.32 |
| `file` | `depends_on` | `config` | 0.32 |
| `project` | `depends_on` | `git` | 0.32 |
| `release` | `depends_on` | `git` | 0.32 |
| `release` | `depends_on` | `name` | 0.32 |
| `runner` | `depends_on` | `deploynator` | 0.32 |

## Dialectic Prompts

- Thesis: `all` centralizes 4 files; Antithesis: `commit` pulls 7 files with 3 shared (Jaccard 0.38); Synthesis: should they merge, split by layer, or keep `bridges` explicit?
- Thesis: `auth` centralizes 4 files; Antithesis: `changelog` pulls 4 files with 2 shared (Jaccard 0.33); Synthesis: should they merge, split by layer, or keep `bridges` explicit?
- Thesis: `auth` centralizes 4 files; Antithesis: `cli` pulls 4 files with 2 shared (Jaccard 0.33); Synthesis: should they merge, split by layer, or keep `bridges` explicit?
- Thesis: `auth` centralizes 4 files; Antithesis: `commit` pulls 7 files with 4 shared (Jaccard 0.57); Synthesis: should they merge, split by layer, or keep `bridges` explicit?
- Thesis: `auth` centralizes 4 files; Antithesis: `config` pulls 6 files with 3 shared (Jaccard 0.43); Synthesis: should they merge, split by layer, or keep `bridges` explicit?
- Thesis: `auth` centralizes 4 files; Antithesis: `contract` pulls 3 files with 2 shared (Jaccard 0.40); Synthesis: should they merge, split by layer, or keep `bridges` explicit?
- Thesis: `auth` centralizes 4 files; Antithesis: `header` pulls 4 files with 2 shared (Jaccard 0.33); Synthesis: should they merge, split by layer, or keep `bridges` explicit?
- Thesis: `auth` centralizes 4 files; Antithesis: `log` pulls 4 files with 2 shared (Jaccard 0.33); Synthesis: should they merge, split by layer, or keep `bridges` explicit?
- Thesis: `auth` centralizes 4 files; Antithesis: `platform` pulls 4 files with 2 shared (Jaccard 0.33); Synthesis: should they merge, split by layer, or keep `bridges` explicit?
- Thesis: `auth` centralizes 4 files; Antithesis: `resolve` pulls 4 files with 2 shared (Jaccard 0.33); Synthesis: should they merge, split by layer, or keep `bridges` explicit?
