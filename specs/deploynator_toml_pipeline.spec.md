# SPEC: deploynator pipeline — tests + docs + semver secuencial

Objetivo: jubilar DEPLOY.sh. Un comando despliega con versionado semántico
correcto, corriendo tests (salvo flag) y regenerando docs con readmenator.

## 1. deploynator.toml (por proyecto, en root del proyecto objetivo)

```toml
[project]
name = "my-app"              # default: dirname
version_file = "version.json" # default: version.json

[tests]
commands = ["python -m pytest tests/ -q"]  # default si falta toml
timeout_s = 300              # default 300, rango 1..3600
allow_no_tests = false       # si true y no hay dir tests/, pasa

[docs]
auto = true                  # default true
command = "python -m readmenator . --rebuild"  # default
timeout_s = 300

[deploy]
branch = "main"
remote = "origin"
```

### Happy paths
- H1: toml ausente → defaults (1 comando pytest, docs auto true).
- H2: toml válido → TestRunner ejecuta cada comando en orden, cwd=project_path.
- H3: `--no-test` salta tests aunque fallen.
- H4: `--no-docs` salta readmenator.
- H5: `--bump major|minor|patch` fuerza estrategia sobre mapa commit-type.
- H6: docs falla → warning, continúa deploy (no bloquea).
- H7: versión actual = max(version_file, último git tag) → continuidad secuencial.

### Sad paths
- S1: toml es symlink → ValueError("Symlink rejected").
- S2: toml > max_file_size_bytes (10MB) → ValueError("File too large").
- S3: toml malformado (TOML inválido) → ValueError.
- S4: `[tests] commands` vacío + allow_no_tests=false + sin dir tests/ → fail "No tests configured".
- S5: comando test retorna !=0 → abort deploy, DeployResult(success=False, error="Tests failed..."), sin bump/commit/tag.
- S6: timeout excedido → fail como S5.
- S7: shell injection: comando con `;`, `|`, `$()` NO se ejecuta vía shell → se splitea con shlex, shell=False.
- S8: sin ref inicial (ni tag ni commit) → error "No starting ref" (existente).
- S9: `--bump` inválido → ValueError (argparse lo rechaza).
- S10: test command vacío/string vacío → ValueError.

## 2. Mapa semver (correcto, NO legado frágil)

| type | bump |
|------|------|
| feat | minor |
| fix, hotfix, patch | patch |
| release | major |
| docs, refactor, style, chore, test | none (misma versión) |

Legado DEPLOY.sh hacía feat/fix→patch y patch→minor (incoherente). Se abandona.
Continuidad secuencial: `current = max(file_version, latest_tag)`.
Colisión tag: `while tag_exists: patch++` (ya implementado, se mantiene).

## 3. Pipeline deploy (orden)

1. resolve project_path
2. load deploynator.toml (defaults si ausente)
3. current = max(file, tag); strategy = force_bump or bump(commit_type); next = current.bump(strategy)
4. si run_tests y no dry_run: TestRunner.run() → si fail: return error, sin mutar
5. si run_docs y no dry_run: DocsRunner.run() → si fail: print warning, continúa
6. resto idéntico: write_version, add, changelog, commit, tag+colisión, push, release
7. dry_run: imprime "Would run tests", "Would run docs", "Would deploy", sin mutar

## 4. CLI agent-friendly + interactivo

```
deploynator release --type feat --project X [--bump major|minor|patch] [--no-test] [--no-docs] [--dry-run] [--platforms ...] [--all]
deploynator interactive   # menú guidado estilo DEPLOY.sh
```

## 5. Contratos nuevos

- `_toml.py`: TomlConfig (frozen) + load_toml_config(path) -> TomlConfig. Rechaza symlink, tamaño, parse.
- `_runner.py`: TestRunner(config).run(project_path, toml) -> (ok, output). shlex split, shell=False, timeout.
- `_docs.py`: DocsRunner(config).run(project_path, toml) -> bool. Misma seguridad.
- `_semver.py`: get_current_version() → max(file, tag). Nuevo método max_version(a,b).
- `_deploy.py`: deploy(..., run_tests=True, run_docs=True, force_bump=None|str).
- `_app.py`: release(..., no_test=False, no_docs=False, bump="").
- `__main__.py`: flags --no-test, --no-docs, --bump ya existe → cablear.

## 6. Mutación (tests deben cazar)

- M1: minor→patch en feat → debe fallar test_version_bump.
- M2: quitar gate tests (siempre ok) → test_pipeline_aborts_on_test_failure debe fallar.
- M3: docs fail bloquea → test_docs_failure_does_not_block debe fallar.
- M4: max→min en versión → test_current_is_max debe fallar.
- M5: shell=True → test_no_shell_injection debe fallar.
- M6: --bump ignorado → test_force_bump_overrides debe fallar.
