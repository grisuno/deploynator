# `deploy.sh`

> Source: [deploy.sh:1](../../deploy.sh#L1) | language `sh` | coverage 100.0% | [API index](../index.md)

deploy.sh -- one-liner deploy via deploynator (generic per-repo script).

Deployed by deploynator: detects its own directory, ensures tooling, then releases this repo. Usage: ./deploy.sh                    # patch release (smallest bump) ./deploy.sh feat --dry-run     # preview a minor release ./deploy.sh fix --no-test      # patch release skipping tests
