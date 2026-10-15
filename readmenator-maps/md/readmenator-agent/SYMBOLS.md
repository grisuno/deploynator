# Symbols

| Symbol | Kind | File:Line | Signature |
|--------|------|-----------|-----------|
| `build_parser` | function | `deploynator/__main__.py:17` | `def build_parser()` |
| `main` | function | `deploynator/__main__.py:164` | `def main(argv)` |
| `preprocess_argv` | function | `deploynator/__main__.py:130` | `def preprocess_argv(argv)` |
| `DeploynatorApp` | class | `deploynator/_app.py:20` | `class DeploynatorApp` |
| `__init__` | method | `deploynator/_app.py:21` | `def __init__(self, config, workdir)` |
| `_auth_bitbucket` | method | `deploynator/_app.py:86` | `def _auth_bitbucket()` |
| `_auth_github` | method | `deploynator/_app.py:56` | `def _auth_github()` |
| `_auth_gitlab` | method | `deploynator/_app.py:69` | `def _auth_gitlab()` |
| `_interactive_auth` | method | `deploynator/_app.py:508` | `def _interactive_auth(self)` |
| `_interactive_auth_status` | method | `deploynator/_app.py:531` | `def _interactive_auth_status(self)` |
| `_interactive_ci` | method | `deploynator/_app.py:544` | `def _interactive_ci(self)` |
| `_interactive_commit` | method | `deploynator/_app.py:457` | `def _interactive_commit(self)` |
| `_interactive_docs` | method | `deploynator/_app.py:537` | `def _interactive_docs(self)` |
| `_interactive_init` | method | `deploynator/_app.py:558` | `def _interactive_init(self)` |
| `_interactive_release` | method | `deploynator/_app.py:415` | `def _interactive_release(self)` |
| `_interactive_start` | method | `deploynator/_app.py:484` | `def _interactive_start(self)` |
| `_interactive_status` | method | `deploynator/_app.py:553` | `def _interactive_status(self)` |
| `_is_path_like` | method | `deploynator/_app.py:149` | `def _is_path_like(value)` |
| `_looks_like_path` | method | `deploynator/_app.py:153` | `def _looks_like_path(value)` |
| `_print_result` | method | `deploynator/_app.py:564` | `def _print_result(result)` |
| `_resolve_project_path` | method | `deploynator/_app.py:160` | `def _resolve_project_path(self, project_name)` |
| `_smart_prepare` | method | `deploynator/_app.py:174` | `def _smart_prepare(self, base, changelog_content, dry_run)` |
| `auth_login` | method | `deploynator/_app.py:31` | `def auth_login(self, platforms)` |
| `auth_status` | method | `deploynator/_app.py:45` | `def auth_status(self)` |
| `commit` | method | `deploynator/_app.py:189` | `def commit(self, commit_type, subject, scope, body, project_path, project_name, dry_run)` |
| `generate_ci` | method | `deploynator/_app.py:350` | `def generate_ci(self, project_name, all_projects)` |
| `generate_docs` | method | `deploynator/_app.py:319` | `def generate_docs(self, project_path, project_name)` |
| `init_project` | method | `deploynator/_app.py:96` | `def init_project(self, project_path, name)` |
| `install_deps` | method | `deploynator/_app.py:366` | `def install_deps(self, project_name)` |
| `interactive_menu` | method | `deploynator/_app.py:379` | `def interactive_menu(self)` |
| `list_projects` | method | `deploynator/_app.py:345` | `def list_projects(self, search_path)` |
| `release` | method | `deploynator/_app.py:229` | `def release(self, commit_type, subject, scope, body, project_name, bump, dry_run, platforms, all_projects, no_test...` |
| `start_branch` | method | `deploynator/_app.py:131` | `def start_branch(self, commit_type, description, project_path, project_name, remote)` |
| `status` | method | `deploynator/_app.py:325` | `def status(self, project_path, project_name)` |
| `ChangelogGenerator` | class | `deploynator/_changelog.py:12` | `class ChangelogGenerator` |
| `__init__` | method | `deploynator/_changelog.py:13` | `def __init__(self, config)` |
| `_collect_entries` | method | `deploynator/_changelog.py:48` | `def _collect_entries(self, repo_path, from_ref, to_ref)` |
| `_format_entries` | method | `deploynator/_changelog.py:69` | `def _format_entries(self, entries)` |
| `format_for_release` | method | `deploynator/_changelog.py:110` | `def format_for_release(self, changelog_content, max_chars)` |
| `generate_from_log` | method | `deploynator/_changelog.py:16` | `def generate_from_log(self, repo_path, from_ref, to_ref)` |
| `generate_from_messages` | method | `deploynator/_changelog.py:25` | `def generate_from_messages(self, messages)` |
| `generate_header` | method | `deploynator/_changelog.py:45` | `def generate_header(self)` |
| `write_changelog` | method | `deploynator/_changelog.py:100` | `def write_changelog(self, repo_path, content, filename)` |
| `Config` | class | `deploynator/_config.py:8` | `class Config` |
| `bb_authd` | method | `deploynator/_config.py:99` | `def bb_authd(self)` |
| `create` | method | `deploynator/_config.py:79` | `def create(overrides)` |
| `gh_authd` | method | `deploynator/_config.py:91` | `def gh_authd(self)` |
| `glab_authd` | method | `deploynator/_config.py:95` | `def glab_authd(self)` |
| `resolve_path` | method | `deploynator/_config.py:85` | `def resolve_path(self)` |
| `DeployOrchestrator` | class | `deploynator/_deploy.py:76` | `class DeployOrchestrator` |
| `ProjectDiscovery` | class | `deploynator/_deploy.py:31` | `class ProjectDiscovery` |
| `__init__` | method | `deploynator/_deploy.py:32` | `def __init__(self, config)` |
| `__init__` | method | `deploynator/_deploy.py:77` | `def __init__(self, config)` |
| `_add_temp_remote` | method | `deploynator/_deploy.py:384` | `def _add_temp_remote(self, repo_path, name, url)` |
| `_ci_workflow_content` | method | `deploynator/_deploy.py:431` | `def _ci_workflow_content(self, project)` |
| `_get_remote_url` | method | `deploynator/_deploy.py:403` | `def _get_remote_url(repo_path, pc)` |
| `_gh_release_in_repo` | method | `deploynator/_deploy.py:351` | `def _gh_release_in_repo(self, repo_path, project_name, version, notes, branch)` |
| `_load_single` | method | `deploynator/_deploy.py:63` | `def _load_single(yaml_path)` |
| `_release_workflow_content` | method | `deploynator/_deploy.py:452` | `def _release_workflow_content(self, project)` |
| `_remove_temp_remote` | method | `deploynator/_deploy.py:393` | `def _remove_temp_remote(self, repo_path, name)` |
| `_resolve_project_path` | method | `deploynator/_deploy.py:88` | `def _resolve_project_path(project)` |
| `deploy` | method | `deploynator/_deploy.py:97` | `def deploy(self, project, commit_type, subject, scope, body, dry_run, platforms_override, run_tests, run_docs...` |
| `discover` | method | `deploynator/_deploy.py:35` | `def discover(self, search_path)` |
| `find_by_name` | method | `deploynator/_deploy.py:56` | `def find_by_name(self, name, search_path)` |
| `generate_workflows` | method | `deploynator/_deploy.py:412` | `def generate_workflows(self, project, output_dir)` |
| `install_dependencies` | method | `deploynator/_deploy.py:480` | `def install_dependencies(self, project)` |
| `install_lazygit` | method | `deploynator/_deploy.py:524` | `def install_lazygit(self)` |
| `integrate_readmenator` | method | `deploynator/_deploy.py:490` | `def integrate_readmenator(self, project_path)` |
| `DocsRunner` | class | `deploynator/_docs.py:10` | `class DocsRunner` |
| `__init__` | method | `deploynator/_docs.py:11` | `def __init__(self, config)` |
| `run` | method | `deploynator/_docs.py:14` | `def run(self, project_path, toml)` |
| `GitOperations` | class | `deploynator/_git.py:10` | `class GitOperations` |
| `__init__` | method | `deploynator/_git.py:11` | `def __init__(self, config)` |
| `add_all` | method | `deploynator/_git.py:46` | `def add_all(self, repo_path)` |
| `amend_no_edit` | method | `deploynator/_git.py:68` | `def amend_no_edit(self, repo_path)` |
| `check_gpg` | method | `deploynator/_git.py:14` | `def check_gpg(self)` |
| `checkout` | method | `deploynator/_git.py:143` | `def checkout(self, repo_path, branch)` |
| `clone` | method | `deploynator/_git.py:36` | `def clone(self, url, dest, depth)` |
| `commit` | method | `deploynator/_git.py:56` | `def commit(self, repo_path, message)` |
| `create_branch` | method | `deploynator/_git.py:127` | `def create_branch(self, repo_path, branch_name, base)` |
| `current_branch` | method | `deploynator/_git.py:214` | `def current_branch(self, repo_path)` |
| `delete_tag` | method | `deploynator/_git.py:87` | `def delete_tag(self, repo_path, tag_name)` |
| `get_changed_files` | method | `deploynator/_git.py:153` | `def get_changed_files(self, repo_path, from_ref, to_ref)` |
| `get_log` | method | `deploynator/_git.py:184` | `def get_log(self, repo_path, from_ref, to_ref, format_str)` |
| `get_start_ref` | method | `deploynator/_git.py:196` | `def get_start_ref(self, repo_path)` |
| `gpg_sign_flag` | method | `deploynator/_git.py:32` | `def gpg_sign_flag(self)` |
| `has_remote` | method | `deploynator/_git.py:236` | `def has_remote(self, repo_path, remote)` |
| `is_dirty` | method | `deploynator/_git.py:226` | `def is_dirty(self, repo_path)` |
| `push` | method | `deploynator/_git.py:107` | `def push(self, repo_path, remote, branch, follow_tags)` |
| `push_tags` | method | `deploynator/_git.py:117` | `def push_tags(self, repo_path, remote)` |
| `tag` | method | `deploynator/_git.py:77` | `def tag(self, repo_path, tag_name, message)` |
| `tag_exists` | method | `deploynator/_git.py:97` | `def tag_exists(self, repo_path, tag_name)` |
| `MCPRequest` | class | `deploynator/_mcp_server.py:35` | `class MCPRequest` |
| `MCPResource` | class | `deploynator/_mcp_server.py:71` | `class MCPResource` |
| `MCPServer` | class | `deploynator/_mcp_server.py:86` | `class MCPServer` |
| `MCPTool` | class | `deploynator/_mcp_server.py:56` | `class MCPTool` |
| `__init__` | method | `deploynator/_mcp_server.py:36` | `def __init__(self, msg)` |
| `__init__` | method | `deploynator/_mcp_server.py:57` | `def __init__(self, name, description, handler, input_schema)` |
| `__init__` | method | `deploynator/_mcp_server.py:72` | `def __init__(self, uri, name, description, mime_type, handler)` |
| `__init__` | method | `deploynator/_mcp_server.py:87` | `def __init__(self, app, target_dir)` |
| `_handle_call_tool` | method | `deploynator/_mcp_server.py:111` | `def _handle_call_tool(self, req)` |
| `_handle_initialize` | method | `deploynator/_mcp_server.py:100` | `def _handle_initialize(self, req)` |
| `_handle_list_resources` | method | `deploynator/_mcp_server.py:128` | `def _handle_list_resources(self, req)` |
| `_handle_list_tools` | method | `deploynator/_mcp_server.py:108` | `def _handle_list_tools(self, req)` |
| `_handle_read_resource` | method | `deploynator/_mcp_server.py:131` | `def _handle_read_resource(self, req)` |
| `_register_all` | method | `deploynator/_mcp_server.py:180` | `def _register_all(self)` |
| `_resource_projects` | method | `deploynator/_mcp_server.py:265` | `def _resource_projects(self)` |
| `_tool_commit` | method | `deploynator/_mcp_server.py:248` | `def _tool_commit(self, commit_type, subject, project, scope, body, dry_run)` |
| `_tool_docs` | method | `deploynator/_mcp_server.py:261` | `def _tool_docs(self, project)` |
| `_tool_projects` | method | `deploynator/_mcp_server.py:255` | `def _tool_projects(self)` |
| `_tool_release` | method | `deploynator/_mcp_server.py:233` | `def _tool_release(self, project, commit_type, subject, scope, body, bump, dry_run, no_test, no_docs, no_pypi)` |
| `_tool_status` | method | `deploynator/_mcp_server.py:252` | `def _tool_status(self, project)` |
| `call` | method | `deploynator/_mcp_server.py:67` | `def call(self, arguments)` |
| `definition` | method | `deploynator/_mcp_server.py:64` | `def definition(self)` |
| `definition` | method | `deploynator/_mcp_server.py:79` | `def definition(self)` |
| `dispatch` | method | `deploynator/_mcp_server.py:144` | `def dispatch(self, req)` |
| `error` | method | `deploynator/_mcp_server.py:49` | `def error(self, code, message, data)` |
| `is_notification` | method | `deploynator/_mcp_server.py:43` | `def is_notification(self)` |
| `main` | function | `deploynator/_mcp_server.py:269` | `def main()` |
| `read` | method | `deploynator/_mcp_server.py:82` | `def read(self)` |
| `register_resource` | method | `deploynator/_mcp_server.py:97` | `def register_resource(self, resource)` |
| `register_tool` | method | `deploynator/_mcp_server.py:94` | `def register_tool(self, tool)` |
| `response` | method | `deploynator/_mcp_server.py:46` | `def response(self, result)` |
| `run` | method | `deploynator/_mcp_server.py:162` | `def run(self)` |
| `ChangelogEntry` | class | `deploynator/_models.py:239` | `class ChangelogEntry` |
| `CommitMessage` | class | `deploynator/_models.py:175` | `class CommitMessage` |
| `CommitType` | class | `deploynator/_models.py:45` | `class CommitType(Enum)` |
| `DeployResult` | class | `deploynator/_models.py:276` | `class DeployResult` |
| `Platform` | class | `deploynator/_models.py:10` | `class Platform(Enum)` |
| `PlatformConfig` | class | `deploynator/_models.py:98` | `class PlatformConfig` |
| `ProjectConfig` | class | `deploynator/_models.py:130` | `class ProjectConfig` |
| `ReleaseInfo` | class | `deploynator/_models.py:266` | `class ReleaseInfo` |
| `VersionConfig` | class | `deploynator/_models.py:115` | `class VersionConfig` |
| `VersionInfo` | class | `deploynator/_models.py:208` | `class VersionInfo` |
| `__str__` | method | `deploynator/_models.py:213` | `def __str__(self)` |
| `auth_env_var` | method | `deploynator/_models.py:37` | `def auth_env_var(self)` |
| `bump` | method | `deploynator/_models.py:228` | `def bump(self, strategy)` |
| `bump_strategy` | method | `deploynator/_models.py:68` | `def bump_strategy(self)` |
| `cli_name` | method | `deploynator/_models.py:30` | `def cli_name(self)` |
| `format` | method | `deploynator/_models.py:183` | `def format(self)` |
| `from_dict` | method | `deploynator/_models.py:105` | `def from_dict(cls, data)` |
| `from_dict` | method | `deploynator/_models.py:121` | `def from_dict(cls, data)` |
| `from_dict` | method | `deploynator/_models.py:139` | `def from_dict(cls, data)` |
| `from_git_log_line` | method | `deploynator/_models.py:247` | `def from_git_log_line(cls, line, author, sha)` |
| `from_string` | method | `deploynator/_models.py:16` | `def from_string(cls, name)` |
| `from_string` | method | `deploynator/_models.py:58` | `def from_string(cls, value)` |
| `label` | method | `deploynator/_models.py:27` | `def label(self)` |
| `parse` | method | `deploynator/_models.py:195` | `def parse(cls, raw)` |
| `parse` | method | `deploynator/_models.py:217` | `def parse(cls, version_str)` |
| `section_header` | method | `deploynator/_models.py:82` | `def section_header(self)` |
| `valid_types` | method | `deploynator/_models.py:65` | `def valid_types(cls)` |
| `BitbucketCLI` | class | `deploynator/_platforms.py:164` | `class BitbucketCLI(PlatformClient)` |
| `GitHubCLI` | class | `deploynator/_platforms.py:49` | `class GitHubCLI(PlatformClient)` |
| `GitLabCLI` | class | `deploynator/_platforms.py:113` | `class GitLabCLI(PlatformClient)` |
| `PlatformClient` | class | `deploynator/_platforms.py:14` | `class PlatformClient(ABC)` |
| `PlatformFactory` | class | `deploynator/_platforms.py:223` | `class PlatformFactory` |
| `__init__` | method | `deploynator/_platforms.py:15` | `def __init__(self, config)` |
| `_run` | method | `deploynator/_platforms.py:42` | `def _run(self, cmd, cwd, check)` |
| `create` | method | `deploynator/_platforms.py:235` | `def create(cls, platform, config)` |
| `create_all_available` | method | `deploynator/_platforms.py:242` | `def create_all_available(cls, config)` |
| `create_pull_request` | method | `deploynator/_platforms.py:35` | `def create_pull_request(self, repo, title, body, head, base)` |
| `create_pull_request` | method | `deploynator/_platforms.py:91` | `def create_pull_request(self, repo, title, body, head, base)` |
| `create_pull_request` | method | `deploynator/_platforms.py:142` | `def create_pull_request(self, repo, title, body, head, base)` |
| `create_pull_request` | method | `deploynator/_platforms.py:201` | `def create_pull_request(self, repo, title, body, head, base)` |
| `create_release` | method | `deploynator/_platforms.py:31` | `def create_release(self, repo, release)` |
| `create_release` | method | `deploynator/_platforms.py:67` | `def create_release(self, repo, release)` |
| `create_release` | method | `deploynator/_platforms.py:131` | `def create_release(self, repo, release)` |
| `create_release` | method | `deploynator/_platforms.py:181` | `def create_release(self, repo, release)` |
| `is_authenticated` | method | `deploynator/_platforms.py:27` | `def is_authenticated(self)` |
| `is_authenticated` | method | `deploynator/_platforms.py:60` | `def is_authenticated(self)` |
| `is_authenticated` | method | `deploynator/_platforms.py:124` | `def is_authenticated(self)` |
| `is_authenticated` | method | `deploynator/_platforms.py:178` | `def is_authenticated(self)` |
| `is_available` | method | `deploynator/_platforms.py:23` | `def is_available(self)` |
| `is_available` | method | `deploynator/_platforms.py:53` | `def is_available(self)` |
| `is_available` | method | `deploynator/_platforms.py:117` | `def is_available(self)` |
| `is_available` | method | `deploynator/_platforms.py:168` | `def is_available(self)` |
| `name` | method | `deploynator/_platforms.py:19` | `def name(self)` |
| `name` | method | `deploynator/_platforms.py:50` | `def name(self)` |
| `name` | method | `deploynator/_platforms.py:114` | `def name(self)` |
| `name` | method | `deploynator/_platforms.py:165` | `def name(self)` |
| `push_changes` | method | `deploynator/_platforms.py:39` | `def push_changes(self, repo_path, remote, branch, tags)` |
| `push_changes` | method | `deploynator/_platforms.py:105` | `def push_changes(self, repo_path, remote, branch, tags)` |
| `push_changes` | method | `deploynator/_platforms.py:156` | `def push_changes(self, repo_path, remote, branch, tags)` |
| `push_changes` | method | `deploynator/_platforms.py:215` | `def push_changes(self, repo_path, remote, branch, tags)` |
| `register` | method | `deploynator/_platforms.py:231` | `def register(cls, platform, client_class)` |
| `PyPIRunner` | class | `deploynator/_pypi.py:12` | `class PyPIRunner` |
| `__init__` | method | `deploynator/_pypi.py:13` | `def __init__(self, config)` |
| `clean` | method | `deploynator/_pypi.py:90` | `def clean(self, project_path, toml)` |
| `has_credentials` | method | `deploynator/_pypi.py:33` | `def has_credentials(self)` |
| `is_packaging_project` | method | `deploynator/_pypi.py:16` | `def is_packaging_project(self, project_path)` |
| `prompt_for_credentials` | method | `deploynator/_pypi.py:39` | `def prompt_for_credentials(self)` |
| `run` | method | `deploynator/_pypi.py:107` | `def run(self, project_path, toml, version, token)` |
| `save_pypirc` | method | `deploynator/_pypi.py:72` | `def save_pypirc(self, token, path)` |
| `TestRunner` | class | `deploynator/_runner.py:11` | `class TestRunner` |
| `__init__` | method | `deploynator/_runner.py:12` | `def __init__(self, config)` |
| `run` | method | `deploynator/_runner.py:15` | `def run(self, project_path, toml)` |
| `SemverManager` | class | `deploynator/_semver.py:12` | `class SemverManager` |
| `__init__` | method | `deploynator/_semver.py:13` | `def __init__(self, config)` |
| `_get_latest_tag` | method | `deploynator/_semver.py:122` | `def _get_latest_tag(self, project_path)` |
| `calculate_next_version` | method | `deploynator/_semver.py:114` | `def calculate_next_version(self, current, strategy)` |
| `determine_bump` | method | `deploynator/_semver.py:111` | `def determine_bump(self, commit_type)` |
| `get_current_version` | method | `deploynator/_semver.py:21` | `def get_current_version(self, project_path, version_file, version_pattern)` |
| `is_valid_version` | method | `deploynator/_semver.py:118` | `def is_valid_version(version_str)` |
| `max_version` | method | `deploynator/_semver.py:16` | `def max_version(self, a, b)` |
| `write_version_file` | method | `deploynator/_semver.py:66` | `def write_version_file(self, project_path, version, version_file)` |
| `TomlConfig` | class | `deploynator/_toml.py:14` | `class TomlConfig` |
| `__post_init__` | method | `deploynator/_toml.py:30` | `def __post_init__(self)` |
| `_clamp_timeout` | function | `deploynator/_toml.py:38` | `def _clamp_timeout(value)` |
| `load_toml_config` | function | `deploynator/_toml.py:46` | `def load_toml_config(project_path)` |
| `TestBDDDeployScenarios` | class | `tests/bdd_test_deploy.py:28` | `class TestBDDDeployScenarios` |
| `TestBDDPipeline` | class | `tests/bdd_test_deploy.py:84` | `class TestBDDPipeline` |
| `project` | method | `tests/bdd_test_deploy.py:30` | `def project(self)` |
| `test_commit_message_format_is_consistent` | method | `tests/bdd_test_deploy.py:69` | `def test_commit_message_format_is_consistent(self)` |
| `test_conventional_commit_parsing` | method | `tests/bdd_test_deploy.py:55` | `def test_conventional_commit_parsing(self)` |
| `test_docs_failure_does_not_block_release` | method | `tests/bdd_test_deploy.py:120` | `def test_docs_failure_does_not_block_release(self)` |
| `test_force_bump_overrides_commit_type` | method | `tests/bdd_test_deploy.py:137` | `def test_force_bump_overrides_commit_type(self)` |
| `test_tests_failure_blocks_release` | method | `tests/bdd_test_deploy.py:92` | `def test_tests_failure_blocks_release(self)` |
| `test_version_bump_by_commit_type` | method | `tests/bdd_test_deploy.py:46` | `def test_version_bump_by_commit_type(self, project, commit_type, expected_bump, initial, final)` |
| `test_version_is_max_file_tag` | method | `tests/bdd_test_deploy.py:144` | `def test_version_is_max_file_tag(self)` |
| `TestChangelogGenerator` | class | `tests/test_changelog.py:7` | `class TestChangelogGenerator` |
| `generator` | method | `tests/test_changelog.py:9` | `def generator(self)` |
| `test_format_for_release_short` | method | `tests/test_changelog.py:47` | `def test_format_for_release_short(self, generator)` |
| `test_format_for_release_truncated` | method | `tests/test_changelog.py:52` | `def test_format_for_release_truncated(self, generator)` |
| `test_generate_empty` | method | `tests/test_changelog.py:43` | `def test_generate_empty(self, generator)` |
| `test_generate_from_messages` | method | `tests/test_changelog.py:17` | `def test_generate_from_messages(self, generator)` |
| `test_generate_from_messages_organizes_by_type` | method | `tests/test_changelog.py:32` | `def test_generate_from_messages_organizes_by_type(self, generator)` |
| `test_generate_header` | method | `tests/test_changelog.py:13` | `def test_generate_header(self, generator)` |
| `TestCliMode` | class | `tests/test_cli_mcp.py:5` | `class TestCliMode` |
| `TestMCPServer` | class | `tests/test_cli_mcp.py:36` | `class TestMCPServer` |
| `_server` | method | `tests/test_cli_mcp.py:37` | `def _server(self, tmp)` |
| `test_bare_invokes_interactive` | method | `tests/test_cli_mcp.py:6` | `def test_bare_invokes_interactive(self, monkeypatch)` |
| `test_call_status_and_projects` | method | `tests/test_cli_mcp.py:56` | `def test_call_status_and_projects(self, tmp_path)` |
| `test_explicit_interactive_still_works` | method | `tests/test_cli_mcp.py:16` | `def test_explicit_interactive_still_works(self)` |
| `test_initialize_and_list` | method | `tests/test_cli_mcp.py:44` | `def test_initialize_and_list(self, tmp_path)` |
| `test_release_flags_headless` | method | `tests/test_cli_mcp.py:21` | `def test_release_flags_headless(self)` |
| `test_resources_list` | method | `tests/test_cli_mcp.py:83` | `def test_resources_list(self, tmp_path)` |
| `test_serve_command_exists` | method | `tests/test_cli_mcp.py:30` | `def test_serve_command_exists(self)` |
| `test_unknown_tool_errors` | method | `tests/test_cli_mcp.py:72` | `def test_unknown_tool_errors(self, tmp_path)` |
| `TestConfigContract` | class | `tests/test_config.py:5` | `class TestConfigContract` |
| `test_auth_checks` | method | `tests/test_config.py:34` | `def test_auth_checks(self, monkeypatch)` |
| `test_commit_type_pattern_valid` | method | `tests/test_config.py:52` | `def test_commit_type_pattern_valid(self)` |
| `test_config_frozen` | method | `tests/test_config.py:19` | `def test_config_frozen(self)` |
| `test_config_immutability` | method | `tests/test_config.py:24` | `def test_config_immutability(self)` |
| `test_config_with_overrides` | method | `tests/test_config.py:13` | `def test_config_with_overrides(self)` |
| `test_conventional_types_contains_all` | method | `tests/test_config.py:40` | `def test_conventional_types_contains_all(self)` |
| `test_default_config_creation` | method | `tests/test_config.py:6` | `def test_default_config_creation(self)` |
| `test_resolve_path` | method | `tests/test_config.py:30` | `def test_resolve_path(self)` |
| `test_semver_pattern_valid` | method | `tests/test_config.py:45` | `def test_semver_pattern_valid(self)` |
| `TestDeployOrchestrator` | class | `tests/test_deploy.py:81` | `class TestDeployOrchestrator` |
| `TestProjectDiscovery` | class | `tests/test_deploy.py:10` | `class TestProjectDiscovery` |
| `discovery` | method | `tests/test_deploy.py:12` | `def discovery(self)` |
| `test_discover_empty_dir` | method | `tests/test_deploy.py:16` | `def test_discover_empty_dir(self, discovery)` |
| `test_discover_ignores_non_yaml` | method | `tests/test_deploy.py:42` | `def test_discover_ignores_non_yaml(self, discovery)` |
| `test_discover_multiple_yamls` | method | `tests/test_deploy.py:32` | `def test_discover_multiple_yamls(self, discovery)` |
| `test_discover_single_yaml` | method | `tests/test_deploy.py:21` | `def test_discover_single_yaml(self, discovery)` |
| `test_find_by_name` | method | `tests/test_deploy.py:53` | `def test_find_by_name(self, discovery)` |
| `test_install_dependencies_file_not_found` | method | `tests/test_deploy.py:82` | `def test_install_dependencies_file_not_found(self)` |
| `test_load_single_from_deploynator_yaml` | method | `tests/test_deploy.py:64` | `def test_load_single_from_deploynator_yaml(self, discovery)` |
| `test_load_single_invalid` | method | `tests/test_deploy.py:72` | `def test_load_single_invalid(self, discovery)` |
| `TestChangelogEntryContract` | class | `tests/test_models.py:196` | `class TestChangelogEntryContract` |
| `TestCommitMessageContract` | class | `tests/test_models.py:65` | `class TestCommitMessageContract` |
| `TestCommitTypeContract` | class | `tests/test_models.py:34` | `class TestCommitTypeContract` |
| `TestDeployResultContract` | class | `tests/test_models.py:230` | `class TestDeployResultContract` |
| `TestPlatformConfigContract` | class | `tests/test_models.py:145` | `class TestPlatformConfigContract` |
| `TestPlatformContract` | class | `tests/test_models.py:10` | `class TestPlatformContract` |
| `TestProjectConfigContract` | class | `tests/test_models.py:160` | `class TestProjectConfigContract` |
| `TestReleaseInfoContract` | class | `tests/test_models.py:213` | `class TestReleaseInfoContract` |
| `TestVersionInfoContract` | class | `tests/test_models.py:107` | `class TestVersionInfoContract` |
| `test_bump_major` | method | `tests/test_models.py:118` | `def test_bump_major(self)` |
| `test_bump_minor` | method | `tests/test_models.py:123` | `def test_bump_minor(self)` |
| `test_bump_none` | method | `tests/test_models.py:133` | `def test_bump_none(self)` |
| `test_bump_patch` | method | `tests/test_models.py:128` | `def test_bump_patch(self)` |
| `test_bump_strategy` | method | `tests/test_models.py:51` | `def test_bump_strategy(self)` |
| `test_commit_type_from_string` | method | `tests/test_models.py:35` | `def test_commit_type_from_string(self)` |
| `test_commit_type_invalid` | method | `tests/test_models.py:40` | `def test_commit_type_invalid(self)` |
| `test_commit_type_valid_types` | method | `tests/test_models.py:44` | `def test_commit_type_valid_types(self)` |
| `test_custom` | method | `tests/test_models.py:220` | `def test_custom(self)` |
| `test_defaults` | method | `tests/test_models.py:214` | `def test_defaults(self)` |
| `test_defaults` | method | `tests/test_models.py:231` | `def test_defaults(self)` |
| `test_format_basic` | method | `tests/test_models.py:66` | `def test_format_basic(self)` |
| `test_format_with_body_and_footer` | method | `tests/test_models.py:80` | `def test_format_with_body_and_footer(self)` |
| `test_format_with_version` | method | `tests/test_models.py:71` | `def test_format_with_version(self)` |
| `test_from_dict_defaults` | method | `tests/test_models.py:153` | `def test_from_dict_defaults(self)` |
| `test_from_dict_full` | method | `tests/test_models.py:146` | `def test_from_dict_full(self)` |
| `test_from_dict_full` | method | `tests/test_models.py:169` | `def test_from_dict_full(self)` |
| `test_from_dict_minimal` | method | `tests/test_models.py:161` | `def test_from_dict_minimal(self)` |
| `test_from_dict_platform_string` | method | `tests/test_models.py:185` | `def test_from_dict_platform_string(self)` |
| `test_from_git_log_line` | method | `tests/test_models.py:197` | `def test_from_git_log_line(self)` |
| `test_from_git_log_line_scope` | method | `tests/test_models.py:208` | `def test_from_git_log_line_scope(self)` |
| `test_from_git_log_line_unparseable` | method | `tests/test_models.py:204` | `def test_from_git_log_line_unparseable(self)` |
| `test_parse` | method | `tests/test_models.py:108` | `def test_parse(self)` |
| `test_parse_invalid` | method | `tests/test_models.py:102` | `def test_parse_invalid(self)` |
| `test_parse_invalid` | method | `tests/test_models.py:138` | `def test_parse_invalid(self)` |
| `test_parse_no_scope` | method | `tests/test_models.py:96` | `def test_parse_no_scope(self)` |
| `test_parse_valid` | method | `tests/test_models.py:90` | `def test_parse_valid(self)` |
| `test_platform_auth_env` | method | `tests/test_models.py:29` | `def test_platform_auth_env(self)` |
| `test_platform_cli_name` | method | `tests/test_models.py:24` | `def test_platform_cli_name(self)` |
| `test_platform_from_string` | method | `tests/test_models.py:11` | `def test_platform_from_string(self)` |
| `test_platform_from_string_case` | method | `tests/test_models.py:16` | `def test_platform_from_string_case(self)` |
| `test_platform_from_string_invalid` | method | `tests/test_models.py:20` | `def test_platform_from_string_invalid(self)` |
| `test_section_header` | method | `tests/test_models.py:59` | `def test_section_header(self)` |
| `test_str` | method | `tests/test_models.py:114` | `def test_str(self)` |
| `test_with_data` | method | `tests/test_models.py:239` | `def test_with_data(self)` |
| `TestPathDirectRelease` | class | `tests/test_path_deploy.py:52` | `class TestPathDirectRelease` |
| `TestTagPrefixes` | class | `tests/test_path_deploy.py:18` | `class TestTagPrefixes` |
| `TestTomlVersionFile` | class | `tests/test_path_deploy.py:38` | `class TestTomlVersionFile` |
| `_git_init` | function | `tests/test_path_deploy.py:8` | `def _git_init(tmp)` |
| `test_name_wins_over_cwd_subdir` | method | `tests/test_path_deploy.py:95` | `def test_name_wins_over_cwd_subdir(self)` |
| `test_no_platforms_pushes_to_origin` | method | `tests/test_path_deploy.py:64` | `def test_no_platforms_pushes_to_origin(self)` |
| `test_release_by_path_dry_run` | method | `tests/test_path_deploy.py:53` | `def test_release_by_path_dry_run(self)` |
| `test_release_v_prefix` | method | `tests/test_path_deploy.py:19` | `def test_release_v_prefix(self)` |
| `test_v_prefix` | method | `tests/test_path_deploy.py:28` | `def test_v_prefix(self)` |
| `test_write_pyproject_toml` | method | `tests/test_path_deploy.py:39` | `def test_write_pyproject_toml(self)` |
| `TestDeployPipeline` | class | `tests/test_pipeline.py:53` | `class TestDeployPipeline` |
| `TestSemverMax` | class | `tests/test_pipeline.py:21` | `class TestSemverMax` |
| `_git_init` | function | `tests/test_pipeline.py:11` | `def _git_init(tmp)` |
| `_project` | method | `tests/test_pipeline.py:54` | `def _project(self, path)` |
| `test_aborts_on_test_failure` | method | `tests/test_pipeline.py:62` | `def test_aborts_on_test_failure(self)` |
| `test_current_is_max_of_file_and_tag` | method | `tests/test_pipeline.py:22` | `def test_current_is_max_of_file_and_tag(self)` |
| `test_docs_failure_does_not_block` | method | `tests/test_pipeline.py:103` | `def test_docs_failure_does_not_block(self)` |
| `test_dry_run_prints_would` | method | `tests/test_pipeline.py:144` | `def test_dry_run_prints_would(self, capsys)` |
| `test_file_ahead_of_tag` | method | `tests/test_pipeline.py:33` | `def test_file_ahead_of_tag(self)` |
| `test_force_bump_overrides` | method | `tests/test_pipeline.py:121` | `def test_force_bump_overrides(self)` |
| `test_max_version_helper` | method | `tests/test_pipeline.py:44` | `def test_max_version_helper(self)` |
| `test_no_test_skips_failing_tests` | method | `tests/test_pipeline.py:86` | `def test_no_test_skips_failing_tests(self)` |
| `TestCleanAndRun` | class | `tests/test_pypi.py:146` | `class TestCleanAndRun` |
| `TestDetect` | class | `tests/test_pypi.py:17` | `class TestDetect` |
| `TestPipelinePyPI` | class | `tests/test_pypi.py:188` | `class TestPipelinePyPI` |
| `TestPromptCredentials` | class | `tests/test_pypi.py:56` | `class TestPromptCredentials` |
| `_git_init` | function | `tests/test_pypi.py:7` | `def _git_init(tmp)` |
| `_toml` | method | `tests/test_pypi.py:147` | `def _toml(self)` |
| `test_clean_removes_dist` | method | `tests/test_pypi.py:156` | `def test_clean_removes_dist(self)` |
| `test_credentials_from_env` | method | `tests/test_pypi.py:40` | `def test_credentials_from_env(self, monkeypatch)` |
| `test_empty_dir_no_packaging` | method | `tests/test_pypi.py:26` | `def test_empty_dir_no_packaging(self)` |
| `test_no_credentials_skips_pypi` | method | `tests/test_pypi.py:221` | `def test_no_credentials_skips_pypi(self, monkeypatch)` |
| `test_no_shell_in_runner` | method | `tests/test_pypi.py:50` | `def test_no_shell_in_runner(self)` |
| `test_no_tty_returns_none` | method | `tests/test_pypi.py:57` | `def test_no_tty_returns_none(self, monkeypatch)` |
| `test_prompt_empty_token_returns_none` | method | `tests/test_pypi.py:73` | `def test_prompt_empty_token_returns_none(self, monkeypatch)` |
| `test_prompt_returns_token_without_save` | method | `tests/test_pypi.py:64` | `def test_prompt_returns_token_without_save(self, monkeypatch)` |
| `test_prompted_token_used_for_upload` | method | `tests/test_pypi.py:109` | `def test_prompted_token_used_for_upload(self, monkeypatch)` |
| `test_pypi_failure_aborts_with_error` | method | `tests/test_pypi.py:189` | `def test_pypi_failure_aborts_with_error(self, monkeypatch)` |
| `test_pyproject_with_project_table` | method | `tests/test_pypi.py:18` | `def test_pyproject_with_project_table(self)` |
| `test_run_fails_on_broken_build` | method | `tests/test_pypi.py:168` | `def test_run_fails_on_broken_build(self, monkeypatch)` |
| `test_run_skips_without_packaging` | method | `tests/test_pypi.py:179` | `def test_run_skips_without_packaging(self)` |
| `test_save_pypirc_rejects_symlink` | method | `tests/test_pypi.py:95` | `def test_save_pypirc_rejects_symlink(self)` |
| `test_save_pypirc_roundtrip` | method | `tests/test_pypi.py:81` | `def test_save_pypirc_roundtrip(self)` |
| `test_setup_py_counts` | method | `tests/test_pypi.py:32` | `def test_setup_py_counts(self)` |
| `TestDocsRunner` | class | `tests/test_runner.py:105` | `class TestDocsRunner` |
| `TestTestRunner` | class | `tests/test_runner.py:23` | `class TestTestRunner` |
| `_toml` | function | `tests/test_runner.py:7` | `def _toml(commands, timeout)` |
| `test_auto_false_skips` | method | `tests/test_runner.py:127` | `def test_auto_false_skips(self)` |
| `test_empty_commands_allow_no_tests_passes` | method | `tests/test_runner.py:58` | `def test_empty_commands_allow_no_tests_passes(self)` |
| `test_empty_commands_no_tests_dir_fails` | method | `tests/test_runner.py:49` | `def test_empty_commands_no_tests_dir_fails(self)` |
| `test_empty_string_command_rejected` | method | `tests/test_runner.py:96` | `def test_empty_string_command_rejected(self)` |
| `test_failing_command` | method | `tests/test_runner.py:32` | `def test_failing_command(self)` |
| `test_failing_docs_returns_false` | method | `tests/test_runner.py:113` | `def test_failing_docs_returns_false(self)` |
| `test_multiple_commands_stop_on_first_failure` | method | `tests/test_runner.py:41` | `def test_multiple_commands_stop_on_first_failure(self)` |
| `test_no_shell_injection` | method | `tests/test_runner.py:73` | `def test_no_shell_injection(self)` |
| `test_no_shell_injection` | method | `tests/test_runner.py:141` | `def test_no_shell_injection(self)` |
| `test_passing_command` | method | `tests/test_runner.py:24` | `def test_passing_command(self)` |
| `test_passing_docs` | method | `tests/test_runner.py:106` | `def test_passing_docs(self)` |
| `test_timeout_fails` | method | `tests/test_runner.py:87` | `def test_timeout_fails(self)` |
| `TestSemverManager` | class | `tests/test_semver.py:10` | `class TestSemverManager` |
| `manager` | method | `tests/test_semver.py:12` | `def manager(self)` |
| `test_calculate_next_version_major` | method | `tests/test_semver.py:43` | `def test_calculate_next_version_major(self, manager)` |
| `test_calculate_next_version_minor` | method | `tests/test_semver.py:48` | `def test_calculate_next_version_minor(self, manager)` |
| `test_calculate_next_version_none` | method | `tests/test_semver.py:58` | `def test_calculate_next_version_none(self, manager)` |
| `test_calculate_next_version_patch` | method | `tests/test_semver.py:53` | `def test_calculate_next_version_patch(self, manager)` |
| `test_determine_bump` | method | `tests/test_semver.py:37` | `def test_determine_bump(self, manager)` |
| `test_get_current_version_from_file` | method | `tests/test_semver.py:16` | `def test_get_current_version_from_file(self, manager)` |
| `test_get_current_version_no_file` | method | `tests/test_semver.py:24` | `def test_get_current_version_no_file(self, manager)` |
| `test_is_valid_version` | method | `tests/test_semver.py:72` | `def test_is_valid_version(self, manager, ver_str, expected)` |
| `test_write_version_file` | method | `tests/test_semver.py:29` | `def test_write_version_file(self, manager)` |
| `TestTomlConfig` | class | `tests/test_toml.py:7` | `class TestTomlConfig` |
| `test_frozen` | method | `tests/test_toml.py:76` | `def test_frozen(self)` |
| `test_load_missing_returns_defaults` | method | `tests/test_toml.py:8` | `def test_load_missing_returns_defaults(self)` |
| `test_load_valid_toml` | method | `tests/test_toml.py:18` | `def test_load_valid_toml(self)` |
| `test_malformed_toml_raises` | method | `tests/test_toml.py:56` | `def test_malformed_toml_raises(self)` |
| `test_oversize_rejected` | method | `tests/test_toml.py:48` | `def test_oversize_rejected(self)` |
| `test_symlink_rejected` | method | `tests/test_toml.py:37` | `def test_symlink_rejected(self)` |
| `test_timeout_clamped` | method | `tests/test_toml.py:64` | `def test_timeout_clamped(self)` |
