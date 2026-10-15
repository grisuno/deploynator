# Second Brain

*Last synthesized: 2026-10-14 | 33 files | 4 concept pages | offline, zero tokens*

> Raw sources -> readmenator wiki -> links (Karpathy LLM Wiki Pattern, deterministic).
> Start here, then open one community page. Prefer grep over full reads.

## Vault Overview

The codebase centres on `_config.py`, `_deploy.py`, `_models.py`. Architecturally it is 4 layers, dominant utility (16 files) across 4 import-based communities. Recorded risk surface: 0 security findings and 0 dependency cycles.

Surprising tissue lives between deploynator: _mcp_server, deploynator: _platforms, deploynator: _pypi: 3 extracted cross-community imports and 6 inferred bridges. Follow `connections.json` sorted by strength before refactoring.

Open work clusters around documentation (36% file coverage), 0 security findings, 20 taint paths, and 5 suggested exploration questions in `queries.md`.

## Stats

| Metric | Value |
|--------|-------|
| Files | 33 |
| Symbols | 405 |
| Resolved imports | 199 |
| Languages | py, sh |
| Communities | 4 |
| Doc coverage | 36% (12/33 files) |
| Security findings | 0 |
| Estimated read cost | ~3594 tokens (chars/4, offline so $0) |

## Reading Order

1. Skim Stats and God Nodes below for blast radius.
2. Open the largest community page first, then follow Connections.
3. Use `queries.md` for the next question; log the answer there.

```
grep -rn '<keyword>' index.md community_*.md
readmenator query "<question>" --target deploynator
```

## Concept Wiki

- [deploynator: _mcp_server (11 files, cohesion 0.47)](./community_0_deploynator_mcp_server.md)
- [deploynator: _platforms (11 files, cohesion 0.46)](./community_1_deploynator_platforms.md)
- [deploynator: _pypi (8 files, cohesion 0.38)](./community_2_deploynator_pypi.md)
- [orphans (3 files, cohesion 0.00)](./community_3_orphans.md)

## God Nodes

| File | Score |
|------|-------|
| `deploynator/_config.py` | 50.6 |
| `deploynator/_deploy.py` | 33.9 |
| `deploynator/_models.py` | 30.7 |
| `deploynator/_toml.py` | 22.4 |
| `deploynator/_app.py` | 17.2 |

## Strongest Connections

- 0 -> 1: depends_on (strength 0.9, EXTRACTED)
- 1 -> 2: depends_on (strength 0.9, EXTRACTED)
- 2 -> 0: depends_on (strength 0.9, EXTRACTED)
- 0 -> 1: bridges (strength 0.6, INFERRED)
- 0 -> 1: bridges (strength 0.6, INFERRED)
- 0 -> 1: bridges (strength 0.6, INFERRED)
- 1 -> 2: bridges (strength 0.6, INFERRED)
- 1 -> 2: bridges (strength 0.6, INFERRED)
- 0 -> 3: shares_context (strength 0.5, INFERRED)

## Navigation Tips

- Obsidian Graph View works: every community page links back here.
- `connections.json` is machine-readable for GraphRAG pipelines.
- `REPORT.md` states what was extracted vs inferred and current limits.
- Regenerate offline: `readmenator . --rebuild` (no network, no tokens).
