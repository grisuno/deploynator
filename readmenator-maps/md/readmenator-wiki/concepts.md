# Concepts

Second-brain semantic layer: nouns map atomically to file sets (EXTRACTED); verbs aggregate structural edges (INFERRED).

| Concept | Files | Mentions | Top Files |
|---------|-------|----------|-----------|
| `deploynator` | 23 | 37 | `app.py`, `deploy.sh`, `deploynator/__init__.py`, `deploynator/__main__.py`, `deploynator/_app.py` |
| `deploy` | 12 | 35 | `deploy.sh`, `deploynator/_deploy.py`, `deploynator/_mcp_server.py`, `deploynator/_models.py`, `deploynator/_readme.py` |
| `release` | 12 | 34 | `deploy.sh`, `deploynator/_app.py`, `deploynator/_changelog.py`, `deploynator/_deploy.py`, `deploynator/_mcp_server.py` |
| `run` | 12 | 17 | `app.py`, `deploy.sh`, `deploynator/_docs.py`, `deploynator/_mcp_server.py`, `deploynator/_platforms.py` |
| `git` | 11 | 22 | `deploy.sh`, `deploynator/_git.py`, `deploynator/_models.py`, `deploynator/_platforms.py`, `deploynator/_pypi.py` |
| `project` | 11 | 19 | `deploynator/_app.py`, `deploynator/_deploy.py`, `deploynator/_models.py`, `deploynator/_pypi.py`, `deploynator/_toml.py` |
| `config` | 8 | 26 | `deploynator/_config.py`, `deploynator/_models.py`, `deploynator/_readme.py`, `deploynator/_toml.py`, `tests/test_config.py` |
| `version` | 7 | 27 | `deploynator/_models.py`, `deploynator/_semver.py`, `tests/bdd_test_deploy.py`, `tests/test_models.py`, `tests/test_path_deploy.py` |
| `commit` | 7 | 19 | `deploynator/_app.py`, `deploynator/_git.py`, `deploynator/_mcp_server.py`, `deploynator/_models.py`, `tests/bdd_test_deploy.py` |
| `bump` | 7 | 18 | `deploy.sh`, `deploynator/_models.py`, `deploynator/_semver.py`, `tests/bdd_test_deploy.py`, `tests/test_models.py` |
| `install` | 7 | 17 | `app.py`, `deploy.sh`, `deploynator/_app.py`, `deploynator/_deploy.py`, `install.sh` |
| `file` | 7 | 14 | `deploynator/_semver.py`, `deploynator/_toml.py`, `tests/bdd_test_deploy.py`, `tests/test_deploy.py`, `tests/test_path_deploy.py` |
| `none` | 7 | 9 | `deploynator/_app.py`, `deploynator/_pypi.py`, `deploynator/_readme.py`, `deploynator/_toml.py`, `tests/test_models.py` |
| `valid` | 7 | 9 | `deploynator/_models.py`, `deploynator/_semver.py`, `tests/test_config.py`, `tests/test_init.py`, `tests/test_models.py` |
| `current` | 7 | 8 | `deploy.sh`, `deploynator/_git.py`, `deploynator/_semver.py`, `tests/bdd_test_deploy.py`, `tests/test_pipeline.py` |
| `red` | 7 | 7 | `tests/test_cli_mcp.py`, `tests/test_init.py`, `tests/test_install_example.py`, `tests/test_pipeline.py`, `tests/test_pypi.py` |
| `toml` | 6 | 21 | `deploynator/_toml.py`, `tests/test_init.py`, `tests/test_path_deploy.py`, `tests/test_pypi.py`, `tests/test_runner.py` |
| `docs` | 6 | 20 | `deploynator/_app.py`, `deploynator/_docs.py`, `deploynator/_mcp_server.py`, `tests/bdd_test_deploy.py`, `tests/test_pipeline.py` |
| `type` | 6 | 15 | `deploynator/_app.py`, `deploynator/_models.py`, `tests/bdd_test_deploy.py`, `tests/test_changelog.py`, `tests/test_config.py` |
| `path` | 6 | 14 | `deploynator/_app.py`, `deploynator/_config.py`, `deploynator/_deploy.py`, `deploynator/_readme.py`, `tests/test_config.py` |
| `tag` | 6 | 14 | `deploynator/_git.py`, `deploynator/_mcp_server.py`, `deploynator/_semver.py`, `tests/bdd_test_deploy.py`, `tests/test_path_deploy.py` |
| `semver` | 6 | 10 | `deploynator/_mcp_server.py`, `deploynator/_semver.py`, `tests/bdd_test_deploy.py`, `tests/test_config.py`, `tests/test_pipeline.py` |
| `name` | 6 | 9 | `deploynator/_deploy.py`, `deploynator/_models.py`, `deploynator/_platforms.py`, `tests/test_deploy.py`, `tests/test_models.py` |
| `create` | 5 | 18 | `deploynator/_config.py`, `deploynator/_deploy.py`, `deploynator/_git.py`, `deploynator/_platforms.py`, `tests/bdd_test_deploy.py` |
| `cli` | 5 | 9 | `deploynator/_models.py`, `deploynator/_platforms.py`, `tests/test_cli_mcp.py`, `tests/test_install_example.py`, `tests/test_models.py` |
| `format` | 5 | 9 | `deploynator/_changelog.py`, `deploynator/_models.py`, `tests/bdd_test_deploy.py`, `tests/test_changelog.py`, `tests/test_models.py` |
| `empty` | 5 | 8 | `tests/test_changelog.py`, `tests/test_deploy.py`, `tests/test_install_example.py`, `tests/test_pypi.py`, `tests/test_runner.py` |
| `list` | 5 | 8 | `deploynator/_app.py`, `deploynator/_mcp_server.py`, `deploynator/_toml.py`, `tests/test_cli_mcp.py`, `tests/test_toml.py` |
| `repo` | 5 | 8 | `deploy.sh`, `deploynator/_deploy.py`, `deploynator/_mcp_server.py`, `deploynator/_readme.py`, `tests/test_git_sync.py` |
| `default` | 5 | 7 | `deploynator/_app.py`, `deploynator/_toml.py`, `tests/test_config.py`, `tests/test_install_example.py`, `tests/test_pypi.py` |
| `failure` | 5 | 7 | `tests/bdd_test_deploy.py`, `tests/test_install_example.py`, `tests/test_pipeline.py`, `tests/test_pypi.py`, `tests/test_runner.py` |
| `exists` | 5 | 6 | `deploynator/_git.py`, `deploynator/_readme.py`, `tests/test_cli_mcp.py`, `tests/test_git_sync.py`, `tests/test_install_example.py` |
| `dry` | 5 | 5 | `app.py`, `deploy.sh`, `deploynator/_mcp_server.py`, `tests/test_path_deploy.py`, `tests/test_pipeline.py` |
| `force` | 5 | 5 | `deploynator/_deploy.py`, `deploynator/_git.py`, `tests/bdd_test_deploy.py`, `tests/test_git_sync.py`, `tests/test_pipeline.py` |
| `platform` | 4 | 13 | `deploynator/_models.py`, `deploynator/_platforms.py`, `tests/bdd_test_deploy.py`, `tests/test_models.py` |
| `pypi` | 4 | 12 | `deploynator/_pypi.py`, `deploynator/_toml.py`, `tests/test_pypi.py`, `tests/test_toml.py` |
| `runner` | 4 | 12 | `deploynator/_docs.py`, `deploynator/_runner.py`, `tests/test_pypi.py`, `tests/test_runner.py` |
| `when` | 4 | 12 | `deploynator/_readme.py`, `tests/bdd_test_deploy.py`, `tests/test_git_sync.py`, `tests/test_readme_footer.py` |
| `line` | 4 | 11 | `deploynator/_models.py`, `deploynator/_readme.py`, `tests/test_models.py`, `tests/test_readme_footer.py` |
| `packaging` | 4 | 11 | `deploynator/_pypi.py`, `deploynator/_toml.py`, `tests/test_pypi.py`, `tests/test_toml.py` |
| `auth` | 4 | 10 | `deploynator/_app.py`, `deploynator/_models.py`, `tests/test_config.py`, `tests/test_models.py` |
| `generate` | 4 | 10 | `deploynator/_app.py`, `deploynator/_changelog.py`, `deploynator/_deploy.py`, `tests/test_changelog.py` |
| `changelog` | 4 | 9 | `deploynator/_changelog.py`, `deploynator/_models.py`, `tests/test_changelog.py`, `tests/test_models.py` |
| `push` | 4 | 9 | `deploynator/_deploy.py`, `deploynator/_git.py`, `deploynator/_mcp_server.py`, `deploynator/_platforms.py` |
| `returns` | 4 | 9 | `deploynator/_readme.py`, `tests/test_pypi.py`, `tests/test_runner.py`, `tests/test_toml.py` |
| `get` | 4 | 8 | `deploynator/_deploy.py`, `deploynator/_git.py`, `deploynator/_semver.py`, `tests/test_semver.py` |
| `max` | 4 | 8 | `deploynator/_semver.py`, `deploynator/_toml.py`, `tests/bdd_test_deploy.py`, `tests/test_pipeline.py` |
| `load` | 4 | 7 | `deploynator/_deploy.py`, `deploynator/_toml.py`, `tests/test_deploy.py`, `tests/test_toml.py` |
| `pipeline` | 4 | 7 | `deploynator/_mcp_server.py`, `tests/bdd_test_deploy.py`, `tests/test_pipeline.py`, `tests/test_pypi.py` |
| `block` | 4 | 6 | `deploynator/_readme.py`, `tests/bdd_test_deploy.py`, `tests/test_pipeline.py`, `tests/test_readme_footer.py` |

## Verb Edges

| Source | Verb | Target | Strength |
|--------|------|--------|----------|
| `release` | `depends_on` | `deploynator` | 1.00 |
| `project` | `depends_on` | `deploynator` | 0.98 |
| `deploy` | `depends_on` | `deploynator` | 0.93 |
| `deploynator` | `depends_on` | `config` | 0.85 |
| `run` | `depends_on` | `deploynator` | 0.76 |
| `git` | `depends_on` | `deploynator` | 0.71 |
| `deploynator` | `depends_on` | `create` | 0.61 |
| `force` | `depends_on` | `deploynator` | 0.61 |
| `install` | `depends_on` | `deploynator` | 0.61 |
| `docs` | `depends_on` | `deploynator` | 0.59 |
| `file` | `depends_on` | `deploynator` | 0.59 |
| `path` | `depends_on` | `deploynator` | 0.59 |
| `red` | `depends_on` | `deploynator` | 0.59 |
| `deploynator` | `depends_on` | `path` | 0.56 |
| `failure` | `depends_on` | `deploynator` | 0.54 |
| `name` | `depends_on` | `deploynator` | 0.54 |
| `project` | `depends_on` | `config` | 0.54 |
| `deploynator` | `depends_on` | `project` | 0.51 |
| `generate` | `depends_on` | `deploynator` | 0.51 |
| `version` | `depends_on` | `deploynator` | 0.51 |
| `create` | `depends_on` | `deploynator` | 0.49 |
| `deploy` | `depends_on` | `config` | 0.49 |
| `release` | `depends_on` | `config` | 0.49 |
| `run` | `depends_on` | `config` | 0.49 |
| `tag` | `depends_on` | `deploynator` | 0.49 |
| `none` | `depends_on` | `deploynator` | 0.46 |
| `toml` | `depends_on` | `deploynator` | 0.46 |
| `current` | `depends_on` | `deploynator` | 0.44 |
| `semver` | `depends_on` | `deploynator` | 0.44 |
| `commit` | `depends_on` | `deploynator` | 0.41 |
| `empty` | `depends_on` | `deploynator` | 0.41 |
| `get` | `depends_on` | `deploynator` | 0.41 |
| `git` | `depends_on` | `config` | 0.41 |
| `pipeline` | `depends_on` | `deploynator` | 0.41 |
| `project` | `depends_on` | `create` | 0.41 |
| `repo` | `depends_on` | `deploynator` | 0.41 |
| `bump` | `depends_on` | `deploynator` | 0.39 |
| `default` | `depends_on` | `deploynator` | 0.39 |
| `deploynator` | `depends_on` | `release` | 0.39 |
| `load` | `depends_on` | `deploynator` | 0.39 |
| `push` | `depends_on` | `deploynator` | 0.39 |
| `release` | `depends_on` | `create` | 0.39 |
| `type` | `depends_on` | `deploynator` | 0.39 |
| `deploy` | `depends_on` | `create` | 0.37 |
| `deploy` | `depends_on` | `path` | 0.37 |
| `git` | `depends_on` | `project` | 0.37 |
| `project` | `depends_on` | `release` | 0.37 |
| `run` | `depends_on` | `path` | 0.37 |
| `deploy` | `depends_on` | `project` | 0.34 |
| `file` | `depends_on` | `config` | 0.34 |

## Dialectic Prompts

- Thesis: `auth` centralizes 4 files; Antithesis: `changelog` pulls 4 files with 2 shared (Jaccard 0.33); Synthesis: should they merge, split by layer, or keep `bridges` explicit?
- Thesis: `auth` centralizes 4 files; Antithesis: `commit` pulls 7 files with 4 shared (Jaccard 0.57); Synthesis: should they merge, split by layer, or keep `bridges` explicit?
- Thesis: `auth` centralizes 4 files; Antithesis: `config` pulls 8 files with 3 shared (Jaccard 0.33); Synthesis: should they merge, split by layer, or keep `bridges` explicit?
- Thesis: `auth` centralizes 4 files; Antithesis: `line` pulls 4 files with 2 shared (Jaccard 0.33); Synthesis: should they merge, split by layer, or keep `bridges` explicit?
- Thesis: `auth` centralizes 4 files; Antithesis: `platform` pulls 4 files with 2 shared (Jaccard 0.33); Synthesis: should they merge, split by layer, or keep `bridges` explicit?
- Thesis: `auth` centralizes 4 files; Antithesis: `type` pulls 6 files with 4 shared (Jaccard 0.67); Synthesis: should they merge, split by layer, or keep `bridges` explicit?
- Thesis: `auth` centralizes 4 files; Antithesis: `valid` pulls 7 files with 3 shared (Jaccard 0.38); Synthesis: should they merge, split by layer, or keep `bridges` explicit?
- Thesis: `block` centralizes 4 files; Antithesis: `current` pulls 7 files with 3 shared (Jaccard 0.38); Synthesis: should they merge, split by layer, or keep `bridges` explicit?
- Thesis: `block` centralizes 4 files; Antithesis: `deploy` pulls 12 files with 4 shared (Jaccard 0.33); Synthesis: should they merge, split by layer, or keep `bridges` explicit?
- Thesis: `block` centralizes 4 files; Antithesis: `line` pulls 4 files with 2 shared (Jaccard 0.33); Synthesis: should they merge, split by layer, or keep `bridges` explicit?
