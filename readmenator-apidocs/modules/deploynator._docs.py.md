# `deploynator._docs`

> Source: [deploynator/_docs.py:1](../../deploynator/_docs.py#L1) | language `py` | coverage 0.0% | [API index](../index.md)

## Contents

- **Classes:** [`DocsRunner`](#docsrunner)

## Classes

<a id="docsrunner"></a>

### `DocsRunner`

`class` | [deploynator/_docs.py:10](../../deploynator/_docs.py#L10)

```python
class DocsRunner
```

**Members**

| Member | Kind | Summary |
|---|---|---|
| [`__init__`](#docsrunner-__init__) | constructor |  |
| [`run`](#docsrunner-run) | method |  |

<a id="docsrunner-__init__"></a>

#### `DocsRunner.__init__`

`constructor` | [deploynator/_docs.py:11](../../deploynator/_docs.py#L11)

```python
def __init__(self, config: Config) -> None
```

**Parameters**

| Name | Type | Default | Description |
|---|---|---|---|
| `config` | `Config` |  |  |

*Called by:* [`DeployOrchestrator.__init__`](deploynator._deploy.py.md#deployorchestrator-__init__)

<a id="docsrunner-run"></a>

#### `DocsRunner.run`

`method` | [deploynator/_docs.py:14](../../deploynator/_docs.py#L14)

```python
def run(self, project_path: str, toml: TomlConfig) -> bool
```

**Parameters**

| Name | Type | Default | Description |
|---|---|---|---|
| `project_path` | `str` |  |  |
| `toml` | `TomlConfig` |  |  |

**Returns:** `bool`

*Called by:* [`DeployOrchestrator.deploy`](deploynator._deploy.py.md#deployorchestrator-deploy), [`DeployOrchestrator.integrate_readmenator`](deploynator._deploy.py.md#deployorchestrator-integrate_readmenator)

---
