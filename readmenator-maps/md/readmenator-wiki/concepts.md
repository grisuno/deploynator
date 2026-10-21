# Concepts

Second-brain semantic layer: nouns map atomically to file sets (EXTRACTED); verbs aggregate structural edges (INFERRED).

| Concept | Files | Mentions | Top Files |
|---------|-------|----------|-----------|
| `deploynator` | 25 | 41 | `app.py`, `deploy.sh`, `deploynator/__init__.py`, `deploynator/__main__.py`, `deploynator/_app.py` |
| `run` | 16 | 30 | `app.py`, `deploy.sh`, `deploynator/_deb.py`, `deploynator/_docs.py`, `deploynator/_mcp_server.py` |
| `deploy` | 15 | 42 | `deploy.sh`, `deploynator/_deploy.py`, `deploynator/_mcp_server.py`, `deploynator/_models.py`, `deploynator/_readme.py` |
| `release` | 14 | 44 | `deploy.sh`, `deploynator/_app.py`, `deploynator/_changelog.py`, `deploynator/_deploy.py`, `deploynator/_mcp_server.py` |
| `project` | 14 | 23 | `deploynator/_app.py`, `deploynator/_deb.py`, `deploynator/_deploy.py`, `deploynator/_models.py`, `deploynator/_pypi.py` |
| `git` | 13 | 25 | `deploy.sh`, `deploynator/_git.py`, `deploynator/_models.py`, `deploynator/_platforms.py`, `deploynator/_pypi.py` |
| `config` | 10 | 29 | `deploynator/_config.py`, `deploynator/_models.py`, `deploynator/_readme.py`, `deploynator/_receipt.py`, `deploynator/_toml.py` |
| `tag` | 9 | 17 | `deploynator/_deploy.py`, `deploynator/_git.py`, `deploynator/_mcp_server.py`, `deploynator/_platforms.py`, `deploynator/_receipt.py` |
| `default` | 9 | 12 | `deploynator/_app.py`, `deploynator/_deb.py`, `deploynator/_platforms.py`, `deploynator/_receipt.py`, `deploynator/_toml.py` |
| `current` | 9 | 11 | `deploy.sh`, `deploynator/_git.py`, `deploynator/_receipt.py`, `deploynator/_semver.py`, `tests/bdd_test_deploy.py` |
| `toml` | 8 | 25 | `deploynator/_toml.py`, `tests/test_deb.py`, `tests/test_init.py`, `tests/test_path_deploy.py`, `tests/test_pypi.py` |
| `commit` | 8 | 21 | `deploynator/_app.py`, `deploynator/_git.py`, `deploynator/_mcp_server.py`, `deploynator/_models.py`, `deploynator/_receipt.py` |
| `path` | 8 | 16 | `deploynator/_app.py`, `deploynator/_config.py`, `deploynator/_deploy.py`, `deploynator/_readme.py`, `deploynator/_receipt.py` |
| `failure` | 8 | 12 | `deploynator/_receipt.py`, `tests/bdd_test_deploy.py`, `tests/test_deb.py`, `tests/test_install_example.py`, `tests/test_pipeline.py` |
| `repo` | 8 | 12 | `deploy.sh`, `deploynator/_deploy.py`, `deploynator/_mcp_server.py`, `deploynator/_platforms.py`, `deploynator/_readme.py` |
| `red` | 8 | 8 | `tests/test_cli_mcp.py`, `tests/test_deb.py`, `tests/test_init.py`, `tests/test_install_example.py`, `tests/test_pipeline.py` |
| `version` | 7 | 27 | `deploynator/_models.py`, `deploynator/_semver.py`, `tests/bdd_test_deploy.py`, `tests/test_models.py`, `tests/test_path_deploy.py` |
| `docs` | 7 | 22 | `deploynator/_app.py`, `deploynator/_docs.py`, `deploynator/_mcp_server.py`, `tests/bdd_test_deploy.py`, `tests/test_pipeline.py` |
| `bump` | 7 | 18 | `deploy.sh`, `deploynator/_models.py`, `deploynator/_semver.py`, `tests/bdd_test_deploy.py`, `tests/test_models.py` |
| `build` | 7 | 17 | `deploynator/__main__.py`, `deploynator/_deb.py`, `deploynator/_receipt.py`, `deploynator/_toml.py`, `tests/test_deb.py` |
| `install` | 7 | 17 | `app.py`, `deploy.sh`, `deploynator/_app.py`, `deploynator/_deploy.py`, `install.sh` |
| `file` | 7 | 14 | `deploynator/_semver.py`, `deploynator/_toml.py`, `tests/bdd_test_deploy.py`, `tests/test_deploy.py`, `tests/test_path_deploy.py` |
| `make` | 7 | 12 | `deploynator/_deb.py`, `deploynator/_toml.py`, `tests/test_deb.py`, `tests/test_git_sync.py`, `tests/test_receipt.py` |
| `empty` | 7 | 10 | `tests/test_changelog.py`, `tests/test_deb.py`, `tests/test_deploy.py`, `tests/test_install_example.py`, `tests/test_pypi.py` |
| `name` | 7 | 10 | `deploynator/_deploy.py`, `deploynator/_models.py`, `deploynator/_platforms.py`, `deploynator/_receipt.py`, `tests/test_deploy.py` |
| `none` | 7 | 9 | `deploynator/_app.py`, `deploynator/_pypi.py`, `deploynator/_readme.py`, `deploynator/_toml.py`, `tests/test_models.py` |
| `valid` | 7 | 9 | `deploynator/_models.py`, `deploynator/_semver.py`, `tests/test_config.py`, `tests/test_init.py`, `tests/test_models.py` |
| `platform` | 6 | 20 | `deploynator/_models.py`, `deploynator/_platforms.py`, `deploynator/_receipt.py`, `tests/bdd_test_deploy.py`, `tests/test_models.py` |
| `runner` | 6 | 15 | `deploynator/_deb.py`, `deploynator/_docs.py`, `deploynator/_runner.py`, `tests/test_deb.py`, `tests/test_pypi.py` |
| `type` | 6 | 15 | `deploynator/_app.py`, `deploynator/_models.py`, `tests/bdd_test_deploy.py`, `tests/test_changelog.py`, `tests/test_config.py` |
| `cli` | 6 | 13 | `deploynator/_models.py`, `deploynator/_platforms.py`, `deploynator/_receipt.py`, `tests/test_cli_mcp.py`, `tests/test_install_example.py` |
| `write` | 6 | 11 | `deploynator/_changelog.py`, `deploynator/_receipt.py`, `deploynator/_semver.py`, `tests/test_path_deploy.py`, `tests/test_receipt.py` |
| `command` | 6 | 10 | `deploynator/_deb.py`, `deploynator/_receipt.py`, `tests/test_cli_mcp.py`, `tests/test_deb.py`, `tests/test_receipt.py` |
| `load` | 6 | 10 | `deploynator/_deploy.py`, `deploynator/_receipt.py`, `deploynator/_toml.py`, `tests/test_deploy.py`, `tests/test_receipt.py` |
| `semver` | 6 | 10 | `deploynator/_mcp_server.py`, `deploynator/_semver.py`, `tests/bdd_test_deploy.py`, `tests/test_config.py`, `tests/test_pipeline.py` |
| `not` | 6 | 9 | `deploynator/_receipt.py`, `tests/bdd_test_deploy.py`, `tests/test_deb.py`, `tests/test_deploy.py`, `tests/test_pipeline.py` |
| `target` | 6 | 9 | `deploynator/_deb.py`, `deploynator/_receipt.py`, `deploynator/_toml.py`, `tests/test_deb.py`, `tests/test_runner.py` |
| `without` | 6 | 9 | `deploynator/_mcp_server.py`, `deploynator/_readme.py`, `deploynator/_receipt.py`, `tests/test_deb.py`, `tests/test_pypi.py` |
| `dir` | 6 | 7 | `deploynator/_deb.py`, `deploynator/_receipt.py`, `tests/test_deb.py`, `tests/test_deploy.py`, `tests/test_pypi.py` |
| `shell` | 6 | 7 | `deploynator/_deb.py`, `deploynator/_platforms.py`, `tests/test_deb.py`, `tests/test_install_example.py`, `tests/test_pypi.py` |
| `dry` | 6 | 6 | `app.py`, `deploy.sh`, `deploynator/_mcp_server.py`, `tests/test_path_deploy.py`, `tests/test_pipeline.py` |
| `create` | 5 | 18 | `deploynator/_config.py`, `deploynator/_deploy.py`, `deploynator/_git.py`, `deploynator/_platforms.py`, `tests/bdd_test_deploy.py` |
| `packaging` | 5 | 13 | `deploynator/_pypi.py`, `deploynator/_toml.py`, `tests/test_deb.py`, `tests/test_pypi.py`, `tests/test_toml.py` |
| `format` | 5 | 9 | `deploynator/_changelog.py`, `deploynator/_models.py`, `tests/bdd_test_deploy.py`, `tests/test_changelog.py`, `tests/test_models.py` |
| `upload` | 5 | 9 | `deploy.sh`, `deploynator/_deploy.py`, `deploynator/_platforms.py`, `tests/test_deb.py`, `tests/test_pypi.py` |
| `list` | 5 | 8 | `deploynator/_app.py`, `deploynator/_mcp_server.py`, `deploynator/_toml.py`, `tests/test_cli_mcp.py`, `tests/test_toml.py` |
| `pipeline` | 5 | 8 | `deploynator/_mcp_server.py`, `tests/bdd_test_deploy.py`, `tests/test_deb.py`, `tests/test_pipeline.py`, `tests/test_pypi.py` |
| `para` | 5 | 7 | `deploynator/_deb.py`, `deploynator/_deploy.py`, `deploynator/_pypi.py`, `deploynator/_toml.py`, `tests/bdd_test_deploy.py` |
| `exists` | 5 | 6 | `deploynator/_git.py`, `deploynator/_readme.py`, `tests/test_cli_mcp.py`, `tests/test_git_sync.py`, `tests/test_install_example.py` |
| `como` | 5 | 5 | `deploynator/_deb.py`, `deploynator/_platforms.py`, `tests/bdd_test_deploy.py`, `tests/test_deb.py`, `tests/test_install_example.py` |

## Verb Edges

| Source | Verb | Target | Strength |
|--------|------|--------|----------|
| `project` | `depends_on` | `deploynator` | 1.00 |
| `deploy` | `depends_on` | `deploynator` | 0.94 |
| `release` | `depends_on` | `deploynator` | 0.91 |
| `run` | `depends_on` | `deploynator` | 0.81 |
| `deploynator` | `depends_on` | `config` | 0.72 |
| `tag` | `depends_on` | `deploynator` | 0.67 |
| `git` | `depends_on` | `deploynator` | 0.65 |
| `failure` | `depends_on` | `deploynator` | 0.61 |
| `path` | `depends_on` | `deploynator` | 0.59 |
| `project` | `depends_on` | `config` | 0.59 |
| `run` | `depends_on` | `config` | 0.56 |
| `deploy` | `depends_on` | `config` | 0.54 |
| `docs` | `depends_on` | `deploynator` | 0.54 |
| `red` | `depends_on` | `deploynator` | 0.54 |
| `toml` | `depends_on` | `deploynator` | 0.54 |
| `deploynator` | `depends_on` | `create` | 0.50 |
| `empty` | `depends_on` | `deploynator` | 0.50 |
| `install` | `depends_on` | `deploynator` | 0.50 |
| `repo` | `depends_on` | `deploynator` | 0.50 |
| `default` | `depends_on` | `deploynator` | 0.48 |
| `deploynator` | `depends_on` | `path` | 0.48 |
| `release` | `depends_on` | `config` | 0.48 |
| `name` | `depends_on` | `deploynator` | 0.46 |
| `upload` | `depends_on` | `deploynator` | 0.46 |
| `current` | `depends_on` | `deploynator` | 0.44 |
| `file` | `depends_on` | `deploynator` | 0.44 |
| `load` | `depends_on` | `deploynator` | 0.44 |
| `not` | `depends_on` | `deploynator` | 0.44 |
| `para` | `depends_on` | `deploynator` | 0.44 |
| `build` | `depends_on` | `deploynator` | 0.43 |
| `deploynator` | `depends_on` | `project` | 0.43 |
| `create` | `depends_on` | `deploynator` | 0.41 |
| `deploy` | `depends_on` | `path` | 0.41 |
| `deploy` | `depends_on` | `project` | 0.41 |
| `pipeline` | `depends_on` | `deploynator` | 0.41 |
| `project` | `depends_on` | `create` | 0.41 |
| `run` | `depends_on` | `path` | 0.41 |
| `command` | `depends_on` | `deploynator` | 0.39 |
| `git` | `depends_on` | `config` | 0.39 |
| `make` | `depends_on` | `deploynator` | 0.39 |
| `project` | `depends_on` | `path` | 0.39 |
| `project` | `depends_on` | `release` | 0.39 |
| `shell` | `depends_on` | `deploynator` | 0.39 |
| `version` | `depends_on` | `deploynator` | 0.39 |
| `deploy` | `depends_on` | `create` | 0.37 |
| `dir` | `depends_on` | `deploynator` | 0.37 |
| `project` | `depends_on` | `name` | 0.37 |
| `project` | `depends_on` | `para` | 0.37 |
| `run` | `depends_on` | `create` | 0.37 |
| `run` | `depends_on` | `project` | 0.37 |

## Dialectic Prompts

- Thesis: `build` centralizes 7 files; Antithesis: `command` pulls 6 files with 4 shared (Jaccard 0.44); Synthesis: should they merge, split by layer, or keep `bridges` explicit?
- Thesis: `build` centralizes 7 files; Antithesis: `default` pulls 9 files with 5 shared (Jaccard 0.45); Synthesis: should they merge, split by layer, or keep `bridges` explicit?
- Thesis: `build` centralizes 7 files; Antithesis: `dir` pulls 6 files with 4 shared (Jaccard 0.44); Synthesis: should they merge, split by layer, or keep `bridges` explicit?
- Thesis: `build` centralizes 7 files; Antithesis: `failure` pulls 8 files with 4 shared (Jaccard 0.36); Synthesis: should they merge, split by layer, or keep `bridges` explicit?
- Thesis: `build` centralizes 7 files; Antithesis: `load` pulls 6 files with 3 shared (Jaccard 0.30); Synthesis: should they merge, split by layer, or keep `bridges` explicit?
- Thesis: `build` centralizes 7 files; Antithesis: `make` pulls 7 files with 4 shared (Jaccard 0.40); Synthesis: should they merge, split by layer, or keep `bridges` explicit?
- Thesis: `build` centralizes 7 files; Antithesis: `not` pulls 6 files with 3 shared (Jaccard 0.30); Synthesis: should they merge, split by layer, or keep `bridges` explicit?
- Thesis: `build` centralizes 7 files; Antithesis: `packaging` pulls 5 files with 3 shared (Jaccard 0.33); Synthesis: should they merge, split by layer, or keep `bridges` explicit?
- Thesis: `build` centralizes 7 files; Antithesis: `project` pulls 14 files with 5 shared (Jaccard 0.31); Synthesis: should they merge, split by layer, or keep `bridges` explicit?
- Thesis: `build` centralizes 7 files; Antithesis: `runner` pulls 6 files with 3 shared (Jaccard 0.30); Synthesis: should they merge, split by layer, or keep `bridges` explicit?
