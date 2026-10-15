# Second Brain

*Last synthesized: 2026-10-14 | 30 files | 6 concept pages | offline, zero tokens*

> Raw sources -> readmenator wiki -> links (Karpathy LLM Wiki Pattern, deterministic).
> Start here, then open one community page. Prefer grep over full reads.

## Vault Overview

The codebase centres on `_config.py`, `_deploy.py`, `_models.py`. Architecturally it is 4 layers, dominant utility (15 files) across 6 import-based communities. Recorded risk surface: 0 security findings and 0 dependency cycles.

Surprising tissue lives between deploynator: _changelog, deploynator: _toml, deploynator: _models: 9 extracted cross-community imports and 10 inferred bridges. Follow `connections.json` sorted by strength before refactoring.

Open work clusters around documentation (30% file coverage), 0 security findings, 20 taint paths, and 5 suggested exploration questions in `queries.md`.

## Stats

| Metric | Value |
|--------|-------|
| Files | 30 |
| Symbols | 381 |
| Resolved imports | 174 |
| Languages | py, sh |
| Communities | 6 |
| Doc coverage | 30% (9/30 files) |
| Security findings | 0 |
| Estimated read cost | ~3551 tokens (chars/4, offline so $0) |

## Reading Order

1. Skim Stats and God Nodes below for blast radius.
2. Open the largest community page first, then follow Connections.
3. Use `queries.md` for the next question; log the answer there.

```
grep -rn '<keyword>' index.md community_*.md
readmenator query "<question>" --target deploynator
```

## Concept Wiki

- [deploynator: _changelog (6 files, cohesion 0.22)](./community_0_deploynator_changelog.md)
- [deploynator: _toml (6 files, cohesion 0.36)](./community_1_deploynator_toml.md)
- [deploynator: _models (6 files, cohesion 0.31)](./community_2_deploynator_models.md)
- [deploynator: _platforms (5 files, cohesion 0.22)](./community_3_deploynator_platforms.md)
- [deploynator: _mcp_server (4 files, cohesion 0.50)](./community_4_deploynator_mcp_server.md)
- [orphans (3 files, cohesion 0.00)](./community_5_orphans.md)

## God Nodes

| File | Score |
|------|-------|
| `deploynator/_config.py` | 44.6 |
| `deploynator/_deploy.py` | 33.9 |
| `deploynator/_models.py` | 30.7 |
| `deploynator/_toml.py` | 20.4 |
| `deploynator/_app.py` | 17.1 |

## Strongest Connections

- 4 -> 3: depends_on (strength 0.9, EXTRACTED)
- 4 -> 0: depends_on (strength 0.9, EXTRACTED)
- 4 -> 2: depends_on (strength 0.9, EXTRACTED)
- 3 -> 0: depends_on (strength 0.9, EXTRACTED)
- 3 -> 2: depends_on (strength 0.9, EXTRACTED)
- 3 -> 1: depends_on (strength 0.9, EXTRACTED)
- 0 -> 2: depends_on (strength 0.9, EXTRACTED)
- 1 -> 0: depends_on (strength 0.9, EXTRACTED)
- 1 -> 2: depends_on (strength 0.9, EXTRACTED)
- 4 -> 0: bridges (strength 0.7, INFERRED)

## Navigation Tips

- Obsidian Graph View works: every community page links back here.
- `connections.json` is machine-readable for GraphRAG pipelines.
- `REPORT.md` states what was extracted vs inferred and current limits.
- Regenerate offline: `readmenator . --rebuild` (no network, no tokens).
