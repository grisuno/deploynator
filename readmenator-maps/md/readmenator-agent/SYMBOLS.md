# Symbols

| Symbol | Kind | File:Line | Signature |
|--------|------|-----------|-----------|
| `main` | function | `app.py:12` | `def main()` |
| `ensure_pkg` | function | `deploy.sh:22` | `` |
| `build_parser` | function | `deploynator/__main__.py:16` | `def build_parser()` |
| `main` | function | `deploynator/__main__.py:178` | `def main(argv)` |
| `preprocess_argv` | function | `deploynator/__main__.py:144` | `def preprocess_argv(argv)` |
| `DeploynatorApp` | class | `deploynator/_app.py:18` | `class DeploynatorApp` |
| `__init__` | method | `deploynator/_app.py:19` | `def __init__(self, config, workdir)` |
| `_auth_bitbucket` | method | `deploynator/_app.py:84` | `def _auth_bitbucket()` |
| `_auth_github` | method | `deploynator/_app.py:54` | `def _auth_github()` |
| `_auth_gitlab` | method | `deploynator/_app.py:67` | `def _auth_gitlab()` |
| `_interactive_auth` | method | `deploynator/_app.py:720` | `def _interactive_auth(self)` |
| `_interactive_auth_status` | method | `deploynator/_app.py:743` | `def _interactive_auth_status(self)` |
| `_interactive_ci` | method | `deploynator/_app.py:756` | `def _interactive_ci(self)` |
| `_interactive_commit` | method | `deploynator/_app.py:669` | `def _interactive_commit(self)` |
| `_interactive_docs` | method | `deploynator/_app.py:749` | `def _interactive_docs(self)` |
| `_interactive_init` | method | `deploynator/_app.py:770` | `def _interactive_init(self)` |
| `_interactive_release` | method | `deploynator/_app.py:623` | `def _interactive_release(self)` |
| `_interactive_start` | method | `deploynator/_app.py:696` | `def _interactive_start(self)` |
| `_interactive_status` | method | `deploynator/_app.py:765` | `def _interactive_status(self)` |
| `_is_path_like` | method | `deploynator/_app.py:267` | `def _is_path_like(value)` |
| `_looks_like_path` | method | `deploynator/_app.py:271` | `def _looks_like_path(value)` |
| `_parse_release_message` | method | `deploynator/_app.py:348` | `def _parse_release_message(raw)` |
| `_print_result` | method | `deploynator/_app.py:776` | `def _print_result(result)` |
| `_resolve_project_path` | method | `deploynator/_app.py:278` | `def _resolve_project_path(self, project_name)` |
| `_smart_prepare` | method | `deploynator/_app.py:292` | `def _smart_prepare(self, base, changelog_content, dry_run)` |
| `auth_login` | method | `deploynator/_app.py:29` | `def auth_login(self, platforms)` |
| `auth_status` | method | `deploynator/_app.py:43` | `def auth_status(self)` |
| `commit` | method | `deploynator/_app.py:307` | `def commit(self, commit_type, subject, scope, body, project_path, project_name, dry_run)` |
| `generate_ci` | method | `deploynator/_app.py:533` | `def generate_ci(self, project_name, all_projects)` |
| `generate_docs` | method | `deploynator/_app.py:502` | `def generate_docs(self, project_path, project_name)` |
| `init_project` | method | `deploynator/_app.py:172` | `def init_project(self, project_path, name)` |
| `install_deps` | method | `deploynator/_app.py:549` | `def install_deps(self, project_name)` |
| `install_packages` | method | `deploynator/_app.py:560` | `def install_packages(self, packages)` |
| `interactive_menu` | method | `deploynator/_app.py:587` | `def interactive_menu(self)` |
| `list_projects` | method | `deploynator/_app.py:528` | `def list_projects(self, search_path)` |
| `release` | method | `deploynator/_app.py:366` | `def release(self, commit_type, subject, scope, body, message, project_name, bump, dry_run, platforms, all_projects...` |
| `start_branch` | method | `deploynator/_app.py:249` | `def start_branch(self, commit_type, description, project_path, project_name, remote)` |
| `status` | method | `deploynator/_app.py:508` | `def status(self, project_path, project_name)` |
| `ChangelogGenerator` | class | `deploynator/_changelog.py:11` | `class ChangelogGenerator` |
| `__init__` | method | `deploynator/_changelog.py:12` | `def __init__(self, config)` |
| `_collect_entries` | method | `deploynator/_changelog.py:47` | `def _collect_entries(self, repo_path, from_ref, to_ref)` |
| `_format_entries` | method | `deploynator/_changelog.py:68` | `def _format_entries(self, entries)` |
| `format_for_release` | method | `deploynator/_changelog.py:108` | `def format_for_release(self, changelog_content, max_chars)` |
| `generate_from_log` | method | `deploynator/_changelog.py:15` | `def generate_from_log(self, repo_path, from_ref, to_ref)` |
| `generate_from_messages` | method | `deploynator/_changelog.py:24` | `def generate_from_messages(self, messages)` |
| `generate_header` | method | `deploynator/_changelog.py:44` | `def generate_header(self)` |
| `write_changelog` | method | `deploynator/_changelog.py:99` | `def write_changelog(self, repo_path, content, filename)` |
| `Config` | class | `deploynator/_config.py:8` | `class Config` |
| `bb_authd` | method | `deploynator/_config.py:100` | `def bb_authd(self)` |
| `create` | method | `deploynator/_config.py:80` | `def create(overrides)` |
| `gh_authd` | method | `deploynator/_config.py:92` | `def gh_authd(self)` |
| `glab_authd` | method | `deploynator/_config.py:96` | `def glab_authd(self)` |
| `resolve_path` | method | `deploynator/_config.py:86` | `def resolve_path(self)` |
| `DeployOrchestrator` | class | `deploynator/_deploy.py:74` | `class DeployOrchestrator` |
| `ProjectDiscovery` | class | `deploynator/_deploy.py:29` | `class ProjectDiscovery` |
| `__init__` | method | `deploynator/_deploy.py:30` | `def __init__(self, config)` |
| `__init__` | method | `deploynator/_deploy.py:75` | `def __init__(self, config)` |
| `_add_temp_remote` | method | `deploynator/_deploy.py:410` | `def _add_temp_remote(self, repo_path, name, url)` |
| `_ci_workflow_content` | method | `deploynator/_deploy.py:484` | `def _ci_workflow_content(self, project)` |
| `_get_remote_url` | method | `deploynator/_deploy.py:456` | `def _get_remote_url(repo_path, pc)` |
| `_gh_release_in_repo` | method | `deploynator/_deploy.py:377` | `def _gh_release_in_repo(self, repo_path, project_name, version, notes, branch)` |
| `_listed` | function | `deploynator/_deploy.py:197` | `def _listed(files)` |
| `_load_single` | method | `deploynator/_deploy.py:61` | `def _load_single(yaml_path)` |
| `_release_workflow_content` | method | `deploynator/_deploy.py:505` | `def _release_workflow_content(self, project)` |
| `_remove_temp_remote` | method | `deploynator/_deploy.py:419` | `def _remove_temp_remote(self, repo_path, name)` |
| `_resolve_project_path` | method | `deploynator/_deploy.py:86` | `def _resolve_project_path(project)` |
| `_sync_dev_to_main` | method | `deploynator/_deploy.py:428` | `def _sync_dev_to_main(self, repo_path)` |
| `deploy` | method | `deploynator/_deploy.py:95` | `def deploy(self, project, commit_type, subject, scope, body, dry_run, platforms_override, run_tests, run_docs...` |
| `discover` | method | `deploynator/_deploy.py:33` | `def discover(self, search_path)` |
| `find_by_name` | method | `deploynator/_deploy.py:54` | `def find_by_name(self, name, search_path)` |
| `generate_workflows` | method | `deploynator/_deploy.py:465` | `def generate_workflows(self, project, output_dir)` |
| `install_dependencies` | method | `deploynator/_deploy.py:532` | `def install_dependencies(self, project)` |
| `install_lazygit` | method | `deploynator/_deploy.py:578` | `def install_lazygit(self)` |
| `integrate_readmenator` | method | `deploynator/_deploy.py:542` | `def integrate_readmenator(self, project_path)` |
| `DocsRunner` | class | `deploynator/_docs.py:10` | `class DocsRunner` |
| `__init__` | method | `deploynator/_docs.py:11` | `def __init__(self, config)` |
| `run` | method | `deploynator/_docs.py:14` | `def run(self, project_path, toml)` |
| `GitOperations` | class | `deploynator/_git.py:9` | `class GitOperations` |
| `__init__` | method | `deploynator/_git.py:10` | `def __init__(self, config)` |
| `add_all` | method | `deploynator/_git.py:45` | `def add_all(self, repo_path)` |
| `amend_no_edit` | method | `deploynator/_git.py:87` | `def amend_no_edit(self, repo_path)` |
| `branch_exists` | method | `deploynator/_git.py:265` | `def branch_exists(self, repo_path, branch)` |
| `check_gpg` | method | `deploynator/_git.py:13` | `def check_gpg(self)` |
| `checkout` | method | `deploynator/_git.py:162` | `def checkout(self, repo_path, branch)` |
| `clone` | method | `deploynator/_git.py:35` | `def clone(self, url, dest, depth)` |
| `commit` | method | `deploynator/_git.py:58` | `def commit(self, repo_path, message)` |
| `create_branch` | method | `deploynator/_git.py:146` | `def create_branch(self, repo_path, branch_name, base)` |
| `current_branch` | method | `deploynator/_git.py:233` | `def current_branch(self, repo_path)` |
| `delete_tag` | method | `deploynator/_git.py:106` | `def delete_tag(self, repo_path, tag_name)` |
| `get_changed_files` | method | `deploynator/_git.py:172` | `def get_changed_files(self, repo_path, from_ref, to_ref)` |
| `get_log` | method | `deploynator/_git.py:203` | `def get_log(self, repo_path, from_ref, to_ref, format_str)` |
| `get_start_ref` | method | `deploynator/_git.py:215` | `def get_start_ref(self, repo_path)` |
| `gpg_sign_flag` | method | `deploynator/_git.py:31` | `def gpg_sign_flag(self)` |
| `has_remote` | method | `deploynator/_git.py:255` | `def has_remote(self, repo_path, remote)` |
| `is_behind` | method | `deploynator/_git.py:275` | `def is_behind(self, repo_path, behind_branch, ahead_branch)` |
| `is_dirty` | method | `deploynator/_git.py:245` | `def is_dirty(self, repo_path)` |
| `push` | method | `deploynator/_git.py:126` | `def push(self, repo_path, remote, branch, follow_tags)` |
| `push_force` | method | `deploynator/_git.py:290` | `def push_force(self, repo_path, remote, src_branch, dst_branch)` |
| `push_tags` | method | `deploynator/_git.py:136` | `def push_tags(self, repo_path, remote)` |
| `tag` | method | `deploynator/_git.py:96` | `def tag(self, repo_path, tag_name, message)` |
| `tag_exists` | method | `deploynator/_git.py:116` | `def tag_exists(self, repo_path, tag_name)` |
| `MCPRequest` | class | `deploynator/_mcp_server.py:36` | `class MCPRequest` |
| `MCPResource` | class | `deploynator/_mcp_server.py:72` | `class MCPResource` |
| `MCPServer` | class | `deploynator/_mcp_server.py:87` | `class MCPServer` |
| `MCPTool` | class | `deploynator/_mcp_server.py:57` | `class MCPTool` |
| `__init__` | method | `deploynator/_mcp_server.py:37` | `def __init__(self, msg)` |
| `__init__` | method | `deploynator/_mcp_server.py:58` | `def __init__(self, name, description, handler, input_schema)` |
| `__init__` | method | `deploynator/_mcp_server.py:73` | `def __init__(self, uri, name, description, mime_type, handler)` |
| `__init__` | method | `deploynator/_mcp_server.py:88` | `def __init__(self, app, target_dir)` |
| `_handle_call_tool` | method | `deploynator/_mcp_server.py:112` | `def _handle_call_tool(self, req)` |
| `_handle_initialize` | method | `deploynator/_mcp_server.py:101` | `def _handle_initialize(self, req)` |
| `_handle_list_resources` | method | `deploynator/_mcp_server.py:129` | `def _handle_list_resources(self, req)` |
| `_handle_list_tools` | method | `deploynator/_mcp_server.py:109` | `def _handle_list_tools(self, req)` |
| `_handle_read_resource` | method | `deploynator/_mcp_server.py:132` | `def _handle_read_resource(self, req)` |
| `_register_all` | method | `deploynator/_mcp_server.py:181` | `def _register_all(self)` |
| `_resource_projects` | method | `deploynator/_mcp_server.py:267` | `def _resource_projects(self)` |
| `_tool_commit` | method | `deploynator/_mcp_server.py:250` | `def _tool_commit(self, commit_type, subject, project, scope, body, dry_run)` |
| `_tool_docs` | method | `deploynator/_mcp_server.py:263` | `def _tool_docs(self, project)` |
| `_tool_projects` | method | `deploynator/_mcp_server.py:257` | `def _tool_projects(self)` |
| `_tool_release` | method | `deploynator/_mcp_server.py:235` | `def _tool_release(self, project, commit_type, subject, message, scope, body, bump, dry_run, no_test, no_docs, no_pypi)` |
| `_tool_status` | method | `deploynator/_mcp_server.py:254` | `def _tool_status(self, project)` |
| `call` | method | `deploynator/_mcp_server.py:68` | `def call(self, arguments)` |
| `definition` | method | `deploynator/_mcp_server.py:65` | `def definition(self)` |
| `definition` | method | `deploynator/_mcp_server.py:80` | `def definition(self)` |
| `dispatch` | method | `deploynator/_mcp_server.py:145` | `def dispatch(self, req)` |
| `error` | method | `deploynator/_mcp_server.py:50` | `def error(self, code, message, data)` |
| `is_notification` | method | `deploynator/_mcp_server.py:44` | `def is_notification(self)` |
| `main` | function | `deploynator/_mcp_server.py:271` | `def main()` |
| `read` | method | `deploynator/_mcp_server.py:83` | `def read(self)` |
| `register_resource` | method | `deploynator/_mcp_server.py:98` | `def register_resource(self, resource)` |
| `register_tool` | method | `deploynator/_mcp_server.py:95` | `def register_tool(self, tool)` |
| `response` | method | `deploynator/_mcp_server.py:47` | `def response(self, result)` |
| `run` | method | `deploynator/_mcp_server.py:163` | `def run(self)` |
| `ChangelogEntry` | class | `deploynator/_models.py:238` | `class ChangelogEntry` |
| `CommitMessage` | class | `deploynator/_models.py:174` | `class CommitMessage` |
| `CommitType` | class | `deploynator/_models.py:44` | `class CommitType(Enum)` |
| `DeployResult` | class | `deploynator/_models.py:275` | `class DeployResult` |
| `Platform` | class | `deploynator/_models.py:9` | `class Platform(Enum)` |
| `PlatformConfig` | class | `deploynator/_models.py:97` | `class PlatformConfig` |
| `ProjectConfig` | class | `deploynator/_models.py:129` | `class ProjectConfig` |
| `ReleaseInfo` | class | `deploynator/_models.py:265` | `class ReleaseInfo` |
| `VersionConfig` | class | `deploynator/_models.py:114` | `class VersionConfig` |
| `VersionInfo` | class | `deploynator/_models.py:207` | `class VersionInfo` |
| `__str__` | method | `deploynator/_models.py:212` | `def __str__(self)` |
| `auth_env_var` | method | `deploynator/_models.py:36` | `def auth_env_var(self)` |
| `bump` | method | `deploynator/_models.py:227` | `def bump(self, strategy)` |
| `bump_strategy` | method | `deploynator/_models.py:67` | `def bump_strategy(self)` |
| `cli_name` | method | `deploynator/_models.py:29` | `def cli_name(self)` |
| `format` | method | `deploynator/_models.py:182` | `def format(self)` |
| `from_dict` | method | `deploynator/_models.py:104` | `def from_dict(cls, data)` |
| `from_dict` | method | `deploynator/_models.py:120` | `def from_dict(cls, data)` |
| `from_dict` | method | `deploynator/_models.py:138` | `def from_dict(cls, data)` |
| `from_git_log_line` | method | `deploynator/_models.py:246` | `def from_git_log_line(cls, line, author, sha)` |
| `from_string` | method | `deploynator/_models.py:15` | `def from_string(cls, name)` |
| `from_string` | method | `deploynator/_models.py:57` | `def from_string(cls, value)` |
| `label` | method | `deploynator/_models.py:26` | `def label(self)` |
| `parse` | method | `deploynator/_models.py:194` | `def parse(cls, raw)` |
| `parse` | method | `deploynator/_models.py:216` | `def parse(cls, version_str)` |
| `section_header` | method | `deploynator/_models.py:81` | `def section_header(self)` |
| `valid_types` | method | `deploynator/_models.py:64` | `def valid_types(cls)` |
| `BitbucketCLI` | class | `deploynator/_platforms.py:163` | `class BitbucketCLI(PlatformClient)` |
| `GitHubCLI` | class | `deploynator/_platforms.py:48` | `class GitHubCLI(PlatformClient)` |
| `GitLabCLI` | class | `deploynator/_platforms.py:112` | `class GitLabCLI(PlatformClient)` |
| `PlatformClient` | class | `deploynator/_platforms.py:13` | `class PlatformClient(ABC)` |
| `PlatformFactory` | class | `deploynator/_platforms.py:222` | `class PlatformFactory` |
| `__init__` | method | `deploynator/_platforms.py:14` | `def __init__(self, config)` |
| `_run` | method | `deploynator/_platforms.py:41` | `def _run(self, cmd, cwd, check)` |
| `create` | method | `deploynator/_platforms.py:234` | `def create(cls, platform, config)` |
| `create_all_available` | method | `deploynator/_platforms.py:241` | `def create_all_available(cls, config)` |
| `create_pull_request` | method | `deploynator/_platforms.py:34` | `def create_pull_request(self, repo, title, body, head, base)` |
| `create_pull_request` | method | `deploynator/_platforms.py:90` | `def create_pull_request(self, repo, title, body, head, base)` |
| `create_pull_request` | method | `deploynator/_platforms.py:141` | `def create_pull_request(self, repo, title, body, head, base)` |
| `create_pull_request` | method | `deploynator/_platforms.py:200` | `def create_pull_request(self, repo, title, body, head, base)` |
| `create_release` | method | `deploynator/_platforms.py:30` | `def create_release(self, repo, release)` |
| `create_release` | method | `deploynator/_platforms.py:66` | `def create_release(self, repo, release)` |
| `create_release` | method | `deploynator/_platforms.py:130` | `def create_release(self, repo, release)` |
| `create_release` | method | `deploynator/_platforms.py:180` | `def create_release(self, repo, release)` |
| `is_authenticated` | method | `deploynator/_platforms.py:26` | `def is_authenticated(self)` |
| `is_authenticated` | method | `deploynator/_platforms.py:59` | `def is_authenticated(self)` |
| `is_authenticated` | method | `deploynator/_platforms.py:123` | `def is_authenticated(self)` |
| `is_authenticated` | method | `deploynator/_platforms.py:177` | `def is_authenticated(self)` |
| `is_available` | method | `deploynator/_platforms.py:22` | `def is_available(self)` |
| `is_available` | method | `deploynator/_platforms.py:52` | `def is_available(self)` |
| `is_available` | method | `deploynator/_platforms.py:116` | `def is_available(self)` |
| `is_available` | method | `deploynator/_platforms.py:167` | `def is_available(self)` |
| `name` | method | `deploynator/_platforms.py:18` | `def name(self)` |
| `name` | method | `deploynator/_platforms.py:49` | `def name(self)` |
| `name` | method | `deploynator/_platforms.py:113` | `def name(self)` |
| `name` | method | `deploynator/_platforms.py:164` | `def name(self)` |
| `push_changes` | method | `deploynator/_platforms.py:38` | `def push_changes(self, repo_path, remote, branch, tags)` |
| `push_changes` | method | `deploynator/_platforms.py:104` | `def push_changes(self, repo_path, remote, branch, tags)` |
| `push_changes` | method | `deploynator/_platforms.py:155` | `def push_changes(self, repo_path, remote, branch, tags)` |
| `push_changes` | method | `deploynator/_platforms.py:214` | `def push_changes(self, repo_path, remote, branch, tags)` |
| `register` | method | `deploynator/_platforms.py:230` | `def register(cls, platform, client_class)` |
| `PyPIRunner` | class | `deploynator/_pypi.py:12` | `class PyPIRunner` |
| `__init__` | method | `deploynator/_pypi.py:13` | `def __init__(self, config)` |
| `clean` | method | `deploynator/_pypi.py:90` | `def clean(self, project_path, toml)` |
| `has_credentials` | method | `deploynator/_pypi.py:33` | `def has_credentials(self)` |
| `is_packaging_project` | method | `deploynator/_pypi.py:16` | `def is_packaging_project(self, project_path)` |
| `prompt_for_credentials` | method | `deploynator/_pypi.py:39` | `def prompt_for_credentials(self)` |
| `run` | method | `deploynator/_pypi.py:107` | `def run(self, project_path, toml, version, token, verbose)` |
| `save_pypirc` | method | `deploynator/_pypi.py:72` | `def save_pypirc(self, token, path)` |
| `_find_readme` | function | `deploynator/_readme.py:31` | `def _find_readme(repo_path)` |
| `ensure_deployed_footer` | function | `deploynator/_readme.py:48` | `def ensure_deployed_footer(repo_path, config)` |
| `footer_block` | function | `deploynator/_readme.py:18` | `def footer_block(config)` |
| `footer_line` | function | `deploynator/_readme.py:95` | `def footer_line(config)` |
| `TestRunner` | class | `deploynator/_runner.py:11` | `class TestRunner` |
| `__init__` | method | `deploynator/_runner.py:12` | `def __init__(self, config)` |
| `run` | method | `deploynator/_runner.py:15` | `def run(self, project_path, toml)` |
| `SemverManager` | class | `deploynator/_semver.py:11` | `class SemverManager` |
| `__init__` | method | `deploynator/_semver.py:12` | `def __init__(self, config)` |
| `_get_latest_tag` | method | `deploynator/_semver.py:121` | `def _get_latest_tag(self, project_path)` |
| `calculate_next_version` | method | `deploynator/_semver.py:113` | `def calculate_next_version(self, current, strategy)` |
| `determine_bump` | method | `deploynator/_semver.py:110` | `def determine_bump(self, commit_type)` |
| `get_current_version` | method | `deploynator/_semver.py:20` | `def get_current_version(self, project_path, version_file, version_pattern)` |
| `is_valid_version` | method | `deploynator/_semver.py:117` | `def is_valid_version(version_str)` |
| `max_version` | method | `deploynator/_semver.py:15` | `def max_version(self, a, b)` |
| `write_version_file` | method | `deploynator/_semver.py:65` | `def write_version_file(self, project_path, version, version_file)` |
| `TomlConfig` | class | `deploynator/_toml.py:177` | `class TomlConfig` |
| `__post_init__` | method | `deploynator/_toml.py:194` | `def __post_init__(self)` |
| `_auto_toml_config` | function | `deploynator/_toml.py:150` | `def _auto_toml_config(project_path)` |
| `_clamp_timeout` | function | `deploynator/_toml.py:202` | `def _clamp_timeout(value)` |
| `_has_python_tests` | function | `deploynator/_toml.py:63` | `def _has_python_tests(project_path)` |
| `_target_regex` | function | `deploynator/_toml.py:23` | `def _target_regex()` |
| `detect_test_commands` | function | `deploynator/_toml.py:101` | `def detect_test_commands(project_path)` |
| `list_make_targets` | function | `deploynator/_toml.py:31` | `def list_make_targets(project_path)` |
| `load_toml_config` | function | `deploynator/_toml.py:210` | `def load_toml_config(project_path)` |
| `looks_like_packaging_project` | function | `deploynator/_toml.py:75` | `def looks_like_packaging_project(project_path)` |
| `TestBDDDeployScenarios` | class | `tests/bdd_test_deploy.py:29` | `class TestBDDDeployScenarios` |
| `TestBDDPipeline` | class | `tests/bdd_test_deploy.py:85` | `class TestBDDPipeline` |
| `project` | method | `tests/bdd_test_deploy.py:31` | `def project(self)` |
| `test_commit_message_format_is_consistent` | method | `tests/bdd_test_deploy.py:70` | `def test_commit_message_format_is_consistent(self)` |
| `test_conventional_commit_parsing` | method | `tests/bdd_test_deploy.py:56` | `def test_conventional_commit_parsing(self)` |
| `test_docs_failure_does_not_block_release` | method | `tests/bdd_test_deploy.py:122` | `def test_docs_failure_does_not_block_release(self)` |
| `test_force_bump_overrides_commit_type` | method | `tests/bdd_test_deploy.py:139` | `def test_force_bump_overrides_commit_type(self)` |
| `test_tests_failure_blocks_release` | method | `tests/bdd_test_deploy.py:93` | `def test_tests_failure_blocks_release(self)` |
| `test_version_bump_by_commit_type` | method | `tests/bdd_test_deploy.py:47` | `def test_version_bump_by_commit_type(self, project, commit_type, expected_bump, initial, final)` |
| `test_version_is_max_file_tag` | method | `tests/bdd_test_deploy.py:146` | `def test_version_is_max_file_tag(self)` |
| `TestChangelogGenerator` | class | `tests/test_changelog.py:7` | `class TestChangelogGenerator` |
| `generator` | method | `tests/test_changelog.py:9` | `def generator(self)` |
| `test_format_for_release_short` | method | `tests/test_changelog.py:47` | `def test_format_for_release_short(self, generator)` |
| `test_format_for_release_truncated` | method | `tests/test_changelog.py:52` | `def test_format_for_release_truncated(self, generator)` |
| `test_generate_empty` | method | `tests/test_changelog.py:43` | `def test_generate_empty(self, generator)` |
| `test_generate_from_messages` | method | `tests/test_changelog.py:17` | `def test_generate_from_messages(self, generator)` |
| `test_generate_from_messages_organizes_by_type` | method | `tests/test_changelog.py:32` | `def test_generate_from_messages_organizes_by_type(self, generator)` |
| `test_generate_header` | method | `tests/test_changelog.py:13` | `def test_generate_header(self, generator)` |
| `TestCliMode` | class | `tests/test_cli_mcp.py:4` | `class TestCliMode` |
| `TestMCPServer` | class | `tests/test_cli_mcp.py:35` | `class TestMCPServer` |
| `_server` | method | `tests/test_cli_mcp.py:36` | `def _server(self, tmp)` |
| `test_bare_invokes_interactive` | method | `tests/test_cli_mcp.py:5` | `def test_bare_invokes_interactive(self, monkeypatch)` |
| `test_call_status_and_projects` | method | `tests/test_cli_mcp.py:55` | `def test_call_status_and_projects(self, tmp_path)` |
| `test_explicit_interactive_still_works` | method | `tests/test_cli_mcp.py:15` | `def test_explicit_interactive_still_works(self)` |
| `test_initialize_and_list` | method | `tests/test_cli_mcp.py:43` | `def test_initialize_and_list(self, tmp_path)` |
| `test_release_flags_headless` | method | `tests/test_cli_mcp.py:20` | `def test_release_flags_headless(self)` |
| `test_resources_list` | method | `tests/test_cli_mcp.py:82` | `def test_resources_list(self, tmp_path)` |
| `test_serve_command_exists` | method | `tests/test_cli_mcp.py:29` | `def test_serve_command_exists(self)` |
| `test_unknown_tool_errors` | method | `tests/test_cli_mcp.py:71` | `def test_unknown_tool_errors(self, tmp_path)` |
| `TestConfigContract` | class | `tests/test_config.py:8` | `class TestConfigContract` |
| `test_auth_checks` | method | `tests/test_config.py:37` | `def test_auth_checks(self, monkeypatch)` |
| `test_commit_type_pattern_valid` | method | `tests/test_config.py:55` | `def test_commit_type_pattern_valid(self)` |
| `test_config_frozen` | method | `tests/test_config.py:22` | `def test_config_frozen(self)` |
| `test_config_immutability` | method | `tests/test_config.py:27` | `def test_config_immutability(self)` |
| `test_config_with_overrides` | method | `tests/test_config.py:16` | `def test_config_with_overrides(self)` |
| `test_conventional_types_contains_all` | method | `tests/test_config.py:43` | `def test_conventional_types_contains_all(self)` |
| `test_default_config_creation` | method | `tests/test_config.py:9` | `def test_default_config_creation(self)` |
| `test_resolve_path` | method | `tests/test_config.py:33` | `def test_resolve_path(self)` |
| `test_semver_pattern_valid` | method | `tests/test_config.py:48` | `def test_semver_pattern_valid(self)` |
| `TestDeployOrchestrator` | class | `tests/test_deploy.py:82` | `class TestDeployOrchestrator` |
| `TestProjectDiscovery` | class | `tests/test_deploy.py:11` | `class TestProjectDiscovery` |
| `discovery` | method | `tests/test_deploy.py:13` | `def discovery(self)` |
| `test_discover_empty_dir` | method | `tests/test_deploy.py:17` | `def test_discover_empty_dir(self, discovery)` |
| `test_discover_ignores_non_yaml` | method | `tests/test_deploy.py:43` | `def test_discover_ignores_non_yaml(self, discovery)` |
| `test_discover_multiple_yamls` | method | `tests/test_deploy.py:33` | `def test_discover_multiple_yamls(self, discovery)` |
| `test_discover_single_yaml` | method | `tests/test_deploy.py:22` | `def test_discover_single_yaml(self, discovery)` |
| `test_find_by_name` | method | `tests/test_deploy.py:54` | `def test_find_by_name(self, discovery)` |
| `test_install_dependencies_file_not_found` | method | `tests/test_deploy.py:83` | `def test_install_dependencies_file_not_found(self)` |
| `test_load_single_from_deploynator_yaml` | method | `tests/test_deploy.py:65` | `def test_load_single_from_deploynator_yaml(self, discovery)` |
| `test_load_single_invalid` | method | `tests/test_deploy.py:73` | `def test_load_single_invalid(self, discovery)` |
| `TestGitSync` | class | `tests/test_git_sync.py:15` | `class TestGitSync` |
| `_config_git` | function | `tests/test_git_sync.py:10` | `def _config_git(path)` |
| `_make_repo` | method | `tests/test_git_sync.py:16` | `def _make_repo(self, tmp)` |
| `test_branch_exists_is_behind` | method | `tests/test_git_sync.py:22` | `def test_branch_exists_is_behind(self)` |
| `test_sync_dev_to_main_force_pushes` | method | `tests/test_git_sync.py:46` | `def test_sync_dev_to_main_force_pushes(self)` |
| `test_sync_noop_when_dev_equal_or_missing` | method | `tests/test_git_sync.py:80` | `def test_sync_noop_when_dev_equal_or_missing(self)` |
| `TestInitScript` | class | `tests/test_init.py:7` | `class TestInitScript` |
| `test_deploy_sh_content_generic` | method | `tests/test_init.py:32` | `def test_deploy_sh_content_generic(self)` |
| `test_deploy_sh_executable_and_valid_bash` | method | `tests/test_init.py:20` | `def test_deploy_sh_executable_and_valid_bash(self)` |
| `test_init_creates_files` | method | `tests/test_init.py:8` | `def test_init_creates_files(self)` |
| `test_init_no_overwrite` | method | `tests/test_init.py:50` | `def test_init_no_overwrite(self)` |
| `test_toml_starter_parseable` | method | `tests/test_init.py:64` | `def test_toml_starter_parseable(self)` |
| `R` | class | `tests/test_install_example.py:19` | `class R` |
| `TestAppExample` | class | `tests/test_install_example.py:56` | `class TestAppExample` |
| `TestInstallPackages` | class | `tests/test_install_example.py:5` | `class TestInstallPackages` |
| `fake_run` | function | `tests/test_install_example.py:17` | `def fake_run(cmd)` |
| `fake_run` | function | `tests/test_install_example.py:35` | `def fake_run(cmd)` |
| `test_cli_install_parses_packages` | method | `tests/test_install_example.py:47` | `def test_cli_install_parses_packages(self)` |
| `test_default_targets_deploynator` | method | `tests/test_install_example.py:11` | `def test_default_targets_deploynator(self, monkeypatch)` |
| `test_empty_is_noop` | method | `tests/test_install_example.py:6` | `def test_empty_is_noop(self)` |
| `test_example_exists_and_compiles` | method | `tests/test_install_example.py:57` | `def test_example_exists_and_compiles(self)` |
| `test_example_uses_library` | method | `tests/test_install_example.py:64` | `def test_example_uses_library(self)` |
| `test_failure_reported` | method | `tests/test_install_example.py:29` | `def test_failure_reported(self, monkeypatch)` |
| `test_no_shell` | method | `tests/test_install_example.py:40` | `def test_no_shell(self)` |
| `TestChangelogEntryContract` | class | `tests/test_models.py:204` | `class TestChangelogEntryContract` |
| `TestCommitMessageContract` | class | `tests/test_models.py:73` | `class TestCommitMessageContract` |
| `TestCommitTypeContract` | class | `tests/test_models.py:42` | `class TestCommitTypeContract` |
| `TestDeployResultContract` | class | `tests/test_models.py:238` | `class TestDeployResultContract` |
| `TestPlatformConfigContract` | class | `tests/test_models.py:153` | `class TestPlatformConfigContract` |
| `TestPlatformContract` | class | `tests/test_models.py:18` | `class TestPlatformContract` |
| `TestProjectConfigContract` | class | `tests/test_models.py:168` | `class TestProjectConfigContract` |
| `TestReleaseInfoContract` | class | `tests/test_models.py:221` | `class TestReleaseInfoContract` |
| `TestVersionInfoContract` | class | `tests/test_models.py:115` | `class TestVersionInfoContract` |
| `test_bump_major` | method | `tests/test_models.py:126` | `def test_bump_major(self)` |
| `test_bump_minor` | method | `tests/test_models.py:131` | `def test_bump_minor(self)` |
| `test_bump_none` | method | `tests/test_models.py:141` | `def test_bump_none(self)` |
| `test_bump_patch` | method | `tests/test_models.py:136` | `def test_bump_patch(self)` |
| `test_bump_strategy` | method | `tests/test_models.py:59` | `def test_bump_strategy(self)` |
| `test_commit_type_from_string` | method | `tests/test_models.py:43` | `def test_commit_type_from_string(self)` |
| `test_commit_type_invalid` | method | `tests/test_models.py:48` | `def test_commit_type_invalid(self)` |
| `test_commit_type_valid_types` | method | `tests/test_models.py:52` | `def test_commit_type_valid_types(self)` |
| `test_custom` | method | `tests/test_models.py:228` | `def test_custom(self)` |
| `test_defaults` | method | `tests/test_models.py:222` | `def test_defaults(self)` |
| `test_defaults` | method | `tests/test_models.py:239` | `def test_defaults(self)` |
| `test_format_basic` | method | `tests/test_models.py:74` | `def test_format_basic(self)` |
| `test_format_with_body_and_footer` | method | `tests/test_models.py:88` | `def test_format_with_body_and_footer(self)` |
| `test_format_with_version` | method | `tests/test_models.py:79` | `def test_format_with_version(self)` |
| `test_from_dict_defaults` | method | `tests/test_models.py:161` | `def test_from_dict_defaults(self)` |
| `test_from_dict_full` | method | `tests/test_models.py:154` | `def test_from_dict_full(self)` |
| `test_from_dict_full` | method | `tests/test_models.py:177` | `def test_from_dict_full(self)` |
| `test_from_dict_minimal` | method | `tests/test_models.py:169` | `def test_from_dict_minimal(self)` |
| `test_from_dict_platform_string` | method | `tests/test_models.py:193` | `def test_from_dict_platform_string(self)` |
| `test_from_git_log_line` | method | `tests/test_models.py:205` | `def test_from_git_log_line(self)` |
| `test_from_git_log_line_scope` | method | `tests/test_models.py:216` | `def test_from_git_log_line_scope(self)` |
| `test_from_git_log_line_unparseable` | method | `tests/test_models.py:212` | `def test_from_git_log_line_unparseable(self)` |
| `test_parse` | method | `tests/test_models.py:116` | `def test_parse(self)` |
| `test_parse_invalid` | method | `tests/test_models.py:110` | `def test_parse_invalid(self)` |
| `test_parse_invalid` | method | `tests/test_models.py:146` | `def test_parse_invalid(self)` |
| `test_parse_no_scope` | method | `tests/test_models.py:104` | `def test_parse_no_scope(self)` |
| `test_parse_valid` | method | `tests/test_models.py:98` | `def test_parse_valid(self)` |
| `test_platform_auth_env` | method | `tests/test_models.py:37` | `def test_platform_auth_env(self)` |
| `test_platform_cli_name` | method | `tests/test_models.py:32` | `def test_platform_cli_name(self)` |
| `test_platform_from_string` | method | `tests/test_models.py:19` | `def test_platform_from_string(self)` |
| `test_platform_from_string_case` | method | `tests/test_models.py:24` | `def test_platform_from_string_case(self)` |
| `test_platform_from_string_invalid` | method | `tests/test_models.py:28` | `def test_platform_from_string_invalid(self)` |
| `test_section_header` | method | `tests/test_models.py:67` | `def test_section_header(self)` |
| `test_str` | method | `tests/test_models.py:122` | `def test_str(self)` |
| `test_with_data` | method | `tests/test_models.py:247` | `def test_with_data(self)` |
| `TestPathDirectRelease` | class | `tests/test_path_deploy.py:51` | `class TestPathDirectRelease` |
| `TestTagPrefixes` | class | `tests/test_path_deploy.py:17` | `class TestTagPrefixes` |
| `TestTomlVersionFile` | class | `tests/test_path_deploy.py:37` | `class TestTomlVersionFile` |
| `_git_init` | function | `tests/test_path_deploy.py:7` | `def _git_init(tmp)` |
| `test_name_wins_over_cwd_subdir` | method | `tests/test_path_deploy.py:94` | `def test_name_wins_over_cwd_subdir(self)` |
| `test_no_platforms_pushes_to_origin` | method | `tests/test_path_deploy.py:63` | `def test_no_platforms_pushes_to_origin(self)` |
| `test_release_by_path_dry_run` | method | `tests/test_path_deploy.py:52` | `def test_release_by_path_dry_run(self)` |
| `test_release_v_prefix` | method | `tests/test_path_deploy.py:18` | `def test_release_v_prefix(self)` |
| `test_v_prefix` | method | `tests/test_path_deploy.py:27` | `def test_v_prefix(self)` |
| `test_write_pyproject_toml` | method | `tests/test_path_deploy.py:38` | `def test_write_pyproject_toml(self)` |
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
| `TestCleanAndRun` | class | `tests/test_pypi.py:190` | `class TestCleanAndRun` |
| `TestDetect` | class | `tests/test_pypi.py:25` | `class TestDetect` |
| `TestPipelinePyPI` | class | `tests/test_pypi.py:232` | `class TestPipelinePyPI` |
| `TestPromptCredentials` | class | `tests/test_pypi.py:65` | `class TestPromptCredentials` |
| `_git_init` | function | `tests/test_pypi.py:15` | `def _git_init(tmp)` |
| `_isolated_home` | function | `tests/test_pypi.py:10` | `def _isolated_home(tmp_path, monkeypatch)` |
| `_toml` | method | `tests/test_pypi.py:191` | `def _toml(self)` |
| `test_clean_removes_dist` | method | `tests/test_pypi.py:200` | `def test_clean_removes_dist(self)` |
| `test_credentials_from_env` | method | `tests/test_pypi.py:48` | `def test_credentials_from_env(self, monkeypatch)` |
| `test_empty_dir_no_packaging` | method | `tests/test_pypi.py:34` | `def test_empty_dir_no_packaging(self)` |
| `test_no_credentials_skips_pypi` | method | `tests/test_pypi.py:265` | `def test_no_credentials_skips_pypi(self, monkeypatch)` |
| `test_no_shell_in_runner` | method | `tests/test_pypi.py:58` | `def test_no_shell_in_runner(self)` |
| `test_no_tty_returns_none` | method | `tests/test_pypi.py:66` | `def test_no_tty_returns_none(self, monkeypatch)` |
| `test_prompt_default_is_no_save` | method | `tests/test_pypi.py:93` | `def test_prompt_default_is_no_save(self, monkeypatch)` |
| `test_prompt_empty_token_returns_none` | method | `tests/test_pypi.py:84` | `def test_prompt_empty_token_returns_none(self, monkeypatch)` |
| `test_prompt_returns_token_without_save` | method | `tests/test_pypi.py:74` | `def test_prompt_returns_token_without_save(self, monkeypatch)` |
| `test_prompt_yes_saves` | method | `tests/test_pypi.py:108` | `def test_prompt_yes_saves(self, monkeypatch)` |
| `test_prompted_token_used_for_upload` | method | `tests/test_pypi.py:153` | `def test_prompted_token_used_for_upload(self, monkeypatch)` |
| `test_pypi_failure_aborts_with_error` | method | `tests/test_pypi.py:233` | `def test_pypi_failure_aborts_with_error(self, monkeypatch)` |
| `test_pyproject_with_project_table` | method | `tests/test_pypi.py:26` | `def test_pyproject_with_project_table(self)` |
| `test_run_fails_on_broken_build` | method | `tests/test_pypi.py:212` | `def test_run_fails_on_broken_build(self, monkeypatch)` |
| `test_run_skips_without_packaging` | method | `tests/test_pypi.py:223` | `def test_run_skips_without_packaging(self)` |
| `test_save_pypirc_rejects_symlink` | method | `tests/test_pypi.py:137` | `def test_save_pypirc_rejects_symlink(self)` |
| `test_save_pypirc_roundtrip` | method | `tests/test_pypi.py:122` | `def test_save_pypirc_roundtrip(self)` |
| `test_setup_py_counts` | method | `tests/test_pypi.py:40` | `def test_setup_py_counts(self)` |
| `test_ensure_footer_appends_when_missing` | function | `tests/test_readme_footer.py:30` | `def test_ensure_footer_appends_when_missing(tmp_path)` |
| `test_ensure_footer_is_idempotent` | function | `tests/test_readme_footer.py:40` | `def test_ensure_footer_is_idempotent(tmp_path)` |
| `test_ensure_footer_missing_readme` | function | `tests/test_readme_footer.py:58` | `def test_ensure_footer_missing_readme(tmp_path)` |
| `test_ensure_footer_wraps_plain_line` | function | `tests/test_readme_footer.py:48` | `def test_ensure_footer_wraps_plain_line(tmp_path)` |
| `test_footer_block_is_anchored` | function | `tests/test_readme_footer.py:22` | `def test_footer_block_is_anchored()` |
| `test_footer_line_is_english_without_emoji` | function | `tests/test_readme_footer.py:15` | `def test_footer_line_is_english_without_emoji()` |
| `TestDocsRunner` | class | `tests/test_runner.py:122` | `class TestDocsRunner` |
| `TestTestRunner` | class | `tests/test_runner.py:24` | `class TestTestRunner` |
| `_toml` | function | `tests/test_runner.py:8` | `def _toml(commands, timeout)` |
| `test_auto_false_skips` | method | `tests/test_runner.py:144` | `def test_auto_false_skips(self)` |
| `test_empty_commands_allow_no_tests_passes` | method | `tests/test_runner.py:59` | `def test_empty_commands_allow_no_tests_passes(self)` |
| `test_empty_commands_no_tests_dir_fails` | method | `tests/test_runner.py:50` | `def test_empty_commands_no_tests_dir_fails(self)` |
| `test_empty_string_command_rejected` | method | `tests/test_runner.py:98` | `def test_empty_string_command_rejected(self)` |
| `test_failing_command` | method | `tests/test_runner.py:33` | `def test_failing_command(self)` |
| `test_failing_docs_returns_false` | method | `tests/test_runner.py:130` | `def test_failing_docs_returns_false(self)` |
| `test_make_target_runs` | method | `tests/test_runner.py:106` | `def test_make_target_runs(self)` |
| `test_multiple_commands_stop_on_first_failure` | method | `tests/test_runner.py:42` | `def test_multiple_commands_stop_on_first_failure(self)` |
| `test_no_shell_injection` | method | `tests/test_runner.py:74` | `def test_no_shell_injection(self)` |
| `test_no_shell_injection` | method | `tests/test_runner.py:158` | `def test_no_shell_injection(self)` |
| `test_passing_command` | method | `tests/test_runner.py:25` | `def test_passing_command(self)` |
| `test_passing_docs` | method | `tests/test_runner.py:123` | `def test_passing_docs(self)` |
| `test_timeout_fails` | method | `tests/test_runner.py:89` | `def test_timeout_fails(self)` |
| `TestSemverManager` | class | `tests/test_semver.py:12` | `class TestSemverManager` |
| `manager` | method | `tests/test_semver.py:14` | `def manager(self)` |
| `test_calculate_next_version_major` | method | `tests/test_semver.py:45` | `def test_calculate_next_version_major(self, manager)` |
| `test_calculate_next_version_minor` | method | `tests/test_semver.py:50` | `def test_calculate_next_version_minor(self, manager)` |
| `test_calculate_next_version_none` | method | `tests/test_semver.py:60` | `def test_calculate_next_version_none(self, manager)` |
| `test_calculate_next_version_patch` | method | `tests/test_semver.py:55` | `def test_calculate_next_version_patch(self, manager)` |
| `test_determine_bump` | method | `tests/test_semver.py:39` | `def test_determine_bump(self, manager)` |
| `test_get_current_version_from_file` | method | `tests/test_semver.py:18` | `def test_get_current_version_from_file(self, manager)` |
| `test_get_current_version_no_file` | method | `tests/test_semver.py:26` | `def test_get_current_version_no_file(self, manager)` |
| `test_is_valid_version` | method | `tests/test_semver.py:74` | `def test_is_valid_version(self, manager, ver_str, expected)` |
| `test_write_version_file` | method | `tests/test_semver.py:31` | `def test_write_version_file(self, manager)` |
| `TestCMakefileDetection` | class | `tests/test_toml.py:86` | `class TestCMakefileDetection` |
| `TestMultiTargetAndPyPIInference` | class | `tests/test_toml.py:166` | `class TestMultiTargetAndPyPIInference` |
| `TestTomlConfig` | class | `tests/test_toml.py:9` | `class TestTomlConfig` |
| `_mk` | method | `tests/test_toml.py:87` | `def _mk(self, tmp, content)` |
| `_mk` | method | `tests/test_toml.py:170` | `def _mk(self, tmp, content)` |
| `test_auto_pypi_disabled_for_plain_c` | method | `tests/test_toml.py:204` | `def test_auto_pypi_disabled_for_plain_c(self)` |
| `test_auto_pypi_enabled_for_packaging` | method | `tests/test_toml.py:194` | `def test_auto_pypi_enabled_for_packaging(self)` |
| `test_detect_bare_tests_alone_kept` | method | `tests/test_toml.py:188` | `def test_detect_bare_tests_alone_kept(self)` |
| `test_detect_cmake` | method | `tests/test_toml.py:118` | `def test_detect_cmake(self)` |
| `test_detect_combines_test_targets` | method | `tests/test_toml.py:174` | `def test_detect_combines_test_targets(self)` |
| `test_detect_falls_back_to_check` | method | `tests/test_toml.py:112` | `def test_detect_falls_back_to_check(self)` |
| `test_detect_falls_back_to_test` | method | `tests/test_toml.py:106` | `def test_detect_falls_back_to_test(self)` |
| `test_detect_prefers_test_host` | method | `tests/test_toml.py:100` | `def test_detect_prefers_test_host(self)` |
| `test_detect_test_host_alone_wins` | method | `tests/test_toml.py:181` | `def test_detect_test_host_alone_wins(self)` |
| `test_frozen` | method | `tests/test_toml.py:78` | `def test_frozen(self)` |
| `test_list_targets_ignores_recipes` | method | `tests/test_toml.py:91` | `def test_list_targets_ignores_recipes(self)` |
| `test_load_missing_makefile_uses_make` | method | `tests/test_toml.py:126` | `def test_load_missing_makefile_uses_make(self)` |
| `test_load_missing_returns_defaults` | method | `tests/test_toml.py:10` | `def test_load_missing_returns_defaults(self)` |
| `test_load_valid_toml` | method | `tests/test_toml.py:20` | `def test_load_valid_toml(self)` |
| `test_looks_like_packaging_setup_py` | method | `tests/test_toml.py:212` | `def test_looks_like_packaging_setup_py(self)` |
| `test_makefile_symlink_rejected` | method | `tests/test_toml.py:155` | `def test_makefile_symlink_rejected(self)` |
| `test_malformed_toml_raises` | method | `tests/test_toml.py:58` | `def test_malformed_toml_raises(self)` |
| `test_oversize_rejected` | method | `tests/test_toml.py:50` | `def test_oversize_rejected(self)` |
| `test_python_with_aux_makefile_keeps_pytest` | method | `tests/test_toml.py:135` | `def test_python_with_aux_makefile_keeps_pytest(self)` |
| `test_symlink_rejected` | method | `tests/test_toml.py:39` | `def test_symlink_rejected(self)` |
| `test_test_host_wins_over_python_tests` | method | `tests/test_toml.py:145` | `def test_test_host_wins_over_python_tests(self)` |
| `test_timeout_clamped` | method | `tests/test_toml.py:66` | `def test_timeout_clamped(self)` |
