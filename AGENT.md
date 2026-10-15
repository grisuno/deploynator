# AGENT.md — deploynator para harnesses (claude code, codex, opencode)

> Regla de oro: **bare = interactivo, flags = headless**.
> Un agente NUNCA usa el modo interactivo. Siempre headless (CLI con flags o MCP).

## 1. Modo

```bash
deploynator             # INTERACTIVO — solo humanos, sin flags
deploynator interactive # INTERACTIVO explícito — solo humanos, sin flags
deploynator release --type feat --project X   # HEADLESS — agentes y CI
deploynator serve .     # MCP stdio — agentes con tool-calls
```

## 2. Headless CLI (fallback sin MCP)

```bash
# Descubrir
deploynator projects
deploynator status --project X
# Preview obligatorio antes de mutar
deploynator release --type <t> --project X --dry-run
# Real
deploynator release --type feat --project X --subject "add login"
deploynator release --type fix --project X --bump major --no-test --no-docs
deploynator release --type feat --all --dry-run
# Utilidades
deploynator commit --type feat --subject "msg" --scope auth [--dry-run]
deploynator start --type feat --desc slug [--remote]
deploynator docs --project X
deploynator workflow --all
deploynator auth status
```

Tipos válidos: `feat fix hotfix docs refactor style chore test release patch`.
Bump: `feat→minor, fix/hotfix/patch→patch, release→major, resto→none`. `--bump` fuerza.

## 3. MCP (vía primaria con tool-calls)

```json
{"mcpServers": {"deploynator": {"command": "deploynator-mcp", "args": ["/path/to/project"]}}}
```

Tools: `deploynator.release | commit | status | projects | docs`.
Resources: `deploynator://projects | deploynator://status`.
`release` args: `project, commit_type, subject, scope, body, bump, dry_run, no_test, no_docs, no_pypi`.
Siempre `dry_run=true` primero.

## 4. Config por proyecto

`projects/<name>.yaml` (descubrimiento) + `deploynator.toml` (raíz objetivo):

```toml
[tests]
commands = ["python -m pytest tests/ -q"]
timeout_s = 300
allow_no_tests = false
[docs]
auto = true
command = "python -m readmenator . --rebuild"
[deploy]
branch = "main"
remote = "origin"
```

Tests fallan → abort. Docs fallan → warning y sigue.

## 5. PyPI

Si hay `pyproject.toml [project]` o `setup.py` + credenciales (`TWINE_PASSWORD`/`PYPI_TOKEN`/`~/.pypirc`): tras el push, `dist/` limpio → `python -m build` → `twine upload`. Sin credenciales → warning y sigue. Fallo de build/upload → error. Salta con `--no-pypi` / `[pypi] enabled=false` / `repo="testpypi"` para probar.

## 5. Seguridad

Env tokens, nunca CLI. `shell=False` siempre. `dry_run` para preview. GPG auto.

## 6. Referencias

- SPEC: `specs/deploynator_toml_pipeline.spec.md`
- Ejemplo: `example.deploynator.toml`
- Hermana: `readmenator . --rebuild` (https://github.com/grisuno/ReadMenator)
