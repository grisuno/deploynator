# `deploynator._git`

> Source: [deploynator/_git.py:1](../../deploynator/_git.py#L1) | language `py` | coverage 3.8% | [API index](../index.md)

## Contents

- **Classes:** [`GitOperations`](#gitoperations)

## Call Graph

Solid arrows stay in this module, dashed arrows leave it.

```mermaid
flowchart LR
    n_deploynator__git_py__GitOperations_gpg_sign_flag(["GitOperations.gpg_sign_flag"])
    n_deploynator__git_py__GitOperations_check_gpg(["GitOperations.check_gpg"])
    n_deploynator__git_py__GitOperations_commit(["GitOperations.commit"])
    n_deploynator__git_py__GitOperations_amend_no_edit(["GitOperations.amend_no_edit"])
    n_deploynator__git_py__GitOperations_gpg_sign_flag --> n_deploynator__git_py__GitOperations_check_gpg
    n_deploynator__git_py__GitOperations_commit --> n_deploynator__git_py__GitOperations_gpg_sign_flag
    n_deploynator__git_py__GitOperations_amend_no_edit --> n_deploynator__git_py__GitOperations_gpg_sign_flag
```

## Classes

<a id="gitoperations"></a>

### `GitOperations`

`class` | [deploynator/_git.py:9](../../deploynator/_git.py#L9)

```python
class GitOperations
```

**Members**

| Member | Kind | Summary |
|---|---|---|
| [`__init__`](#gitoperations-__init__) | constructor |  |
| [`head_commit`](#gitoperations-head_commit) | method |  |
| [`check_gpg`](#gitoperations-check_gpg) | method |  |
| [`gpg_sign_flag`](#gitoperations-gpg_sign_flag) | method |  |
| [`clone`](#gitoperations-clone) | method |  |
| [`add_all`](#gitoperations-add_all) | method |  |
| [`commit`](#gitoperations-commit) | method |  |
| [`amend_no_edit`](#gitoperations-amend_no_edit) | method |  |
| [`tag`](#gitoperations-tag) | method |  |
| [`delete_tag`](#gitoperations-delete_tag) | method |  |
| [`tag_exists`](#gitoperations-tag_exists) | method |  |
| [`push`](#gitoperations-push) | method |  |
| [`push_tags`](#gitoperations-push_tags) | method |  |
| [`create_branch`](#gitoperations-create_branch) | method |  |
| [`checkout`](#gitoperations-checkout) | method |  |
| [`get_changed_files`](#gitoperations-get_changed_files) | method |  |
| [`get_log`](#gitoperations-get_log) | method |  |
| [`get_start_ref`](#gitoperations-get_start_ref) | method |  |
| [`current_branch`](#gitoperations-current_branch) | method |  |
| [`is_dirty`](#gitoperations-is_dirty) | method |  |
| [`has_remote`](#gitoperations-has_remote) | method |  |
| [`branch_exists`](#gitoperations-branch_exists) | method |  |
| [`is_behind`](#gitoperations-is_behind) | method | True si `ahead_branch` tiene commits que `behind_branch` no tiene (es decir, behind_branch esta por debajo de ahead_branch). |
| [`push_force`](#gitoperations-push_force) | method |  |

<a id="gitoperations-__init__"></a>

#### `GitOperations.__init__`

`constructor` | [deploynator/_git.py:10](../../deploynator/_git.py#L10)

```python
def __init__(self, config: Config) -> None
```

**Parameters**

| Name | Type | Default | Description |
|---|---|---|---|
| `config` | `Config` |  |  |

*Called by:* [`DeploynatorApp.commit`](deploynator._app.py.md#deploynatorapp-commit), [`DeploynatorApp.start_branch`](deploynator._app.py.md#deploynatorapp-start_branch), [`DeploynatorApp.status`](deploynator._app.py.md#deploynatorapp-status), [`DeployOrchestrator.__init__`](deploynator._deploy.py.md#deployorchestrator-__init__)

<a id="gitoperations-head_commit"></a>

#### `GitOperations.head_commit`

`method` | [deploynator/_git.py:13](../../deploynator/_git.py#L13)

```python
def head_commit(self, repo_path: str) -> str
```

**Parameters**

| Name | Type | Default | Description |
|---|---|---|---|
| `repo_path` | `str` |  |  |

**Returns:** `str`

<a id="gitoperations-check_gpg"></a>

#### `GitOperations.check_gpg`

`method` | [deploynator/_git.py:23](../../deploynator/_git.py#L23)

```python
def check_gpg(self) -> tuple[bool, str]
```

**Returns:** `tuple[bool, str]`

*Called by:* [`GitOperations.gpg_sign_flag`](#gitoperations-gpg_sign_flag)

<a id="gitoperations-gpg_sign_flag"></a>

#### `GitOperations.gpg_sign_flag`

`method` | [deploynator/_git.py:41](../../deploynator/_git.py#L41)

```python
def gpg_sign_flag(self) -> list[str]
```

**Returns:** `list[str]`

*Calls:* [`GitOperations.check_gpg`](#gitoperations-check_gpg)

*Called by:* [`GitOperations.amend_no_edit`](#gitoperations-amend_no_edit), [`GitOperations.commit`](#gitoperations-commit)

<a id="gitoperations-clone"></a>

#### `GitOperations.clone`

`method` | [deploynator/_git.py:45](../../deploynator/_git.py#L45)

```python
def clone(self, url: str, dest: str, depth: int = 1) -> bool
```

**Parameters**

| Name | Type | Default | Description |
|---|---|---|---|
| `url` | `str` |  |  |
| `dest` | `str` |  |  |
| `depth` | `int` | `1` |  |

**Returns:** `bool`

<a id="gitoperations-add_all"></a>

#### `GitOperations.add_all`

`method` | [deploynator/_git.py:55](../../deploynator/_git.py#L55)

```python
def add_all(self, repo_path: str) -> bool
```

**Parameters**

| Name | Type | Default | Description |
|---|---|---|---|
| `repo_path` | `str` |  |  |

**Returns:** `bool`

<a id="gitoperations-commit"></a>

#### `GitOperations.commit`

`method` | [deploynator/_git.py:68](../../deploynator/_git.py#L68)

```python
def commit(self, repo_path: str, message: str) -> tuple[bool, str]
```

**Parameters**

| Name | Type | Default | Description |
|---|---|---|---|
| `repo_path` | `str` |  |  |
| `message` | `str` |  |  |

**Returns:** `tuple[bool, str]`

*Calls:* [`GitOperations.gpg_sign_flag`](#gitoperations-gpg_sign_flag)

*Called by:* [`DeploynatorApp.commit`](deploynator._app.py.md#deploynatorapp-commit)

<a id="gitoperations-amend_no_edit"></a>

#### `GitOperations.amend_no_edit`

`method` | [deploynator/_git.py:97](../../deploynator/_git.py#L97)

```python
def amend_no_edit(self, repo_path: str) -> bool
```

**Parameters**

| Name | Type | Default | Description |
|---|---|---|---|
| `repo_path` | `str` |  |  |

**Returns:** `bool`

*Calls:* [`GitOperations.gpg_sign_flag`](#gitoperations-gpg_sign_flag)

<a id="gitoperations-tag"></a>

#### `GitOperations.tag`

`method` | [deploynator/_git.py:106](../../deploynator/_git.py#L106)

```python
def tag(self, repo_path: str, tag_name: str, message: str) -> bool
```

**Parameters**

| Name | Type | Default | Description |
|---|---|---|---|
| `repo_path` | `str` |  |  |
| `tag_name` | `str` |  |  |
| `message` | `str` |  |  |

**Returns:** `bool`

<a id="gitoperations-delete_tag"></a>

#### `GitOperations.delete_tag`

`method` | [deploynator/_git.py:116](../../deploynator/_git.py#L116)

```python
def delete_tag(self, repo_path: str, tag_name: str) -> bool
```

**Parameters**

| Name | Type | Default | Description |
|---|---|---|---|
| `repo_path` | `str` |  |  |
| `tag_name` | `str` |  |  |

**Returns:** `bool`

<a id="gitoperations-tag_exists"></a>

#### `GitOperations.tag_exists`

`method` | [deploynator/_git.py:126](../../deploynator/_git.py#L126)

```python
def tag_exists(self, repo_path: str, tag_name: str) -> bool
```

**Parameters**

| Name | Type | Default | Description |
|---|---|---|---|
| `repo_path` | `str` |  |  |
| `tag_name` | `str` |  |  |

**Returns:** `bool`

<a id="gitoperations-push"></a>

#### `GitOperations.push`

`method` | [deploynator/_git.py:136](../../deploynator/_git.py#L136)

```python
def push(self, repo_path: str, remote: str, branch: str, follow_tags: bool = True) -> bool
```

**Parameters**

| Name | Type | Default | Description |
|---|---|---|---|
| `repo_path` | `str` |  |  |
| `remote` | `str` |  |  |
| `branch` | `str` |  |  |
| `follow_tags` | `bool` | `True` |  |

**Returns:** `bool`

*Called by:* [`DeploynatorApp.start_branch`](deploynator._app.py.md#deploynatorapp-start_branch)

<a id="gitoperations-push_tags"></a>

#### `GitOperations.push_tags`

`method` | [deploynator/_git.py:146](../../deploynator/_git.py#L146)

```python
def push_tags(self, repo_path: str, remote: str = 'origin') -> bool
```

**Parameters**

| Name | Type | Default | Description |
|---|---|---|---|
| `repo_path` | `str` |  |  |
| `remote` | `str` | `'origin'` |  |

**Returns:** `bool`

<a id="gitoperations-create_branch"></a>

#### `GitOperations.create_branch`

`method` | [deploynator/_git.py:156](../../deploynator/_git.py#L156)

```python
def create_branch(self, repo_path: str, branch_name: str, base: str | None = None) -> bool
```

**Parameters**

| Name | Type | Default | Description |
|---|---|---|---|
| `repo_path` | `str` |  |  |
| `branch_name` | `str` |  |  |
| `base` | `str \| None` | `None` |  |

**Returns:** `bool`

*Called by:* [`DeploynatorApp.start_branch`](deploynator._app.py.md#deploynatorapp-start_branch)

<a id="gitoperations-checkout"></a>

#### `GitOperations.checkout`

`method` | [deploynator/_git.py:172](../../deploynator/_git.py#L172)

```python
def checkout(self, repo_path: str, branch: str) -> bool
```

**Parameters**

| Name | Type | Default | Description |
|---|---|---|---|
| `repo_path` | `str` |  |  |
| `branch` | `str` |  |  |

**Returns:** `bool`

<a id="gitoperations-get_changed_files"></a>

#### `GitOperations.get_changed_files`

`method` | [deploynator/_git.py:182](../../deploynator/_git.py#L182)

```python
def get_changed_files(self, repo_path: str, from_ref: str, to_ref: str = 'HEAD') -> dict[str, list[str]]
```

**Parameters**

| Name | Type | Default | Description |
|---|---|---|---|
| `repo_path` | `str` |  |  |
| `from_ref` | `str` |  |  |
| `to_ref` | `str` | `'HEAD'` |  |

**Returns:** `dict[str, list[str]]`

<a id="gitoperations-get_log"></a>

#### `GitOperations.get_log`

`method` | [deploynator/_git.py:213](../../deploynator/_git.py#L213)

```python
def get_log(self, repo_path: str, from_ref: str, to_ref: str = 'HEAD', format_str: str = '%s|||%an|||%h') -> list[str]
```

**Parameters**

| Name | Type | Default | Description |
|---|---|---|---|
| `repo_path` | `str` |  |  |
| `from_ref` | `str` |  |  |
| `to_ref` | `str` | `'HEAD'` |  |
| `format_str` | `str` | `'%s\|\|\|%an\|\|\|%h'` |  |

**Returns:** `list[str]`

<a id="gitoperations-get_start_ref"></a>

#### `GitOperations.get_start_ref`

`method` | [deploynator/_git.py:225](../../deploynator/_git.py#L225)

```python
def get_start_ref(self, repo_path: str) -> str | None
```

**Parameters**

| Name | Type | Default | Description |
|---|---|---|---|
| `repo_path` | `str` |  |  |

**Returns:** `str | None`

<a id="gitoperations-current_branch"></a>

#### `GitOperations.current_branch`

`method` | [deploynator/_git.py:243](../../deploynator/_git.py#L243)

```python
def current_branch(self, repo_path: str) -> str | None
```

**Parameters**

| Name | Type | Default | Description |
|---|---|---|---|
| `repo_path` | `str` |  |  |

**Returns:** `str | None`

*Called by:* [`DeploynatorApp.status`](deploynator._app.py.md#deploynatorapp-status)

<a id="gitoperations-is_dirty"></a>

#### `GitOperations.is_dirty`

`method` | [deploynator/_git.py:255](../../deploynator/_git.py#L255)

```python
def is_dirty(self, repo_path: str) -> bool
```

**Parameters**

| Name | Type | Default | Description |
|---|---|---|---|
| `repo_path` | `str` |  |  |

**Returns:** `bool`

*Called by:* [`DeploynatorApp.commit`](deploynator._app.py.md#deploynatorapp-commit), [`DeploynatorApp.status`](deploynator._app.py.md#deploynatorapp-status)

<a id="gitoperations-has_remote"></a>

#### `GitOperations.has_remote`

`method` | [deploynator/_git.py:265](../../deploynator/_git.py#L265)

```python
def has_remote(self, repo_path: str, remote: str = 'origin') -> bool
```

**Parameters**

| Name | Type | Default | Description |
|---|---|---|---|
| `repo_path` | `str` |  |  |
| `remote` | `str` | `'origin'` |  |

**Returns:** `bool`

*Called by:* [`DeploynatorApp.status`](deploynator._app.py.md#deploynatorapp-status)

<a id="gitoperations-branch_exists"></a>

#### `GitOperations.branch_exists`

`method` | [deploynator/_git.py:275](../../deploynator/_git.py#L275)

```python
def branch_exists(self, repo_path: str, branch: str) -> bool
```

**Parameters**

| Name | Type | Default | Description |
|---|---|---|---|
| `repo_path` | `str` |  |  |
| `branch` | `str` |  |  |

**Returns:** `bool`

<a id="gitoperations-is_behind"></a>

#### `GitOperations.is_behind`

`method` | [deploynator/_git.py:285](../../deploynator/_git.py#L285)

```python
def is_behind(self, repo_path: str, behind_branch: str, ahead_branch: str) -> bool
```

True si `ahead_branch` tiene commits que `behind_branch` no tiene (es decir, behind_branch esta por debajo de ahead_branch).

**Parameters**

| Name | Type | Default | Description |
|---|---|---|---|
| `repo_path` | `str` |  |  |
| `behind_branch` | `str` |  |  |
| `ahead_branch` | `str` |  |  |

**Returns:** `bool`

<a id="gitoperations-push_force"></a>

#### `GitOperations.push_force`

`method` | [deploynator/_git.py:300](../../deploynator/_git.py#L300)

```python
def push_force(self, repo_path: str, remote: str, src_branch: str, dst_branch: str) -> bool
```

**Parameters**

| Name | Type | Default | Description |
|---|---|---|---|
| `repo_path` | `str` |  |  |
| `remote` | `str` |  |  |
| `src_branch` | `str` |  |  |
| `dst_branch` | `str` |  |  |

**Returns:** `bool`

---
