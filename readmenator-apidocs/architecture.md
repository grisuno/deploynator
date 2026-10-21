# deploynator Architecture and Execution Flows

[Back to index](index.md)

## Architecture Overview

6 components stacked in 4 dependency tiers (weighted Eades-Lin-Smyth ordering: arrows point from dependent to dependency, top to bottom). Labels are import counts, thick arrows the top quartile; 3 transitively implied edges are omitted. Dashed red arrows are upward dependencies: the smallest set of imports that closes every cycle and breaks the layering. Cyan components hold entry points. Interactive version: `readmenator-apidocs/index.html#/flows`.

Upward dependencies to fix first: `deploynator: _changelog` -> `deploynator: _models` (1 imports)

```mermaid
flowchart TB
    classDef cycle fill:#1f1530,stroke:#f472b6,color:#fce7f3,stroke-width:2px;
    classDef default fill:#111827,stroke:#38bdf8,color:#e5e7eb;
    classDef entry fill:#0e7490,stroke:#22d3ee,color:#ecfeff,stroke-width:2px;
    subgraph lane_0["Tier 1 - entry / orchestration"]
        direction LR
        n_c1["deploynator: _mcp_server<br/>4 files, 36 symbols<br/>Core / utility"]:::entry
        n_d__root_["(root)<br/>2 files, 1 symbols<br/>Core / utility"]:::default
    end
    subgraph lane_1["Tier 2"]
        direction LR
        n_c2["deploynator: _receipt<br/>5 files, 160 symbols<br/>Core / utility"]:::default
    end
    subgraph lane_2["Tier 3"]
        direction LR
        n_c0["deploynator: _toml<br/>5 files, 33 symbols<br/>Core / utility"]:::default
        n_c3["deploynator: _models<br/>2 files, 36 symbols<br/>Business logic"]:::cycle
    end
    subgraph lane_3["Tier 4 - foundation"]
        direction LR
        n_c4["deploynator: _changelog<br/>3 files, 19 symbols<br/>Core / utility"]:::cycle
    end
    n_c0 -->|"5"| n_c4
    n_c1 -->|"1"| n_c2
    n_c2 ==>|"8"| n_c0
    n_c2 ==>|"8"| n_c3
    n_c3 -->|"1"| n_c4
    n_c3 <-.-|"1 upward"| n_c4
    linkStyle 5 stroke:#f87171,stroke-width:2px;
    n_c1 ~~~ n_c2
    n_c2 ~~~ n_c0
    n_c0 ~~~ n_c4
```

---

## Execution Flows

Entry points are scored from `__main__` guards, `main` functions, entry-style names and files, and call-graph sources. Each flow walks resolved calls in call-site order (depth <= 4, <= 40 steps); numbers give the call order, dashed arrows revisit an already expanded callee, red arrows are recursion. Interactive version with zoom and per-node docs: `readmenator-apidocs/index.html#/flows`.

### `app.main`

`app.py:12`, score 9: entry-style name `main`; defined in entry file `app.py`; called from the `__main__` guard.

Control flow:

```mermaid
flowchart TB
    classDef decision fill:#1e1b4b,stroke:#a78bfa,color:#ede9fe;
    classDef default fill:#111827,stroke:#38bdf8,color:#e5e7eb;
    classDef entry fill:#0e7490,stroke:#22d3ee,color:#ecfeff,stroke-width:2px;
    n_s1(["start app.main"]):::entry
    n_s2["DeploynatorApp(), create()"]:::default
    n_s3{{"for p in app.list_projects()"}}:::decision
    n_s4{{"for (key, value) in app.status().items()"}}:::decision
    n_s5{{"for result in app.release(commit_type='patch', subject='e..."}}:::decision
    n_s6(["end"]):::entry
    n_s1 --> n_s2
    n_s2 --> n_s3
    n_s3 -.->|"each"| n_s3
    n_s3 -->|"done"| n_s4
    n_s4 -.->|"each"| n_s4
    n_s4 -->|"done"| n_s5
    n_s5 -.->|"each"| n_s5
    n_s5 -->|"done"| n_s6
    linkStyle 2,4,6 stroke:#f87171,stroke-width:2px;
```

Call tree:

```mermaid
flowchart LR
    classDef entry fill:#0e7490,stroke:#22d3ee,color:#ecfeff,stroke-width:2px;
    classDef external fill:#1a1530,stroke:#a78bfa,color:#ede9fe;
    n_app_py__main["app.main<br/>app.py:12"]:::entry
    n_deploynator__app_py__DeploynatorApp["_app.DeploynatorApp<br/>_app.py:18"]:::external
    n_deploynator__config_py__create["_config.Config.create<br/>_config.py:83"]:::external
    n_deploynator__config_py__Config["_config.Config<br/>_config.py:8"]:::external
    n_deploynator__app_py__list_projects["_app.DeploynatorApp.list_projects<br/>_app.py:545"]:::external
    n_deploynator__deploy_py__discover["_deploy.ProjectDiscovery.discover<br/>_deploy.py:42"]:::external
    n_deploynator__deploy_py___load_single["_deploy.ProjectDiscovery._load_single<br/>_deploy.py:70"]:::external
    n_deploynator__models_py__from_dict_138["_models.ProjectConfig.from_dict<br/>_models.py:138"]:::external
    n_deploynator__app_py__status["_app.DeploynatorApp.status<br/>_app.py:525"]:::external
    n_deploynator__git_py__GitOperations["_git.GitOperations<br/>_git.py:9"]:::external
    n_deploynator__app_py___resolve_project_path["_app.DeploynatorApp._resolve_project_path<br/>_app.py:291"]:::external
    n_deploynator__deploy_py__find_by_name["_deploy.ProjectDiscovery.find_by_name<br/>_deploy.py:63"]:::external
    n_deploynator__deploy_py___resolve_project_path["_deploy.DeployOrchestrator._resolve_project_path<br/>_deploy.py:96"]:::external
    n_deploynator__app_py___looks_like_path["_app.DeploynatorApp._looks_like_path<br/>_app.py:284"]:::external
    n_deploynator__git_py__current_branch["_git.GitOperations.current_branch<br/>_git.py:243"]:::external
    n_deploynator__git_py__is_dirty["_git.GitOperations.is_dirty<br/>_git.py:255"]:::external
    n_deploynator__git_py__has_remote["_git.GitOperations.has_remote<br/>_git.py:265"]:::external
    n_deploynator__app_py__release["_app.DeploynatorApp.release<br/>_app.py:377"]:::external
    n_deploynator__models_py__from_string_57["_models.CommitType.from_string<br/>_models.py:57"]:::external
    n_deploynator__toml_py__load_toml_config["_toml.load_toml_config<br/>_toml.py:217"]:::external
    n_deploynator__toml_py___auto_toml_config["_toml._auto_toml_config<br/>Config auto para proyectos sin deploynator.to...<br/>_toml.py:150"]:::external
    n_deploynator__toml_py__detect_test_commands["_toml.detect_test_commands<br/>Detecta comandos de test para proyectos C/aut...<br/>_toml.py:101"]:::external
    n_deploynator__toml_py___has_python_tests["_toml._has_python_tests<br/>_toml.py:63"]:::external
    n_deploynator__toml_py__TomlConfig["_toml.TomlConfig<br/>_toml.py:177"]:::external
    n_deploynator__toml_py__looks_like_packaging_project["_toml.looks_like_packaging_project<br/>Inferencia runtime (multi-proyecto): ¿es un p...<br/>_toml.py:75"]:::external
    n_deploynator__toml_py__list_make_targets["_toml.list_make_targets<br/>Lee el Makefile y devuelve sus targets sin ej...<br/>_toml.py:31"]:::external
    n_deploynator__toml_py___clamp_timeout["_toml._clamp_timeout<br/>_toml.py:209"]:::external
    n_deploynator__models_py__ProjectConfig["_models.ProjectConfig<br/>_models.py:129"]:::external
    n_deploynator__models_py__VersionConfig["_models.VersionConfig<br/>_models.py:114"]:::external
    n_deploynator__models_py__DeployResult["_models.DeployResult<br/>_models.py:276"]:::external
    n_app_py__main -->|"1"| n_deploynator__app_py__DeploynatorApp
    n_app_py__main -->|"2"| n_deploynator__config_py__create
    n_deploynator__config_py__create -->|"1"| n_deploynator__config_py__Config
    n_app_py__main -->|"3"| n_deploynator__app_py__list_projects
    n_deploynator__app_py__list_projects -->|"1"| n_deploynator__deploy_py__discover
    n_deploynator__deploy_py__discover -->|"1"| n_deploynator__deploy_py___load_single
    n_deploynator__deploy_py___load_single -.-> n_deploynator__config_py__create
    n_deploynator__deploy_py___load_single -->|"1"| n_deploynator__models_py__from_dict_138
    n_app_py__main -->|"4"| n_deploynator__app_py__status
    n_deploynator__app_py__status -->|"1"| n_deploynator__git_py__GitOperations
    n_deploynator__app_py__status -->|"2"| n_deploynator__app_py___resolve_project_path
    n_deploynator__app_py___resolve_project_path -->|"1"| n_deploynator__deploy_py__find_by_name
    n_deploynator__deploy_py__find_by_name -.-> n_deploynator__deploy_py__discover
    n_deploynator__app_py___resolve_project_path -->|"2"| n_deploynator__deploy_py___resolve_project_path
    n_deploynator__app_py___resolve_project_path -->|"3"| n_deploynator__app_py___looks_like_path
    n_deploynator__app_py__status -->|"3"| n_deploynator__git_py__current_branch
    n_deploynator__app_py__status -->|"4"| n_deploynator__git_py__is_dirty
    n_deploynator__app_py__status -->|"5"| n_deploynator__git_py__has_remote
    n_deploynator__app_py__status -.-> n_deploynator__deploy_py__discover
    n_app_py__main -->|"5"| n_deploynator__app_py__release
    n_deploynator__app_py__release -->|"1"| n_deploynator__models_py__from_string_57
    n_deploynator__app_py__release -.-> n_deploynator__deploy_py__discover
    n_deploynator__app_py__release -.-> n_deploynator__deploy_py__find_by_name
    n_deploynator__app_py__release -.-> n_deploynator__app_py___looks_like_path
    n_deploynator__app_py__release -->|"2"| n_deploynator__toml_py__load_toml_config
    n_deploynator__toml_py__load_toml_config -->|"1"| n_deploynator__toml_py___auto_toml_config
    n_deploynator__toml_py___auto_toml_config -->|"1"| n_deploynator__toml_py__detect_test_commands
    n_deploynator__toml_py___auto_toml_config -->|"2"| n_deploynator__toml_py___has_python_tests
    n_deploynator__toml_py___auto_toml_config -->|"3"| n_deploynator__toml_py__TomlConfig
    n_deploynator__toml_py___auto_toml_config -->|"4"| n_deploynator__toml_py__looks_like_packaging_project
    n_deploynator__toml_py__load_toml_config -->|"2"| n_deploynator__toml_py__TomlConfig
    n_deploynator__toml_py__load_toml_config -.-> n_deploynator__config_py__create
    n_deploynator__toml_py__load_toml_config -->|"3"| n_deploynator__toml_py__detect_test_commands
    n_deploynator__toml_py__detect_test_commands -->|"1"| n_deploynator__toml_py__list_make_targets
    n_deploynator__toml_py__load_toml_config -->|"4"| n_deploynator__toml_py___has_python_tests
    n_deploynator__toml_py__load_toml_config -->|"5"| n_deploynator__toml_py___clamp_timeout
    n_deploynator__app_py__release -->|"3"| n_deploynator__models_py__ProjectConfig
    n_deploynator__app_py__release -->|"4"| n_deploynator__models_py__VersionConfig
    n_deploynator__app_py__release -.-> n_deploynator__deploy_py___load_single
    n_deploynator__app_py__release -->|"5"| n_deploynator__models_py__DeployResult
```

Cross-file sequence:

```mermaid
sequenceDiagram
    autonumber
    participant p_app_py as app.py
    participant p_deploynator__app_py as _app.py
    participant p_deploynator__config_py as _config.py
    participant p_deploynator__deploy_py as _deploy.py
    participant p_deploynator__models_py as _models.py
    participant p_deploynator__git_py as _git.py
    participant p_deploynator__toml_py as _toml.py
    p_app_py->>p_deploynator__app_py: DeploynatorApp()
    p_app_py->>p_deploynator__config_py: Config.create()
    p_app_py->>p_deploynator__app_py: DeploynatorApp.list_projects()
    p_deploynator__app_py->>p_deploynator__deploy_py: ProjectDiscovery.discover()
    p_deploynator__deploy_py->>p_deploynator__models_py: ProjectConfig.from_dict()
    p_app_py->>p_deploynator__app_py: DeploynatorApp.status()
    p_deploynator__app_py->>p_deploynator__git_py: GitOperations()
    p_deploynator__app_py->>p_deploynator__deploy_py: ProjectDiscovery.find_by_name()
    p_deploynator__app_py->>p_deploynator__deploy_py: DeployOrchestrator._resolve_project_path()
    p_deploynator__app_py->>p_deploynator__git_py: GitOperations.current_branch()
    p_deploynator__app_py->>p_deploynator__git_py: GitOperations.is_dirty()
    p_deploynator__app_py->>p_deploynator__git_py: GitOperations.has_remote()
    p_app_py->>p_deploynator__app_py: DeploynatorApp.release()
    p_deploynator__app_py->>p_deploynator__models_py: CommitType.from_string()
    p_deploynator__app_py->>p_deploynator__toml_py: load_toml_config()
    p_deploynator__app_py->>p_deploynator__models_py: ProjectConfig()
    p_deploynator__app_py->>p_deploynator__models_py: VersionConfig()
    p_deploynator__app_py->>p_deploynator__models_py: DeployResult()
```

### `__main__.main`

`deploynator/__main__.py:185`, score 9: entry-style name `main`; defined in entry file `__main__.py`; called from the `__main__` guard.

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
    n_s38{"project?"}:::decision
    n_s39["install_deps()"]:::default
    n_s40{{"for (p, ok) in deps.items()"}}:::decision
    n_s41["install_packages()<br/>pip install/upgrade packages (default: deploy..."]:::default
    n_s42{"not all(results.values())?"}:::decision
    n_s43{"args.command == 'interactive'?"}:::decision
    n_s44["interactive_menu()"]:::default
    n_s45{"args.command == 'serve'?"}:::decision
    n_s46["run(), MCPServer()"]:::default
    n_s47(["end"]):::entry
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
    n_s38 -->|"yes"| n_s39
    n_s39 --> n_s40
    n_s40 -.->|"each"| n_s40
    n_s38 -->|"no"| n_s41
    n_s41 --> n_s42
    n_s37 -->|"no"| n_s43
    n_s43 -->|"yes"| n_s44
    n_s43 -->|"no"| n_s45
    n_s45 -->|"yes"| n_s46
    n_s8 --> n_s47
    n_s10 --> n_s47
    n_s12 --> n_s47
    n_s16 -->|"done"| n_s47
    n_s19 -->|"done"| n_s47
    n_s20 --> n_s47
    n_s22 --> n_s47
    n_s24 --> n_s47
    n_s27 -->|"done"| n_s47
    n_s32 -->|"done"| n_s47
    n_s36 -->|"done"| n_s47
    n_s40 -->|"done"| n_s47
    n_s42 -->|"yes"| n_s47
    n_s42 -->|"no"| n_s47
    n_s44 --> n_s47
    n_s46 --> n_s47
    n_s45 -->|"no"| n_s47
    linkStyle 15,19,28,35,39,44 stroke:#f87171,stroke-width:2px;
```

Call tree:

```mermaid
flowchart LR
    classDef default fill:#111827,stroke:#38bdf8,color:#e5e7eb;
    classDef entry fill:#0e7490,stroke:#22d3ee,color:#ecfeff,stroke-width:2px;
    classDef external fill:#1a1530,stroke:#a78bfa,color:#ede9fe;
    n_deploynator___main___py__main["__main__.main<br/>__main__.py:185"]:::entry
    n_deploynator__config_py__create["_config.Config.create<br/>_config.py:83"]:::external
    n_deploynator__config_py__Config["_config.Config<br/>_config.py:8"]:::external
    n_deploynator__app_py__DeploynatorApp["_app.DeploynatorApp<br/>_app.py:18"]:::external
    n_deploynator__app_py__interactive_menu["_app.DeploynatorApp.interactive_menu<br/>_app.py:604"]:::external
    n_deploynator___main___py__preprocess_argv["__main__.preprocess_argv<br/>__main__.py:151"]:::default
    n_deploynator___main___py__build_parser["__main__.build_parser<br/>__main__.py:16"]:::default
    n_deploynator__models_py__valid_types["_models.CommitType.valid_types<br/>_models.py:64"]:::external
    n_deploynator__app_py__release["_app.DeploynatorApp.release<br/>_app.py:377"]:::external
    n_deploynator__models_py__from_string_57["_models.CommitType.from_string<br/>_models.py:57"]:::external
    n_deploynator__deploy_py__discover["_deploy.ProjectDiscovery.discover<br/>_deploy.py:42"]:::external
    n_deploynator__deploy_py___load_single["_deploy.ProjectDiscovery._load_single<br/>_deploy.py:70"]:::external
    n_deploynator__models_py__from_dict_138["_models.ProjectConfig.from_dict<br/>_models.py:138"]:::external
    n_deploynator__deploy_py__find_by_name["_deploy.ProjectDiscovery.find_by_name<br/>_deploy.py:63"]:::external
    n_deploynator__app_py___looks_like_path["_app.DeploynatorApp._looks_like_path<br/>_app.py:284"]:::external
    n_deploynator__toml_py__load_toml_config["_toml.load_toml_config<br/>_toml.py:217"]:::external
    n_deploynator__toml_py___auto_toml_config["_toml._auto_toml_config<br/>Config auto para proyectos sin deploynator.to...<br/>_toml.py:150"]:::external
    n_deploynator__toml_py__detect_test_commands["_toml.detect_test_commands<br/>Detecta comandos de test para proyectos C/aut...<br/>_toml.py:101"]:::external
    n_deploynator__toml_py___has_python_tests["_toml._has_python_tests<br/>_toml.py:63"]:::external
    n_deploynator__toml_py__TomlConfig["_toml.TomlConfig<br/>_toml.py:177"]:::external
    n_deploynator__toml_py__looks_like_packaging_project["_toml.looks_like_packaging_project<br/>Inferencia runtime (multi-proyecto): ¿es un p...<br/>_toml.py:75"]:::external
    n_deploynator__toml_py__list_make_targets["_toml.list_make_targets<br/>Lee el Makefile y devuelve sus targets sin ej...<br/>_toml.py:31"]:::external
    n_deploynator__toml_py___clamp_timeout["_toml._clamp_timeout<br/>_toml.py:209"]:::external
    n_deploynator__models_py__ProjectConfig["_models.ProjectConfig<br/>_models.py:129"]:::external
    n_deploynator__models_py__VersionConfig["_models.VersionConfig<br/>_models.py:114"]:::external
    n_deploynator__models_py__DeployResult["_models.DeployResult<br/>_models.py:276"]:::external
    n_deploynator__models_py__from_string["_models.Platform.from_string<br/>_models.py:15"]:::external
    n_deploynator__app_py___parse_release_message["_app.DeploynatorApp._parse_release_message<br/>Parsea #96;test(module): texto#96; o #96;test(module)...<br/>_app.py:359"]:::external
    n_deploynator__deploy_py__deploy["_deploy.DeployOrchestrator.deploy<br/>_deploy.py:113"]:::external
    n_deploynator__receipt_py__ReceiptCollector["_receipt.ReceiptCollector<br/>Collects steps, subprocess calls and evidence...<br/>_receipt.py:263"]:::external
    n_deploynator__receipt_py__capture["_receipt.ReceiptCollector.capture<br/>_receipt.py:380"]:::external
    n_deploynator__deploy_py___deploy_impl["_deploy.DeployOrchestrator._deploy_impl<br/>_deploy.py:180"]:::external
    n_deploynator___main___py__main -->|"1"| n_deploynator__config_py__create
    n_deploynator__config_py__create -->|"1"| n_deploynator__config_py__Config
    n_deploynator___main___py__main -->|"2"| n_deploynator__app_py__DeploynatorApp
    n_deploynator___main___py__main -->|"3"| n_deploynator__app_py__interactive_menu
    n_deploynator___main___py__main -->|"4"| n_deploynator___main___py__preprocess_argv
    n_deploynator___main___py__preprocess_argv -->|"1"| n_deploynator___main___py__build_parser
    n_deploynator___main___py__build_parser -->|"1"| n_deploynator__models_py__valid_types
    n_deploynator___main___py__main -.-> n_deploynator___main___py__build_parser
    n_deploynator___main___py__main -->|"5"| n_deploynator__app_py__release
    n_deploynator__app_py__release -->|"1"| n_deploynator__models_py__from_string_57
    n_deploynator__app_py__release -->|"2"| n_deploynator__deploy_py__discover
    n_deploynator__deploy_py__discover -->|"1"| n_deploynator__deploy_py___load_single
    n_deploynator__deploy_py___load_single -.-> n_deploynator__config_py__create
    n_deploynator__deploy_py___load_single -->|"1"| n_deploynator__models_py__from_dict_138
    n_deploynator__app_py__release -->|"3"| n_deploynator__deploy_py__find_by_name
    n_deploynator__deploy_py__find_by_name -.-> n_deploynator__deploy_py__discover
    n_deploynator__app_py__release -->|"4"| n_deploynator__app_py___looks_like_path
    n_deploynator__app_py__release -->|"5"| n_deploynator__toml_py__load_toml_config
    n_deploynator__toml_py__load_toml_config -->|"1"| n_deploynator__toml_py___auto_toml_config
    n_deploynator__toml_py___auto_toml_config -->|"1"| n_deploynator__toml_py__detect_test_commands
    n_deploynator__toml_py___auto_toml_config -->|"2"| n_deploynator__toml_py___has_python_tests
    n_deploynator__toml_py___auto_toml_config -->|"3"| n_deploynator__toml_py__TomlConfig
    n_deploynator__toml_py___auto_toml_config -->|"4"| n_deploynator__toml_py__looks_like_packaging_project
    n_deploynator__toml_py__load_toml_config -->|"2"| n_deploynator__toml_py__TomlConfig
    n_deploynator__toml_py__load_toml_config -.-> n_deploynator__config_py__create
    n_deploynator__toml_py__load_toml_config -->|"3"| n_deploynator__toml_py__detect_test_commands
    n_deploynator__toml_py__detect_test_commands -->|"1"| n_deploynator__toml_py__list_make_targets
    n_deploynator__toml_py__load_toml_config -->|"4"| n_deploynator__toml_py___has_python_tests
    n_deploynator__toml_py__load_toml_config -->|"5"| n_deploynator__toml_py___clamp_timeout
    n_deploynator__app_py__release -->|"6"| n_deploynator__models_py__ProjectConfig
    n_deploynator__app_py__release -->|"7"| n_deploynator__models_py__VersionConfig
    n_deploynator__app_py__release -.-> n_deploynator__deploy_py___load_single
    n_deploynator__app_py__release -->|"8"| n_deploynator__models_py__DeployResult
    n_deploynator__app_py__release -->|"9"| n_deploynator__models_py__from_string
    n_deploynator__app_py__release -->|"10"| n_deploynator__app_py___parse_release_message
    n_deploynator__app_py__release -->|"11"| n_deploynator__deploy_py__deploy
    n_deploynator__deploy_py__deploy -->|"1"| n_deploynator__receipt_py__ReceiptCollector
    n_deploynator__deploy_py__deploy -->|"2"| n_deploynator__receipt_py__capture
    n_deploynator__deploy_py__deploy -->|"3"| n_deploynator__deploy_py___deploy_impl
    n_deploynator__deploy_py___deploy_impl -.-> n_deploynator__receipt_py__ReceiptCollector
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
    participant p_deploynator__receipt_py as _receipt.py
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
    p_deploynator__deploy_py->>p_deploynator__receipt_py: ReceiptCollector()
    p_deploynator__deploy_py->>p_deploynator__receipt_py: ReceiptCollector.capture()
```

### `_mcp_server (__main__)`

`deploynator/_mcp_server.py:285`, score 8: `if __name__ == "__main__"` guard.

Call tree:

```mermaid
flowchart LR
    classDef default fill:#111827,stroke:#38bdf8,color:#e5e7eb;
    classDef entry fill:#0e7490,stroke:#22d3ee,color:#ecfeff,stroke-width:2px;
    classDef external fill:#1a1530,stroke:#a78bfa,color:#ede9fe;
    n_deploynator__mcp_server_py___main_["_mcp_server (__main__)<br/>_mcp_server.py"]:::entry
    n_deploynator__mcp_server_py__main["_mcp_server.main<br/>_mcp_server.py:277"]:::default
    n_deploynator__app_py__DeploynatorApp["_app.DeploynatorApp<br/>_app.py:18"]:::external
    n_deploynator__config_py__create["_config.Config.create<br/>_config.py:83"]:::external
    n_deploynator__config_py__Config["_config.Config<br/>_config.py:8"]:::external
    n_deploynator__mcp_server_py__MCPServer["_mcp_server.MCPServer<br/>_mcp_server.py:87"]:::default
    n_deploynator__mcp_server_py__run["_mcp_server.MCPServer.run<br/>_mcp_server.py:163"]:::default
    n_deploynator__mcp_server_py___register_all["_mcp_server.MCPServer._register_all<br/>_mcp_server.py:181"]:::default
    n_deploynator__mcp_server_py__MCPTool["_mcp_server.MCPTool<br/>_mcp_server.py:57"]:::default
    n_deploynator__mcp_server_py__register_tool["_mcp_server.MCPServer.register_tool<br/>_mcp_server.py:95"]:::default
    n_deploynator__mcp_server_py__MCPResource["_mcp_server.MCPResource<br/>_mcp_server.py:72"]:::default
    n_deploynator__mcp_server_py__register_resource["_mcp_server.MCPServer.register_resource<br/>_mcp_server.py:98"]:::default
    n_deploynator__mcp_server_py__MCPRequest["_mcp_server.MCPRequest<br/>_mcp_server.py:36"]:::default
    n_deploynator__mcp_server_py__dispatch["_mcp_server.MCPServer.dispatch<br/>_mcp_server.py:145"]:::default
    n_deploynator__mcp_server_py___handle_initialize["_mcp_server.MCPServer._handle_initialize<br/>_mcp_server.py:101"]:::default
    n_deploynator__mcp_server_py__error["_mcp_server.MCPRequest.error<br/>_mcp_server.py:50"]:::default
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

---
