# Second Brain

*Last synthesized: 2026-10-16 | 35 files | 5 concept pages | offline, zero tokens*

> Raw sources -> readmenator wiki -> links (Karpathy LLM Wiki Pattern, deterministic).
> Start here, then open one community page. Prefer grep over full reads.

## Vault Overview

The codebase centres on `_config.py`, `_deploy.py`, `_models.py`. Architecturally it is 4 layers, dominant utility (17 files) across 5 import-based communities. Recorded risk surface: 0 security findings and 0 dependency cycles.

Surprising tissue lives between deploynator: _platforms, deploynator: _toml, deploynator: _mcp_server: 6 extracted cross-community imports and 7 inferred bridges. Follow `connections.json` sorted by strength before refactoring.

Open work clusters around documentation (37% file coverage), 0 security findings, 20 taint paths, and 5 suggested exploration questions in `queries.md`.

## Stats

| Metric | Value |
|--------|-------|
| Files | 35 |
| Symbols | 433 |
| Resolved imports | 214 |
| Languages | py, sh |
| Communities | 5 |
| Doc coverage | 37% (13/35 files) |
| Security findings | 0 |
| Estimated read cost | ~4271 tokens (chars/4, offline so $0) |

## Reading Order

1. Skim Stats and God Nodes below for blast radius.
2. Open the largest community page first, then follow Connections.
3. Use `queries.md` for the next question; log the answer there.

```
grep -rn '<keyword>' index.md community_*.md
readmenator query "<question>" --target deploynator
```

## Concept Wiki

- [deploynator: _platforms (11 files, cohesion 0.45)](./community_0_deploynator_platforms.md)
- [deploynator: _toml (8 files, cohesion 0.38)](./community_1_deploynator_toml.md)
- [deploynator: _mcp_server (7 files, cohesion 0.50)](./community_2_deploynator_mcp_server.md)
- [deploynator: _changelog (6 files, cohesion 0.21)](./community_3_deploynator_changelog.md)
- [orphans (3 files, cohesion 0.00)](./community_4_orphans.md)

## God Nodes

| File | Score |
|------|-------|
| `deploynator/_config.py` | 54.6 |
| `deploynator/_deploy.py` | 36.0 |
| `deploynator/_models.py` | 30.7 |
| `deploynator/_toml.py` | 22.9 |
| `deploynator/_app.py` | 17.2 |

## Strongest Connections

- 2 -> 3: depends_on (strength 0.9, EXTRACTED)
- 2 -> 0: depends_on (strength 0.9, EXTRACTED)
- 0 -> 3: depends_on (strength 0.9, EXTRACTED)
- 0 -> 1: depends_on (strength 0.9, EXTRACTED)
- 1 -> 3: depends_on (strength 0.9, EXTRACTED)
- 2 -> 1: depends_on (strength 0.9, EXTRACTED)
- 2 -> 0: bridges (strength 0.6, INFERRED)
- 3 -> 0: bridges (strength 0.6, INFERRED)
- 2 -> 0: bridges (strength 0.6, INFERRED)
- 0 -> 3: bridges (strength 0.6, INFERRED)

## Navigation Tips

- Obsidian Graph View works: every community page links back here.
- `connections.json` is machine-readable for GraphRAG pipelines.
- `REPORT.md` states what was extracted vs inferred and current limits.
- Regenerate offline: `readmenator . --rebuild` (no network, no tokens).
