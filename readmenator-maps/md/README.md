# deploynator

Token-free, offline, multi-platform deployer for GitHub, GitLab, and Bitbucket.

**No cloud costs. No vendor lock-in. One codebase, three platforms.**

A production-grade CLI that unifies deployment across the holy trinity of git platforms using a single YAML-driven configuration.

```bash
pip install .
deploynator release --type feat --project my-app
```

## Features

| Feature | Description |
|---------|-------------|
| Multi-platform | GitHub (gh), GitLab (glab), Bitbucket (bb) |
| Project discovery | YAML-based project configs in `projects/` dir |
| Conventional commits | feat, fix, hotfix, docs, refactor, style, chore, test, release, patch |
| Semver management | Automatic version bumping per commit type |
| Changelog generation | Auto-generated from git log, organized by type |
| Release automation | Tag, push, and create releases on all platforms |
| Documentation | ReadMenator integration for knowledge base generation |
| CI/CD workflows | Auto-generate `.github/workflows/deploynator-*.yml` |
| Interactive mode | Terminal menu for guided operations |
| Headless mode | Full flag-based CLI for scripting and automation |
| Dry-run mode | Simulate without making changes |
| GPG support | Automatic GPG signing detection and usage |
| lazygit integration | Optional native lazygit hooks |
| Backward compatible | Wraps original DEPLOY.sh workflow |

## Architecture

| Contract | File | Responsibility |
|----------|------|----------------|
| Config | `_config.py` | Immutable centralized configuration |
| Models | `_models.py` | Types: Platform, CommitType, VersionInfo, ProjectConfig |
| Platform | `_platforms.py` | GitHubCLI, GitLabCLI, BitbucketCLI (Strategy pattern) |
| Git | `_git.py` | Git operations (commit, tag, push, branch) |
| Changelog | `_changelog.py` | Changelog generation and formatting |
| Semver | `_semver.py` | Semantic version management |
| Deploy | `_deploy.py` | Deploy orchestration + project discovery |
| App | `_app.py` | Application orchestrator + interactive menu |
| CLI | `__main__.py` | Entry point and argument dispatch |

## Installation

```bash
# From PyPI
pip install deploynator

# From source
git clone https://github.com/grisuno/deploynator.git
cd deploynator
pip install .

# Install with dev dependencies (tests + ReadMenator)
pip install -e ".[dev]"
```

## Usage

### Programmatic use (library)

```python
from deploynator import DeploynatorApp
from deploynator._config import Config

app = DeploynatorApp(Config.create())
app.status()
app.release(commit_type="feat", subject="add login", dry_run=True)
```

See `app.py` for a runnable example.

### Initialize a project

```bash
deploynator init
# Creates deploynator.yaml in current directory
```

### Authenticate with platforms

```bash
deploynator auth login --platforms github gitlab
deploynator auth status
```

### Start a feature branch

```bash
deploynator start --type feat --desc add-login
deploynator start --type fix --desc timeout-issue --remote
```

### Make a conventional commit

```bash
deploynator commit --type feat --subject "add OAuth login" --scope auth
deploynator commit --type fix --subject "fix timeout" --body "Increased timeout to 30s" --dry-run
```

### Create a release

```bash
# Auto-bump based on commit type
deploynator release --type feat --project my-app --all

# Specify version bump explicitly
deploynator release --type release --bump major --project my-app

# Skip tests (like DEPLOY.sh --no-test) or docs
deploynator release --type feat --project my-app --no-test --no-docs

# Dry run to preview
deploynator release --type feat --project my-app --dry-run

# Deploy to specific platforms
deploynator release --type fix --project my-app --platforms github gitlab

# Deploy all discovered projects
deploynator release --type feat --all
```

### Generate documentation

```bash
deploynator docs
# Runs ReadMenator to generate KNOWLEDGE_BASE.md with Mermaid graph
```

### Generate CI/CD workflows

```bash
deploynator workflow --all
# Creates .github/workflows/deploynator-ci.yml and deploynator-release.yml
```

### Check status

```bash
deploynator status
```

### Interactive mode

```bash
deploynator interactive
```

## Repository Structure

```
deployer/
├── deploynator/           # Tool package (9 contracts)
├── deploynator_repos/     # Local clones of managed repos
│   ├── LazyOwn/           # github.com/grisuno/LazyOwn
│   └── deploynator/       # github.com/grisuno/deploynator (self)
├── projects/              # YAML project definitions
│   ├── deploynator.yaml   # Self-deployment config
│   ├── lazyown.yaml       # LazyOwn deployment config
│   └── template.yaml      # Template for new projects
├── SKILL.md               # AI agent integration guide
├── CLAUDE.md              # Contract documentation
└── README.md              # This file
```

## Project Configuration

Place YAML files in `projects/` directory. Each file defines a deployable project:

```yaml
# projects/my-app.yaml
version: 1.0
name: my-app
description: "My awesome application"
repo_url: "https://github.com/username/my-app"
path: "deploynator_repos/my-app"       # Local clone path (relative to deployer root)
platforms:
  github:
    repo: "username/my-app"
    enabled: true
  gitlab:
    repo: "group/my-app"
    enabled: true
  bitbucket:
    repo: "workspace/my-app"
    enabled: false
version:
  file: version.json
  file_type: json
```

## Requirements

| Tool | Purpose | Required |
|------|---------|----------|
| git | Version control | Yes |
| gh | GitHub CLI | For GitHub releases |
| glab | GitLab CLI | For GitLab releases |
| bb | Bitbucket CLI | For Bitbucket releases |
| jq | JSON processing | Optional |
| pandoc | HTML generation | Optional |
| readmenator | Knowledge base | Optional (pip) |
| lazygit | Interactive TUI | Optional |

## Changelog

See [CHANGELOG.md](CHANGELOG.md) for release history.

## License

AGPL-3.0

<!-- deploynator-footer -->

---

Deployed with [deploynator](https://github.com/grisuno/deploynator)

<!-- /deploynator-footer -->

<!-- readmenator-kb-link -->
## Knowledge Base

This project has been analyzed by [ReadMenator](https://github.com/grisuno/ReadMenator),
a zero-token polyglot static analysis tool. Regenerate with
`pip install readmenator && readmenator . --rebuild`. Analysis outputs:

- **[KNOWLEDGE_BASE.md](./KNOWLEDGE_BASE.md)** -- Full architecture reference with all
  classes, functions, imports, dependency graphs, UML class diagrams, security
  audit findings, community analysis, taint paths, hotspots, cycles, and more.
- **[readmenator-agent/](./readmenator-agent/)** -- Agent-friendly, grep-optimized index.
  - `INDEX.md` -- Quick reference: what each file does
  - `SYMBOLS.md` -- Every symbol with file:line
  - `ARCHITECTURE.md` -- Internal dependency pairs + external imports
  - `API.md` -- Public function contracts
  - `GOTCHAS.md` -- Change warnings (blast radius, cycles, hotspots)
  - `SECURITY.md` -- Findings by severity with fix hints
  - `MEMORY.md` -- Rules, workflow, style, deliverables, session log
  - `MANIFEST.json` -- Freshness (git_commit + source_fingerprint) + read order
  - `KB_<subsystem>.md` -- Per-subsystem context
  - `recipes/*.md` -- Grounded task guides (add-function, fix-cycle, ...)
- **[readmenator-wiki/](./readmenator-wiki/)** -- Navigable wiki (start here for the big picture).
  - `index.md` -- Entry point: overview, reading order, god nodes, connections
  - `community_*.md` -- One synthesis page per code community
  - `connections.json` -- Typed bridges between communities
  - `queries.md` -- Suggested questions + answer log
  - `REPORT.md` -- Honest audit: coverage, confidence, limits
- **[readmenator-graphrag/](./readmenator-graphrag/)** -- Zero-token GraphRAG index.
  - `index.json` + `REPORTS.md` -- Query with `readmenator . ask "<question>"`
- **[readmenator-apidocs/](./readmenator-apidocs/)** -- API reference (Sphinx/Doxygen style).
  - `index.md` + `modules/*.md` -- Signatures, parameters, returns, raises, examples, call graphs
  - `architecture.md` -- Tiered architecture + execution flows (control flow, call tree, sequence)
  - `classes.md`, `genindex.md`, `COVERAGE.md` -- Hierarchy, A-Z index, doc coverage + warnings
  - `index.html` + `api/` -- Offline searchable browser and machine-readable model (`api/index.json`, `api/modules/*.jsonl` one entity per line)
- **[readmenator-maps/](./readmenator-maps/)** -- Interactive gallery (`index.html`).
  - 5 system maps: architecture, workflow, sequence, dataflow, lifecycle
  - `graph-force.html` -- Force-graph explorer (2D/3D, reach, paths, lenses)
  - `graph-bundle.html` -- Edge bundle explorer (circle + sphere)
  - `components.html` -- Component diagrams
- **[docs/](./docs/)** -- Static site (GitHub Pages ready).
  - Gallery copy + `llms.txt` (agent entry point) + `md/` docs + video
- **[readmenator-diagrams/](./readmenator-diagrams/)** -- Component diagrams.
  - `analysis.json` + `graph LR` markdown + per-component pages + `index.html`
- **[readmenator-rules/](./readmenator-rules/)** -- Suggested Semgrep rules (`*.yml`),
  `yara_rules.yar` (YARA-lite) + `exclusions.yaml` (false-positive blocklist)
- **[readmenator.mp4](./readmenator.mp4)** -- Cinematic synthwave overview video
- **[.cursorrules](./.cursorrules)** -- Generated AI assistant rules
- **[readmenator_audit.sarif](./readmenator_audit.sarif)** -- SARIF v2.1.0 audit (when security scan is on)

Cache (`.readmenator_cache/`), packaged agent skills (`.claude/skills/`), and the
GitHub wiki mirror are also produced on `run`/`--rebuild`.

AI agents: Read `readmenator-wiki/index.md` first for the big picture, then `readmenator-agent/INDEX.md` for grep-friendly lookup.
Developers: Read `KNOWLEDGE_BASE.md` for full architecture reference, open `readmenator-maps/index.html` for the visual gallery.
<!-- /readmenator-kb-link -->

