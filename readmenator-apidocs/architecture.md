# deploynator Architecture and Execution Flows

[Back to index](index.md)

## Architecture Overview

6 components stacked in 5 dependency tiers (weighted Eades-Lin-Smyth ordering: arrows point from dependent to dependency, top to bottom). Labels are import counts, thick arrows the top quartile; 4 transitively implied edges are omitted. Dashed red arrows are upward dependencies: the smallest set of imports that closes every cycle and breaks the layering. Cyan components hold entry points. Interactive version: `readmenator-apidocs/index.html#/flows`.

Upward dependencies to fix first: `deploynator: _changelog` -> `deploynator: _toml` (1 imports); `deploynator: _models` -> `deploynator: _changelog` (1 imports)

```mermaid
flowchart TB
    classDef cycle fill:#1f1530,stroke:#f472b6,color:#fce7f3,stroke-width:2px;
    classDef default fill:#111827,stroke:#38bdf8,color:#e5e7eb;
    classDef entry fill:#0e7490,stroke:#22d3ee,color:#ecfeff,stroke-width:2px;
    subgraph lane_0["Tier 1 - entry / orchestration"]
        direction LR
        n_c4["deploynator: _mcp_server<br/>3 files, 35 symbols<br/>Core / utility"]:::entry
        n_d__root_["(root)<br/>2 files, 0 symbols<br/>Core / utility"]:::entry
    end
    subgraph lane_1["Tier 2"]
        direction LR
        n_c3["deploynator: _platforms<br/>4 files, 105 symbols<br/>Core / utility"]:::default
    end
    subgraph lane_2["Tier 3"]
        direction LR
        n_c1["deploynator: _toml<br/>3 files, 10 symbols<br/>Core / utility"]:::cycle
    end
    subgraph lane_3["Tier 4"]
        direction LR
        n_c0["deploynator: _changelog<br/>3 files, 23 symbols<br/>Core / utility"]:::cycle
    end
    subgraph lane_4["Tier 5 - foundation"]
        direction LR
        n_c2["deploynator: _models<br/>2 files, 36 symbols<br/>Business logic"]:::cycle
    end
    n_c0 -->|"1"| n_c2
    n_c1 ==>|"3"| n_c0
    n_c3 ==>|"4"| n_c1
    n_c4 -->|"1"| n_c3
    n_c1 <-.-|"1 upward"| n_c0
    n_c0 <-.-|"1 upward"| n_c2
    linkStyle 4,5 stroke:#f87171,stroke-width:2px;
    n_c4 ~~~ n_c3
    n_c3 ~~~ n_c1
    n_c1 ~~~ n_c0
    n_c0 ~~~ n_c2
```

---

## Execution Flows

Entry points are scored from `__main__` guards, `main` functions, entry-style names and files, and call-graph sources. Each flow walks resolved calls in call-site order (depth <= 4, <= 40 steps); numbers give the call order, dashed arrows revisit an already expanded callee, red arrows are recursion. Interactive version with zoom and per-node docs: `readmenator-apidocs/index.html#/flows`.

### `__main__.main`

`deploynator/__main__.py:164`, score 9: entry-style name `main`; defined in entry file `__main__.py`; called from the `__main__` guard.

Control flow:

```mermaid
flowchart TB
    classDef decision fill:#1e1b4b,stroke:#a78bfa,color:#ede9fe;
    classDef default fill:#111827,stroke:#38bdf8,color:#e5e7eb;
    classDef entry fill:#0e7490,stroke:#22d3ee,color:#ecfeff,stroke-width:2px;
    n_s1(["start __main__.main"]):::entry
    n_s2{"not raw_argv?"}:::decision
    n_s3(["return after create(), interactive_menu(), DeploynatorApp()"]):::entry
    n_s4["preprocess_argv(), create(), DeploynatorApp()"]:::default
    n_s5{"not args.command?"}:::decision
    n_s6(["return after build_parser()"]):::entry
    n_s7{"args.command == 'release'?"}:::decision
    n_s8["release()"]:::default
    n_s9{"args.command == 'commit'?"}:::decision
    n_s10["commit()"]:::default
    n_s11{"args.command == 'start'?"}:::decision
    n_s12["start_branch()"]:::default
    n_s13{"args.command == 'auth'?"}:::decision
    n_s14{"args.auth_command == 'login'?"}:::decision
    n_s15["auth_login()"]:::default
    n_s16{{"for (p, ok) in results.items()"}}:::decision
    n_s17{"args.auth_command == 'status'?"}:::decision
    n_s18["auth_status()"]:::default
    n_s19{{"for (p, ok) in status.items()"}}:::decision
    n_s20["build_parser()"]:::default
    n_s21{"args.command == 'docs'?"}:::decision
    n_s22["generate_docs()"]:::default
    n_s23{"args.command == 'init'?"}:::decision
    n_s24["init_project()"]:::default
    n_s25{"args.command == 'status'?"}:::decision
    n_s26["status()"]:::default
    n_s27{{"for (k, v) in info.items()"}}:::decision
    n_s28{"args.command == 'projects'?"}:::decision
    n_s29["list_projects()"]:::default
    n_s30{"not projects?"}:::decision
    n_s31(["return"]):::entry
    n_s32{{"for p in projects"}}:::decision
    n_s33["label()"]:::default
    n_s34{"args.command == 'workflow'?"}:::decision
    n_s35["generate_ci()"]:::default
    n_s36{{"for path in created"}}:::decision
    n_s37{"args.command == 'install'?"}:::decision
    n_s38["install_deps()"]:::default
    n_s39{{"for (p, ok) in deps.items()"}}:::decision
    n_s40{"args.command == 'interactive'?"}:::decision
    n_s41["interactive_menu()"]:::default
    n_s42{"args.command == 'serve'?"}:::decision
    n_s43["run(), MCPServer()"]:::default
    n_s44(["end"]):::entry
    n_s1 --> n_s2
    n_s2 -->|"yes"| n_s3
    n_s2 -->|"no"| n_s4
    n_s4 --> n_s5
    n_s5 -->|"yes"| n_s6
    n_s5 -->|"no"| n_s7
    n_s7 -->|"yes"| n_s8
    n_s7 -->|"no"| n_s9
    n_s9 -->|"yes"| n_s10
    n_s9 -->|"no"| n_s11
    n_s11 -->|"yes"| n_s12
    n_s11 -->|"no"| n_s13
    n_s13 -->|"yes"| n_s14
    n_s14 -->|"yes"| n_s15
    n_s15 --> n_s16
    n_s16 -.->|"each"| n_s16
    n_s14 -->|"no"| n_s17
    n_s17 -->|"yes"| n_s18
    n_s18 --> n_s19
    n_s19 -.->|"each"| n_s19
    n_s17 -->|"no"| n_s20
    n_s13 -->|"no"| n_s21
    n_s21 -->|"yes"| n_s22
    n_s21 -->|"no"| n_s23
    n_s23 -->|"yes"| n_s24
    n_s23 -->|"no"| n_s25
    n_s25 -->|"yes"| n_s26
    n_s26 --> n_s27
    n_s27 -.->|"each"| n_s27
    n_s25 -->|"no"| n_s28
    n_s28 -->|"yes"| n_s29
    n_s29 --> n_s30
    n_s30 -->|"yes"| n_s31
    n_s30 -->|"no"| n_s32
    n_s32 -->|"each"| n_s33
    n_s33 -.->|"next"| n_s32
    n_s28 -->|"no"| n_s34
    n_s34 -->|"yes"| n_s35
    n_s35 --> n_s36
    n_s36 -.->|"each"| n_s36
    n_s34 -->|"no"| n_s37
    n_s37 -->|"yes"| n_s38
    n_s38 --> n_s39
    n_s39 -.->|"each"| n_s39
    n_s37 -->|"no"| n_s40
    n_s40 -->|"yes"| n_s41
    n_s40 -->|"no"| n_s42
    n_s42 -->|"yes"| n_s43
    n_s8 --> n_s44
    n_s10 --> n_s44
    n_s12 --> n_s44
    n_s16 -->|"done"| n_s44
    n_s19 -->|"done"| n_s44
    n_s20 --> n_s44
    n_s22 --> n_s44
    n_s24 --> n_s44
    n_s27 -->|"done"| n_s44
    n_s32 -->|"done"| n_s44
    n_s36 -->|"done"| n_s44
    n_s39 -->|"done"| n_s44
    n_s41 --> n_s44
    n_s43 --> n_s44
    n_s42 -->|"no"| n_s44
    linkStyle 15,19,28,35,39,43 stroke:#f87171,stroke-width:2px;
```

Call tree:

```mermaid
flowchart LR
    classDef default fill:#111827,stroke:#38bdf8,color:#e5e7eb;
    classDef entry fill:#0e7490,stroke:#22d3ee,color:#ecfeff,stroke-width:2px;
    classDef external fill:#1a1530,stroke:#a78bfa,color:#ede9fe;
    n_deploynator___main___py__main["__main__.main<br/>__main__.py:164"]:::entry
    n_deploynator__config_py__create["_config.Config.create<br/>_config.py:79"]:::external
    n_deploynator__config_py__Config["_config.Config<br/>_config.py:8"]:::external
    n_deploynator__app_py__DeploynatorApp["_app.DeploynatorApp<br/>_app.py:20"]:::external
    n_deploynator__app_py__interactive_menu["_app.DeploynatorApp.interactive_menu<br/>_app.py:379"]:::external
    n_deploynator___main___py__preprocess_argv["__main__.preprocess_argv<br/>__main__.py:130"]:::default
    n_deploynator___main___py__build_parser["__main__.build_parser<br/>__main__.py:17"]:::default
    n_deploynator__models_py__valid_types["_models.CommitType.valid_types<br/>_models.py:65"]:::external
    n_deploynator__app_py__release["_app.DeploynatorApp.release<br/>_app.py:229"]:::external
    n_deploynator__models_py__from_string_58["_models.CommitType.from_string<br/>_models.py:58"]:::external
    n_deploynator__deploy_py__discover["_deploy.ProjectDiscovery.discover<br/>_deploy.py:35"]:::external
    n_deploynator__deploy_py___load_single["_deploy.ProjectDiscovery._load_single<br/>_deploy.py:63"]:::external
    n_deploynator__models_py__from_dict_139["_models.ProjectConfig.from_dict<br/>_models.py:139"]:::external
    n_deploynator__deploy_py__find_by_name["_deploy.ProjectDiscovery.find_by_name<br/>_deploy.py:56"]:::external
    n_deploynator__app_py___looks_like_path["_app.DeploynatorApp._looks_like_path<br/>_app.py:153"]:::external
    n_deploynator__toml_py__load_toml_config["_toml.load_toml_config<br/>_toml.py:46"]:::external
    n_deploynator__toml_py__TomlConfig["_toml.TomlConfig<br/>_toml.py:14"]:::external
    n_deploynator__toml_py___clamp_timeout["_toml._clamp_timeout<br/>_toml.py:38"]:::external
    n_deploynator__models_py__ProjectConfig["_models.ProjectConfig<br/>_models.py:130"]:::external
    n_deploynator__models_py__VersionConfig["_models.VersionConfig<br/>_models.py:115"]:::external
    n_deploynator__models_py__DeployResult["_models.DeployResult<br/>_models.py:276"]:::external
    n_deploynator__models_py__from_string["_models.Platform.from_string<br/>_models.py:16"]:::external
    n_deploynator__deploy_py__deploy["_deploy.DeployOrchestrator.deploy<br/>_deploy.py:97"]:::external
    n_deploynator__deploy_py___resolve_project_path["_deploy.DeployOrchestrator._resolve_project_path<br/>_deploy.py:88"]:::external
    n_deploynator__semver_py__get_current_version["_semver.SemverManager.get_current_version<br/>_semver.py:21"]:::external
    n_deploynator__models_py__parse_217["_models.VersionInfo.parse<br/>_models.py:217"]:::external
    n_deploynator__models_py__VersionInfo["_models.VersionInfo<br/>_models.py:208"]:::external
    n_deploynator__semver_py___get_latest_tag["_semver.SemverManager._get_latest_tag<br/>_semver.py:122"]:::external
    n_deploynator__semver_py__max_version["_semver.SemverManager.max_version<br/>_semver.py:16"]:::external
    n_deploynator__semver_py__determine_bump["_semver.SemverManager.determine_bump<br/>_semver.py:111"]:::external
    n_deploynator__models_py__bump_strategy["_models.CommitType.bump_strategy<br/>_models.py:68"]:::external
    n_deploynator__semver_py__calculate_next_version["_semver.SemverManager.calculate_next_version<br/>_semver.py:114"]:::external
    n_deploynator__models_py__bump["_models.VersionInfo.bump<br/>_models.py:228"]:::external
    n_deploynator__runner_py__run["_runner.TestRunner.run<br/>_runner.py:15"]:::external
    n_deploynator___main___py__main -->|"1"| n_deploynator__config_py__create
    n_deploynator__config_py__create -->|"1"| n_deploynator__config_py__Config
    n_deploynator___main___py__main -->|"2"| n_deploynator__app_py__DeploynatorApp
    n_deploynator___main___py__main -->|"3"| n_deploynator__app_py__interactive_menu
    n_deploynator___main___py__main -->|"4"| n_deploynator___main___py__preprocess_argv
    n_deploynator___main___py__preprocess_argv -->|"1"| n_deploynator___main___py__build_parser
    n_deploynator___main___py__build_parser -->|"1"| n_deploynator__models_py__valid_types
    n_deploynator___main___py__main -.-> n_deploynator___main___py__build_parser
    n_deploynator___main___py__main -->|"5"| n_deploynator__app_py__release
    n_deploynator__app_py__release -->|"1"| n_deploynator__models_py__from_string_58
    n_deploynator__app_py__release -->|"2"| n_deploynator__deploy_py__discover
    n_deploynator__deploy_py__discover -->|"1"| n_deploynator__deploy_py___load_single
    n_deploynator__deploy_py___load_single -.-> n_deploynator__config_py__create
    n_deploynator__deploy_py___load_single -->|"1"| n_deploynator__models_py__from_dict_139
    n_deploynator__app_py__release -->|"3"| n_deploynator__deploy_py__find_by_name
    n_deploynator__deploy_py__find_by_name -.-> n_deploynator__deploy_py__discover
    n_deploynator__app_py__release -->|"4"| n_deploynator__app_py___looks_like_path
    n_deploynator__app_py__release -->|"5"| n_deploynator__toml_py__load_toml_config
    n_deploynator__toml_py__load_toml_config -->|"1"| n_deploynator__toml_py__TomlConfig
    n_deploynator__toml_py__load_toml_config -.-> n_deploynator__config_py__create
    n_deploynator__toml_py__load_toml_config -->|"2"| n_deploynator__toml_py___clamp_timeout
    n_deploynator__app_py__release -->|"6"| n_deploynator__models_py__ProjectConfig
    n_deploynator__app_py__release -->|"7"| n_deploynator__models_py__VersionConfig
    n_deploynator__app_py__release -.-> n_deploynator__deploy_py___load_single
    n_deploynator__app_py__release -->|"8"| n_deploynator__models_py__DeployResult
    n_deploynator__app_py__release -->|"9"| n_deploynator__models_py__from_string
    n_deploynator__app_py__release -->|"10"| n_deploynator__deploy_py__deploy
    n_deploynator__deploy_py__deploy -->|"1"| n_deploynator__deploy_py___resolve_project_path
    n_deploynator__deploy_py__deploy -.-> n_deploynator__models_py__DeployResult
    n_deploynator__deploy_py__deploy -.-> n_deploynator__toml_py__load_toml_config
    n_deploynator__deploy_py__deploy -->|"2"| n_deploynator__semver_py__get_current_version
    n_deploynator__semver_py__get_current_version -->|"1"| n_deploynator__models_py__parse_217
    n_deploynator__semver_py__get_current_version -->|"2"| n_deploynator__models_py__VersionInfo
    n_deploynator__semver_py__get_current_version -->|"3"| n_deploynator__semver_py___get_latest_tag
    n_deploynator__semver_py__get_current_version -->|"4"| n_deploynator__semver_py__max_version
    n_deploynator__deploy_py__deploy -->|"3"| n_deploynator__semver_py__determine_bump
    n_deploynator__semver_py__determine_bump -->|"1"| n_deploynator__models_py__bump_strategy
    n_deploynator__deploy_py__deploy -->|"4"| n_deploynator__semver_py__calculate_next_version
    n_deploynator__semver_py__calculate_next_version -->|"1"| n_deploynator__models_py__bump
    n_deploynator__deploy_py__deploy -->|"5"| n_deploynator__runner_py__run
```

Cross-file sequence:

```mermaid
sequenceDiagram
    autonumber
    participant p_deploynator___main___py as __main__.py
    participant p_deploynator__config_py as _config.py
    participant p_deploynator__app_py as _app.py
    participant p_deploynator__models_py as _models.py
    participant p_deploynator__deploy_py as _deploy.py
    participant p_deploynator__toml_py as _toml.py
    participant p_deploynator__semver_py as _semver.py
    participant p_deploynator__runner_py as _runner.py
    p_deploynator___main___py->>p_deploynator__config_py: Config.create()
    p_deploynator___main___py->>p_deploynator__app_py: DeploynatorApp()
    p_deploynator___main___py->>p_deploynator__app_py: DeploynatorApp.interactive_menu()
    p_deploynator___main___py->>p_deploynator__models_py: CommitType.valid_types()
    p_deploynator___main___py->>p_deploynator__app_py: DeploynatorApp.release()
    p_deploynator__app_py->>p_deploynator__models_py: CommitType.from_string()
    p_deploynator__app_py->>p_deploynator__deploy_py: ProjectDiscovery.discover()
    p_deploynator__deploy_py->>p_deploynator__models_py: ProjectConfig.from_dict()
    p_deploynator__app_py->>p_deploynator__deploy_py: ProjectDiscovery.find_by_name()
    p_deploynator__app_py->>p_deploynator__toml_py: load_toml_config()
    p_deploynator__app_py->>p_deploynator__models_py: ProjectConfig()
    p_deploynator__app_py->>p_deploynator__models_py: VersionConfig()
    p_deploynator__app_py->>p_deploynator__models_py: DeployResult()
    p_deploynator__app_py->>p_deploynator__models_py: Platform.from_string()
    p_deploynator__app_py->>p_deploynator__deploy_py: DeployOrchestrator.deploy()
    p_deploynator__deploy_py->>p_deploynator__semver_py: SemverManager.get_current_version()
    p_deploynator__semver_py->>p_deploynator__models_py: VersionInfo.parse()
    p_deploynator__semver_py->>p_deploynator__models_py: VersionInfo()
    p_deploynator__deploy_py->>p_deploynator__semver_py: SemverManager.determine_bump()
    p_deploynator__semver_py->>p_deploynator__models_py: CommitType.bump_strategy()
    p_deploynator__deploy_py->>p_deploynator__semver_py: SemverManager.calculate_next_version()
    p_deploynator__semver_py->>p_deploynator__models_py: VersionInfo.bump()
    p_deploynator__deploy_py->>p_deploynator__runner_py: TestRunner.run()
```

### `_mcp_server (__main__)`

`deploynator/_mcp_server.py:277`, score 8: `if __name__ == "__main__"` guard.

Call tree:

```mermaid
flowchart LR
    classDef default fill:#111827,stroke:#38bdf8,color:#e5e7eb;
    classDef entry fill:#0e7490,stroke:#22d3ee,color:#ecfeff,stroke-width:2px;
    classDef external fill:#1a1530,stroke:#a78bfa,color:#ede9fe;
    n_deploynator__mcp_server_py___main_["_mcp_server (__main__)<br/>_mcp_server.py"]:::entry
    n_deploynator__mcp_server_py__main["_mcp_server.main<br/>_mcp_server.py:269"]:::default
    n_deploynator__app_py__DeploynatorApp["_app.DeploynatorApp<br/>_app.py:20"]:::external
    n_deploynator__config_py__create["_config.Config.create<br/>_config.py:79"]:::external
    n_deploynator__config_py__Config["_config.Config<br/>_config.py:8"]:::external
    n_deploynator__mcp_server_py__MCPServer["_mcp_server.MCPServer<br/>_mcp_server.py:86"]:::default
    n_deploynator__mcp_server_py__run["_mcp_server.MCPServer.run<br/>_mcp_server.py:162"]:::default
    n_deploynator__mcp_server_py___register_all["_mcp_server.MCPServer._register_all<br/>_mcp_server.py:180"]:::default
    n_deploynator__mcp_server_py__MCPTool["_mcp_server.MCPTool<br/>_mcp_server.py:56"]:::default
    n_deploynator__mcp_server_py__register_tool["_mcp_server.MCPServer.register_tool<br/>_mcp_server.py:94"]:::default
    n_deploynator__mcp_server_py__MCPResource["_mcp_server.MCPResource<br/>_mcp_server.py:71"]:::default
    n_deploynator__mcp_server_py__register_resource["_mcp_server.MCPServer.register_resource<br/>_mcp_server.py:97"]:::default
    n_deploynator__mcp_server_py__MCPRequest["_mcp_server.MCPRequest<br/>_mcp_server.py:35"]:::default
    n_deploynator__mcp_server_py__dispatch["_mcp_server.MCPServer.dispatch<br/>_mcp_server.py:144"]:::default
    n_deploynator__mcp_server_py___handle_initialize["_mcp_server.MCPServer._handle_initialize<br/>_mcp_server.py:100"]:::default
    n_deploynator__mcp_server_py__error["_mcp_server.MCPRequest.error<br/>_mcp_server.py:49"]:::default
    n_deploynator__mcp_server_py___main_ -->|"1"| n_deploynator__mcp_server_py__main
    n_deploynator__mcp_server_py__main -->|"1"| n_deploynator__app_py__DeploynatorApp
    n_deploynator__mcp_server_py__main -->|"2"| n_deploynator__config_py__create
    n_deploynator__config_py__create -->|"1"| n_deploynator__config_py__Config
    n_deploynator__mcp_server_py__main -->|"3"| n_deploynator__mcp_server_py__MCPServer
    n_deploynator__mcp_server_py__main -->|"4"| n_deploynator__mcp_server_py__run
    n_deploynator__mcp_server_py__run -->|"1"| n_deploynator__mcp_server_py___register_all
    n_deploynator__mcp_server_py___register_all -->|"1"| n_deploynator__mcp_server_py__MCPTool
    n_deploynator__mcp_server_py___register_all -->|"2"| n_deploynator__mcp_server_py__register_tool
    n_deploynator__mcp_server_py___register_all -->|"3"| n_deploynator__mcp_server_py__MCPResource
    n_deploynator__mcp_server_py___register_all -->|"4"| n_deploynator__mcp_server_py__register_resource
    n_deploynator__mcp_server_py__run -->|"2"| n_deploynator__mcp_server_py__MCPRequest
    n_deploynator__mcp_server_py__run -->|"3"| n_deploynator__mcp_server_py__dispatch
    n_deploynator__mcp_server_py__dispatch -->|"1"| n_deploynator__mcp_server_py___handle_initialize
    n_deploynator__mcp_server_py__dispatch -->|"2"| n_deploynator__mcp_server_py__error
```

Cross-file sequence:

```mermaid
sequenceDiagram
    autonumber
    participant p_deploynator__mcp_server_py as _mcp_server.py
    participant p_deploynator__app_py as _app.py
    participant p_deploynator__config_py as _config.py
    p_deploynator__mcp_server_py->>p_deploynator__app_py: DeploynatorApp()
    p_deploynator__mcp_server_py->>p_deploynator__config_py: Config.create()
```

### `_pypi.PyPIRunner.run`

`deploynator/_pypi.py:107`, score 3: entry-style name `run`.

Control flow:

```mermaid
flowchart TB
    classDef decision fill:#1e1b4b,stroke:#a78bfa,color:#ede9fe;
    classDef default fill:#111827,stroke:#38bdf8,color:#e5e7eb;
    classDef entry fill:#0e7490,stroke:#22d3ee,color:#ecfeff,stroke-width:2px;
    n_s1(["start _pypi.PyPIRunner.run"]):::entry
    n_s2{"not self.is_packaging_project(project_path)?"}:::decision
    n_s3(["return"]):::entry
    n_s4[/"try"/]:::default
    n_s5["clean()"]:::default
    n_s6(["return"]):::entry
    n_s7["run()"]:::default
    n_s8{"build.returncode != 0?"}:::decision
    n_s9(["return"]):::entry
    n_s10{"not artifacts?"}:::decision
    n_s11(["return"]):::entry
    n_s12{"toml.pypi_repo == 'testpypi'?"}:::decision
    n_s13{"toml.pypi_repo not in ('pypi', 'testpypi')?"}:::decision
    n_s14{"token and (not os.environ.get('TWINE_PASSWORD'))?"}:::decision
    n_s15[/"try"/]:::default
    n_s16["run()"]:::default
    n_s17(["return"]):::entry
    n_s18{"upload.returncode != 0?"}:::decision
    n_s19(["return"]):::entry
    n_s20(["return"]):::entry
    n_s1 --> n_s2
    n_s2 -->|"yes"| n_s3
    n_s2 -->|"no"| n_s4
    n_s4 --> n_s5
    n_s4 -->|"except (ValueError, OSError)"| n_s6
    n_s5 --> n_s7
    n_s7 --> n_s8
    n_s8 -->|"yes"| n_s9
    n_s8 -->|"no"| n_s10
    n_s10 -->|"yes"| n_s11
    n_s10 -->|"no"| n_s12
    n_s12 -->|"no"| n_s13
    n_s12 -->|"yes"| n_s14
    n_s13 -->|"yes"| n_s14
    n_s13 -->|"no"| n_s14
    n_s14 -->|"yes"| n_s15
    n_s14 -->|"no"| n_s15
    n_s15 --> n_s16
    n_s15 -->|"except subprocess.TimeoutExpired"| n_s17
    n_s16 --> n_s18
    n_s18 -->|"yes"| n_s19
    n_s18 -->|"no"| n_s20
```

Call tree:

```mermaid
flowchart LR
    classDef default fill:#111827,stroke:#38bdf8,color:#e5e7eb;
    classDef entry fill:#0e7490,stroke:#22d3ee,color:#ecfeff,stroke-width:2px;
    n_deploynator__pypi_py__run["_pypi.PyPIRunner.run<br/>_pypi.py:107"]:::entry
    n_deploynator__pypi_py__is_packaging_project["_pypi.PyPIRunner.is_packaging_project<br/>_pypi.py:16"]:::default
    n_deploynator__pypi_py__clean["_pypi.PyPIRunner.clean<br/>_pypi.py:90"]:::default
    n_deploynator__pypi_py__run -->|"1"| n_deploynator__pypi_py__is_packaging_project
    n_deploynator__pypi_py__run -->|"2"| n_deploynator__pypi_py__clean
```

---
