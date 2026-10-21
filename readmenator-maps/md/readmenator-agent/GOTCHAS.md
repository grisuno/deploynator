# Gotchas

## God Nodes (high connectivity)

These files have the most connections. Changes here have high blast radius.

- `deploynator/_config.py` (score: 64.60, imported by 32 files)
- `deploynator/_deploy.py` (score: 46.30, imported by 9 files)
- `deploynator/_models.py` (score: 32.70, imported by 15 files)
- `deploynator/_toml.py` (score: 29.00, imported by 13 files)
- `deploynator/_app.py` (score: 17.30, imported by 1 files)
- `deploynator/__init__.py` (score: 16.00, imported by 7 files)
- `deploynator/_semver.py` (score: 14.90, imported by 5 files)

## Blast Radius (change impact)

Editing these files can break the listed number of dependents. Run their tests after any change.

- `deploynator/_config.py` -- 32 direct, 34 total dependents
- `deploynator/_models.py` -- 15 direct, 23 total dependents
- `deploynator/_toml.py` -- 13 direct, 23 total dependents
- `deploynator/_changelog.py` -- 2 direct, 18 total dependents
- `deploynator/_docs.py` -- 3 direct, 18 total dependents
- `deploynator/_readme.py` -- 2 direct, 18 total dependents
- `deploynator/_runner.py` -- 2 direct, 18 total dependents
- `deploynator/_semver.py` -- 5 direct, 18 total dependents
- `deploynator/_deb.py` -- 2 direct, 17 total dependents
- `deploynator/_git.py` -- 3 direct, 17 total dependents

## Hotspots (complexity + centrality)

- `deploynator/_config.py` -- complexity: 0.1, centrality: 1.0, combined: 0.6
- `deploynator/_app.py` -- complexity: 0.7, centrality: 0.5, combined: 0.6
- `deploynator/_deploy.py` -- complexity: 0.5, centrality: 0.6, combined: 0.5
- `deploynator/_receipt.py` -- complexity: 0.9, centrality: 0.2, combined: 0.5
- `deploynator/_models.py` -- complexity: 0.6, centrality: 0.4, combined: 0.4
- `deploynator/_toml.py` -- complexity: 0.2, centrality: 0.5, combined: 0.4
- `deploynator/_platforms.py` -- complexity: 0.8, centrality: 0.1, combined: 0.4
- `deploynator/_mcp_server.py` -- complexity: 0.7, centrality: 0.2, combined: 0.4
- `deploynator/_git.py` -- complexity: 0.5, centrality: 0.1, combined: 0.3
- `deploynator/_pypi.py` -- complexity: 0.2, centrality: 0.3, combined: 0.3
