# orphans

*Community 5 | 4 files | cohesion 0.00*

## Definition

This community groups 4 file(s) rooted at `root` with dominant language py (cohesion 0.00). Central symbols: `ensure_pkg`. Core file: `deploy.sh` (1 symbols). Documented purpose: Autor: Gris Iscomeback Correo electrónico: grisiscomeback[at]gmail[dot]com Fecha de creación: xx/xx/xxxx Licencia: GPL v3  Descripción:.

## Files

| File | Language | Layer | Symbols | Doc |
|------|----------|-------|---------|-----|
| `app.py` | py | utility | 0 | yes |
| `deploy.sh` | sh | utility | 1 | yes |
| `install.sh` | sh | utility | 0 | no |
| `tests/__init__.py` | py | testing | 0 | no |

## Key Symbols

- `ensure_pkg` (function, `deploy.sh:22`) - Install or update one package (best effort: works offline with current versions, on PEP 668 systems,

## Internal vs External Edges

- Internal resolved imports (EXTRACTED): 0
- Cross-boundary resolved imports (EXTRACTED): 0

## Connections

- [INFERRED] shares_context community 0 <-> 5 (strength 0.5): Inferred shared context (language py) with no import path between community 0 (deploynator: _changelog) and community 5 (orphans).
- [INFERRED] shares_context community 1 <-> 5 (strength 0.5): Inferred shared context (language py and layer utility) with no import path between community 1 (deploynator: _toml) and community 5 (orphans).
- [INFERRED] shares_context community 2 <-> 5 (strength 0.5): Inferred shared context (language py) with no import path between community 2 (deploynator: _models) and community 5 (orphans).
- [INFERRED] shares_context community 3 <-> 5 (strength 0.5): Inferred shared context (language py and layer utility) with no import path between community 3 (deploynator: _mcp_server) and community 5 (orphans).
- [INFERRED] shares_context community 4 <-> 5 (strength 0.5): Inferred shared context (language py and layer utility) with no import path between community 4 (deploynator: _platforms) and community 5 (orphans).

## Risks

- No scoped security, taint, cycle, or layer risks.

## Open Questions

- Why do 2 file(s) lack file-level docs (e.g. `install.sh`)? What purpose do they serve?
- What would break if the most connected file in orphans changed?
- Should orphans be split, given cohesion 0.00?

## Sources

- `app.py`
- `deploy.sh`
- `install.sh`
- `tests/__init__.py`
