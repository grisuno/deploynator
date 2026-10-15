# Project Memory

> Cross-session context for agents. Sections 1-6 are regenerated from the source tree with zero LLM tokens: declared rules are quoted verbatim with `file:line`, measured baselines come from the scan. Section 7 is written by agents and humans and is preserved across rebuilds.

Generated from 33 files at commit `72de9b538b7f`. Read this first, then `readmenator-wiki/index.md`, then `readmenator . ask "<question>"` for anything specific.

## 1. Purpose and domain

- What it is: Token-free, offline, multi-platform deployer for GitHub, GitLab, and Bitbucket. (`README.md:3`)
- Domain vocabulary (term, files): `deploynator` (22), `release` (12), `run` (11), `deploy` (10), `git` (10), `project` (10), `version` (7), `bump` (7), `commit` (7), `install` (7), `valid` (7), `red` (7), `docs` (6), `config` (6), `toml` (6)
- Subsystem `deploynator: _mcp_server`: 11 files, core `deploynator/_mcp_server.py`: MCP (Model Context Protocol) stdio server for deploynator.
- Subsystem `deploynator: _platforms`: 11 files, core `deploynator/_platforms.py`
- Subsystem `deploynator: _pypi`: 8 files, core `deploynator/_pypi.py`: prompt_for_credentials: Pide el token PyPI por input oculto solo si hay TTY.
- Business rules that the code cannot show live in section 7: record them there.

## 2. Workflow

Detected commands:
- `python -m pytest -q` (pyproject.toml)
- `deploynator --help` (pyproject.toml [project.scripts])
- `deploynator-mcp --help` (pyproject.toml [project.scripts])
- `CI workflow github-actions-demo.yml` (workflows/github-actions-demo.yml)

Session protocol:
1. Start: read this file, then `readmenator . fresh` (exit 1 means run `readmenator . --rebuild`).
2. Orient: `readmenator-wiki/index.md`; for a question use `readmenator . ask "<question>"` (local = entities + sources, `--global` = community reports).
3. Before editing a file: `grep -n '<file>' readmenator-agent/GOTCHAS.md readmenator-agent/SECURITY.md`.
4. After the change: run the tests above, then `readmenator . --rebuild` so the maps, wiki, and this file stay true.
5. End: record decisions, business rules, and gotchas with `readmenator . remember "<note>" --kind decision`.

## 3. Rules and constraints

Declared:
- All configuration in `Config` frozen dataclass (`CLAUDE.md:52`)
- No hardcoded strings, paths, or magic numbers (`CLAUDE.md:53`)
- Platform factory prevents client duplication (`CLAUDE.md:54`)
- **S**: Single responsibility per contract file (`CLAUDE.md:57`)
- **O**: PlatformFactory open for extension, closed for modification (`CLAUDE.md:58`)
- **L**: PlatformClient subtypes substitutable for base (`CLAUDE.md:59`)
- **I**: Platform interface minimal and focused (`CLAUDE.md:60`)
- **D**: DeployOrchestrator depends on abstractions, not concretions (`CLAUDE.md:61`)
- No absolute paths from developer system (`CLAUDE.md:64`)
- Token environment variables (GITHUB_TOKEN, GITLAB_TOKEN, BITCOIN_TOKEN) (`CLAUDE.md:65`)
- GPG support with graceful fallback (`CLAUDE.md:66`)
- Dry-run mode prevents accidental mutations (`CLAUDE.md:67`)
- Commands use subprocess with shell=False (`CLAUDE.md:68`)
- Removed shell injection vectors (shell=True, string formatting in subprocess) (`CLAUDE.md:94`)
- Replaced hardcoded paths with Config-based resolution (`CLAUDE.md:95`)
- Removed TODO markers, replaced with proper error handling (`CLAUDE.md:96`)
- Standardized on frozen dataclasses for all models (`CLAUDE.md:97`)
- GPG detection with graceful degradation (`CLAUDE.md:98`)
- Replaced hardcoded `/tmp/` paths with `tempfile.NamedTemporaryFile` (TOCTOU fix) (`CLAUDE.md:99`)
- Single-commit release flow (removed double-commit bug) (`CLAUDE.md:100`)
- Removed `sudo apt install` from application code (`CLAUDE.md:101`)
- Added `os.path.islink()` rejection before all file writes (`CLAUDE.md:102`)
- Added `max_file_size_bytes` enforcement in project discovery (`CLAUDE.md:103`)
- Sanitized branch descriptions to prevent git injection (`CLAUDE.md:104`)

Measured baseline:
- Security findings at medium or above: 0 (see `readmenator-agent/SECURITY.md`); do not add new ones.
- Dependency cycles: 0; layer violations: 0 (see `readmenator-agent/GOTCHAS.md`).

## 4. Style norms

Declared:
- none declared in instruction files (add them to AGENTS.md or record them in section 7)

Measured baseline:
- py: 31 files, 403 symbols; docstrings on 3% of symbols; functions snake_case (100%); types PascalCase (100%); median file 109 lines, max 685.
- sh: 2 files, 1 symbols; docstrings on 100% of symbols; functions snake_case (100%); median file 42 lines, max 42.
- Tests: 15 files under tests; follow the existing naming (e.g. `bdd_test_deploy.py`).

## 5. Minimum deliverables

Declared:
- none declared in instruction files (add them to AGENTS.md or record them in section 7)

Measured baseline:
- Tests pass: `python -m pytest -q`.
- Docstring coverage stays at or above 3%.
- No new security findings at medium or above (current: 0).
- No new dependency cycles (current: 0).
- Files stay under 300 lines where possible (`readmenator . lint`).
- Docs refreshed: `readmenator . --rebuild`, and decisions recorded in section 7.

## 6. Risks to respect

- God nodes (changes ripple widely): `deploynator/_config.py`, `deploynator/_deploy.py`, `deploynator/_models.py`, `deploynator/_toml.py`, `deploynator/_app.py`
- Hotspots (complex and central): `tests/test_pypi.py`, `deploynator/_app.py`, `tests/test_runner.py`, `deploynator/_config.py`, `deploynator/_deploy.py`
- Full blast radius: `readmenator-agent/GOTCHAS.md`; findings: `readmenator-agent/SECURITY.md`.

## 7. Session log (preserved across rebuilds)

Append with `readmenator . remember "<note>" --kind <kind>` (kinds: business, decision, rule, workflow, style, deliverable, gotcha, todo, note) or the MCP tool `readmenator.remember`. Record business rules, decisions and their reasons, workflow changes, and anything the next session must not rediscover.

<!-- readmenator:memory:notes:begin -->
<!-- readmenator:memory:notes:end -->
