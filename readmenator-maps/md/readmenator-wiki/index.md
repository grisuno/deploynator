# Second Brain

*Last synthesized: 2026-10-14 | 32 files | 6 concept pages | offline, zero tokens*

> Raw sources -> readmenator wiki -> links (Karpathy LLM Wiki Pattern, deterministic).
> Start here, then open one community page. Prefer grep over full reads.

## Vault Overview

The codebase centres on `_config.py`, `_deploy.py`, `_models.py`. Architecturally it is 4 layers, dominant utility (16 files) across 6 import-based communities. Recorded risk surface: 0 security findings and 0 dependency cycles.

Surprising tissue lives between deploynator: _changelog, deploynator: _toml, deploynator: _models: 10 extracted cross-community imports and 10 inferred bridges. Follow `connections.json` sorted by strength before refactoring.

Open work clusters around documentation (34% file coverage), 0 security findings, 20 taint paths, and 5 suggested exploration questions in `queries.md`.

## Stats

| Metric | Value |
|--------|-------|
| Files | 32 |
| Symbols | 389 |
| Resolved imports | 189 |
| Languages | py, sh |
| Communities | 6 |
| Doc coverage | 34% (11/32 files) |
| Security findings | 0 |
| Estimated read cost | ~3754 tokens (chars/4, offline so $0) |

## Reading Order

1. Skim Stats and God Nodes below for blast radius.
2. Open the largest community page first, then follow Connections.
3. Use `queries.md` for the next question; log the answer there.

```
grep -rn '<keyword>' index.md community_*.md
readmenator query "<question>" --target deploynator
```

## Concept Wiki

- [deploynator: _changelog (6 files, cohesion 0.21)](./community_0_deploynator_changelog.md)
- [deploynator: _toml (6 files, cohesion 0.35)](./community_1_deploynator_toml.md)
- [deploynator: _models (6 files, cohesion 0.31)](./community_2_deploynator_models.md)
- [deploynator: _mcp_server (5 files, cohesion 0.47)](./community_3_deploynator_mcp_server.md)
- [deploynator: _platforms (5 files, cohesion 0.22)](./community_4_deploynator_platforms.md)
- [orphans (4 files, cohesion 0.00)](./community_5_orphans.md)

## God Nodes

| File | Score |
|------|-------|
| `deploynator/_config.py` | 46.6 |
| `deploynator/_deploy.py` | 33.9 |
| `deploynator/_models.py` | 30.7 |
| `deploynator/_toml.py` | 22.4 |
| `deploynator/_app.py` | 17.1 |

## Strongest Connections

- 3 -> 4: depends_on (strength 0.9, EXTRACTED)
- 3 -> 0: depends_on (strength 0.9, EXTRACTED)
- 3 -> 2: depends_on (strength 0.9, EXTRACTED)
- 4 -> 0: depends_on (strength 0.9, EXTRACTED)
- 4 -> 2: depends_on (strength 0.9, EXTRACTED)
- 4 -> 1: depends_on (strength 0.9, EXTRACTED)
- 0 -> 2: depends_on (strength 0.9, EXTRACTED)
- 1 -> 0: depends_on (strength 0.9, EXTRACTED)
- 1 -> 2: depends_on (strength 0.9, EXTRACTED)
- 3 -> 1: depends_on (strength 0.9, EXTRACTED)

## Navigation Tips

- Obsidian Graph View works: every community page links back here.
- `connections.json` is machine-readable for GraphRAG pipelines.
- `REPORT.md` states what was extracted vs inferred and current limits.
- Regenerate offline: `readmenator . --rebuild` (no network, no tokens).
