# Second Brain

*Last synthesized: 2026-10-19 | 38 files | 6 concept pages | offline, zero tokens*

> Raw sources -> readmenator wiki -> links (Karpathy LLM Wiki Pattern, deterministic).
> Start here, then open one community page. Prefer grep over full reads.

## Vault Overview

The codebase centres on `_config.py`, `_deploy.py`, `_models.py`. Architecturally it is 4 layers, dominant utility (18 files) across 6 import-based communities. Recorded risk surface: 0 security findings and 0 dependency cycles.

Surprising tissue lives between deploynator: _toml, deploynator: _mcp_server, deploynator: _platforms: 10 extracted cross-community imports and 8 inferred bridges. Follow `connections.json` sorted by strength before refactoring.

Open work clusters around documentation (37% file coverage), 0 security findings, 20 taint paths, and 5 suggested exploration questions in `queries.md`.

## Stats

| Metric | Value |
|--------|-------|
| Files | 38 |
| Symbols | 489 |
| Resolved imports | 264 |
| Languages | py, sh |
| Communities | 6 |
| Doc coverage | 37% (14/38 files) |
| Security findings | 0 |
| Estimated read cost | ~5281 tokens (chars/4, offline so $0) |

## Reading Order

1. Skim Stats and God Nodes below for blast radius.
2. Open the largest community page first, then follow Connections.
3. Use `queries.md` for the next question; log the answer there.

```
grep -rn '<keyword>' index.md community_*.md
readmenator query "<question>" --target deploynator
```

## Concept Wiki

- [deploynator: _toml (8 files, cohesion 0.35)](./community_0_deploynator_toml.md)
- [deploynator: _mcp_server (7 files, cohesion 0.50)](./community_1_deploynator_mcp_server.md)
- [deploynator: _platforms (7 files, cohesion 0.27)](./community_2_deploynator_platforms.md)
- [deploynator: _models (7 files, cohesion 0.32)](./community_3_deploynator_models.md)
- [deploynator: _changelog (6 files, cohesion 0.20)](./community_4_deploynator_changelog.md)
- [orphans (3 files, cohesion 0.00)](./community_5_orphans.md)

## God Nodes

| File | Score |
|------|-------|
| `deploynator/_config.py` | 60.6 |
| `deploynator/_deploy.py` | 42.2 |
| `deploynator/_models.py` | 30.7 |
| `deploynator/_toml.py` | 27.0 |
| `deploynator/_app.py` | 17.3 |

## Strongest Connections

- 1 -> 4: depends_on (strength 0.9, EXTRACTED)
- 1 -> 2: depends_on (strength 0.9, EXTRACTED)
- 1 -> 3: depends_on (strength 0.9, EXTRACTED)
- 2 -> 4: depends_on (strength 0.9, EXTRACTED)
- 2 -> 3: depends_on (strength 0.9, EXTRACTED)
- 2 -> 0: depends_on (strength 0.9, EXTRACTED)
- 4 -> 3: depends_on (strength 0.9, EXTRACTED)
- 0 -> 4: depends_on (strength 0.9, EXTRACTED)
- 0 -> 3: depends_on (strength 0.9, EXTRACTED)
- 1 -> 0: depends_on (strength 0.9, EXTRACTED)

## Navigation Tips

- Obsidian Graph View works: every community page links back here.
- `connections.json` is machine-readable for GraphRAG pipelines.
- `REPORT.md` states what was extracted vs inferred and current limits.
- Regenerate offline: `readmenator . --rebuild` (no network, no tokens).
