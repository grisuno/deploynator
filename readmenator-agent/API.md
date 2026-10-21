# API

## app.py
Depends on: `deploynator/__init__.py`, `deploynator/_config.py`
- `main` (function) `app.py:12` `def main()`

## deploy.sh
- `ensure_pkg` (function) `deploy.sh:22` -- Install or update one package (best effort: works offline with current versions, on PEP 668 systems, and before the...

## deploynator/__main__.py
Depends on: `deploynator/__init__.py`, `deploynator/_config.py`, `deploynator/_mcp_server.py`, `deploynator/_models.py`
Imported by: `tests/test_cli_mcp.py`, `tests/test_install_example.py`
- `build_parser` (function) `deploynator/__main__.py:16` `def build_parser()`
- `preprocess_argv` (function) `deploynator/__main__.py:151` `def preprocess_argv(argv)`
- `main` (function) `deploynator/__main__.py:185` `def main(argv)`

## deploynator/_app.py
Depends on: `deploynator/_config.py`, `deploynator/_deploy.py`, `deploynator/_git.py`, `deploynator/_models.py`, `deploynator/_platforms.py`, `deploynator/_toml.py`
Imported by: `deploynator/__init__.py`
- `DeploynatorApp.__init__` (method) `deploynator/_app.py:19` `def __init__(self, config, workdir)`
- `DeploynatorApp.auth_login` (method) `deploynator/_app.py:29` `def auth_login(self, platforms)`
- `DeploynatorApp.auth_status` (method) `deploynator/_app.py:43` `def auth_status(self)`
- `DeploynatorApp.init_project` (method) `deploynator/_app.py:185` `def init_project(self, project_path, name)`
- `DeploynatorApp.start_branch` (method) `deploynator/_app.py:262` `def start_branch(self, commit_type, description, project_path, project_name, remote)`
- `DeploynatorApp.commit` (method) `deploynator/_app.py:318` `def commit(self, commit_type, subject, scope, body, project_path, project_name, dry_run)`
- `DeploynatorApp.release` (method) `deploynator/_app.py:377` `def release(self, commit_type, subject, scope, body, message, project_name, bump, dry_run, platforms, all_projects...`
- `DeploynatorApp.generate_docs` (method) `deploynator/_app.py:519` `def generate_docs(self, project_path, project_name)`
- `DeploynatorApp.status` (method) `deploynator/_app.py:525` `def status(self, project_path, project_name)`
- `DeploynatorApp.list_projects` (method) `deploynator/_app.py:545` `def list_projects(self, search_path)`
- `DeploynatorApp.generate_ci` (method) `deploynator/_app.py:550` `def generate_ci(self, project_name, all_projects)`
- `DeploynatorApp.install_deps` (method) `deploynator/_app.py:566` `def install_deps(self, project_name)`
- `DeploynatorApp.install_packages` (method) `deploynator/_app.py:577` `def install_packages(self, packages)` -- pip install/upgrade packages (default: deploynator from PyPI).
- `DeploynatorApp.interactive_menu` (method) `deploynator/_app.py:604` `def interactive_menu(self)`

## deploynator/_changelog.py
Depends on: `deploynator/_config.py`, `deploynator/_models.py`
Imported by: `deploynator/_deploy.py`, `tests/test_changelog.py`
- `ChangelogGenerator.__init__` (method) `deploynator/_changelog.py:12` `def __init__(self, config)`
- `ChangelogGenerator.generate_from_log` (method) `deploynator/_changelog.py:15` `def generate_from_log(self, repo_path, from_ref, to_ref)`
- `ChangelogGenerator.generate_from_messages` (method) `deploynator/_changelog.py:24` `def generate_from_messages(self, messages)`
- `ChangelogGenerator.generate_header` (method) `deploynator/_changelog.py:44` `def generate_header(self)`
- `ChangelogGenerator.write_changelog` (method) `deploynator/_changelog.py:99` `def write_changelog(self, repo_path, content, filename)`
- `ChangelogGenerator.format_for_release` (method) `deploynator/_changelog.py:108` `def format_for_release(self, changelog_content, max_chars)`

## deploynator/_config.py
Imported by: `app.py`, `deploynator/__main__.py`, `deploynator/_app.py`, `deploynator/_changelog.py`, `deploynator/_deb.py`, `deploynator/_deploy.py`, `deploynator/_docs.py`, `deploynator/_git.py`, `deploynator/_mcp_server.py`, `deploynator/_platforms.py`, `deploynator/_pypi.py`, `deploynator/_readme.py`, `deploynator/_receipt.py`, `deploynator/_runner.py`, `deploynator/_semver.py`, `deploynator/_toml.py`, `tests/bdd_test_deploy.py`, `tests/test_changelog.py`, `tests/test_cli_mcp.py`, `tests/test_config.py`, `tests/test_deb.py`, `tests/test_deploy.py`, `tests/test_git_sync.py`, `tests/test_init.py`, `tests/test_install_example.py`, `tests/test_path_deploy.py`, `tests/test_pipeline.py`, `tests/test_pypi.py`, `tests/test_readme_footer.py`, `tests/test_receipt.py`, `tests/test_runner.py`, `tests/test_semver.py`
- `Config.create` (method) `deploynator/_config.py:83` `def create(overrides)`
- `Config.resolve_path` (method) `deploynator/_config.py:89` `def resolve_path(self)`
- `Config.gh_authd` (method) `deploynator/_config.py:95` `def gh_authd(self)`
- `Config.glab_authd` (method) `deploynator/_config.py:99` `def glab_authd(self)`
- `Config.bb_authd` (method) `deploynator/_config.py:103` `def bb_authd(self)`

## deploynator/_deb.py
Depends on: `deploynator/_config.py`, `deploynator/_toml.py`
Imported by: `deploynator/_deploy.py`, `tests/test_deb.py`
- `DebRunner.__init__` (method) `deploynator/_deb.py:35` `def __init__(self, config)`
- `DebRunner.deb_make_target` (method) `deploynator/_deb.py:38` `def deb_make_target(self, project_path)`
- `DebRunner.is_deb_project` (method) `deploynator/_deb.py:48` `def is_deb_project(self, project_path)`
- `DebRunner.clean` (method) `deploynator/_deb.py:62` `def clean(self, project_path, toml)`
- `DebRunner.build_command` (method) `deploynator/_deb.py:110` `def build_command(self, project_path, toml)`
- `DebRunner.run` (method) `deploynator/_deb.py:126` `def run(self, project_path, toml, version, verbose)`

## deploynator/_deploy.py
Depends on: `deploynator/_changelog.py`, `deploynator/_config.py`, `deploynator/_deb.py`, `deploynator/_docs.py`, `deploynator/_git.py`, `deploynator/_models.py`, `deploynator/_platforms.py`, `deploynator/_pypi.py`, `deploynator/_readme.py`, `deploynator/_receipt.py`, `deploynator/_runner.py`, `deploynator/_semver.py`, `deploynator/_toml.py`
Imported by: `deploynator/_app.py`, `tests/bdd_test_deploy.py`, `tests/test_deb.py`, `tests/test_deploy.py`, `tests/test_git_sync.py`, `tests/test_path_deploy.py`, `tests/test_pipeline.py`, `tests/test_pypi.py`, `tests/test_receipt.py`
- `ProjectDiscovery.__init__` (method) `deploynator/_deploy.py:39` `def __init__(self, config)`
- `ProjectDiscovery.discover` (method) `deploynator/_deploy.py:42` `def discover(self, search_path)`
- `ProjectDiscovery.find_by_name` (method) `deploynator/_deploy.py:63` `def find_by_name(self, name, search_path)`
- `DeployOrchestrator.__init__` (method) `deploynator/_deploy.py:84` `def __init__(self, config)`
- `DeployOrchestrator.deploy` (method) `deploynator/_deploy.py:113` `def deploy(self, project, commit_type, subject, scope, body, dry_run, platforms_override, run_tests, run_docs...`
- `DeployOrchestrator.generate_workflows` (method) `deploynator/_deploy.py:715` `def generate_workflows(self, project, output_dir)`
- `DeployOrchestrator.install_dependencies` (method) `deploynator/_deploy.py:782` `def install_dependencies(self, project)`
- `DeployOrchestrator.integrate_readmenator` (method) `deploynator/_deploy.py:792` `def integrate_readmenator(self, project_path)`
- `DeployOrchestrator.install_lazygit` (method) `deploynator/_deploy.py:828` `def install_lazygit(self)`

## deploynator/_docs.py
Depends on: `deploynator/_config.py`, `deploynator/_toml.py`
Imported by: `deploynator/_deploy.py`, `tests/bdd_test_deploy.py`, `tests/test_runner.py`
- `DocsRunner.__init__` (method) `deploynator/_docs.py:11` `def __init__(self, config)`
- `DocsRunner.run` (method) `deploynator/_docs.py:14` `def run(self, project_path, toml)`

## deploynator/_git.py
Depends on: `deploynator/_config.py`
Imported by: `deploynator/_app.py`, `deploynator/_deploy.py`, `tests/test_git_sync.py`
- `GitOperations.__init__` (method) `deploynator/_git.py:10` `def __init__(self, config)`
- `GitOperations.head_commit` (method) `deploynator/_git.py:13` `def head_commit(self, repo_path)`
- `GitOperations.check_gpg` (method) `deploynator/_git.py:23` `def check_gpg(self)`
- `GitOperations.gpg_sign_flag` (method) `deploynator/_git.py:41` `def gpg_sign_flag(self)`
- `GitOperations.clone` (method) `deploynator/_git.py:45` `def clone(self, url, dest, depth)`
- `GitOperations.add_all` (method) `deploynator/_git.py:55` `def add_all(self, repo_path)`
- `GitOperations.commit` (method) `deploynator/_git.py:68` `def commit(self, repo_path, message)`
- `GitOperations.amend_no_edit` (method) `deploynator/_git.py:97` `def amend_no_edit(self, repo_path)`
- `GitOperations.tag` (method) `deploynator/_git.py:106` `def tag(self, repo_path, tag_name, message)`
- `GitOperations.delete_tag` (method) `deploynator/_git.py:116` `def delete_tag(self, repo_path, tag_name)`
- `GitOperations.tag_exists` (method) `deploynator/_git.py:126` `def tag_exists(self, repo_path, tag_name)`
- `GitOperations.push` (method) `deploynator/_git.py:136` `def push(self, repo_path, remote, branch, follow_tags)`
- `GitOperations.push_tags` (method) `deploynator/_git.py:146` `def push_tags(self, repo_path, remote)`
- `GitOperations.create_branch` (method) `deploynator/_git.py:156` `def create_branch(self, repo_path, branch_name, base)`
- `GitOperations.checkout` (method) `deploynator/_git.py:172` `def checkout(self, repo_path, branch)`
- `GitOperations.get_changed_files` (method) `deploynator/_git.py:182` `def get_changed_files(self, repo_path, from_ref, to_ref)`
- `GitOperations.get_log` (method) `deploynator/_git.py:213` `def get_log(self, repo_path, from_ref, to_ref, format_str)`
- `GitOperations.get_start_ref` (method) `deploynator/_git.py:225` `def get_start_ref(self, repo_path)`
- `GitOperations.current_branch` (method) `deploynator/_git.py:243` `def current_branch(self, repo_path)`
- `GitOperations.is_dirty` (method) `deploynator/_git.py:255` `def is_dirty(self, repo_path)`
- `GitOperations.has_remote` (method) `deploynator/_git.py:265` `def has_remote(self, repo_path, remote)`
- `GitOperations.branch_exists` (method) `deploynator/_git.py:275` `def branch_exists(self, repo_path, branch)`
- `GitOperations.is_behind` (method) `deploynator/_git.py:285` `def is_behind(self, repo_path, behind_branch, ahead_branch)` -- True si `ahead_branch` tiene commits que `behind_branch` no tiene (es decir, behind_branch esta por debajo de...
- `GitOperations.push_force` (method) `deploynator/_git.py:300` `def push_force(self, repo_path, remote, src_branch, dst_branch)`

## deploynator/_mcp_server.py
Depends on: `deploynator/__init__.py`, `deploynator/_config.py`
Imported by: `deploynator/__main__.py`, `tests/test_cli_mcp.py`
- `MCPRequest.__init__` (method) `deploynator/_mcp_server.py:37` `def __init__(self, msg)`
- `MCPRequest.is_notification` (method) `deploynator/_mcp_server.py:44` `def is_notification(self)`
- `MCPRequest.response` (method) `deploynator/_mcp_server.py:47` `def response(self, result)`
- `MCPRequest.error` (method) `deploynator/_mcp_server.py:50` `def error(self, code, message, data)`
- `MCPTool.__init__` (method) `deploynator/_mcp_server.py:58` `def __init__(self, name, description, handler, input_schema)`
- `MCPTool.definition` (method) `deploynator/_mcp_server.py:65` `def definition(self)`
- `MCPTool.call` (method) `deploynator/_mcp_server.py:68` `def call(self, arguments)`
- `MCPResource.__init__` (method) `deploynator/_mcp_server.py:73` `def __init__(self, uri, name, description, mime_type, handler)`
- `MCPResource.definition` (method) `deploynator/_mcp_server.py:80` `def definition(self)`
- `MCPResource.read` (method) `deploynator/_mcp_server.py:83` `def read(self)`
- `MCPServer.__init__` (method) `deploynator/_mcp_server.py:88` `def __init__(self, app, target_dir)`
- `MCPServer.register_tool` (method) `deploynator/_mcp_server.py:95` `def register_tool(self, tool)`
- `MCPServer.register_resource` (method) `deploynator/_mcp_server.py:98` `def register_resource(self, resource)`
- `MCPServer.dispatch` (method) `deploynator/_mcp_server.py:145` `def dispatch(self, req)`
- `MCPServer.run` (method) `deploynator/_mcp_server.py:163` `def run(self)`
- `main` (function) `deploynator/_mcp_server.py:277` `def main()`

## deploynator/_models.py
Imported by: `deploynator/__main__.py`, `deploynator/_app.py`, `deploynator/_changelog.py`, `deploynator/_deploy.py`, `deploynator/_platforms.py`, `deploynator/_semver.py`, `tests/bdd_test_deploy.py`, `tests/test_deb.py`, `tests/test_deploy.py`, `tests/test_models.py`, `tests/test_path_deploy.py`, `tests/test_pipeline.py`, `tests/test_pypi.py`, `tests/test_receipt.py`, `tests/test_semver.py`
- `Platform.from_string` (method) `deploynator/_models.py:15` `def from_string(cls, name)`
- `Platform.label` (method) `deploynator/_models.py:26` `def label(self)`
- `Platform.cli_name` (method) `deploynator/_models.py:29` `def cli_name(self)`
- `Platform.auth_env_var` (method) `deploynator/_models.py:36` `def auth_env_var(self)`
- `CommitType.from_string` (method) `deploynator/_models.py:57` `def from_string(cls, value)`
- `CommitType.valid_types` (method) `deploynator/_models.py:64` `def valid_types(cls)`
- `CommitType.bump_strategy` (method) `deploynator/_models.py:67` `def bump_strategy(self)`
- `CommitType.section_header` (method) `deploynator/_models.py:81` `def section_header(self)`
- `PlatformConfig.from_dict` (method) `deploynator/_models.py:104` `def from_dict(cls, data)`
- `VersionConfig.from_dict` (method) `deploynator/_models.py:120` `def from_dict(cls, data)`
- `ProjectConfig.from_dict` (method) `deploynator/_models.py:138` `def from_dict(cls, data)`
- `CommitMessage.format` (method) `deploynator/_models.py:182` `def format(self)`
- `CommitMessage.parse` (method) `deploynator/_models.py:194` `def parse(cls, raw)`
- `VersionInfo.parse` (method) `deploynator/_models.py:216` `def parse(cls, version_str)`
- `VersionInfo.bump` (method) `deploynator/_models.py:227` `def bump(self, strategy)`
- `ChangelogEntry.from_git_log_line` (method) `deploynator/_models.py:246` `def from_git_log_line(cls, line, author, sha)`

## deploynator/_platforms.py
Depends on: `deploynator/_config.py`, `deploynator/_models.py`
Imported by: `deploynator/_app.py`, `deploynator/_deploy.py`
- `PlatformClient.__init__` (method) `deploynator/_platforms.py:14` `def __init__(self, config)`
- `PlatformClient.name` (method) `deploynator/_platforms.py:18` `def name(self)`
- `PlatformClient.is_available` (method) `deploynator/_platforms.py:22` `def is_available(self)`
- `PlatformClient.is_authenticated` (method) `deploynator/_platforms.py:26` `def is_authenticated(self)`
- `PlatformClient.create_release` (method) `deploynator/_platforms.py:30` `def create_release(self, repo, release)`
- `PlatformClient.create_pull_request` (method) `deploynator/_platforms.py:34` `def create_pull_request(self, repo, title, body, head, base)`
- `PlatformClient.push_changes` (method) `deploynator/_platforms.py:38` `def push_changes(self, repo_path, remote, branch, tags)`
- `PlatformClient.upload_release_assets` (method) `deploynator/_platforms.py:41` `def upload_release_assets(self, repo, version, assets)` -- Sube ficheros como assets del release.
- `GitHubCLI.name` (method) `deploynator/_platforms.py:53` `def name(self)`
- `GitHubCLI.is_available` (method) `deploynator/_platforms.py:56` `def is_available(self)`
- `GitHubCLI.is_authenticated` (method) `deploynator/_platforms.py:63` `def is_authenticated(self)`
- `GitHubCLI.create_release` (method) `deploynator/_platforms.py:70` `def create_release(self, repo, release)`
- `GitHubCLI.create_pull_request` (method) `deploynator/_platforms.py:94` `def create_pull_request(self, repo, title, body, head, base)`
- `GitHubCLI.upload_release_assets` (method) `deploynator/_platforms.py:108` `def upload_release_assets(self, repo, version, assets)` -- `gh release upload <tag> <files> --repo <repo> --clobber` (shell=False).
- `GitHubCLI.push_changes` (method) `deploynator/_platforms.py:125` `def push_changes(self, repo_path, remote, branch, tags)`
- `GitLabCLI.name` (method) `deploynator/_platforms.py:134` `def name(self)`
- `GitLabCLI.is_available` (method) `deploynator/_platforms.py:137` `def is_available(self)`
- `GitLabCLI.is_authenticated` (method) `deploynator/_platforms.py:144` `def is_authenticated(self)`
- `GitLabCLI.create_release` (method) `deploynator/_platforms.py:151` `def create_release(self, repo, release)`
- `GitLabCLI.create_pull_request` (method) `deploynator/_platforms.py:162` `def create_pull_request(self, repo, title, body, head, base)`
- `GitLabCLI.push_changes` (method) `deploynator/_platforms.py:176` `def push_changes(self, repo_path, remote, branch, tags)`
- `BitbucketCLI.name` (method) `deploynator/_platforms.py:185` `def name(self)`
- `BitbucketCLI.is_available` (method) `deploynator/_platforms.py:188` `def is_available(self)`
- `BitbucketCLI.is_authenticated` (method) `deploynator/_platforms.py:198` `def is_authenticated(self)`
- `BitbucketCLI.create_release` (method) `deploynator/_platforms.py:201` `def create_release(self, repo, release)`
- `BitbucketCLI.create_pull_request` (method) `deploynator/_platforms.py:221` `def create_pull_request(self, repo, title, body, head, base)`
- `BitbucketCLI.push_changes` (method) `deploynator/_platforms.py:235` `def push_changes(self, repo_path, remote, branch, tags)`
- `PlatformFactory.register` (method) `deploynator/_platforms.py:251` `def register(cls, platform, client_class)`
- `PlatformFactory.create` (method) `deploynator/_platforms.py:255` `def create(cls, platform, config)`
- `PlatformFactory.create_all_available` (method) `deploynator/_platforms.py:262` `def create_all_available(cls, config)`

## deploynator/_pypi.py
Depends on: `deploynator/_config.py`, `deploynator/_toml.py`
Imported by: `deploynator/_deploy.py`, `tests/test_pypi.py`
- `PyPIRunner.__init__` (method) `deploynator/_pypi.py:13` `def __init__(self, config)`
- `PyPIRunner.is_packaging_project` (method) `deploynator/_pypi.py:16` `def is_packaging_project(self, project_path)`
- `PyPIRunner.has_credentials` (method) `deploynator/_pypi.py:33` `def has_credentials(self)`
- `PyPIRunner.prompt_for_credentials` (method) `deploynator/_pypi.py:39` `def prompt_for_credentials(self)` -- Pide el token PyPI por input oculto solo si hay TTY.
- `PyPIRunner.save_pypirc` (method) `deploynator/_pypi.py:72` `def save_pypirc(self, token, path)` -- Guarda el token en ~/.pypirc (username __token__, modo 600).
- `PyPIRunner.clean` (method) `deploynator/_pypi.py:90` `def clean(self, project_path, toml)`
- `PyPIRunner.run` (method) `deploynator/_pypi.py:107` `def run(self, project_path, toml, version, token, verbose)`

## deploynator/_readme.py
Depends on: `deploynator/_config.py`
Imported by: `deploynator/_deploy.py`, `tests/test_readme_footer.py`
- `footer_block` (function) `deploynator/_readme.py:18` `def footer_block(config)` -- Return the anchored deploy footer block.
- `ensure_deployed_footer` (function) `deploynator/_readme.py:48` `def ensure_deployed_footer(repo_path, config)` -- Append or refresh the deploy footer in the repository README.
- `footer_line` (function) `deploynator/_readme.py:95` `def footer_line(config)` -- Return the plain deploy footer line.

## deploynator/_receipt.py
Depends on: `deploynator/_config.py`
Imported by: `deploynator/_deploy.py`, `tests/test_receipt.py`
- `collect_secret_values` (function) `deploynator/_receipt.py:80` `def collect_secret_values()` -- Current env token values worth redacting (length >= threshold).
- `redact` (function) `deploynator/_receipt.py:96` `def redact(text, secrets)`
- `StepRecord.to_dict` (method) `deploynator/_receipt.py:114` `def to_dict(self)`
- `CommandRecord.to_dict` (method) `deploynator/_receipt.py:132` `def to_dict(self)`
- `EdgeRecord.to_dict` (method) `deploynator/_receipt.py:145` `def to_dict(self)`
- `ReleaseReceipt.__init__` (method) `deploynator/_receipt.py:157` `def __init__(self, project, mode, dry_run, trace, flags)`
- `ReleaseReceipt.note_platform` (method) `deploynator/_receipt.py:185` `def note_platform(self, label, repo, enabled, pushed, released, error)` -- Insert or merge a platform state entry (insertion only once).
- `ReleaseReceipt.to_dict` (method) `deploynator/_receipt.py:213` `def to_dict(self)`
- `ReleaseReceipt.load_dict` (method) `deploynator/_receipt.py:236` `def load_dict(self, data)` -- Restore state from a plain dict (round-trip support).
- `_StageHandle.__init__` (method) `deploynator/_receipt.py:251` `def __init__(self)`
- `_StageHandle.failed` (method) `deploynator/_receipt.py:255` `def failed(self)`
- `_StageHandle.fail` (method) `deploynator/_receipt.py:258` `def fail(self, error)`
- `ReceiptCollector.__init__` (method) `deploynator/_receipt.py:274` `def __init__(self, project, mode, dry_run, trace, flags, secrets, tail_chars)`
- `ReceiptCollector.stage` (method) `deploynator/_receipt.py:295` `def stage(self, label, caller)` -- Record a logical step.
- `ReceiptCollector.mark_failure` (method) `deploynator/_receipt.py:313` `def mark_failure(self, label, error, caller)` -- Record a guard/condition failure occurring outside stage blocks.
- `ReceiptCollector.note_platform` (method) `deploynator/_receipt.py:319` `def note_platform(self, label, repo, enabled, pushed, released, error)` -- Insert or merge platform state on the underlying receipt.
- `ReceiptCollector.current_stage` (method) `deploynator/_receipt.py:326` `def current_stage(self)`
- `ReceiptCollector.observe_edge` (method) `deploynator/_receipt.py:331` `def observe_edge(self, caller, callee, evidence)`
- `ReceiptCollector.add_edge` (method) `deploynator/_receipt.py:342` `def add_edge(self, edge)`
- `ReceiptCollector.add_edges` (method) `deploynator/_receipt.py:345` `def add_edges(self, edges)`
- `ReceiptCollector.add_commands` (method) `deploynator/_receipt.py:348` `def add_commands(self, commands)`
- `ReceiptCollector.set_run_context` (method) `deploynator/_receipt.py:353` `def set_run_context(self, version_from, version_to, commit, branch)`
- `ReceiptCollector.set_tag` (method) `deploynator/_receipt.py:362` `def set_tag(self, tag)`
- `ReceiptCollector.set_commit` (method) `deploynator/_receipt.py:367` `def set_commit(self, commit)`
- `ReceiptCollector.finalize` (method) `deploynator/_receipt.py:371` `def finalize(self, status, error)`
- `ReceiptCollector.capture` (method) `deploynator/_receipt.py:380` `def capture(self)`
- `ReceiptCollector.write` (method) `deploynator/_receipt.py:438` `def write(self, path)` -- Atomic write.
- `default_receipt_path` (function) `deploynator/_receipt.py:476` `def default_receipt_path(base_dir, project, mode, status, version)` -- Default atomic receipt location: <base_dir>/<receipts_dir>/.
- `build_receipt_from_result` (function) `deploynator/_receipt.py:491` `def build_receipt_from_result(receipt, result, error)` -- Stay consistent with the DeployResult before writing.
- `build_plan` (function) `deploynator/_receipt.py:510` `def build_plan(config, project, toml, platforms_override, run_tests, run_docs, run_pypi, run_deb, version)` -- Feasible set from effective config + CLI flags + interface contract.

## deploynator/_runner.py
Depends on: `deploynator/_config.py`, `deploynator/_toml.py`
Imported by: `deploynator/_deploy.py`, `tests/test_runner.py`
- `TestRunner.__init__` (method) `deploynator/_runner.py:12` `def __init__(self, config)`
- `TestRunner.run` (method) `deploynator/_runner.py:15` `def run(self, project_path, toml)`

## deploynator/_semver.py
Depends on: `deploynator/_config.py`, `deploynator/_models.py`
Imported by: `deploynator/_deploy.py`, `tests/bdd_test_deploy.py`, `tests/test_path_deploy.py`, `tests/test_pipeline.py`, `tests/test_semver.py`
- `SemverManager.__init__` (method) `deploynator/_semver.py:12` `def __init__(self, config)`
- `SemverManager.max_version` (method) `deploynator/_semver.py:15` `def max_version(self, a, b)`
- `SemverManager.get_current_version` (method) `deploynator/_semver.py:20` `def get_current_version(self, project_path, version_file, version_pattern)`
- `SemverManager.write_version_file` (method) `deploynator/_semver.py:65` `def write_version_file(self, project_path, version, version_file)`
- `SemverManager.determine_bump` (method) `deploynator/_semver.py:110` `def determine_bump(self, commit_type)`
- `SemverManager.calculate_next_version` (method) `deploynator/_semver.py:113` `def calculate_next_version(self, current, strategy)`
- `SemverManager.is_valid_version` (method) `deploynator/_semver.py:117` `def is_valid_version(version_str)`

## deploynator/_toml.py
Depends on: `deploynator/_config.py`
Imported by: `deploynator/_app.py`, `deploynator/_deb.py`, `deploynator/_deploy.py`, `deploynator/_docs.py`, `deploynator/_pypi.py`, `deploynator/_runner.py`, `tests/bdd_test_deploy.py`, `tests/test_deb.py`, `tests/test_init.py`, `tests/test_pypi.py`, `tests/test_receipt.py`, `tests/test_runner.py`, `tests/test_toml.py`
- `list_make_targets` (function) `deploynator/_toml.py:31` `def list_make_targets(project_path)` -- Lee el Makefile y devuelve sus targets sin ejecutar nada.
- `looks_like_packaging_project` (function) `deploynator/_toml.py:75` `def looks_like_packaging_project(project_path)` -- Inferencia runtime (multi-proyecto): ¿es un paquete PyPI?
- `detect_test_commands` (function) `deploynator/_toml.py:101` `def detect_test_commands(project_path)` -- Detecta comandos de test para proyectos C/autotools sin toml.
- `load_toml_config` (function) `deploynator/_toml.py:217` `def load_toml_config(project_path)`
