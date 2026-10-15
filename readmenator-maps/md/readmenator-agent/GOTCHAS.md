# Gotchas

## God Nodes (high connectivity)

These files have the most connections. Changes here have high blast radius.

- `deploynator/_config.py` (score: 44.60, imported by 22 files)
- `deploynator/_deploy.py` (score: 33.90, imported by 6 files)
- `deploynator/_models.py` (score: 30.70, imported by 14 files)
- `deploynator/_toml.py` (score: 20.40, imported by 9 files)
- `deploynator/_app.py` (score: 17.00, imported by 1 files)
- `deploynator/_semver.py` (score: 14.90, imported by 5 files)
- `deploynator/_platforms.py` (score: 11.40, imported by 2 files)
- `deploynator/_mcp_server.py` (score: 11.20, imported by 2 files)

## Blast Radius (change impact)

Editing these files can break the listed number of dependents. Run their tests after any change.

- `deploynator/_config.py` -- 22 direct, 24 total dependents
- `deploynator/_models.py` -- 14 direct, 17 total dependents
- `deploynator/_toml.py` -- 9 direct, 16 total dependents
- `deploynator/_changelog.py` -- 2 direct, 12 total dependents
- `deploynator/_docs.py` -- 3 direct, 12 total dependents
- `deploynator/_runner.py` -- 2 direct, 12 total dependents
- `deploynator/_semver.py` -- 5 direct, 12 total dependents
- `deploynator/_git.py` -- 2 direct, 11 total dependents
- `deploynator/_platforms.py` -- 2 direct, 11 total dependents
- `deploynator/_pypi.py` -- 2 direct, 11 total dependents

## Hotspots (complexity + centrality)

- `deploynator/_app.py` -- complexity: 0.7, centrality: 0.4, combined: 0.5
- `deploynator/_deploy.py` -- complexity: 0.4, centrality: 0.5, combined: 0.5
- `deploynator/_models.py` -- complexity: 0.6, centrality: 0.4, combined: 0.5
- `deploynator/_config.py` -- complexity: 0.1, centrality: 0.7, combined: 0.5
- `deploynator/_platforms.py` -- complexity: 0.8, centrality: 0.2, combined: 0.4
- `deploynator/_mcp_server.py` -- complexity: 0.7, centrality: 0.2, combined: 0.4
- `deploynator/_pypi.py` -- complexity: 0.2, centrality: 0.3, combined: 0.3
- `deploynator/_git.py` -- complexity: 0.5, centrality: 0.1, combined: 0.3
- `deploynator/_semver.py` -- complexity: 0.2, centrality: 0.2, combined: 0.2
- `deploynator/_toml.py` -- complexity: 0.1, centrality: 0.3, combined: 0.2
