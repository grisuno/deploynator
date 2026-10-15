# `deploynator._changelog`

> Source: [deploynator/_changelog.py:1](../../deploynator/_changelog.py#L1) | language `py` | coverage 0.0% | [API index](../index.md)

## Contents

- **Classes:** [`ChangelogGenerator`](#changeloggenerator)

## Call Graph

Solid arrows stay in this module, dashed arrows leave it.

```mermaid
flowchart LR
    n_deploynator__changelog_py__ChangelogGenerator_generate_from_messages(["ChangelogGenerator.generate_from_messages"])
    n_deploynator__models_py__ChangelogEntry["_models.ChangelogEntry"]
    n_deploynator__models_py__CommitMessage_parse["_models.CommitMessage.parse"]
    n_deploynator__changelog_py__ChangelogGenerator_generate_from_messages -.-> n_deploynator__models_py__ChangelogEntry
    n_deploynator__changelog_py__ChangelogGenerator_generate_from_messages -.-> n_deploynator__models_py__CommitMessage_parse
```

## Classes

<a id="changeloggenerator"></a>

### `ChangelogGenerator`

`class` | [deploynator/_changelog.py:12](../../deploynator/_changelog.py#L12)

```python
class ChangelogGenerator
```

**Members**

| Member | Kind | Summary |
|---|---|---|
| [`__init__`](#changeloggenerator-__init__) | constructor |  |
| [`generate_from_log`](#changeloggenerator-generate_from_log) | method |  |
| [`generate_from_messages`](#changeloggenerator-generate_from_messages) | method |  |
| [`generate_header`](#changeloggenerator-generate_header) | method |  |
| [`write_changelog`](#changeloggenerator-write_changelog) | method |  |
| [`format_for_release`](#changeloggenerator-format_for_release) | method |  |

<a id="changeloggenerator-__init__"></a>

#### `ChangelogGenerator.__init__`

`constructor` | [deploynator/_changelog.py:13](../../deploynator/_changelog.py#L13)

```python
def __init__(self, config: Config) -> None
```

**Parameters**

| Name | Type | Default | Description |
|---|---|---|---|
| `config` | `Config` |  |  |

*Called by:* [`DeployOrchestrator.__init__`](deploynator._deploy.py.md#deployorchestrator-__init__)

<a id="changeloggenerator-generate_from_log"></a>

#### `ChangelogGenerator.generate_from_log`

`method` | [deploynator/_changelog.py:16](../../deploynator/_changelog.py#L16)

```python
def generate_from_log(self, repo_path: str, from_ref: str, to_ref: str = 'HEAD') -> str
```

**Parameters**

| Name | Type | Default | Description |
|---|---|---|---|
| `repo_path` | `str` |  |  |
| `from_ref` | `str` |  |  |
| `to_ref` | `str` | `'HEAD'` |  |

**Returns:** `str`

*Called by:* [`DeployOrchestrator.deploy`](deploynator._deploy.py.md#deployorchestrator-deploy)

<a id="changeloggenerator-generate_from_messages"></a>

#### `ChangelogGenerator.generate_from_messages`

`method` | [deploynator/_changelog.py:25](../../deploynator/_changelog.py#L25)

```python
def generate_from_messages(self, messages: list[str]) -> str
```

**Parameters**

| Name | Type | Default | Description |
|---|---|---|---|
| `messages` | `list[str]` |  |  |

**Returns:** `str`

*Calls:* [`ChangelogEntry`](deploynator._models.py.md#changelogentry), [`CommitMessage.parse`](deploynator._models.py.md#commitmessage-parse)

*Called by:* [`DeploynatorApp.commit`](deploynator._app.py.md#deploynatorapp-commit)

<a id="changeloggenerator-generate_header"></a>

#### `ChangelogGenerator.generate_header`

`method` | [deploynator/_changelog.py:45](../../deploynator/_changelog.py#L45)

```python
def generate_header(self) -> str
```

**Returns:** `str`

<a id="changeloggenerator-write_changelog"></a>

#### `ChangelogGenerator.write_changelog`

`method` | [deploynator/_changelog.py:100](../../deploynator/_changelog.py#L100)

```python
def write_changelog(self, repo_path: str, content: str, filename: Optional[str] = None) -> str
```

**Parameters**

| Name | Type | Default | Description |
|---|---|---|---|
| `repo_path` | `str` |  |  |
| `content` | `str` |  |  |
| `filename` | `Optional[str]` | `None` |  |

**Returns:** `str`

**Raises**

- `OSError`: (raised in the body, not documented)

*Called by:* [`DeployOrchestrator.deploy`](deploynator._deploy.py.md#deployorchestrator-deploy)

<a id="changeloggenerator-format_for_release"></a>

#### `ChangelogGenerator.format_for_release`

`method` | [deploynator/_changelog.py:110](../../deploynator/_changelog.py#L110)

```python
def format_for_release(self, changelog_content: str, max_chars: Optional[int] = None) -> str
```

**Parameters**

| Name | Type | Default | Description |
|---|---|---|---|
| `changelog_content` | `str` |  |  |
| `max_chars` | `Optional[int]` | `None` |  |

**Returns:** `str`

*Called by:* [`DeployOrchestrator.deploy`](deploynator._deploy.py.md#deployorchestrator-deploy)

---
