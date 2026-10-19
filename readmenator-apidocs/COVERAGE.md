# Documentation Coverage

Overall: **8.3%** (17 of 206 public modules, types, and callables). Data members are excluded from the ratio.

[Back to index](index.md)

## By kind

| Kind | Documented | Total | Coverage |
|---|---|---|---|
| class | 1 | 29 | 3.4% |
| classmethod | 0 | 12 | 0.0% |
| constructor | 0 | 15 | 0.0% |
| enum | 0 | 2 | 0.0% |
| function | 7 | 13 | 53.8% |
| method | 6 | 109 | 5.5% |
| module | 3 | 20 | 15.0% |
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
| [`deploynator._models`](modules/deploynator._models.py.md) | 0 | 27 | 0.0% |
| [`deploynator._runner`](modules/deploynator._runner.py.md) | 0 | 4 | 0.0% |
| [`deploynator._semver`](modules/deploynator._semver.py.md) | 0 | 9 | 0.0% |
| [`install.sh`](modules/install.sh.md) | 0 | 1 | 0.0% |
| [`deploynator._git`](modules/deploynator._git.py.md) | 1 | 25 | 4.0% |
| [`deploynator._mcp_server`](modules/deploynator._mcp_server.py.md) | 1 | 21 | 4.8% |
| [`deploynator._platforms`](modules/deploynator._platforms.py.md) | 2 | 36 | 5.6% |
| [`deploynator._app`](modules/deploynator._app.py.md) | 1 | 16 | 6.2% |
| [`deploynator._deb`](modules/deploynator._deb.py.md) | 1 | 8 | 12.5% |
| [`deploynator._pypi`](modules/deploynator._pypi.py.md) | 2 | 9 | 22.2% |
| [`app`](modules/app.py.md) | 1 | 2 | 50.0% |
| [`deploynator._toml`](modules/deploynator._toml.py.md) | 3 | 6 | 50.0% |
| [`deploynator._readme`](modules/deploynator._readme.py.md) | 3 | 4 | 75.0% |
| [`deploy.sh`](modules/deploy.sh.md) | 2 | 2 | 100.0% |

## Warnings

DOC001 undocumented public item, DOC002 parameter not documented, DOC003 documented parameter missing from the signature (stale doc), DOC004 return value not documented, DOC005 raised exception not documented.

DOC001: 188

- DOC001 `app.py:12` function main is not documented
- DOC001 `deploynator/__init__.py:1` module deploynator/__init__.py is not documented
- DOC001 `deploynator/__main__.py:1` module deploynator/__main__.py is not documented
- DOC001 `deploynator/__main__.py:16` function build_parser is not documented
- DOC001 `deploynator/__main__.py:146` function preprocess_argv is not documented
- DOC001 `deploynator/__main__.py:180` function main is not documented
- DOC001 `deploynator/_app.py:1` module deploynator/_app.py is not documented
- DOC001 `deploynator/_app.py:18` class DeploynatorApp is not documented
- DOC001 `deploynator/_app.py:19` constructor DeploynatorApp.__init__ is not documented
- DOC001 `deploynator/_app.py:29` method DeploynatorApp.auth_login is not documented
- DOC001 `deploynator/_app.py:43` method DeploynatorApp.auth_status is not documented
- DOC001 `deploynator/_app.py:185` method DeploynatorApp.init_project is not documented
- DOC001 `deploynator/_app.py:262` method DeploynatorApp.start_branch is not documented
- DOC001 `deploynator/_app.py:320` method DeploynatorApp.commit is not documented
- DOC001 `deploynator/_app.py:379` method DeploynatorApp.release is not documented
- DOC001 `deploynator/_app.py:517` method DeploynatorApp.generate_docs is not documented
- DOC001 `deploynator/_app.py:523` method DeploynatorApp.status is not documented
- DOC001 `deploynator/_app.py:543` method DeploynatorApp.list_projects is not documented
- DOC001 `deploynator/_app.py:548` method DeploynatorApp.generate_ci is not documented
- DOC001 `deploynator/_app.py:564` method DeploynatorApp.install_deps is not documented
- DOC001 `deploynator/_app.py:602` method DeploynatorApp.interactive_menu is not documented
- DOC001 `deploynator/_changelog.py:1` module deploynator/_changelog.py is not documented
- DOC001 `deploynator/_changelog.py:11` class ChangelogGenerator is not documented
- DOC001 `deploynator/_changelog.py:12` constructor ChangelogGenerator.__init__ is not documented
- DOC001 `deploynator/_changelog.py:15` method ChangelogGenerator.generate_from_log is not documented
- DOC001 `deploynator/_changelog.py:24` method ChangelogGenerator.generate_from_messages is not documented
- DOC001 `deploynator/_changelog.py:44` method ChangelogGenerator.generate_header is not documented
- DOC001 `deploynator/_changelog.py:99` method ChangelogGenerator.write_changelog is not documented
- DOC001 `deploynator/_changelog.py:108` method ChangelogGenerator.format_for_release is not documented
- DOC001 `deploynator/_config.py:1` module deploynator/_config.py is not documented
- DOC001 `deploynator/_config.py:8` class Config is not documented
- DOC001 `deploynator/_config.py:80` staticmethod Config.create is not documented
- DOC001 `deploynator/_config.py:86` method Config.resolve_path is not documented
- DOC001 `deploynator/_config.py:92` property Config.gh_authd is not documented
- DOC001 `deploynator/_config.py:96` property Config.glab_authd is not documented
- DOC001 `deploynator/_config.py:100` property Config.bb_authd is not documented
- DOC001 `deploynator/_deb.py:1` module deploynator/_deb.py is not documented
- DOC001 `deploynator/_deb.py:38` method DebRunner.deb_make_target is not documented
- DOC001 `deploynator/_deb.py:48` method DebRunner.is_deb_project is not documented
- DOC001 `deploynator/_deb.py:62` method DebRunner.clean is not documented
- DOC001 `deploynator/_deb.py:110` method DebRunner.build_command is not documented
- DOC001 `deploynator/_deb.py:126` method DebRunner.run is not documented
- DOC001 `deploynator/_deploy.py:1` module deploynator/_deploy.py is not documented
- DOC001 `deploynator/_deploy.py:30` class ProjectDiscovery is not documented
- DOC001 `deploynator/_deploy.py:31` constructor ProjectDiscovery.__init__ is not documented
- DOC001 `deploynator/_deploy.py:34` method ProjectDiscovery.discover is not documented
- DOC001 `deploynator/_deploy.py:55` method ProjectDiscovery.find_by_name is not documented
- DOC001 `deploynator/_deploy.py:75` class DeployOrchestrator is not documented
- DOC001 `deploynator/_deploy.py:76` constructor DeployOrchestrator.__init__ is not documented
- DOC001 `deploynator/_deploy.py:97` method DeployOrchestrator.deploy is not documented
- DOC001 `deploynator/_deploy.py:524` method DeployOrchestrator.generate_workflows is not documented
- DOC001 `deploynator/_deploy.py:591` method DeployOrchestrator.install_dependencies is not documented
- DOC001 `deploynator/_deploy.py:601` method DeployOrchestrator.integrate_readmenator is not documented
- DOC001 `deploynator/_deploy.py:637` method DeployOrchestrator.install_lazygit is not documented
- DOC001 `deploynator/_docs.py:1` module deploynator/_docs.py is not documented
- DOC001 `deploynator/_docs.py:10` class DocsRunner is not documented
- DOC001 `deploynator/_docs.py:11` constructor DocsRunner.__init__ is not documented
- DOC001 `deploynator/_docs.py:14` method DocsRunner.run is not documented
- DOC001 `deploynator/_git.py:1` module deploynator/_git.py is not documented
- DOC001 `deploynator/_git.py:9` class GitOperations is not documented
- DOC001 `deploynator/_git.py:10` constructor GitOperations.__init__ is not documented
- DOC001 `deploynator/_git.py:13` method GitOperations.check_gpg is not documented
- DOC001 `deploynator/_git.py:31` method GitOperations.gpg_sign_flag is not documented
- DOC001 `deploynator/_git.py:35` method GitOperations.clone is not documented
- DOC001 `deploynator/_git.py:45` method GitOperations.add_all is not documented
- DOC001 `deploynator/_git.py:58` method GitOperations.commit is not documented
- DOC001 `deploynator/_git.py:87` method GitOperations.amend_no_edit is not documented
- DOC001 `deploynator/_git.py:96` method GitOperations.tag is not documented
- DOC001 `deploynator/_git.py:106` method GitOperations.delete_tag is not documented
- DOC001 `deploynator/_git.py:116` method GitOperations.tag_exists is not documented
- DOC001 `deploynator/_git.py:126` method GitOperations.push is not documented
- DOC001 `deploynator/_git.py:136` method GitOperations.push_tags is not documented
- DOC001 `deploynator/_git.py:146` method GitOperations.create_branch is not documented
- DOC001 `deploynator/_git.py:162` method GitOperations.checkout is not documented
- DOC001 `deploynator/_git.py:172` method GitOperations.get_changed_files is not documented
- DOC001 `deploynator/_git.py:203` method GitOperations.get_log is not documented
- DOC001 `deploynator/_git.py:215` method GitOperations.get_start_ref is not documented
- DOC001 `deploynator/_git.py:233` method GitOperations.current_branch is not documented
- DOC001 `deploynator/_git.py:245` method GitOperations.is_dirty is not documented
- DOC001 `deploynator/_git.py:255` method GitOperations.has_remote is not documented
- DOC001 `deploynator/_git.py:265` method GitOperations.branch_exists is not documented
- DOC001 `deploynator/_git.py:290` method GitOperations.push_force is not documented
- DOC001 `deploynator/_mcp_server.py:36` class MCPRequest is not documented
- DOC001 `deploynator/_mcp_server.py:37` constructor MCPRequest.__init__ is not documented
- DOC001 `deploynator/_mcp_server.py:44` property MCPRequest.is_notification is not documented
- DOC001 `deploynator/_mcp_server.py:47` method MCPRequest.response is not documented
- DOC001 `deploynator/_mcp_server.py:50` method MCPRequest.error is not documented
- DOC001 `deploynator/_mcp_server.py:57` class MCPTool is not documented
- DOC001 `deploynator/_mcp_server.py:58` constructor MCPTool.__init__ is not documented
- DOC001 `deploynator/_mcp_server.py:65` method MCPTool.definition is not documented
- DOC001 `deploynator/_mcp_server.py:68` method MCPTool.call is not documented
- DOC001 `deploynator/_mcp_server.py:72` class MCPResource is not documented
- DOC001 `deploynator/_mcp_server.py:73` constructor MCPResource.__init__ is not documented
- DOC001 `deploynator/_mcp_server.py:80` method MCPResource.definition is not documented
- DOC001 `deploynator/_mcp_server.py:83` method MCPResource.read is not documented
- DOC001 `deploynator/_mcp_server.py:87` class MCPServer is not documented
- DOC001 `deploynator/_mcp_server.py:88` constructor MCPServer.__init__ is not documented
- DOC001 `deploynator/_mcp_server.py:95` method MCPServer.register_tool is not documented
- DOC001 `deploynator/_mcp_server.py:98` method MCPServer.register_resource is not documented
- DOC001 `deploynator/_mcp_server.py:145` method MCPServer.dispatch is not documented
- DOC001 `deploynator/_mcp_server.py:163` method MCPServer.run is not documented
- DOC001 `deploynator/_mcp_server.py:273` function main is not documented
- DOC001 `deploynator/_models.py:1` module deploynator/_models.py is not documented
- DOC001 `deploynator/_models.py:9` enum Platform is not documented
- DOC001 `deploynator/_models.py:15` classmethod Platform.from_string is not documented
- DOC001 `deploynator/_models.py:26` method Platform.label is not documented
- DOC001 `deploynator/_models.py:29` method Platform.cli_name is not documented
- DOC001 `deploynator/_models.py:36` method Platform.auth_env_var is not documented
- DOC001 `deploynator/_models.py:44` enum CommitType is not documented
- DOC001 `deploynator/_models.py:57` classmethod CommitType.from_string is not documented
- DOC001 `deploynator/_models.py:64` classmethod CommitType.valid_types is not documented
- DOC001 `deploynator/_models.py:67` method CommitType.bump_strategy is not documented
- DOC001 `deploynator/_models.py:81` method CommitType.section_header is not documented
- DOC001 `deploynator/_models.py:97` class PlatformConfig is not documented
- DOC001 `deploynator/_models.py:104` classmethod PlatformConfig.from_dict is not documented
- DOC001 `deploynator/_models.py:114` class VersionConfig is not documented
- DOC001 `deploynator/_models.py:120` classmethod VersionConfig.from_dict is not documented
- DOC001 `deploynator/_models.py:129` class ProjectConfig is not documented
- DOC001 `deploynator/_models.py:138` classmethod ProjectConfig.from_dict is not documented
- DOC001 `deploynator/_models.py:174` class CommitMessage is not documented
- DOC001 `deploynator/_models.py:182` method CommitMessage.format is not documented
- DOC001 `deploynator/_models.py:194` classmethod CommitMessage.parse is not documented
- DOC001 `deploynator/_models.py:207` class VersionInfo is not documented
- DOC001 `deploynator/_models.py:216` classmethod VersionInfo.parse is not documented
- DOC001 `deploynator/_models.py:227` method VersionInfo.bump is not documented
- DOC001 `deploynator/_models.py:238` class ChangelogEntry is not documented
- DOC001 `deploynator/_models.py:246` classmethod ChangelogEntry.from_git_log_line is not documented
- DOC001 `deploynator/_models.py:265` class ReleaseInfo is not documented
- DOC001 `deploynator/_models.py:276` class DeployResult is not documented
- DOC001 `deploynator/_platforms.py:1` module deploynator/_platforms.py is not documented
- DOC001 `deploynator/_platforms.py:13` class PlatformClient is not documented
- DOC001 `deploynator/_platforms.py:14` constructor PlatformClient.__init__ is not documented
- DOC001 `deploynator/_platforms.py:18` method PlatformClient.name is not documented
- DOC001 `deploynator/_platforms.py:22` method PlatformClient.is_available is not documented
- DOC001 `deploynator/_platforms.py:26` method PlatformClient.is_authenticated is not documented
- DOC001 `deploynator/_platforms.py:30` method PlatformClient.create_release is not documented
- DOC001 `deploynator/_platforms.py:34` method PlatformClient.create_pull_request is not documented
- DOC001 `deploynator/_platforms.py:38` method PlatformClient.push_changes is not documented
- DOC001 `deploynator/_platforms.py:52` class GitHubCLI is not documented
- DOC001 `deploynator/_platforms.py:53` method GitHubCLI.name is not documented
- DOC001 `deploynator/_platforms.py:56` method GitHubCLI.is_available is not documented
- DOC001 `deploynator/_platforms.py:63` method GitHubCLI.is_authenticated is not documented
- DOC001 `deploynator/_platforms.py:70` method GitHubCLI.create_release is not documented
- DOC001 `deploynator/_platforms.py:94` method GitHubCLI.create_pull_request is not documented
- DOC001 `deploynator/_platforms.py:125` method GitHubCLI.push_changes is not documented
- DOC001 `deploynator/_platforms.py:133` class GitLabCLI is not documented
- DOC001 `deploynator/_platforms.py:134` method GitLabCLI.name is not documented
- DOC001 `deploynator/_platforms.py:137` method GitLabCLI.is_available is not documented
- DOC001 `deploynator/_platforms.py:144` method GitLabCLI.is_authenticated is not documented
- DOC001 `deploynator/_platforms.py:151` method GitLabCLI.create_release is not documented
- DOC001 `deploynator/_platforms.py:162` method GitLabCLI.create_pull_request is not documented
- DOC001 `deploynator/_platforms.py:176` method GitLabCLI.push_changes is not documented
- DOC001 `deploynator/_platforms.py:184` class BitbucketCLI is not documented
- DOC001 `deploynator/_platforms.py:185` method BitbucketCLI.name is not documented
- DOC001 `deploynator/_platforms.py:188` method BitbucketCLI.is_available is not documented
- DOC001 `deploynator/_platforms.py:198` method BitbucketCLI.is_authenticated is not documented
- DOC001 `deploynator/_platforms.py:201` method BitbucketCLI.create_release is not documented
- DOC001 `deploynator/_platforms.py:221` method BitbucketCLI.create_pull_request is not documented
- DOC001 `deploynator/_platforms.py:235` method BitbucketCLI.push_changes is not documented
- DOC001 `deploynator/_platforms.py:243` class PlatformFactory is not documented
- DOC001 `deploynator/_platforms.py:251` classmethod PlatformFactory.register is not documented
- DOC001 `deploynator/_platforms.py:255` classmethod PlatformFactory.create is not documented
- DOC001 `deploynator/_platforms.py:262` classmethod PlatformFactory.create_all_available is not documented
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
- DOC001 `deploynator/_semver.py:11` class SemverManager is not documented
- DOC001 `deploynator/_semver.py:12` constructor SemverManager.__init__ is not documented
- DOC001 `deploynator/_semver.py:15` method SemverManager.max_version is not documented
- DOC001 `deploynator/_semver.py:20` method SemverManager.get_current_version is not documented
- DOC001 `deploynator/_semver.py:65` method SemverManager.write_version_file is not documented
- DOC001 `deploynator/_semver.py:110` method SemverManager.determine_bump is not documented
- DOC001 `deploynator/_semver.py:113` method SemverManager.calculate_next_version is not documented
- DOC001 `deploynator/_semver.py:117` staticmethod SemverManager.is_valid_version is not documented
- DOC001 `deploynator/_toml.py:1` module deploynator/_toml.py is not documented
- DOC001 `deploynator/_toml.py:177` class TomlConfig is not documented
- DOC001 `deploynator/_toml.py:217` function load_toml_config is not documented
- DOC001 `install.sh:1` module install.sh is not documented
