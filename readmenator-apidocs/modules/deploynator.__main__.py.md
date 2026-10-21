# `deploynator.__main__`

> Source: [deploynator/__main__.py:1](../../deploynator/__main__.py#L1) | language `py` | coverage 0.0% | [API index](../index.md)

## Contents

- **Functions:** [`build_parser`](#build_parser), [`preprocess_argv`](#preprocess_argv), [`main`](#main)
- **Constants:** [`KNOWN_COMMANDS`](#known_commands)

## Call Graph

Solid arrows stay in this module, dashed arrows leave it.

```mermaid
flowchart LR
    n_deploynator___main___py__preprocess_argv(["preprocess_argv"])
    n_deploynator___main___py__build_parser(["build_parser"])
    n_deploynator___main___py__main(["main"])
    n_deploynator__models_py__CommitType_valid_types["_models.CommitType.valid_types"]
    n_deploynator__app_py__DeploynatorApp___init__["_app.DeploynatorApp.__init__"]
    n_deploynator__app_py__DeploynatorApp_auth_login["_app.DeploynatorApp.auth_login"]
    n_deploynator__app_py__DeploynatorApp_auth_status["_app.DeploynatorApp.auth_status"]
    n_deploynator__app_py__DeploynatorApp_commit["_app.DeploynatorApp.commit"]
    n_deploynator__app_py__DeploynatorApp_generate_ci["_app.DeploynatorApp.generate_ci"]
    n_deploynator__app_py__DeploynatorApp_generate_docs["_app.DeploynatorApp.generate_docs"]
    n_deploynator__app_py__DeploynatorApp_init_project["_app.DeploynatorApp.init_project"]
    n_deploynator__app_py__DeploynatorApp_install_deps["_app.DeploynatorApp.install_deps"]
    n_deploynator__app_py__DeploynatorApp_install_packages["_app.DeploynatorApp.install_packages"]
    n_deploynator__app_py__DeploynatorApp_interactive_menu["_app.DeploynatorApp.interactive_menu"]
    n_deploynator__app_py__DeploynatorApp_list_projects["_app.DeploynatorApp.list_projects"]
    n_deploynator__app_py__DeploynatorApp_release["_app.DeploynatorApp.release"]
    n_deploynator__app_py__DeploynatorApp_start_branch["_app.DeploynatorApp.start_branch"]
    n_deploynator__app_py__DeploynatorApp_status["_app.DeploynatorApp.status"]
    n_deploynator__config_py__Config_create["_config.Config.create"]
    n_deploynator__mcp_server_py__MCPServer___init__["_mcp_server.MCPServer.__init__"]
    n_deploynator__mcp_server_py__MCPServer_run["_mcp_server.MCPServer.run"]
    n_deploynator___main___py__preprocess_argv --> n_deploynator___main___py__build_parser
    n_deploynator___main___py__main --> n_deploynator___main___py__build_parser
    n_deploynator___main___py__main --> n_deploynator___main___py__preprocess_argv
    n_deploynator___main___py__build_parser -.-> n_deploynator__models_py__CommitType_valid_types
    n_deploynator___main___py__main -.-> n_deploynator__app_py__DeploynatorApp___init__
    n_deploynator___main___py__main -.-> n_deploynator__app_py__DeploynatorApp_auth_login
    n_deploynator___main___py__main -.-> n_deploynator__app_py__DeploynatorApp_auth_status
    n_deploynator___main___py__main -.-> n_deploynator__app_py__DeploynatorApp_commit
    n_deploynator___main___py__main -.-> n_deploynator__app_py__DeploynatorApp_generate_ci
    n_deploynator___main___py__main -.-> n_deploynator__app_py__DeploynatorApp_generate_docs
    n_deploynator___main___py__main -.-> n_deploynator__app_py__DeploynatorApp_init_project
    n_deploynator___main___py__main -.-> n_deploynator__app_py__DeploynatorApp_install_deps
    n_deploynator___main___py__main -.-> n_deploynator__app_py__DeploynatorApp_install_packages
    n_deploynator___main___py__main -.-> n_deploynator__app_py__DeploynatorApp_interactive_menu
    n_deploynator___main___py__main -.-> n_deploynator__app_py__DeploynatorApp_list_projects
    n_deploynator___main___py__main -.-> n_deploynator__app_py__DeploynatorApp_release
    n_deploynator___main___py__main -.-> n_deploynator__app_py__DeploynatorApp_start_branch
    n_deploynator___main___py__main -.-> n_deploynator__app_py__DeploynatorApp_status
    n_deploynator___main___py__main -.-> n_deploynator__config_py__Config_create
    n_deploynator___main___py__main -.-> n_deploynator__mcp_server_py__MCPServer___init__
    n_deploynator___main___py__main -.-> n_deploynator__mcp_server_py__MCPServer_run
```

## Functions

<a id="build_parser"></a>

### `build_parser`

`function` | [deploynator/__main__.py:16](../../deploynator/__main__.py#L16)

```python
def build_parser() -> argparse.ArgumentParser
```

**Returns:** `argparse.ArgumentParser`

*Calls:* [`CommitType.valid_types`](deploynator._models.py.md#committype-valid_types)

*Called by:* [`main`](#main), [`preprocess_argv`](#preprocess_argv)

---

<a id="preprocess_argv"></a>

### `preprocess_argv`

`function` | [deploynator/__main__.py:151](../../deploynator/__main__.py#L151)

```python
def preprocess_argv(argv: list[str]) -> tuple[argparse.Namespace, str]
```

**Parameters**

| Name | Type | Default | Description |
|---|---|---|---|
| `argv` | `list[str]` |  |  |

**Returns:** `tuple[argparse.Namespace, str]`

*Calls:* [`build_parser`](#build_parser)

*Called by:* [`main`](#main)

---

<a id="main"></a>

### `main`

`function` | [deploynator/__main__.py:185](../../deploynator/__main__.py#L185)

```python
def main(argv: list[str] | None = None) -> None
```

**Parameters**

| Name | Type | Default | Description |
|---|---|---|---|
| `argv` | `list[str] \| None` | `None` |  |

*Calls:* [`build_parser`](#build_parser), [`preprocess_argv`](#preprocess_argv), [`DeploynatorApp.__init__`](deploynator._app.py.md#deploynatorapp-__init__), [`DeploynatorApp.auth_login`](deploynator._app.py.md#deploynatorapp-auth_login), [`DeploynatorApp.auth_status`](deploynator._app.py.md#deploynatorapp-auth_status), [`DeploynatorApp.commit`](deploynator._app.py.md#deploynatorapp-commit), [`DeploynatorApp.generate_ci`](deploynator._app.py.md#deploynatorapp-generate_ci), [`DeploynatorApp.generate_docs`](deploynator._app.py.md#deploynatorapp-generate_docs), [`DeploynatorApp.init_project`](deploynator._app.py.md#deploynatorapp-init_project), [`DeploynatorApp.install_deps`](deploynator._app.py.md#deploynatorapp-install_deps), [`DeploynatorApp.install_packages`](deploynator._app.py.md#deploynatorapp-install_packages), [`DeploynatorApp.interactive_menu`](deploynator._app.py.md#deploynatorapp-interactive_menu) and 7 more

---

## Constants

<a id="known_commands"></a>

### `KNOWN_COMMANDS`

`constant` | [deploynator/__main__.py:10](../../deploynator/__main__.py#L10)

```python
KNOWN_COMMANDS
```

---
