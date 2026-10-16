# API

## app.py
Depends on: `deploynator/__init__.py`, `deploynator/_config.py`
- `main` (function) `app.py:12` `def main()`

## deploy.sh
- `ensure_pkg` (function) `deploy.sh:22` -- Install or update one package (best effort: works offline with current versions, on PEP 668 systems, and before the...

## deploynator/__main__.py
Depends on: `deploynator/__init__.py`, `deploynator/_config.py`, `deploynator/_mcp_server.py`, `deploynator/_models.py`
Imported by: `tests/test_cli_mcp.py`, `tests/test_install_example.py`
- `build_parser` (function) `deploynator/__main__.py:17` `def build_parser()`
- `preprocess_argv` (function) `deploynator/__main__.py:133` `def preprocess_argv(argv)`
- `main` (function) `deploynator/__main__.py:167` `def main(argv)`

## deploynator/_app.py
Depends on: `deploynator/_config.py`, `deploynator/_deploy.py`, `deploynator/_git.py`, `deploynator/_models.py`, `deploynator/_platforms.py`, `deploynator/_toml.py`
Imported by: `deploynator/__init__.py`
- `DeploynatorApp.__init__` (method) `deploynator/_app.py:21` `def __init__(self, config, workdir)`
- `DeploynatorApp.auth_login` (method) `deploynator/_app.py:31` `def auth_login(self, platforms)`
- `DeploynatorApp.auth_status` (method) `deploynator/_app.py:45` `def auth_status(self)`
- `DeploynatorApp.init_project` (method) `deploynator/_app.py:168` `def init_project(self, project_path, name)`
- `DeploynatorApp.start_branch` (method) `deploynator/_app.py:218` `def start_branch(self, commit_type, description, project_path, project_name, remote)`
- `DeploynatorApp.commit` (method) `deploynator/_app.py:276` `def commit(self, commit_type, subject, scope, body, project_path, project_name, dry_run)`
- `DeploynatorApp.release` (method) `deploynator/_app.py:316` `def release(self, commit_type, subject, scope, body, project_name, bump, dry_run, platforms, all_projects, no_test...`
- `DeploynatorApp.generate_docs` (method) `deploynator/_app.py:406` `def generate_docs(self, project_path, project_name)`
- `DeploynatorApp.status` (method) `deploynator/_app.py:412` `def status(self, project_path, project_name)`
- `DeploynatorApp.list_projects` (method) `deploynator/_app.py:432` `def list_projects(self, search_path)`
- `DeploynatorApp.generate_ci` (method) `deploynator/_app.py:437` `def generate_ci(self, project_name, all_projects)`
- `DeploynatorApp.install_deps` (method) `deploynator/_app.py:453` `def install_deps(self, project_name)`
- `DeploynatorApp.install_packages` (method) `deploynator/_app.py:464` `def install_packages(self, packages)` -- pip install/upgrade packages (default: deploynator from PyPI).
- `DeploynatorApp.interactive_menu` (method) `deploynator/_app.py:492` `def interactive_menu(self)`

## deploynator/_changelog.py
Depends on: `deploynator/_config.py`, `deploynator/_models.py`
Imported by: `deploynator/_deploy.py`, `tests/test_changelog.py`
- `ChangelogGenerator.__init__` (method) `deploynator/_changelog.py:13` `def __init__(self, config)`
- `ChangelogGenerator.generate_from_log` (method) `deploynator/_changelog.py:16` `def generate_from_log(self, repo_path, from_ref, to_ref)`
- `ChangelogGenerator.generate_from_messages` (method) `deploynator/_changelog.py:25` `def generate_from_messages(self, messages)`
- `ChangelogGenerator.generate_header` (method) `deploynator/_changelog.py:45` `def generate_header(self)`
- `ChangelogGenerator.write_changelog` (method) `deploynator/_changelog.py:100` `def write_changelog(self, repo_path, content, filename)`
- `ChangelogGenerator.format_for_release` (method) `deploynator/_changelog.py:110` `def format_for_release(self, changelog_content, max_chars)`

## deploynator/_config.py
Imported by: `app.py`, `deploynator/__main__.py`, `deploynator/_app.py`, `deploynator/_changelog.py`, `deploynator/_deploy.py`, `deploynator/_docs.py`, `deploynator/_git.py`, `deploynator/_mcp_server.py`, `deploynator/_platforms.py`, `deploynator/_pypi.py`, `deploynator/_readme.py`, `deploynator/_runner.py`, `deploynator/_semver.py`, `deploynator/_toml.py`, `tests/bdd_test_deploy.py`, `tests/test_changelog.py`, `tests/test_cli_mcp.py`, `tests/test_config.py`, `tests/test_deploy.py`, `tests/test_init.py`, `tests/test_install_example.py`, `tests/test_path_deploy.py`, `tests/test_pipeline.py`, `tests/test_pypi.py`, `tests/test_readme_footer.py`, `tests/test_runner.py`, `tests/test_semver.py`
- `Config.create` (method) `deploynator/_config.py:79` `def create(overrides)`
- `Config.resolve_path` (method) `deploynator/_config.py:85` `def resolve_path(self)`
- `Config.gh_authd` (method) `deploynator/_config.py:91` `def gh_authd(self)`
- `Config.glab_authd` (method) `deploynator/_config.py:95` `def glab_authd(self)`
- `Config.bb_authd` (method) `deploynator/_config.py:99` `def bb_authd(self)`

## deploynator/_deploy.py
Depends on: `deploynator/_changelog.py`, `deploynator/_config.py`, `deploynator/_docs.py`, `deploynator/_git.py`, `deploynator/_models.py`, `deploynator/_platforms.py`, `deploynator/_pypi.py`, `deploynator/_readme.py`, `deploynator/_runner.py`, `deploynator/_semver.py`, `deploynator/_toml.py`
Imported by: `deploynator/_app.py`, `tests/bdd_test_deploy.py`, `tests/test_deploy.py`, `tests/test_path_deploy.py`, `tests/test_pipeline.py`, `tests/test_pypi.py`
- `ProjectDiscovery.__init__` (method) `deploynator/_deploy.py:32` `def __init__(self, config)`
- `ProjectDiscovery.discover` (method) `deploynator/_deploy.py:35` `def discover(self, search_path)`
- `ProjectDiscovery.find_by_name` (method) `deploynator/_deploy.py:56` `def find_by_name(self, name, search_path)`
- `DeployOrchestrator.__init__` (method) `deploynator/_deploy.py:77` `def __init__(self, config)`
- `DeployOrchestrator.deploy` (method) `deploynator/_deploy.py:97` `def deploy(self, project, commit_type, subject, scope, body, dry_run, platforms_override, run_tests, run_docs...`
- `DeployOrchestrator.generate_workflows` (method) `deploynator/_deploy.py:431` `def generate_workflows(self, project, output_dir)`
- `DeployOrchestrator.install_dependencies` (method) `deploynator/_deploy.py:499` `def install_dependencies(self, project)`
- `DeployOrchestrator.integrate_readmenator` (method) `deploynator/_deploy.py:509` `def integrate_readmenator(self, project_path)`
- `DeployOrchestrator.install_lazygit` (method) `deploynator/_deploy.py:543` `def install_lazygit(self)`

## deploynator/_docs.py
Depends on: `deploynator/_config.py`, `deploynator/_toml.py`
Imported by: `deploynator/_deploy.py`, `tests/bdd_test_deploy.py`, `tests/test_runner.py`
- `DocsRunner.__init__` (method) `deploynator/_docs.py:11` `def __init__(self, config)`
- `DocsRunner.run` (method) `deploynator/_docs.py:14` `def run(self, project_path, toml)`

## deploynator/_git.py
Depends on: `deploynator/_config.py`
Imported by: `deploynator/_app.py`, `deploynator/_deploy.py`
- `GitOperations.__init__` (method) `deploynator/_git.py:11` `def __init__(self, config)`
- `GitOperations.check_gpg` (method) `deploynator/_git.py:14` `def check_gpg(self)`
- `GitOperations.gpg_sign_flag` (method) `deploynator/_git.py:32` `def gpg_sign_flag(self)`
- `GitOperations.clone` (method) `deploynator/_git.py:36` `def clone(self, url, dest, depth)`
- `GitOperations.add_all` (method) `deploynator/_git.py:46` `def add_all(self, repo_path)`
- `GitOperations.commit` (method) `deploynator/_git.py:59` `def commit(self, repo_path, message)`
- `GitOperations.amend_no_edit` (method) `deploynator/_git.py:88` `def amend_no_edit(self, repo_path)`
- `GitOperations.tag` (method) `deploynator/_git.py:97` `def tag(self, repo_path, tag_name, message)`
- `GitOperations.delete_tag` (method) `deploynator/_git.py:107` `def delete_tag(self, repo_path, tag_name)`
- `GitOperations.tag_exists` (method) `deploynator/_git.py:117` `def tag_exists(self, repo_path, tag_name)`
- `GitOperations.push` (method) `deploynator/_git.py:127` `def push(self, repo_path, remote, branch, follow_tags)`
- `GitOperations.push_tags` (method) `deploynator/_git.py:137` `def push_tags(self, repo_path, remote)`
- `GitOperations.create_branch` (method) `deploynator/_git.py:147` `def create_branch(self, repo_path, branch_name, base)`
- `GitOperations.checkout` (method) `deploynator/_git.py:163` `def checkout(self, repo_path, branch)`
- `GitOperations.get_changed_files` (method) `deploynator/_git.py:173` `def get_changed_files(self, repo_path, from_ref, to_ref)`
- `GitOperations.get_log` (method) `deploynator/_git.py:204` `def get_log(self, repo_path, from_ref, to_ref, format_str)`
- `GitOperations.get_start_ref` (method) `deploynator/_git.py:216` `def get_start_ref(self, repo_path)`
- `GitOperations.current_branch` (method) `deploynator/_git.py:234` `def current_branch(self, repo_path)`
- `GitOperations.is_dirty` (method) `deploynator/_git.py:246` `def is_dirty(self, repo_path)`
- `GitOperations.has_remote` (method) `deploynator/_git.py:256` `def has_remote(self, repo_path, remote)`

## deploynator/_mcp_server.py
Depends on: `deploynator/__init__.py`, `deploynator/_config.py`
Imported by: `deploynator/__main__.py`, `tests/test_cli_mcp.py`
- `MCPRequest.__init__` (method) `deploynator/_mcp_server.py:36` `def __init__(self, msg)`
- `MCPRequest.is_notification` (method) `deploynator/_mcp_server.py:43` `def is_notification(self)`
- `MCPRequest.response` (method) `deploynator/_mcp_server.py:46` `def response(self, result)`
- `MCPRequest.error` (method) `deploynator/_mcp_server.py:49` `def error(self, code, message, data)`
- `MCPTool.__init__` (method) `deploynator/_mcp_server.py:57` `def __init__(self, name, description, handler, input_schema)`
- `MCPTool.definition` (method) `deploynator/_mcp_server.py:64` `def definition(self)`
- `MCPTool.call` (method) `deploynator/_mcp_server.py:67` `def call(self, arguments)`
- `MCPResource.__init__` (method) `deploynator/_mcp_server.py:72` `def __init__(self, uri, name, description, mime_type, handler)`
- `MCPResource.definition` (method) `deploynator/_mcp_server.py:79` `def definition(self)`
- `MCPResource.read` (method) `deploynator/_mcp_server.py:82` `def read(self)`
- `MCPServer.__init__` (method) `deploynator/_mcp_server.py:87` `def __init__(self, app, target_dir)`
- `MCPServer.register_tool` (method) `deploynator/_mcp_server.py:94` `def register_tool(self, tool)`
- `MCPServer.register_resource` (method) `deploynator/_mcp_server.py:97` `def register_resource(self, resource)`
- `MCPServer.dispatch` (method) `deploynator/_mcp_server.py:144` `def dispatch(self, req)`
- `MCPServer.run` (method) `deploynator/_mcp_server.py:162` `def run(self)`
- `main` (function) `deploynator/_mcp_server.py:269` `def main()`

## deploynator/_models.py
Imported by: `deploynator/__main__.py`, `deploynator/_app.py`, `deploynator/_changelog.py`, `deploynator/_deploy.py`, `deploynator/_platforms.py`, `deploynator/_semver.py`, `tests/bdd_test_deploy.py`, `tests/test_changelog.py`, `tests/test_deploy.py`, `tests/test_models.py`, `tests/test_path_deploy.py`, `tests/test_pipeline.py`, `tests/test_pypi.py`, `tests/test_semver.py`
- `Platform.from_string` (method) `deploynator/_models.py:16` `def from_string(cls, name)`
- `Platform.label` (method) `deploynator/_models.py:27` `def label(self)`
- `Platform.cli_name` (method) `deploynator/_models.py:30` `def cli_name(self)`
- `Platform.auth_env_var` (method) `deploynator/_models.py:37` `def auth_env_var(self)`
- `CommitType.from_string` (method) `deploynator/_models.py:58` `def from_string(cls, value)`
- `CommitType.valid_types` (method) `deploynator/_models.py:65` `def valid_types(cls)`
- `CommitType.bump_strategy` (method) `deploynator/_models.py:68` `def bump_strategy(self)`
- `CommitType.section_header` (method) `deploynator/_models.py:82` `def section_header(self)`
- `PlatformConfig.from_dict` (method) `deploynator/_models.py:105` `def from_dict(cls, data)`
- `VersionConfig.from_dict` (method) `deploynator/_models.py:121` `def from_dict(cls, data)`
- `ProjectConfig.from_dict` (method) `deploynator/_models.py:139` `def from_dict(cls, data)`
- `CommitMessage.format` (method) `deploynator/_models.py:183` `def format(self)`
- `CommitMessage.parse` (method) `deploynator/_models.py:195` `def parse(cls, raw)`
- `VersionInfo.parse` (method) `deploynator/_models.py:217` `def parse(cls, version_str)`
- `VersionInfo.bump` (method) `deploynator/_models.py:228` `def bump(self, strategy)`
- `ChangelogEntry.from_git_log_line` (method) `deploynator/_models.py:247` `def from_git_log_line(cls, line, author, sha)`

## deploynator/_platforms.py
Depends on: `deploynator/_config.py`, `deploynator/_models.py`
Imported by: `deploynator/_app.py`, `deploynator/_deploy.py`
- `PlatformClient.__init__` (method) `deploynator/_platforms.py:15` `def __init__(self, config)`
- `PlatformClient.name` (method) `deploynator/_platforms.py:19` `def name(self)`
- `PlatformClient.is_available` (method) `deploynator/_platforms.py:23` `def is_available(self)`
- `PlatformClient.is_authenticated` (method) `deploynator/_platforms.py:27` `def is_authenticated(self)`
- `PlatformClient.create_release` (method) `deploynator/_platforms.py:31` `def create_release(self, repo, release)`
- `PlatformClient.create_pull_request` (method) `deploynator/_platforms.py:35` `def create_pull_request(self, repo, title, body, head, base)`
- `PlatformClient.push_changes` (method) `deploynator/_platforms.py:39` `def push_changes(self, repo_path, remote, branch, tags)`
- `GitHubCLI.name` (method) `deploynator/_platforms.py:50` `def name(self)`
- `GitHubCLI.is_available` (method) `deploynator/_platforms.py:53` `def is_available(self)`
- `GitHubCLI.is_authenticated` (method) `deploynator/_platforms.py:60` `def is_authenticated(self)`
- `GitHubCLI.create_release` (method) `deploynator/_platforms.py:67` `def create_release(self, repo, release)`
- `GitHubCLI.create_pull_request` (method) `deploynator/_platforms.py:91` `def create_pull_request(self, repo, title, body, head, base)`
- `GitHubCLI.push_changes` (method) `deploynator/_platforms.py:105` `def push_changes(self, repo_path, remote, branch, tags)`
- `GitLabCLI.name` (method) `deploynator/_platforms.py:114` `def name(self)`
- `GitLabCLI.is_available` (method) `deploynator/_platforms.py:117` `def is_available(self)`
- `GitLabCLI.is_authenticated` (method) `deploynator/_platforms.py:124` `def is_authenticated(self)`
- `GitLabCLI.create_release` (method) `deploynator/_platforms.py:131` `def create_release(self, repo, release)`
- `GitLabCLI.create_pull_request` (method) `deploynator/_platforms.py:142` `def create_pull_request(self, repo, title, body, head, base)`
- `GitLabCLI.push_changes` (method) `deploynator/_platforms.py:156` `def push_changes(self, repo_path, remote, branch, tags)`
- `BitbucketCLI.name` (method) `deploynator/_platforms.py:165` `def name(self)`
- `BitbucketCLI.is_available` (method) `deploynator/_platforms.py:168` `def is_available(self)`
- `BitbucketCLI.is_authenticated` (method) `deploynator/_platforms.py:178` `def is_authenticated(self)`
- `BitbucketCLI.create_release` (method) `deploynator/_platforms.py:181` `def create_release(self, repo, release)`
- `BitbucketCLI.create_pull_request` (method) `deploynator/_platforms.py:201` `def create_pull_request(self, repo, title, body, head, base)`
- `BitbucketCLI.push_changes` (method) `deploynator/_platforms.py:215` `def push_changes(self, repo_path, remote, branch, tags)`
- `PlatformFactory.register` (method) `deploynator/_platforms.py:231` `def register(cls, platform, client_class)`
- `PlatformFactory.create` (method) `deploynator/_platforms.py:235` `def create(cls, platform, config)`
- `PlatformFactory.create_all_available` (method) `deploynator/_platforms.py:242` `def create_all_available(cls, config)`

## deploynator/_pypi.py
Depends on: `deploynator/_config.py`, `deploynator/_toml.py`
Imported by: `deploynator/_deploy.py`, `tests/test_pypi.py`
- `PyPIRunner.__init__` (method) `deploynator/_pypi.py:13` `def __init__(self, config)`
- `PyPIRunner.is_packaging_project` (method) `deploynator/_pypi.py:16` `def is_packaging_project(self, project_path)`
- `PyPIRunner.has_credentials` (method) `deploynator/_pypi.py:33` `def has_credentials(self)`
- `PyPIRunner.prompt_for_credentials` (method) `deploynator/_pypi.py:39` `def prompt_for_credentials(self)` -- Pide el token PyPI por input oculto solo si hay TTY.
- `PyPIRunner.save_pypirc` (method) `deploynator/_pypi.py:72` `def save_pypirc(self, token, path)` -- Guarda el token en ~/.pypirc (username __token__, modo 600).
- `PyPIRunner.clean` (method) `deploynator/_pypi.py:90` `def clean(self, project_path, toml)`
- `PyPIRunner.run` (method) `deploynator/_pypi.py:107` `def run(self, project_path, toml, version, token)`

## deploynator/_readme.py
Depends on: `deploynator/_config.py`
Imported by: `deploynator/_deploy.py`, `tests/test_readme_footer.py`
- `footer_block` (function) `deploynator/_readme.py:19` `def footer_block(config)` -- Return the anchored deploy footer block.
- `ensure_deployed_footer` (function) `deploynator/_readme.py:49` `def ensure_deployed_footer(repo_path, config)` -- Append or refresh the deploy footer in the repository README.
- `footer_line` (function) `deploynator/_readme.py:96` `def footer_line(config)` -- Return the plain deploy footer line.

## deploynator/_runner.py
Depends on: `deploynator/_config.py`, `deploynator/_toml.py`
Imported by: `deploynator/_deploy.py`, `tests/test_runner.py`
- `TestRunner.__init__` (method) `deploynator/_runner.py:12` `def __init__(self, config)`
- `TestRunner.run` (method) `deploynator/_runner.py:15` `def run(self, project_path, toml)`

## deploynator/_semver.py
Depends on: `deploynator/_config.py`, `deploynator/_models.py`
Imported by: `deploynator/_deploy.py`, `tests/bdd_test_deploy.py`, `tests/test_path_deploy.py`, `tests/test_pipeline.py`, `tests/test_semver.py`
- `SemverManager.__init__` (method) `deploynator/_semver.py:13` `def __init__(self, config)`
- `SemverManager.max_version` (method) `deploynator/_semver.py:16` `def max_version(self, a, b)`
- `SemverManager.get_current_version` (method) `deploynator/_semver.py:21` `def get_current_version(self, project_path, version_file, version_pattern)`
- `SemverManager.write_version_file` (method) `deploynator/_semver.py:66` `def write_version_file(self, project_path, version, version_file)`
- `SemverManager.determine_bump` (method) `deploynator/_semver.py:111` `def determine_bump(self, commit_type)`
- `SemverManager.calculate_next_version` (method) `deploynator/_semver.py:114` `def calculate_next_version(self, current, strategy)`
- `SemverManager.is_valid_version` (method) `deploynator/_semver.py:118` `def is_valid_version(version_str)`

## deploynator/_toml.py
Depends on: `deploynator/_config.py`
Imported by: `deploynator/_app.py`, `deploynator/_deploy.py`, `deploynator/_docs.py`, `deploynator/_pypi.py`, `deploynator/_runner.py`, `tests/bdd_test_deploy.py`, `tests/test_init.py`, `tests/test_pypi.py`, `tests/test_runner.py`, `tests/test_toml.py`
- `list_make_targets` (function) `deploynator/_toml.py:31` `def list_make_targets(project_path)` -- Lee el Makefile y devuelve sus targets sin ejecutar nada.
- `detect_test_commands` (function) `deploynator/_toml.py:77` `def detect_test_commands(project_path)` -- Detecta comandos de test para proyectos C/autotools sin toml.
- `load_toml_config` (function) `deploynator/_toml.py:164` `def load_toml_config(project_path)`
