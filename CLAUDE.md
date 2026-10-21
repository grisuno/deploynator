# deploynator -- Contract Documentation

## Project Overview

Multi-platform deployer for GitHub, GitLab, and Bitbucket.
Single codebase, YAML-driven project discovery, conventional commits,
automatic semver, changelog generation, and release automation.

Source: https://github.com/grisuno/deploynator

## Directory Layout

```
deployer/
├── deploynator/           # Python package (the tool)
├── deploynator_repos/     # Local clones of managed repos
│   ├── LazyOwn/           # grisuno/LazyOwn
│   └── deploynator/       # grisuno/deploynator (self-deploy)
├── projects/              # YAML configs
│   ├── deploynator.yaml   # Self-deployment
│   ├── lazyown.yaml
│   └── template.yaml
├── SKILL.md               # AI agent integration
├── CLAUDE.md              # Contract docs
└── README.md
```

## Contract Architecture (SDD)

Each file is a single contract with strict separation of concerns:

| File | Contract | Pattern |
|------|----------|---------|
| `deploynator/_config.py` | Config contract | Frozen dataclass, centralized constants |
| `deploynator/_models.py` | Model contract | Data types, enums, DTOs |
| `deploynator/_toml.py` | TOML contract | Per-project deploynator.toml, defaults, validation |
| `deploynator/_runner.py` | Test contract | shlex+shell=False, timeout, ordered commands |
| `deploynator/_docs.py` | Docs contract | readmenator . --rebuild, non-blocking |
| `deploynator/_pypi.py` | PyPI contract | detect packaging, clean dist/, build, twine |
| `deploynator/_mcp_server.py` | MCP contract | stdio JSON-RPC, tools+resources, headless |
| `deploynator/_platforms.py` | Platform contract | Strategy pattern, ABC |
| `deploynator/_git.py` | Git contract | Subprocess wrapper, git operations |
| `deploynator/_changelog.py` | Changelog contract | Log parsing, formatting |
| `deploynator/_semver.py` | Semver contract | Version parsing and bumping |
| `deploynator/_deploy.py` | Deploy contract | Orchestration, project discovery |
| `deploynator/_receipt.py` | Receipt contract | Operational trace per release: steps, subprocess commands, evidence edges. Fact=observed, candidate=feasible set, predicted=model (never fact) |
| `deploynator/_app.py` | App contract | High-level API, interactive menu |
| `deploynator/__main__.py` | CLI contract | Argument parsing, dispatch |

## Design Principles

### DRY (Don't Repeat Yourself)
- All configuration in `Config` frozen dataclass
- No hardcoded strings, paths, or magic numbers
- Platform factory prevents client duplication

### SOLID
- **S**: Single responsibility per contract file
- **O**: PlatformFactory open for extension, closed for modification
- **L**: PlatformClient subtypes substitutable for base
- **I**: Platform interface minimal and focused
- **D**: DeployOrchestrator depends on abstractions, not concretions

### Security
- No absolute paths from developer system
- Token environment variables (GITHUB_TOKEN, GITLAB_TOKEN, BITCOIN_TOKEN)
- GPG support with graceful fallback
- Dry-run mode prevents accidental mutations
- Commands use subprocess with shell=False

### Production Quality
- Type hints throughout
- Frozen dataclasses for immutability
- All exceptions caught at boundaries
- No placeholders or TODOs
- Comprehensive test coverage (unit + BDD)

## Methodology

### SDD (Specification-Driven Development)
Each contract has a clear specification file.
Config, Models, Platform, Git, Changelog, Semver, Deploy, App, CLI.

### TDD (Test-Driven Development)
Tests written before or alongside code.
All public methods have corresponding tests.

### BDD (Behavior-Driven Development)
`tests/bdd_test_deploy.py` contains user-story scenarios.
Given/When/Then structure for version bumping and commit parsing.

### Boy Scout Rule
Leave code cleaner than found. All tech debt and security issues
found during development were fixed immediately:
- Removed shell injection vectors (shell=True, string formatting in subprocess)
- Replaced hardcoded paths with Config-based resolution
- Removed TODO markers, replaced with proper error handling
- Standardized on frozen dataclasses for all models
- GPG detection with graceful degradation
- Replaced hardcoded `/tmp/` paths with `tempfile.NamedTemporaryFile` (TOCTOU fix)
- Single-commit release flow (removed double-commit bug)
- Removed `sudo apt install` from application code
- Added `os.path.islink()` rejection before all file writes
- Added `max_file_size_bytes` enforcement in project discovery
- Sanitized branch descriptions to prevent git injection

## Testing

```bash
# Run all tests
python -m pytest tests/

# With coverage
python -m pytest tests/ --cov=deploynator --cov-report=term-missing

# Run specific test
python -m pytest tests/test_models.py -v
```

## Self-Deployment

deploynator can deploy itself. The `projects/deploynator.yaml` config points to
`deploynator_repos/deploynator/` (the local clone of the GitHub repo).

```bash
# Deploy deploynator itself
deploynator release --type release --project deploynator

# Preview the release
deploynator release --type release --project deploynator --dry-run

# Generate docs for deploynator
deploynator docs
```

## CLI Reference

```bash
deploynator --help
deploynator                         # bare = interactive (no flags)
deploynator interactive             # explicit interactive (no flags)
deploynator serve [path]            # MCP stdio server (agent harnesses)
deploynator release --type <type> --project <name> [--bump major|minor|patch] [--no-test] [--no-docs] [--dry-run] [--platforms ...] [--receipt [path]] [--trace]
deploynator commit --type <type> --subject <msg> [--scope <s>] [--body <b>]
deploynator start --type <type> --desc <desc> [--remote]
deploynator auth login [--platforms github gitlab bitbucket]
deploynator auth status
deploynator docs
deploynator init [--name <name>]
deploynator status
deploynator workflow [--project <name>] [--all]
deploynator install [packages...]      # pip install from PyPI (default: deploynator)
deploynator install --project <name>  # legacy: check platform CLI availability
deploynator interactive
```

## Integration Points

### ReadMenator
deploynator docs -> pip install readmenator -> python -m readmenator .

### lazygit
Configured via git config deploynator.lazygit.enabled
Install package via: deploynator install  (pip install deploynator from PyPI)

### CI/CD
deploynator workflow --all creates:
- .github/workflows/deploynator-ci.yml
- .github/workflows/deploynator-release.yml

## Security Report

All subprocess calls use list-based commands (no shell=True).
Environment variables used for tokens, never CLI arguments.
File operations bounded by max_file_size_bytes (10MB) and max_dir_depth (20).
Symlinks rejected by GitOperations layer.
All exceptions caught at contract boundaries.

## Release Receipts (evidence hierarchy)

Every `deploynator release` can write a receipt JSON documenting the
release as evidence, not prose:

```bash
deploynator release --type release --project deploynator --receipt [path]
deploynator release --dry-run --trace            # feasible plan receipt
```

Golden rule: `Fact = observed step (exit_code)`, `Candidate = feasible
set from config/CLI/interface`, `Predicted = model, always labeled`.
A prediction is never presented as fact.

Receipt fields: schema `deploynator/receipt@v1`, mode (`run`/`plan`),
status (`success`/`partial`/`failed`), version_from → version_to, tag,
commit, branch, flags, platforms (enabled/disabled + pushed/released),
steps (logical stage results), commands (every subprocess captured via
a `subprocess.run` wrapper, with argv, exit_code, output tails, stage
label) and edges `(caller, callee, kind, evidence, confidence,
provenance)`.

Handled automatically:
- Written on ALL deploy exits (early returns included): status is
  `failed`/`partial` when the flow stops mid-way.
- Default target `<cwd>/release-receipts/`; token env values
  (GITHUB_TOKEN, GITLAB_TOKEN, BITBUCKET_TOKEN, TWINE...) are redacted
  from tails.
- `--dry-run --trace` adds candidate edges from `build_plan` (feasible
  set honoring `--platforms`, TOML config and the Platform interface),
  never claiming execution.

ReadMenator consumes receipts:
```bash
readmenator . receipts [dir]    # RELEASES.md + release-edges.json
```
 reconciliation of observed vs candidate, uncertainty predictions
(`readmenator/_uncertainty.py`, heuristic + optional sklearn random
forest) and hypothesis validation (`readmenator/_hypotheses.py`,
LLM/agent proposals constrained by the symbol index).

<!-- readmenator-agent-kb-link -->
## Project Knowledge Base (MUST read before coding)

Generated offline by [ReadMenator](https://github.com/grisuno/ReadMenator) (zero-token static analysis). Humans: `KNOWLEDGE_BASE.md`.

0. Memory: `cat readmenator-agent/MEMORY.md` (business rules, workflow, constraints, style, done criteria, session log). Record new decisions with `readmenator . remember "<note>" --kind decision`.
1. Freshness: `readmenator . fresh` (exit 1 means stale: run `readmenator . --rebuild`). Without the CLI, compare `git_commit` in `readmenator-agent/MANIFEST.json` with `git log -1`.
2. Orient: `ls *.md readmenator-agent/ readmenator-wiki/`, then read `readmenator-wiki/index.md` (big picture, communities, god nodes).
3. Locate: `grep -n '<keyword>' readmenator-agent/INDEX*.md readmenator-agent/SYMBOLS*.md` before any `glob` over sources; for questions use `readmenator . ask "<question>"` (GraphRAG, `--global` for overviews).
4. Context: `cat readmenator-agent/KB_<subsystem>.md` for the subsystem you touch.
5. Before editing: `grep -n '<file>' readmenator-agent/GOTCHAS.md readmenator-agent/SECURITY.md` (blast radius, cycles, findings).

Also: `API*.md` (public functions, one line each), `ARCHITECTURE*.md` (dependency pairs), `recipes/*.md` (grounded task steps). Large docs are paged as `NAME_p2.md`, so always grep with `NAME*.md`.

    pip install readmenator && readmenator . --rebuild
<!-- /readmenator-agent-kb-link -->
