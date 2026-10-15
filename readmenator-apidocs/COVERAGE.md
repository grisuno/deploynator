# Documentation Coverage

Overall: **5.3%** (10 of 190 public modules, types, and callables). Data members are excluded from the ratio.

[Back to index](index.md)

## By kind

| Kind | Documented | Total | Coverage |
|---|---|---|---|
| class | 0 | 28 | 0.0% |
| classmethod | 0 | 12 | 0.0% |
| constructor | 0 | 14 | 0.0% |
| enum | 0 | 2 | 0.0% |
| function | 4 | 10 | 40.0% |
| method | 3 | 99 | 3.0% |
| module | 3 | 19 | 15.8% |
| property | 0 | 4 | 0.0% |
| staticmethod | 0 | 2 | 0.0% |

## By module (lowest first)

| Module | Documented | Total | Coverage |
|---|---|---|---|
| [`deploynator`](modules/deploynator.__init__.py.md) | 0 | 1 | 0.0% |
| [`deploynator.__main__`](modules/deploynator.__main__.py.md) | 0 | 4 | 0.0% |
| [`deploynator._changelog`](modules/deploynator._changelog.py.md) | 0 | 8 | 0.0% |
| [`deploynator._config`](modules/deploynator._config.py.md) | 0 | 7 | 0.0% |
| [`deploynator._deploy`](modules/deploynator._deploy.py.md) | 0 | 12 | 0.0% |
| [`deploynator._docs`](modules/deploynator._docs.py.md) | 0 | 4 | 0.0% |
| [`deploynator._git`](modules/deploynator._git.py.md) | 0 | 22 | 0.0% |
| [`deploynator._models`](modules/deploynator._models.py.md) | 0 | 27 | 0.0% |
| [`deploynator._platforms`](modules/deploynator._platforms.py.md) | 0 | 34 | 0.0% |
| [`deploynator._runner`](modules/deploynator._runner.py.md) | 0 | 4 | 0.0% |
| [`deploynator._semver`](modules/deploynator._semver.py.md) | 0 | 9 | 0.0% |
| [`deploynator._toml`](modules/deploynator._toml.py.md) | 0 | 3 | 0.0% |
| [`install.sh`](modules/install.sh.md) | 0 | 1 | 0.0% |
| [`deploynator._mcp_server`](modules/deploynator._mcp_server.py.md) | 1 | 21 | 4.8% |
| [`deploynator._app`](modules/deploynator._app.py.md) | 1 | 16 | 6.2% |
| [`deploynator._pypi`](modules/deploynator._pypi.py.md) | 2 | 9 | 22.2% |
| [`app`](modules/app.py.md) | 1 | 2 | 50.0% |
| [`deploynator._readme`](modules/deploynator._readme.py.md) | 3 | 4 | 75.0% |
| [`deploy.sh`](modules/deploy.sh.md) | 2 | 2 | 100.0% |

## Warnings

DOC001 undocumented public item, DOC002 parameter not documented, DOC003 documented parameter missing from the signature (stale doc), DOC004 return value not documented, DOC005 raised exception not documented.

DOC001: 180

- DOC001 `app.py:12` function main is not documented
- DOC001 `deploynator/__init__.py:1` module deploynator/__init__.py is not documented
- DOC001 `deploynator/__main__.py:1` module deploynator/__main__.py is not documented
- DOC001 `deploynator/__main__.py:17` function build_parser is not documented
- DOC001 `deploynator/__main__.py:133` function preprocess_argv is not documented
- DOC001 `deploynator/__main__.py:167` function main is not documented
- DOC001 `deploynator/_app.py:1` module deploynator/_app.py is not documented
- DOC001 `deploynator/_app.py:20` class DeploynatorApp is not documented
- DOC001 `deploynator/_app.py:21` constructor DeploynatorApp.__init__ is not documented
- DOC001 `deploynator/_app.py:31` method DeploynatorApp.auth_login is not documented
- DOC001 `deploynator/_app.py:45` method DeploynatorApp.auth_status is not documented
- DOC001 `deploynator/_app.py:168` method DeploynatorApp.init_project is not documented
- DOC001 `deploynator/_app.py:218` method DeploynatorApp.start_branch is not documented
- DOC001 `deploynator/_app.py:276` method DeploynatorApp.commit is not documented
- DOC001 `deploynator/_app.py:316` method DeploynatorApp.release is not documented
- DOC001 `deploynator/_app.py:406` method DeploynatorApp.generate_docs is not documented
- DOC001 `deploynator/_app.py:412` method DeploynatorApp.status is not documented
- DOC001 `deploynator/_app.py:432` method DeploynatorApp.list_projects is not documented
- DOC001 `deploynator/_app.py:437` method DeploynatorApp.generate_ci is not documented
- DOC001 `deploynator/_app.py:453` method DeploynatorApp.install_deps is not documented
- DOC001 `deploynator/_app.py:492` method DeploynatorApp.interactive_menu is not documented
- DOC001 `deploynator/_changelog.py:1` module deploynator/_changelog.py is not documented
- DOC001 `deploynator/_changelog.py:12` class ChangelogGenerator is not documented
- DOC001 `deploynator/_changelog.py:13` constructor ChangelogGenerator.__init__ is not documented
- DOC001 `deploynator/_changelog.py:16` method ChangelogGenerator.generate_from_log is not documented
- DOC001 `deploynator/_changelog.py:25` method ChangelogGenerator.generate_from_messages is not documented
- DOC001 `deploynator/_changelog.py:45` method ChangelogGenerator.generate_header is not documented
- DOC001 `deploynator/_changelog.py:100` method ChangelogGenerator.write_changelog is not documented
- DOC001 `deploynator/_changelog.py:110` method ChangelogGenerator.format_for_release is not documented
- DOC001 `deploynator/_config.py:1` module deploynator/_config.py is not documented
- DOC001 `deploynator/_config.py:8` class Config is not documented
- DOC001 `deploynator/_config.py:79` staticmethod Config.create is not documented
- DOC001 `deploynator/_config.py:85` method Config.resolve_path is not documented
- DOC001 `deploynator/_config.py:91` property Config.gh_authd is not documented
- DOC001 `deploynator/_config.py:95` property Config.glab_authd is not documented
- DOC001 `deploynator/_config.py:99` property Config.bb_authd is not documented
- DOC001 `deploynator/_deploy.py:1` module deploynator/_deploy.py is not documented
- DOC001 `deploynator/_deploy.py:31` class ProjectDiscovery is not documented
- DOC001 `deploynator/_deploy.py:32` constructor ProjectDiscovery.__init__ is not documented
- DOC001 `deploynator/_deploy.py:35` method ProjectDiscovery.discover is not documented
- DOC001 `deploynator/_deploy.py:56` method ProjectDiscovery.find_by_name is not documented
- DOC001 `deploynator/_deploy.py:76` class DeployOrchestrator is not documented
- DOC001 `deploynator/_deploy.py:77` constructor DeployOrchestrator.__init__ is not documented
- DOC001 `deploynator/_deploy.py:97` method DeployOrchestrator.deploy is not documented
- DOC001 `deploynator/_deploy.py:421` method DeployOrchestrator.generate_workflows is not documented
- DOC001 `deploynator/_deploy.py:489` method DeployOrchestrator.install_dependencies is not documented
- DOC001 `deploynator/_deploy.py:499` method DeployOrchestrator.integrate_readmenator is not documented
- DOC001 `deploynator/_deploy.py:533` method DeployOrchestrator.install_lazygit is not documented
- DOC001 `deploynator/_docs.py:1` module deploynator/_docs.py is not documented
- DOC001 `deploynator/_docs.py:10` class DocsRunner is not documented
- DOC001 `deploynator/_docs.py:11` constructor DocsRunner.__init__ is not documented
- DOC001 `deploynator/_docs.py:14` method DocsRunner.run is not documented
- DOC001 `deploynator/_git.py:1` module deploynator/_git.py is not documented
- DOC001 `deploynator/_git.py:10` class GitOperations is not documented
- DOC001 `deploynator/_git.py:11` constructor GitOperations.__init__ is not documented
- DOC001 `deploynator/_git.py:14` method GitOperations.check_gpg is not documented
- DOC001 `deploynator/_git.py:32` method GitOperations.gpg_sign_flag is not documented
- DOC001 `deploynator/_git.py:36` method GitOperations.clone is not documented
- DOC001 `deploynator/_git.py:46` method GitOperations.add_all is not documented
- DOC001 `deploynator/_git.py:56` method GitOperations.commit is not documented
- DOC001 `deploynator/_git.py:68` method GitOperations.amend_no_edit is not documented
- DOC001 `deploynator/_git.py:77` method GitOperations.tag is not documented
- DOC001 `deploynator/_git.py:87` method GitOperations.delete_tag is not documented
- DOC001 `deploynator/_git.py:97` method GitOperations.tag_exists is not documented
- DOC001 `deploynator/_git.py:107` method GitOperations.push is not documented
- DOC001 `deploynator/_git.py:117` method GitOperations.push_tags is not documented
- DOC001 `deploynator/_git.py:127` method GitOperations.create_branch is not documented
- DOC001 `deploynator/_git.py:143` method GitOperations.checkout is not documented
- DOC001 `deploynator/_git.py:153` method GitOperations.get_changed_files is not documented
- DOC001 `deploynator/_git.py:184` method GitOperations.get_log is not documented
- DOC001 `deploynator/_git.py:196` method GitOperations.get_start_ref is not documented
- DOC001 `deploynator/_git.py:214` method GitOperations.current_branch is not documented
- DOC001 `deploynator/_git.py:226` method GitOperations.is_dirty is not documented
- DOC001 `deploynator/_git.py:236` method GitOperations.has_remote is not documented
- DOC001 `deploynator/_mcp_server.py:35` class MCPRequest is not documented
- DOC001 `deploynator/_mcp_server.py:36` constructor MCPRequest.__init__ is not documented
- DOC001 `deploynator/_mcp_server.py:43` property MCPRequest.is_notification is not documented
- DOC001 `deploynator/_mcp_server.py:46` method MCPRequest.response is not documented
- DOC001 `deploynator/_mcp_server.py:49` method MCPRequest.error is not documented
- DOC001 `deploynator/_mcp_server.py:56` class MCPTool is not documented
- DOC001 `deploynator/_mcp_server.py:57` constructor MCPTool.__init__ is not documented
- DOC001 `deploynator/_mcp_server.py:64` method MCPTool.definition is not documented
- DOC001 `deploynator/_mcp_server.py:67` method MCPTool.call is not documented
- DOC001 `deploynator/_mcp_server.py:71` class MCPResource is not documented
- DOC001 `deploynator/_mcp_server.py:72` constructor MCPResource.__init__ is not documented
- DOC001 `deploynator/_mcp_server.py:79` method MCPResource.definition is not documented
- DOC001 `deploynator/_mcp_server.py:82` method MCPResource.read is not documented
- DOC001 `deploynator/_mcp_server.py:86` class MCPServer is not documented
- DOC001 `deploynator/_mcp_server.py:87` constructor MCPServer.__init__ is not documented
- DOC001 `deploynator/_mcp_server.py:94` method MCPServer.register_tool is not documented
- DOC001 `deploynator/_mcp_server.py:97` method MCPServer.register_resource is not documented
- DOC001 `deploynator/_mcp_server.py:144` method MCPServer.dispatch is not documented
- DOC001 `deploynator/_mcp_server.py:162` method MCPServer.run is not documented
- DOC001 `deploynator/_mcp_server.py:269` function main is not documented
- DOC001 `deploynator/_models.py:1` module deploynator/_models.py is not documented
- DOC001 `deploynator/_models.py:10` enum Platform is not documented
- DOC001 `deploynator/_models.py:16` classmethod Platform.from_string is not documented
- DOC001 `deploynator/_models.py:27` method Platform.label is not documented
- DOC001 `deploynator/_models.py:30` method Platform.cli_name is not documented
- DOC001 `deploynator/_models.py:37` method Platform.auth_env_var is not documented
- DOC001 `deploynator/_models.py:45` enum CommitType is not documented
- DOC001 `deploynator/_models.py:58` classmethod CommitType.from_string is not documented
- DOC001 `deploynator/_models.py:65` classmethod CommitType.valid_types is not documented
- DOC001 `deploynator/_models.py:68` method CommitType.bump_strategy is not documented
- DOC001 `deploynator/_models.py:82` method CommitType.section_header is not documented
- DOC001 `deploynator/_models.py:98` class PlatformConfig is not documented
- DOC001 `deploynator/_models.py:105` classmethod PlatformConfig.from_dict is not documented
- DOC001 `deploynator/_models.py:115` class VersionConfig is not documented
- DOC001 `deploynator/_models.py:121` classmethod VersionConfig.from_dict is not documented
- DOC001 `deploynator/_models.py:130` class ProjectConfig is not documented
- DOC001 `deploynator/_models.py:139` classmethod ProjectConfig.from_dict is not documented
- DOC001 `deploynator/_models.py:175` class CommitMessage is not documented
- DOC001 `deploynator/_models.py:183` method CommitMessage.format is not documented
- DOC001 `deploynator/_models.py:195` classmethod CommitMessage.parse is not documented
- DOC001 `deploynator/_models.py:208` class VersionInfo is not documented
- DOC001 `deploynator/_models.py:217` classmethod VersionInfo.parse is not documented
- DOC001 `deploynator/_models.py:228` method VersionInfo.bump is not documented
- DOC001 `deploynator/_models.py:239` class ChangelogEntry is not documented
- DOC001 `deploynator/_models.py:247` classmethod ChangelogEntry.from_git_log_line is not documented
- DOC001 `deploynator/_models.py:266` class ReleaseInfo is not documented
- DOC001 `deploynator/_models.py:276` class DeployResult is not documented
- DOC001 `deploynator/_platforms.py:1` module deploynator/_platforms.py is not documented
- DOC001 `deploynator/_platforms.py:14` class PlatformClient is not documented
- DOC001 `deploynator/_platforms.py:15` constructor PlatformClient.__init__ is not documented
- DOC001 `deploynator/_platforms.py:19` method PlatformClient.name is not documented
- DOC001 `deploynator/_platforms.py:23` method PlatformClient.is_available is not documented
- DOC001 `deploynator/_platforms.py:27` method PlatformClient.is_authenticated is not documented
- DOC001 `deploynator/_platforms.py:31` method PlatformClient.create_release is not documented
- DOC001 `deploynator/_platforms.py:35` method PlatformClient.create_pull_request is not documented
- DOC001 `deploynator/_platforms.py:39` method PlatformClient.push_changes is not documented
- DOC001 `deploynator/_platforms.py:49` class GitHubCLI is not documented
- DOC001 `deploynator/_platforms.py:50` method GitHubCLI.name is not documented
- DOC001 `deploynator/_platforms.py:53` method GitHubCLI.is_available is not documented
- DOC001 `deploynator/_platforms.py:60` method GitHubCLI.is_authenticated is not documented
- DOC001 `deploynator/_platforms.py:67` method GitHubCLI.create_release is not documented
- DOC001 `deploynator/_platforms.py:91` method GitHubCLI.create_pull_request is not documented
- DOC001 `deploynator/_platforms.py:105` method GitHubCLI.push_changes is not documented
- DOC001 `deploynator/_platforms.py:113` class GitLabCLI is not documented
- DOC001 `deploynator/_platforms.py:114` method GitLabCLI.name is not documented
- DOC001 `deploynator/_platforms.py:117` method GitLabCLI.is_available is not documented
- DOC001 `deploynator/_platforms.py:124` method GitLabCLI.is_authenticated is not documented
- DOC001 `deploynator/_platforms.py:131` method GitLabCLI.create_release is not documented
- DOC001 `deploynator/_platforms.py:142` method GitLabCLI.create_pull_request is not documented
- DOC001 `deploynator/_platforms.py:156` method GitLabCLI.push_changes is not documented
- DOC001 `deploynator/_platforms.py:164` class BitbucketCLI is not documented
- DOC001 `deploynator/_platforms.py:165` method BitbucketCLI.name is not documented
- DOC001 `deploynator/_platforms.py:168` method BitbucketCLI.is_available is not documented
- DOC001 `deploynator/_platforms.py:178` method BitbucketCLI.is_authenticated is not documented
- DOC001 `deploynator/_platforms.py:181` method BitbucketCLI.create_release is not documented
- DOC001 `deploynator/_platforms.py:201` method BitbucketCLI.create_pull_request is not documented
- DOC001 `deploynator/_platforms.py:215` method BitbucketCLI.push_changes is not documented
- DOC001 `deploynator/_platforms.py:223` class PlatformFactory is not documented
- DOC001 `deploynator/_platforms.py:231` classmethod PlatformFactory.register is not documented
- DOC001 `deploynator/_platforms.py:235` classmethod PlatformFactory.create is not documented
- DOC001 `deploynator/_platforms.py:242` classmethod PlatformFactory.create_all_available is not documented
- DOC001 `deploynator/_pypi.py:1` module deploynator/_pypi.py is not documented
- DOC001 `deploynator/_pypi.py:12` class PyPIRunner is not documented
- DOC001 `deploynator/_pypi.py:13` constructor PyPIRunner.__init__ is not documented
- DOC001 `deploynator/_pypi.py:16` method PyPIRunner.is_packaging_project is not documented
- DOC001 `deploynator/_pypi.py:33` method PyPIRunner.has_credentials is not documented
- DOC001 `deploynator/_pypi.py:90` method PyPIRunner.clean is not documented
- DOC001 `deploynator/_pypi.py:107` method PyPIRunner.run is not documented
- DOC001 `deploynator/_readme.py:1` module deploynator/_readme.py is not documented
- DOC001 `deploynator/_runner.py:1` module deploynator/_runner.py is not documented
- DOC001 `deploynator/_runner.py:11` class TestRunner is not documented
- DOC001 `deploynator/_runner.py:12` constructor TestRunner.__init__ is not documented
- DOC001 `deploynator/_runner.py:15` method TestRunner.run is not documented
- DOC001 `deploynator/_semver.py:1` module deploynator/_semver.py is not documented
- DOC001 `deploynator/_semver.py:12` class SemverManager is not documented
- DOC001 `deploynator/_semver.py:13` constructor SemverManager.__init__ is not documented
- DOC001 `deploynator/_semver.py:16` method SemverManager.max_version is not documented
- DOC001 `deploynator/_semver.py:21` method SemverManager.get_current_version is not documented
- DOC001 `deploynator/_semver.py:66` method SemverManager.write_version_file is not documented
- DOC001 `deploynator/_semver.py:111` method SemverManager.determine_bump is not documented
- DOC001 `deploynator/_semver.py:114` method SemverManager.calculate_next_version is not documented
- DOC001 `deploynator/_semver.py:118` staticmethod SemverManager.is_valid_version is not documented
- DOC001 `deploynator/_toml.py:1` module deploynator/_toml.py is not documented
- DOC001 `deploynator/_toml.py:14` class TomlConfig is not documented
- DOC001 `deploynator/_toml.py:46` function load_toml_config is not documented
- DOC001 `install.sh:1` module install.sh is not documented
