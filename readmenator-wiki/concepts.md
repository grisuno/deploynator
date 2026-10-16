# Concepts

Second-brain semantic layer: nouns map atomically to file sets (EXTRACTED); verbs aggregate structural edges (INFERRED).

| Concept | Files | Mentions | Top Files |
|---------|-------|----------|-----------|
| `deploynator` | 23 | 37 | `app.py`, `deploy.sh`, `deploynator/__init__.py`, `deploynator/__main__.py`, `deploynator/_app.py` |
| `deploy` | 12 | 35 | `deploy.sh`, `deploynator/_deploy.py`, `deploynator/_mcp_server.py`, `deploynator/_models.py`, `deploynator/_readme.py` |
| `release` | 12 | 33 | `deploy.sh`, `deploynator/_app.py`, `deploynator/_changelog.py`, `deploynator/_deploy.py`, `deploynator/_mcp_server.py` |
| `run` | 12 | 17 | `app.py`, `deploy.sh`, `deploynator/_docs.py`, `deploynator/_mcp_server.py`, `deploynator/_platforms.py` |
| `project` | 11 | 19 | `deploynator/_app.py`, `deploynator/_deploy.py`, `deploynator/_models.py`, `deploynator/_pypi.py`, `deploynator/_toml.py` |
| `git` | 10 | 18 | `deploy.sh`, `deploynator/_git.py`, `deploynator/_models.py`, `deploynator/_platforms.py`, `deploynator/_pypi.py` |
| `version` | 7 | 27 | `deploynator/_models.py`, `deploynator/_semver.py`, `tests/bdd_test_deploy.py`, `tests/test_models.py`, `tests/test_path_deploy.py` |
| `config` | 7 | 25 | `deploynator/_config.py`, `deploynator/_models.py`, `deploynator/_readme.py`, `deploynator/_toml.py`, `tests/test_config.py` |
| `bump` | 7 | 18 | `deploy.sh`, `deploynator/_models.py`, `deploynator/_semver.py`, `tests/bdd_test_deploy.py`, `tests/test_models.py` |
| `commit` | 7 | 18 | `deploynator/_app.py`, `deploynator/_git.py`, `deploynator/_mcp_server.py`, `deploynator/_models.py`, `tests/bdd_test_deploy.py` |
| `install` | 7 | 17 | `app.py`, `deploy.sh`, `deploynator/_app.py`, `deploynator/_deploy.py`, `install.sh` |
| `file` | 7 | 14 | `deploynator/_semver.py`, `deploynator/_toml.py`, `tests/bdd_test_deploy.py`, `tests/test_deploy.py`, `tests/test_path_deploy.py` |
| `valid` | 7 | 9 | `deploynator/_models.py`, `deploynator/_semver.py`, `tests/test_config.py`, `tests/test_init.py`, `tests/test_models.py` |
| `current` | 7 | 8 | `deploy.sh`, `deploynator/_git.py`, `deploynator/_semver.py`, `tests/bdd_test_deploy.py`, `tests/test_pipeline.py` |
| `red` | 7 | 7 | `tests/test_cli_mcp.py`, `tests/test_init.py`, `tests/test_install_example.py`, `tests/test_pipeline.py`, `tests/test_pypi.py` |
| `toml` | 6 | 21 | `deploynator/_toml.py`, `tests/test_init.py`, `tests/test_path_deploy.py`, `tests/test_pypi.py`, `tests/test_runner.py` |
| `docs` | 6 | 20 | `deploynator/_app.py`, `deploynator/_docs.py`, `deploynator/_mcp_server.py`, `tests/bdd_test_deploy.py`, `tests/test_pipeline.py` |
| `path` | 6 | 14 | `deploynator/_app.py`, `deploynator/_config.py`, `deploynator/_deploy.py`, `deploynator/_readme.py`, `tests/test_config.py` |
| `tag` | 6 | 14 | `deploynator/_git.py`, `deploynator/_mcp_server.py`, `deploynator/_semver.py`, `tests/bdd_test_deploy.py`, `tests/test_path_deploy.py` |
| `semver` | 6 | 10 | `deploynator/_mcp_server.py`, `deploynator/_semver.py`, `tests/bdd_test_deploy.py`, `tests/test_config.py`, `tests/test_pipeline.py` |
| `name` | 6 | 9 | `deploynator/_deploy.py`, `deploynator/_models.py`, `deploynator/_platforms.py`, `tests/test_deploy.py`, `tests/test_models.py` |
| `none` | 6 | 7 | `deploynator/_pypi.py`, `deploynator/_readme.py`, `deploynator/_toml.py`, `tests/test_models.py`, `tests/test_pypi.py` |
| `create` | 5 | 18 | `deploynator/_config.py`, `deploynator/_deploy.py`, `deploynator/_git.py`, `deploynator/_platforms.py`, `tests/bdd_test_deploy.py` |
| `type` | 5 | 14 | `deploynator/_models.py`, `tests/bdd_test_deploy.py`, `tests/test_changelog.py`, `tests/test_config.py`, `tests/test_models.py` |
| `cli` | 5 | 9 | `deploynator/_models.py`, `deploynator/_platforms.py`, `tests/test_cli_mcp.py`, `tests/test_install_example.py`, `tests/test_models.py` |
| `format` | 5 | 9 | `deploynator/_changelog.py`, `deploynator/_models.py`, `tests/bdd_test_deploy.py`, `tests/test_changelog.py`, `tests/test_models.py` |
| `empty` | 5 | 8 | `tests/test_changelog.py`, `tests/test_deploy.py`, `tests/test_install_example.py`, `tests/test_pypi.py`, `tests/test_runner.py` |
| `list` | 5 | 8 | `deploynator/_app.py`, `deploynator/_mcp_server.py`, `deploynator/_toml.py`, `tests/test_cli_mcp.py`, `tests/test_toml.py` |
| `default` | 5 | 7 | `deploynator/_app.py`, `deploynator/_toml.py`, `tests/test_config.py`, `tests/test_install_example.py`, `tests/test_pypi.py` |
| `failure` | 5 | 7 | `tests/bdd_test_deploy.py`, `tests/test_install_example.py`, `tests/test_pipeline.py`, `tests/test_pypi.py`, `tests/test_runner.py` |
| `dry` | 5 | 5 | `app.py`, `deploy.sh`, `deploynator/_mcp_server.py`, `tests/test_path_deploy.py`, `tests/test_pipeline.py` |
| `platform` | 4 | 13 | `deploynator/_models.py`, `deploynator/_platforms.py`, `tests/bdd_test_deploy.py`, `tests/test_models.py` |
| `pypi` | 4 | 12 | `deploynator/_pypi.py`, `deploynator/_toml.py`, `tests/test_pypi.py`, `tests/test_toml.py` |
| `runner` | 4 | 12 | `deploynator/_docs.py`, `deploynator/_runner.py`, `tests/test_pypi.py`, `tests/test_runner.py` |
| `line` | 4 | 11 | `deploynator/_models.py`, `deploynator/_readme.py`, `tests/test_models.py`, `tests/test_readme_footer.py` |
| `packaging` | 4 | 11 | `deploynator/_pypi.py`, `deploynator/_toml.py`, `tests/test_pypi.py`, `tests/test_toml.py` |
| `auth` | 4 | 10 | `deploynator/_app.py`, `deploynator/_models.py`, `tests/test_config.py`, `tests/test_models.py` |
| `generate` | 4 | 10 | `deploynator/_app.py`, `deploynator/_changelog.py`, `deploynator/_deploy.py`, `tests/test_changelog.py` |
| `changelog` | 4 | 9 | `deploynator/_changelog.py`, `deploynator/_models.py`, `tests/test_changelog.py`, `tests/test_models.py` |
| `returns` | 4 | 9 | `deploynator/_readme.py`, `tests/test_pypi.py`, `tests/test_runner.py`, `tests/test_toml.py` |
| `get` | 4 | 8 | `deploynator/_deploy.py`, `deploynator/_git.py`, `deploynator/_semver.py`, `tests/test_semver.py` |
| `max` | 4 | 8 | `deploynator/_semver.py`, `deploynator/_toml.py`, `tests/bdd_test_deploy.py`, `tests/test_pipeline.py` |
| `load` | 4 | 7 | `deploynator/_deploy.py`, `deploynator/_toml.py`, `tests/test_deploy.py`, `tests/test_toml.py` |
| `pipeline` | 4 | 7 | `deploynator/_mcp_server.py`, `tests/bdd_test_deploy.py`, `tests/test_pipeline.py`, `tests/test_pypi.py` |
| `repo` | 4 | 7 | `deploy.sh`, `deploynator/_deploy.py`, `deploynator/_mcp_server.py`, `deploynator/_readme.py` |
| `block` | 4 | 6 | `deploynator/_readme.py`, `tests/bdd_test_deploy.py`, `tests/test_pipeline.py`, `tests/test_readme_footer.py` |
| `log` | 4 | 6 | `deploynator/_changelog.py`, `deploynator/_git.py`, `deploynator/_models.py`, `tests/test_models.py` |
| `patch` | 4 | 6 | `deploy.sh`, `tests/bdd_test_deploy.py`, `tests/test_models.py`, `tests/test_semver.py` |
| `without` | 4 | 6 | `deploynator/_mcp_server.py`, `deploynator/_readme.py`, `tests/test_pypi.py`, `tests/test_readme_footer.py` |
| `all` | 4 | 4 | `deploynator/_git.py`, `deploynator/_mcp_server.py`, `deploynator/_platforms.py`, `tests/test_config.py` |

## Verb Edges

| Source | Verb | Target | Strength |
|--------|------|--------|----------|
| `release` | `depends_on` | `deploynator` | 1.00 |
| `project` | `depends_on` | `deploynator` | 0.95 |
| `deploy` | `depends_on` | `deploynator` | 0.90 |
| `deploynator` | `depends_on` | `config` | 0.83 |
| `run` | `depends_on` | `deploynator` | 0.74 |
| `git` | `depends_on` | `deploynator` | 0.62 |
| `deploynator` | `depends_on` | `create` | 0.60 |
| `install` | `depends_on` | `deploynator` | 0.60 |
| `docs` | `depends_on` | `deploynator` | 0.57 |
| `file` | `depends_on` | `deploynator` | 0.57 |
| `path` | `depends_on` | `deploynator` | 0.57 |
| `red` | `depends_on` | `deploynator` | 0.57 |
| `deploynator` | `depends_on` | `path` | 0.55 |
| `failure` | `depends_on` | `deploynator` | 0.52 |
| `generate` | `depends_on` | `deploynator` | 0.52 |
| `name` | `depends_on` | `deploynator` | 0.52 |
| `project` | `depends_on` | `config` | 0.52 |
| `deploynator` | `depends_on` | `project` | 0.50 |
| `release` | `depends_on` | `config` | 0.50 |
| `version` | `depends_on` | `deploynator` | 0.50 |
| `create` | `depends_on` | `deploynator` | 0.48 |
| `deploy` | `depends_on` | `config` | 0.48 |
| `run` | `depends_on` | `config` | 0.48 |
| `tag` | `depends_on` | `deploynator` | 0.48 |
| `toml` | `depends_on` | `deploynator` | 0.45 |
| `current` | `depends_on` | `deploynator` | 0.43 |
| `empty` | `depends_on` | `deploynator` | 0.43 |
| `semver` | `depends_on` | `deploynator` | 0.43 |
| `commit` | `depends_on` | `deploynator` | 0.40 |
| `get` | `depends_on` | `deploynator` | 0.40 |
| `pipeline` | `depends_on` | `deploynator` | 0.40 |
| `project` | `depends_on` | `create` | 0.40 |
| `bump` | `depends_on` | `deploynator` | 0.38 |
| `default` | `depends_on` | `deploynator` | 0.38 |
| `deploynator` | `depends_on` | `release` | 0.38 |
| `git` | `depends_on` | `config` | 0.38 |
| `load` | `depends_on` | `deploynator` | 0.38 |
| `release` | `depends_on` | `create` | 0.38 |
| `deploy` | `depends_on` | `create` | 0.36 |
| `deploy` | `depends_on` | `path` | 0.36 |
| `project` | `depends_on` | `release` | 0.36 |
| `release` | `depends_on` | `project` | 0.36 |
| `run` | `depends_on` | `path` | 0.36 |
| `deploy` | `depends_on` | `project` | 0.33 |
| `file` | `depends_on` | `config` | 0.33 |
| `git` | `depends_on` | `project` | 0.33 |
| `list` | `depends_on` | `deploynator` | 0.33 |
| `project` | `depends_on` | `name` | 0.33 |
| `project` | `depends_on` | `path` | 0.33 |
| `repo` | `depends_on` | `deploynator` | 0.33 |

## Dialectic Prompts

- Thesis: `all` centralizes 4 files; Antithesis: `commit` pulls 7 files with 3 shared (Jaccard 0.38); Synthesis: should they merge, split by layer, or keep `bridges` explicit?
- Thesis: `auth` centralizes 4 files; Antithesis: `changelog` pulls 4 files with 2 shared (Jaccard 0.33); Synthesis: should they merge, split by layer, or keep `bridges` explicit?
- Thesis: `auth` centralizes 4 files; Antithesis: `commit` pulls 7 files with 4 shared (Jaccard 0.57); Synthesis: should they merge, split by layer, or keep `bridges` explicit?
- Thesis: `auth` centralizes 4 files; Antithesis: `config` pulls 7 files with 3 shared (Jaccard 0.38); Synthesis: should they merge, split by layer, or keep `bridges` explicit?
- Thesis: `auth` centralizes 4 files; Antithesis: `line` pulls 4 files with 2 shared (Jaccard 0.33); Synthesis: should they merge, split by layer, or keep `bridges` explicit?
- Thesis: `auth` centralizes 4 files; Antithesis: `log` pulls 4 files with 2 shared (Jaccard 0.33); Synthesis: should they merge, split by layer, or keep `bridges` explicit?
- Thesis: `auth` centralizes 4 files; Antithesis: `platform` pulls 4 files with 2 shared (Jaccard 0.33); Synthesis: should they merge, split by layer, or keep `bridges` explicit?
- Thesis: `auth` centralizes 4 files; Antithesis: `type` pulls 5 files with 3 shared (Jaccard 0.50); Synthesis: should they merge, split by layer, or keep `bridges` explicit?
- Thesis: `auth` centralizes 4 files; Antithesis: `valid` pulls 7 files with 3 shared (Jaccard 0.38); Synthesis: should they merge, split by layer, or keep `bridges` explicit?
- Thesis: `block` centralizes 4 files; Antithesis: `current` pulls 7 files with 3 shared (Jaccard 0.38); Synthesis: should they merge, split by layer, or keep `bridges` explicit?
