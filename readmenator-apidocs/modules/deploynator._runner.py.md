# `deploynator._runner`

> Source: [deploynator/_runner.py:1](../../deploynator/_runner.py#L1) | language `py` | coverage 0.0% | [API index](../index.md)

## Contents

- **Classes:** [`TestRunner`](#testrunner)

## Classes

<a id="testrunner"></a>

### `TestRunner`

`class` | [deploynator/_runner.py:11](../../deploynator/_runner.py#L11)

```python
class TestRunner
```

**Members**

| Member | Kind | Summary |
|---|---|---|
| [`__init__`](#testrunner-__init__) | constructor |  |
| [`run`](#testrunner-run) | method |  |

<a id="testrunner-__init__"></a>

#### `TestRunner.__init__`

`constructor` | [deploynator/_runner.py:12](../../deploynator/_runner.py#L12)

```python
def __init__(self, config: Config) -> None
```

**Parameters**

| Name | Type | Default | Description |
|---|---|---|---|
| `config` | `Config` |  |  |

*Called by:* [`DeployOrchestrator.__init__`](deploynator._deploy.py.md#deployorchestrator-__init__)

<a id="testrunner-run"></a>

#### `TestRunner.run`

`method` | [deploynator/_runner.py:15](../../deploynator/_runner.py#L15)

```python
def run(self, project_path: str, toml: TomlConfig) -> tuple[bool, str]
```

**Parameters**

| Name | Type | Default | Description |
|---|---|---|---|
| `project_path` | `str` |  |  |
| `toml` | `TomlConfig` |  |  |

**Returns:** `tuple[bool, str]`

---
