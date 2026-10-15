#!/bin/bash
# deploy.sh -- one-liner deploy via deploynator (generic per-repo script).
# Deployed by deploynator: detects its own directory, ensures tooling,
# then releases this repo. Usage:
#   ./deploy.sh                    # patch release (smallest bump)
#   ./deploy.sh feat --dry-run     # preview a minor release
#   ./deploy.sh fix --no-test      # patch release skipping tests
set -euo pipefail

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TYPE="patch"
if [ $# -gt 0 ]; then
    TYPE="$1"
    shift
fi

# Install or update deploy tooling (best effort: works offline with current versions).
pip install -U deploynator 2>/dev/null \
    || pip install -U "git+https://github.com/grisuno/deploynator.git" \
    || true
pip install -U readmenator 2>/dev/null || true

if ! python3 -c "import deploynator" 2>/dev/null; then
    echo "[!] deploynator not available and install failed (offline?)." >&2
    exit 1
fi

exec python3 -m deploynator release --type "$TYPE" --project "$DIR" "$@"
