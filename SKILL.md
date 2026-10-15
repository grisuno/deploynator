---
name: deploynator
description: "Headless semantic release: tests gate + readmenator docs + semver tag/push. MCP-native. Bare = interactive, flags = headless. Sucesor de DEPLOY.sh."
trigger: /deploynator
---

# /deploynator

Sucesor de `DEPLOY.sh`. Un comando despliega con semver correcto: corre tests (salvo `--no-test`), regenera docs con readmenator (salvo `--no-docs`), bump, commit, changelog, tag, push, release.

## Regla de modo (importante)

```
deploynator            # sin args = menú interactivo (estilo DEPLOY.sh)
deploynator interactive # explícito, igual al anterior, sin flags
deploynator <flags>    # con flags = headless (para agentes y CI)
```

El modo interactivo NO lleva flags. El modo headless SIEMPRE lleva flags.

## Arquitectura: MCP-first, CLI-fallback

```
Agent ──MCP tools──> deploynator-mcp ──> release headless (~200 tokens)
     \
      ──CLI flags──> deploynator release --type ... (sin MCP)
```

MCP es la vía primaria en harnesses (claude code, codex, opencode). CLI es fallback.

## Uso

```
/deploynator                              # bare = interactivo
/deploynator release --type feat --project X --dry-run   # preview headless
/deploynator serve <path>                 # arranca servidor MCP stdio
```

## Lo que debes hacer al ser invocado

Sin path usa `.`. No preguntes path. Nunca uses modo interactivo desde un harness: siempre headless o MCP.

### Paso 1 — MCP tools (vía primaria)

Servidor: `deploynator serve <path>` o `deploynator-mcp <path>` (stdio JSON-RPC).
Config ejemplo (Claude Desktop / opencode):

```json
{
  "mcpServers": {
    "deploynator": {
      "command": "deploynator-mcp",
      "args": ["/path/to/project"]
    }
  }
}
```

O directo:

```json
{
  "mcpServers": {
    "deploynator": {
      "command": "python3",
      "args": ["-m", "deploynator._mcp_server", "/path/to/project"]
    }
  }
}
```

| Tool | Propósito |
|------|-----------|
| `deploynator.release` | Pipeline completo (tests, docs, bump, tag, push). `dry_run=true` para preview |
| `deploynator.commit` | Solo commit convencional |
| `deploynator.status` | Branch, dirty, remote, counts |
| `deploynator.projects` | Proyectos descubiertos |
| `deploynator.docs` | Regen docs vía readmenator |

| Resource | Contenido |
|----------|-----------|
| `deploynator://projects` | Proyectos JSON |
| `deploynator://status` | Estado JSON |

### Paso 2 — Fallback CLI headless (sin MCP)

```bash
# Preview siempre primero
deploynator release --type feat --project X --dry-run
# Release real
deploynator release --type feat --project X
deploynator release --type fix --project X --bump major --no-test --no-docs
deploynator release --type feat --all --dry-run
deploynator commit --type feat --subject "add login" --scope auth
deploynator status --project X
deploynator docs --project X
```

### Paso 3 — Proyectos

YAML en `projects/` + `deploynator.toml` en raíz del proyecto objetivo:

```yaml
# projects/my-app.yaml
version: 1.0
name: my-app
path: "deploynator_repos/my-app"
platforms:
  github: {repo: "user/my-app", enabled: true}
version: {file: version.json, file_type: json}
```

```toml
# deploynator.toml (en proyecto objetivo)
[tests]
commands = ["python -m pytest tests/ -q"]
timeout_s = 300
[docs]
auto = true
command = "python -m readmenator . --rebuild"
```

## Semver (correcto, no legado frágil)

| Type | Bump |
|------|------|
| feat | minor |
| fix, hotfix, patch | patch |
| release | major |
| docs, refactor, style, chore, test | none |

`current = max(version_file, último tag)`. Colisión tag → `patch++`. `--bump` fuerza estrategia.

## Pipeline

1. tests (bloquea si falla, salvo `--no-test` / `dry_run` simula)
2. docs readmenator (no bloquea, solo warning, salvo `--no-docs`)
3. bump → version.json → changelog → commit → tag → push → release
4. PyPI (solo si hay packaging + credenciales, salvo `--no-pypi`): limpia `dist/`, `python -m build`, `twine upload`. Falla → error.

## Seguridad

- Tokens por env: GITHUB_TOKEN, GITLAB_TOKEN, BITBUCKET_TOKEN. Nunca por CLI.
- Todo subprocess con lista + `shell=False`. Symlinks rechazados. TOML cap 10MB.
- `dry_run` no muta. GPG autodetectado con fallback.

## Script location

- Repo: https://github.com/grisuno/deploynator
- MCP: `python3 -m deploynator._mcp_server <path>` / `deploynator serve <path>`
- Hermana docs: https://github.com/grisuno/ReadMenator (`readmenator . --rebuild`)

<!-- readmenator-agent-kb-link -->
## Project Knowledge Base (MUST read before coding)

Generated offline by [ReadMenator](https://github.com/grisuno/ReadMenator) (zero-token static analysis). Humans: `KNOWLEDGE_BASE.md`.

0. Memory: `cat readmenator-agent/MEMORY.md` (business rules, workflow, constraints, style, done criteria, session log). Record new decisions with `readmenator . remember "<note>" --kind decision`.
1. Freshness: `readmenator . fresh` (exit 1 means stale: run `readmenator . --rebuild`). Without the CLI, compare `git_commit` in `readmenator-agent/MANIFEST.json` with `git log -1`.
2. Orient: `ls *.md readmenator-agent/ readmenator-wiki/`, then read `readmenator-wiki/index.md` (big picture, communities, god nodes).
3. Locate: `grep -n '<keyword>' readmenator-agent/INDEX*.md readmenator-agent/SYMBOLS*.md` before any `glob` over sources; for questions use `readmenator . ask "<question>"` (GraphRAG, `--global` for overviews).
4. Context: `cat readmenator-agent/KB_<subsystem>.md` for the subsystem you touch.
5. Before editing: `grep -n '<file>' readmenator-agent/GOTCHAS.md readmenator-agent/SECURITY.md` (blast radius, cycles, findings).

Also: `API*.md` (public functions, one line each), `ARCHITECTURE*.md` (dependency pairs), `recipes/*.md` (grounded task steps). Large docs are paged as `NAME_p2.md`, so always grep with `NAME*.md`.

    pip install readmenator && readmenator . --rebuild
<!-- /readmenator-agent-kb-link -->
