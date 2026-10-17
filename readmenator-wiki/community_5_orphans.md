# orphans

*Community 5 | 3 files | cohesion 0.00*

## Definition

This community groups 3 file(s) rooted at `root` with dominant language sh (cohesion 0.00). Central symbols: `ensure_pkg`. Core file: `deploy.sh` (1 symbols). Documented purpose: one-liner deploy via deploynator (generic per-repo script). Deployed by deploynator: detects its own directory, ensures tooling, then releases this repo. Usage:.

## Files

| File | Language | Layer | Symbols | Doc |
|------|----------|-------|---------|-----|
| `deploy.sh` | sh | utility | 1 | yes |
| `install.sh` | sh | utility | 0 | no |
| `tests/__init__.py` | py | testing | 0 | no |

## Key Symbols

- `ensure_pkg` (function, `deploy.sh:22`) - Install or update one package (best effort: works offline with current versions, on PEP 668 systems,

## Internal vs External Edges

- Internal resolved imports (EXTRACTED): 0
- Cross-boundary resolved imports (EXTRACTED): 0

## Connections

- [INFERRED] shares_context community 0 <-> 5 (strength 0.5): Inferred shared context (layer utility) with no import path between community 0 (deploynator: _toml) and community 5 (orphans).
- [INFERRED] shares_context community 1 <-> 5 (strength 0.5): Inferred shared context (layer utility) with no import path between community 1 (deploynator: _mcp_server) and community 5 (orphans).
- [INFERRED] shares_context community 4 <-> 5 (strength 0.5): Inferred shared context (layer utility) with no import path between community 4 (deploynator: _platforms) and community 5 (orphans).

## Risks

- No scoped security, taint, cycle, or layer risks.

## Open Questions

- Why do 2 file(s) lack file-level docs (e.g. `install.sh`)? What purpose do they serve?
- What would break if the most connected file in orphans changed?
- Should orphans be split, given cohesion 0.00?

## Sources

- `deploy.sh`
- `install.sh`
- `tests/__init__.py`
