# `deploynator._semver`

> Source: [deploynator/_semver.py:1](../../deploynator/_semver.py#L1) | language `py` | coverage 0.0% | [API index](../index.md)

## Contents

- **Classes:** [`SemverManager`](#semvermanager)

## Call Graph

Solid arrows stay in this module, dashed arrows leave it.

```mermaid
flowchart LR
    n_deploynator__semver_py__SemverManager_get_current_version(["SemverManager.get_current_version"])
    n_deploynator__semver_py__SemverManager_max_version(["SemverManager.max_version"])
    n_deploynator__models_py__VersionInfo["_models.VersionInfo"]
    n_deploynator__models_py__VersionInfo_parse["_models.VersionInfo.parse"]
    n_deploynator__semver_py__SemverManager_determine_bump(["SemverManager.determine_bump"])
    n_deploynator__models_py__CommitType_bump_strategy["_models.CommitType.bump_strategy"]
    n_deploynator__semver_py__SemverManager_calculate_next_version(["SemverManager.calculate_next_version"])
    n_deploynator__models_py__VersionInfo_bump["_models.VersionInfo.bump"]
    n_deploynator__semver_py__SemverManager_get_current_version --> n_deploynator__semver_py__SemverManager_max_version
    n_deploynator__semver_py__SemverManager_get_current_version -.-> n_deploynator__models_py__VersionInfo
    n_deploynator__semver_py__SemverManager_get_current_version -.-> n_deploynator__models_py__VersionInfo_parse
    n_deploynator__semver_py__SemverManager_determine_bump -.-> n_deploynator__models_py__CommitType_bump_strategy
    n_deploynator__semver_py__SemverManager_calculate_next_version -.-> n_deploynator__models_py__VersionInfo_bump
```

## Classes

<a id="semvermanager"></a>

### `SemverManager`

`class` | [deploynator/_semver.py:11](../../deploynator/_semver.py#L11)

```python
class SemverManager
```

**Members**

| Member | Kind | Summary |
|---|---|---|
| [`__init__`](#semvermanager-__init__) | constructor |  |
| [`max_version`](#semvermanager-max_version) | method |  |
| [`get_current_version`](#semvermanager-get_current_version) | method |  |
| [`write_version_file`](#semvermanager-write_version_file) | method |  |
| [`determine_bump`](#semvermanager-determine_bump) | method |  |
| [`calculate_next_version`](#semvermanager-calculate_next_version) | method |  |
| [`is_valid_version`](#semvermanager-is_valid_version) | staticmethod |  |

<a id="semvermanager-__init__"></a>

#### `SemverManager.__init__`

`constructor` | [deploynator/_semver.py:12](../../deploynator/_semver.py#L12)

```python
def __init__(self, config: Config) -> None
```

**Parameters**

| Name | Type | Default | Description |
|---|---|---|---|
| `config` | `Config` |  |  |

*Called by:* [`DeployOrchestrator.__init__`](deploynator._deploy.py.md#deployorchestrator-__init__)

<a id="semvermanager-max_version"></a>

#### `SemverManager.max_version`

`method` | [deploynator/_semver.py:15](../../deploynator/_semver.py#L15)

```python
def max_version(self, a: VersionInfo, b: VersionInfo) -> VersionInfo
```

**Parameters**

| Name | Type | Default | Description |
|---|---|---|---|
| `a` | `VersionInfo` |  |  |
| `b` | `VersionInfo` |  |  |

**Returns:** `VersionInfo`

*Called by:* [`SemverManager.get_current_version`](#semvermanager-get_current_version)

<a id="semvermanager-get_current_version"></a>

#### `SemverManager.get_current_version`

`method` | [deploynator/_semver.py:20](../../deploynator/_semver.py#L20)

```python
def get_current_version(self, project_path: str, version_file: str = 'version.json', version_pattern: str = '(\\d+)\\.(\\d+)\\.(\\d+)') -> VersionInfo
```

**Parameters**

| Name | Type | Default | Description |
|---|---|---|---|
| `project_path` | `str` |  |  |
| `version_file` | `str` | `'version.json'` |  |
| `version_pattern` | `str` | `'(\\d+)\\.(\\d+)\\.(\\d+)'` |  |

**Returns:** `VersionInfo`

*Calls:* [`VersionInfo`](deploynator._models.py.md#versioninfo), [`VersionInfo.parse`](deploynator._models.py.md#versioninfo-parse), [`SemverManager.max_version`](#semvermanager-max_version)

<a id="semvermanager-write_version_file"></a>

#### `SemverManager.write_version_file`

`method` | [deploynator/_semver.py:65](../../deploynator/_semver.py#L65)

```python
def write_version_file(self, project_path: str, version: VersionInfo, version_file: str = 'version.json') -> str
```

**Parameters**

| Name | Type | Default | Description |
|---|---|---|---|
| `project_path` | `str` |  |  |
| `version` | `VersionInfo` |  |  |
| `version_file` | `str` | `'version.json'` |  |

**Returns:** `str`

**Raises**

- `OSError`: (raised in the body, not documented)
- `ValueError`: (raised in the body, not documented)

<a id="semvermanager-determine_bump"></a>

#### `SemverManager.determine_bump`

`method` | [deploynator/_semver.py:110](../../deploynator/_semver.py#L110)

```python
def determine_bump(self, commit_type: CommitType) -> str | None
```

**Parameters**

| Name | Type | Default | Description |
|---|---|---|---|
| `commit_type` | `CommitType` |  |  |

**Returns:** `str | None`

*Calls:* [`CommitType.bump_strategy`](deploynator._models.py.md#committype-bump_strategy)

<a id="semvermanager-calculate_next_version"></a>

#### `SemverManager.calculate_next_version`

`method` | [deploynator/_semver.py:113](../../deploynator/_semver.py#L113)

```python
def calculate_next_version(self, current: VersionInfo, strategy: str | None) -> VersionInfo
```

**Parameters**

| Name | Type | Default | Description |
|---|---|---|---|
| `current` | `VersionInfo` |  |  |
| `strategy` | `str \| None` |  |  |

**Returns:** `VersionInfo`

*Calls:* [`VersionInfo.bump`](deploynator._models.py.md#versioninfo-bump)

<a id="semvermanager-is_valid_version"></a>

#### `SemverManager.is_valid_version`

`staticmethod` | [deploynator/_semver.py:117](../../deploynator/_semver.py#L117)

Decorators: `@staticmethod`

```python
def is_valid_version(version_str: str) -> bool
```

**Parameters**

| Name | Type | Default | Description |
|---|---|---|---|
| `version_str` | `str` |  |  |

**Returns:** `bool`

---
