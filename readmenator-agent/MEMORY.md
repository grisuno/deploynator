# Project Memory

> Cross-session context for agents. Sections 1-6 are regenerated from the source tree with zero LLM tokens: declared rules are quoted verbatim with `file:line`, measured baselines come from the scan. Section 7 is written by agents and humans and is preserved across rebuilds.

Generated from 40 files at commit `e63143b99ea4`. Read this first, then `readmenator-wiki/index.md`, then `readmenator . ask "<question>"` for anything specific.

## 1. Purpose and domain

- What it is: Token-free, offline, multi-platform deployer for GitHub, GitLab, and Bitbucket. (`README.md:3`)
- Domain vocabulary (term, files): `deploynator` (25), `run` (16), `deploy` (15), `release` (14), `project` (14), `git` (13), `config` (10), `tag` (9), `default` (9), `current` (9), `toml` (8), `commit` (8), `path` (8), `failure` (8), `repo` (8)
- Subsystem `deploynator: _toml`: 10 files, core `deploynator/_toml.py`: list_make_targets: Lee el Makefile y devuelve sus targets sin ejecutar nada.
- Subsystem `deploynator: _mcp_server`: 7 files, core `deploynator/_mcp_server.py`: MCP (Model Context Protocol) stdio server for deploynator.
- Subsystem `deploynator: _receipt`: 7 files, core `deploynator/_receipt.py`: Receipt contract: operational trace of a deploynator release.
- Subsystem `deploynator: _models`: 7 files, core `deploynator/_models.py`
- Subsystem `deploynator: _changelog`: 6 files, core `deploynator/_changelog.py`
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
- All configuration in `Config` frozen dataclass (`CLAUDE.md:53`)
- No hardcoded strings, paths, or magic numbers (`CLAUDE.md:54`)
- Platform factory prevents client duplication (`CLAUDE.md:55`)
- **S**: Single responsibility per contract file (`CLAUDE.md:58`)
- **O**: PlatformFactory open for extension, closed for modification (`CLAUDE.md:59`)
- **L**: PlatformClient subtypes substitutable for base (`CLAUDE.md:60`)
- **I**: Platform interface minimal and focused (`CLAUDE.md:61`)
- **D**: DeployOrchestrator depends on abstractions, not concretions (`CLAUDE.md:62`)
- No absolute paths from developer system (`CLAUDE.md:65`)
- Token environment variables (GITHUB_TOKEN, GITLAB_TOKEN, BITCOIN_TOKEN) (`CLAUDE.md:66`)
- GPG support with graceful fallback (`CLAUDE.md:67`)
- Dry-run mode prevents accidental mutations (`CLAUDE.md:68`)
- Commands use subprocess with shell=False (`CLAUDE.md:69`)
- Removed shell injection vectors (shell=True, string formatting in subprocess) (`CLAUDE.md:95`)
- Replaced hardcoded paths with Config-based resolution (`CLAUDE.md:96`)
- Removed TODO markers, replaced with proper error handling (`CLAUDE.md:97`)
- Standardized on frozen dataclasses for all models (`CLAUDE.md:98`)
- GPG detection with graceful degradation (`CLAUDE.md:99`)
- Replaced hardcoded `/tmp/` paths with `tempfile.NamedTemporaryFile` (TOCTOU fix) (`CLAUDE.md:100`)
- Single-commit release flow (removed double-commit bug) (`CLAUDE.md:101`)
- Removed `sudo apt install` from application code (`CLAUDE.md:102`)
- Added `os.path.islink()` rejection before all file writes (`CLAUDE.md:103`)
- Added `max_file_size_bytes` enforcement in project discovery (`CLAUDE.md:104`)
- Sanitized branch descriptions to prevent git injection (`CLAUDE.md:105`)

Measured baseline:
- Security findings at medium or above: 0 (see `readmenator-agent/SECURITY.md`); do not add new ones.
- Dependency cycles: 0; layer violations: 0 (see `readmenator-agent/GOTCHAS.md`).

## 4. Style norms

Declared:
- none declared in instruction files (add them to AGENTS.md or record them in section 7)

Measured baseline:
- py: 38 files, 580 symbols; docstrings on 8% of symbols; functions snake_case (100%); types PascalCase (100%); median file 158 lines, max 849.
- sh: 2 files, 1 symbols; docstrings on 100% of symbols; functions snake_case (100%); median file 44 lines, max 44.
- Tests: 19 files under tests; follow the existing naming (e.g. `bdd_test_deploy.py`).

## 5. Minimum deliverables

Declared:
- Written on ALL deploy exits (early returns included): status is (`CLAUDE.md:202`)
- Default target `<cwd>/release-receipts/`; token env values (`CLAUDE.md:204`)
- `--dry-run --trace` adds candidate edges from `build_plan` (feasible (`CLAUDE.md:207`)

Measured baseline:
- Tests pass: `python -m pytest -q`.
- Docstring coverage stays at or above 8%.
- No new security findings at medium or above (current: 0).
- No new dependency cycles (current: 0).
- Files stay under 300 lines where possible (`readmenator . lint`).
- Docs refreshed: `readmenator . --rebuild`, and decisions recorded in section 7.

## 6. Risks to respect

- God nodes (changes ripple widely): `deploynator/_config.py`, `deploynator/_deploy.py`, `deploynator/_models.py`, `deploynator/_toml.py`, `deploynator/_app.py`
- Hotspots (complex and central): `tests/test_pypi.py`, `tests/test_deb.py`, `deploynator/_config.py`, `tests/test_runner.py`, `deploynator/_app.py`
- Full blast radius: `readmenator-agent/GOTCHAS.md`; findings: `readmenator-agent/SECURITY.md`.

## 7. Session log (preserved across rebuilds)

Append with `readmenator . remember "<note>" --kind <kind>` (kinds: business, decision, rule, workflow, style, deliverable, gotcha, todo, note) or the MCP tool `readmenator.remember`. Record business rules, decisions and their reasons, workflow changes, and anything the next session must not rediscover.

<!-- readmenator:memory:notes:begin -->
- 2026-10-21 [decision] Added _receipt.py contract: release receipts (schema deploynator/receipt@v1) written on ALL deploy exits via ReceiptCollector + subprocess.run capture wrapper; --receipt [path] and --trace (feasible plan w/ candidate edges) flags added to release CLI/MCP. Evidence rule: observed=fact, candidate=feasible, predicted=model.
- 2026-10-21 [decision] E2E receipts validated: real releases (ReadMenator 1.7.0, deploynator 1.4.0) each wrote receipts and both repos ingested them via readmenator . receipts producing RELEASES.md + release-edges.json (observed 17, confirmed 8, unobserved 3, predicted 3). Discovery fix committed: relative project path joins against scan base first.
<!-- readmenator:memory:notes:end -->
