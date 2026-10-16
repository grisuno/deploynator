# Subsystem: tests

## tests/__init__.py
- Layer: testing
- Language: py

## tests/bdd_test_deploy.py
- Doc: BDD-style tests for deploynator using behavior-driven patterns.
- Layer: testing
- Language: py
- Symbols:
  - `TestBDDDeployScenarios` (class, line 28) `class TestBDDDeployScenarios`
  - `TestBDDPipeline` (class, line 84) `class TestBDDPipeline`
  - `project` (method, line 30) `def project(self)`
  - `test_version_bump_by_commit_type` (method, line 46) `def test_version_bump_by_commit_type(self, project, commit_type, expected_bump, initial, final)`
  - `test_conventional_commit_parsing` (method, line 55) `def test_conventional_commit_parsing(self)`
  - `test_commit_message_format_is_consistent` (method, line 69) `def test_commit_message_format_is_consistent(self)`
  - `test_tests_failure_blocks_release` (method, line 92) `def test_tests_failure_blocks_release(self)`
  - `test_docs_failure_does_not_block_release` (method, line 120) `def test_docs_failure_does_not_block_release(self)`
  - `test_force_bump_overrides_commit_type` (method, line 137) `def test_force_bump_overrides_commit_type(self)`
  - `test_version_is_max_file_tag` (method, line 144) `def test_version_is_max_file_tag(self)`
- Depends on: `deploynator/_config.py`, `deploynator/_deploy.py`, `deploynator/_docs.py`, `deploynator/_models.py`, `deploynator/_semver.py`, `deploynator/_toml.py`

## tests/test_changelog.py
- Layer: testing
- Language: py
- Symbols:
  - `TestChangelogGenerator` (class, line 7) `class TestChangelogGenerator`
  - `generator` (method, line 9) `def generator(self)`
  - `test_generate_header` (method, line 13) `def test_generate_header(self, generator)`
  - `test_generate_from_messages` (method, line 17) `def test_generate_from_messages(self, generator)`
  - `test_generate_from_messages_organizes_by_type` (method, line 32) `def test_generate_from_messages_organizes_by_type(self, generator)`
  - `test_generate_empty` (method, line 43) `def test_generate_empty(self, generator)`
  - `test_format_for_release_short` (method, line 47) `def test_format_for_release_short(self, generator)`
  - `test_format_for_release_truncated` (method, line 52) `def test_format_for_release_truncated(self, generator)`
- Depends on: `deploynator/_changelog.py`, `deploynator/_config.py`, `deploynator/_models.py`

## tests/test_cli_mcp.py
- Doc: RED: bare = interactive, flags = headless + MCP server.
- Layer: testing
- Language: py
- Symbols:
  - `TestCliMode` (class, line 5) `class TestCliMode`
  - `TestMCPServer` (class, line 36) `class TestMCPServer`
  - `test_bare_invokes_interactive` (method, line 6) `def test_bare_invokes_interactive(self, monkeypatch)`
  - `test_explicit_interactive_still_works` (method, line 16) `def test_explicit_interactive_still_works(self)`
  - `test_release_flags_headless` (method, line 21) `def test_release_flags_headless(self)`
  - `test_serve_command_exists` (method, line 30) `def test_serve_command_exists(self)`
  - `_server` (method, line 37) `def _server(self, tmp)`
  - `test_initialize_and_list` (method, line 44) `def test_initialize_and_list(self, tmp_path)`
  - `test_call_status_and_projects` (method, line 56) `def test_call_status_and_projects(self, tmp_path)`
  - `test_unknown_tool_errors` (method, line 72) `def test_unknown_tool_errors(self, tmp_path)`
  - `test_resources_list` (method, line 83) `def test_resources_list(self, tmp_path)`
- Depends on: `deploynator/__init__.py`, `deploynator/__main__.py`, `deploynator/_config.py`, `deploynator/_mcp_server.py`

## tests/test_config.py
- Layer: testing
- Language: py
- Symbols:
  - `TestConfigContract` (class, line 5) `class TestConfigContract`
  - `test_default_config_creation` (method, line 6) `def test_default_config_creation(self)`
  - `test_config_with_overrides` (method, line 13) `def test_config_with_overrides(self)`
  - `test_config_frozen` (method, line 19) `def test_config_frozen(self)`
  - `test_config_immutability` (method, line 24) `def test_config_immutability(self)`
  - `test_resolve_path` (method, line 30) `def test_resolve_path(self)`
  - `test_auth_checks` (method, line 34) `def test_auth_checks(self, monkeypatch)`
  - `test_conventional_types_contains_all` (method, line 40) `def test_conventional_types_contains_all(self)`
  - `test_semver_pattern_valid` (method, line 45) `def test_semver_pattern_valid(self)`
  - `test_commit_type_pattern_valid` (method, line 52) `def test_commit_type_pattern_valid(self)`
- Depends on: `deploynator/_config.py`

## tests/test_deploy.py
- Layer: testing
- Language: py
- Symbols:
  - `TestProjectDiscovery` (class, line 10) `class TestProjectDiscovery`
  - `TestDeployOrchestrator` (class, line 81) `class TestDeployOrchestrator`
  - `discovery` (method, line 12) `def discovery(self)`
  - `test_discover_empty_dir` (method, line 16) `def test_discover_empty_dir(self, discovery)`
  - `test_discover_single_yaml` (method, line 21) `def test_discover_single_yaml(self, discovery)`
  - `test_discover_multiple_yamls` (method, line 32) `def test_discover_multiple_yamls(self, discovery)`
  - `test_discover_ignores_non_yaml` (method, line 42) `def test_discover_ignores_non_yaml(self, discovery)`
  - `test_find_by_name` (method, line 53) `def test_find_by_name(self, discovery)`
  - `test_load_single_from_deploynator_yaml` (method, line 64) `def test_load_single_from_deploynator_yaml(self, discovery)`
  - `test_load_single_invalid` (method, line 72) `def test_load_single_invalid(self, discovery)`
  - `test_install_dependencies_file_not_found` (method, line 82) `def test_install_dependencies_file_not_found(self)`
- Depends on: `deploynator/_config.py`, `deploynator/_deploy.py`, `deploynator/_models.py`

## tests/test_init.py
- Doc: RED: init deja deploy.sh genérico + deploynator.toml starter.
- Layer: testing
- Language: py
- Symbols:
  - `TestInitScript` (class, line 7) `class TestInitScript`
  - `test_init_creates_files` (method, line 8) `def test_init_creates_files(self)`
  - `test_deploy_sh_executable_and_valid_bash` (method, line 19) `def test_deploy_sh_executable_and_valid_bash(self)`
  - `test_deploy_sh_content_generic` (method, line 30) `def test_deploy_sh_content_generic(self)`
  - `test_init_no_overwrite` (method, line 46) `def test_init_no_overwrite(self)`
  - `test_toml_starter_parseable` (method, line 58) `def test_toml_starter_parseable(self)`
- Depends on: `deploynator/__init__.py`, `deploynator/_config.py`, `deploynator/_toml.py`

## tests/test_install_example.py
- Doc: RED: install como pip install + app.py ejemplo de librería.
- Layer: testing
- Language: py
- Symbols:
  - `TestInstallPackages` (class, line 5) `class TestInstallPackages`
  - `TestAppExample` (class, line 54) `class TestAppExample`
  - `test_empty_is_noop` (method, line 6) `def test_empty_is_noop(self)`
  - `test_default_targets_deploynator` (method, line 11) `def test_default_targets_deploynator(self, monkeypatch)`
  - `test_failure_reported` (method, line 29) `def test_failure_reported(self, monkeypatch)`
  - `test_no_shell` (method, line 39) `def test_no_shell(self)`
  - `test_cli_install_parses_packages` (method, line 45) `def test_cli_install_parses_packages(self)`
  - `test_example_exists_and_compiles` (method, line 55) `def test_example_exists_and_compiles(self)`
  - `test_example_uses_library` (method, line 62) `def test_example_uses_library(self)`
  - `fake_run` (function, line 17) `def fake_run(cmd)`
  - `fake_run` (function, line 34) `def fake_run(cmd)`
  - `R` (class, line 19) `class R`
- Depends on: `deploynator/__init__.py`, `deploynator/__main__.py`, `deploynator/_config.py`

## tests/test_models.py
- Layer: testing
- Language: py
- Symbols:
  - `TestPlatformContract` (class, line 10) `class TestPlatformContract`
  - `TestCommitTypeContract` (class, line 34) `class TestCommitTypeContract`
  - `TestCommitMessageContract` (class, line 65) `class TestCommitMessageContract`
  - `TestVersionInfoContract` (class, line 107) `class TestVersionInfoContract`
  - `TestPlatformConfigContract` (class, line 145) `class TestPlatformConfigContract`
  - `TestProjectConfigContract` (class, line 160) `class TestProjectConfigContract`
  - `TestChangelogEntryContract` (class, line 196) `class TestChangelogEntryContract`
  - `TestReleaseInfoContract` (class, line 213) `class TestReleaseInfoContract`
  - `TestDeployResultContract` (class, line 230) `class TestDeployResultContract`
  - `test_platform_from_string` (method, line 11) `def test_platform_from_string(self)`
  - `test_platform_from_string_case` (method, line 16) `def test_platform_from_string_case(self)`
  - `test_platform_from_string_invalid` (method, line 20) `def test_platform_from_string_invalid(self)`
  - `test_platform_cli_name` (method, line 24) `def test_platform_cli_name(self)`
  - `test_platform_auth_env` (method, line 29) `def test_platform_auth_env(self)`
  - `test_commit_type_from_string` (method, line 35) `def test_commit_type_from_string(self)`
  - `test_commit_type_invalid` (method, line 40) `def test_commit_type_invalid(self)`
  - `test_commit_type_valid_types` (method, line 44) `def test_commit_type_valid_types(self)`
  - `test_bump_strategy` (method, line 51) `def test_bump_strategy(self)`
  - `test_section_header` (method, line 59) `def test_section_header(self)`
  - `test_format_basic` (method, line 66) `def test_format_basic(self)`
  - `test_format_with_version` (method, line 71) `def test_format_with_version(self)`
  - `test_format_with_body_and_footer` (method, line 80) `def test_format_with_body_and_footer(self)`
  - `test_parse_valid` (method, line 90) `def test_parse_valid(self)`
  - `test_parse_no_scope` (method, line 96) `def test_parse_no_scope(self)`
  - `test_parse_invalid` (method, line 102) `def test_parse_invalid(self)`
  - `test_parse` (method, line 108) `def test_parse(self)`
  - `test_str` (method, line 114) `def test_str(self)`
  - `test_bump_major` (method, line 118) `def test_bump_major(self)`
  - `test_bump_minor` (method, line 123) `def test_bump_minor(self)`
  - `test_bump_patch` (method, line 128) `def test_bump_patch(self)`
  - `test_bump_none` (method, line 133) `def test_bump_none(self)`
  - `test_parse_invalid` (method, line 138) `def test_parse_invalid(self)`
  - `test_from_dict_full` (method, line 146) `def test_from_dict_full(self)`
  - `test_from_dict_defaults` (method, line 153) `def test_from_dict_defaults(self)`
  - `test_from_dict_minimal` (method, line 161) `def test_from_dict_minimal(self)`
  - `test_from_dict_full` (method, line 169) `def test_from_dict_full(self)`
  - `test_from_dict_platform_string` (method, line 185) `def test_from_dict_platform_string(self)`
  - `test_from_git_log_line` (method, line 197) `def test_from_git_log_line(self)`
  - `test_from_git_log_line_unparseable` (method, line 204) `def test_from_git_log_line_unparseable(self)`
  - `test_from_git_log_line_scope` (method, line 208) `def test_from_git_log_line_scope(self)`
  - `test_defaults` (method, line 214) `def test_defaults(self)`
  - `test_custom` (method, line 220) `def test_custom(self)`
  - `test_defaults` (method, line 231) `def test_defaults(self)`
  - `test_with_data` (method, line 239) `def test_with_data(self)`
- Depends on: `deploynator/_models.py`

## tests/test_path_deploy.py
- Doc: Path-direct deploy + tag prefijos + version_file toml (ReadMenator real).
- Layer: testing
- Language: py
- Symbols:
  - `_git_init` (function, line 8) `def _git_init(tmp)`
  - `TestTagPrefixes` (class, line 18) `class TestTagPrefixes`
  - `TestTomlVersionFile` (class, line 38) `class TestTomlVersionFile`
  - `TestPathDirectRelease` (class, line 52) `class TestPathDirectRelease`
  - `test_release_v_prefix` (method, line 19) `def test_release_v_prefix(self)`
  - `test_v_prefix` (method, line 28) `def test_v_prefix(self)`
  - `test_write_pyproject_toml` (method, line 39) `def test_write_pyproject_toml(self)`
  - `test_release_by_path_dry_run` (method, line 53) `def test_release_by_path_dry_run(self)`
  - `test_no_platforms_pushes_to_origin` (method, line 64) `def test_no_platforms_pushes_to_origin(self)`
  - `test_name_wins_over_cwd_subdir` (method, line 95) `def test_name_wins_over_cwd_subdir(self)`
- Depends on: `deploynator/__init__.py`, `deploynator/_config.py`, `deploynator/_deploy.py`, `deploynator/_models.py`, `deploynator/_semver.py`

## tests/test_pipeline.py
- Doc: RED: pipeline deploy — tests gate + docs non-blocking + bump override + max(file,tag).
- Layer: testing
- Language: py
- Symbols:
  - `_git_init` (function, line 11) `def _git_init(tmp)`
  - `TestSemverMax` (class, line 21) `class TestSemverMax`
  - `TestDeployPipeline` (class, line 53) `class TestDeployPipeline`
  - `test_current_is_max_of_file_and_tag` (method, line 22) `def test_current_is_max_of_file_and_tag(self)`
  - `test_file_ahead_of_tag` (method, line 33) `def test_file_ahead_of_tag(self)`
  - `test_max_version_helper` (method, line 44) `def test_max_version_helper(self)`
  - `_project` (method, line 54) `def _project(self, path)`
  - `test_aborts_on_test_failure` (method, line 62) `def test_aborts_on_test_failure(self)`
  - `test_no_test_skips_failing_tests` (method, line 86) `def test_no_test_skips_failing_tests(self)`
  - `test_docs_failure_does_not_block` (method, line 103) `def test_docs_failure_does_not_block(self)`
  - `test_force_bump_overrides` (method, line 121) `def test_force_bump_overrides(self)`
  - `test_dry_run_prints_would` (method, line 144) `def test_dry_run_prints_would(self, capsys)`
- Depends on: `deploynator/_config.py`, `deploynator/_deploy.py`, `deploynator/_models.py`, `deploynator/_semver.py`

## tests/test_pypi.py
- Doc: RED: PyPI runner — detecta packaging, build limpio, upload twine.
- Layer: testing
- Language: py
- Symbols:
  - `_isolated_home` (function, line 10) `def _isolated_home(tmp_path, monkeypatch)`
  - `_git_init` (function, line 15) `def _git_init(tmp)`
  - `TestDetect` (class, line 25) `class TestDetect`
  - `TestPromptCredentials` (class, line 64) `class TestPromptCredentials`
  - `TestCleanAndRun` (class, line 181) `class TestCleanAndRun`
  - `TestPipelinePyPI` (class, line 223) `class TestPipelinePyPI`
  - `test_pyproject_with_project_table` (method, line 26) `def test_pyproject_with_project_table(self)`
  - `test_empty_dir_no_packaging` (method, line 34) `def test_empty_dir_no_packaging(self)`
  - `test_setup_py_counts` (method, line 40) `def test_setup_py_counts(self)`
  - `test_credentials_from_env` (method, line 48) `def test_credentials_from_env(self, monkeypatch)`
  - `test_no_shell_in_runner` (method, line 58) `def test_no_shell_in_runner(self)`
  - `test_no_tty_returns_none` (method, line 65) `def test_no_tty_returns_none(self, monkeypatch)`
  - `test_prompt_returns_token_without_save` (method, line 72) `def test_prompt_returns_token_without_save(self, monkeypatch)`
  - `test_prompt_empty_token_returns_none` (method, line 81) `def test_prompt_empty_token_returns_none(self, monkeypatch)`
  - `test_prompt_default_is_no_save` (method, line 89) `def test_prompt_default_is_no_save(self, monkeypatch)`
  - `test_prompt_yes_saves` (method, line 103) `def test_prompt_yes_saves(self, monkeypatch)`
  - `test_save_pypirc_roundtrip` (method, line 116) `def test_save_pypirc_roundtrip(self)`
  - `test_save_pypirc_rejects_symlink` (method, line 130) `def test_save_pypirc_rejects_symlink(self)`
  - `test_prompted_token_used_for_upload` (method, line 144) `def test_prompted_token_used_for_upload(self, monkeypatch)`
  - `_toml` (method, line 182) `def _toml(self)`
  - `test_clean_removes_dist` (method, line 191) `def test_clean_removes_dist(self)`
  - `test_run_fails_on_broken_build` (method, line 203) `def test_run_fails_on_broken_build(self, monkeypatch)`
  - `test_run_skips_without_packaging` (method, line 214) `def test_run_skips_without_packaging(self)`
  - `test_pypi_failure_aborts_with_error` (method, line 224) `def test_pypi_failure_aborts_with_error(self, monkeypatch)`
  - `test_no_credentials_skips_pypi` (method, line 256) `def test_no_credentials_skips_pypi(self, monkeypatch)`
- Depends on: `deploynator/_config.py`, `deploynator/_deploy.py`, `deploynator/_models.py`, `deploynator/_pypi.py`, `deploynator/_toml.py`

## tests/test_readme_footer.py
- Doc: Tests for the deploy README footer injector.
- Layer: testing
- Language: py
- Symbols:
  - `test_footer_line_is_english_without_emoji` (function, line 15) `def test_footer_line_is_english_without_emoji()`
  - `test_footer_block_is_anchored` (function, line 22) `def test_footer_block_is_anchored()`
  - `test_ensure_footer_appends_when_missing` (function, line 30) `def test_ensure_footer_appends_when_missing(tmp_path)`
  - `test_ensure_footer_is_idempotent` (function, line 40) `def test_ensure_footer_is_idempotent(tmp_path)`
  - `test_ensure_footer_wraps_plain_line` (function, line 48) `def test_ensure_footer_wraps_plain_line(tmp_path)`
  - `test_ensure_footer_missing_readme` (function, line 58) `def test_ensure_footer_missing_readme(tmp_path)`
- Depends on: `deploynator/_config.py`, `deploynator/_readme.py`

## tests/test_runner.py
- Doc: RED: TestRunner + DocsRunner contracts.
- Layer: testing
- Language: py
- Symbols:
  - `_toml` (function, line 7) `def _toml(commands, timeout)`
  - `TestTestRunner` (class, line 23) `class TestTestRunner`
  - `TestDocsRunner` (class, line 119) `class TestDocsRunner`
  - `test_passing_command` (method, line 24) `def test_passing_command(self)`
  - `test_failing_command` (method, line 32) `def test_failing_command(self)`
  - `test_multiple_commands_stop_on_first_failure` (method, line 41) `def test_multiple_commands_stop_on_first_failure(self)`
  - `test_empty_commands_no_tests_dir_fails` (method, line 49) `def test_empty_commands_no_tests_dir_fails(self)`
  - `test_empty_commands_allow_no_tests_passes` (method, line 58) `def test_empty_commands_allow_no_tests_passes(self)`
  - `test_no_shell_injection` (method, line 73) `def test_no_shell_injection(self)`
  - `test_timeout_fails` (method, line 87) `def test_timeout_fails(self)`
  - `test_empty_string_command_rejected` (method, line 96) `def test_empty_string_command_rejected(self)`
  - `test_make_target_runs` (method, line 104) `def test_make_target_runs(self)`
  - `test_passing_docs` (method, line 120) `def test_passing_docs(self)`
  - `test_failing_docs_returns_false` (method, line 127) `def test_failing_docs_returns_false(self)`
  - `test_auto_false_skips` (method, line 141) `def test_auto_false_skips(self)`
  - `test_no_shell_injection` (method, line 155) `def test_no_shell_injection(self)`
- Depends on: `deploynator/_config.py`, `deploynator/_docs.py`, `deploynator/_runner.py`, `deploynator/_toml.py`

## tests/test_semver.py
- Layer: testing
- Language: py
- Symbols:
  - `TestSemverManager` (class, line 10) `class TestSemverManager`
  - `manager` (method, line 12) `def manager(self)`
  - `test_get_current_version_from_file` (method, line 16) `def test_get_current_version_from_file(self, manager)`
  - `test_get_current_version_no_file` (method, line 24) `def test_get_current_version_no_file(self, manager)`
  - `test_write_version_file` (method, line 29) `def test_write_version_file(self, manager)`
  - `test_determine_bump` (method, line 37) `def test_determine_bump(self, manager)`
  - `test_calculate_next_version_major` (method, line 43) `def test_calculate_next_version_major(self, manager)`
  - `test_calculate_next_version_minor` (method, line 48) `def test_calculate_next_version_minor(self, manager)`
  - `test_calculate_next_version_patch` (method, line 53) `def test_calculate_next_version_patch(self, manager)`
  - `test_calculate_next_version_none` (method, line 58) `def test_calculate_next_version_none(self, manager)`
  - `test_is_valid_version` (method, line 72) `def test_is_valid_version(self, manager, ver_str, expected)`
- Depends on: `deploynator/_config.py`, `deploynator/_models.py`, `deploynator/_semver.py`

## tests/test_toml.py
- Doc: RED: TomlConfig contract — deploynator.toml per-project.
- Layer: testing
- Language: py
- Symbols:
  - `TestTomlConfig` (class, line 7) `class TestTomlConfig`
  - `TestCMakefileDetection` (class, line 84) `class TestCMakefileDetection`
  - `TestMultiTargetAndPyPIInference` (class, line 164) `class TestMultiTargetAndPyPIInference`
  - `test_load_missing_returns_defaults` (method, line 8) `def test_load_missing_returns_defaults(self)`
  - `test_load_valid_toml` (method, line 18) `def test_load_valid_toml(self)`
  - `test_symlink_rejected` (method, line 37) `def test_symlink_rejected(self)`
  - `test_oversize_rejected` (method, line 48) `def test_oversize_rejected(self)`
  - `test_malformed_toml_raises` (method, line 56) `def test_malformed_toml_raises(self)`
  - `test_timeout_clamped` (method, line 64) `def test_timeout_clamped(self)`
  - `test_frozen` (method, line 76) `def test_frozen(self)`
  - `_mk` (method, line 85) `def _mk(self, tmp, content)`
  - `test_list_targets_ignores_recipes` (method, line 89) `def test_list_targets_ignores_recipes(self)`
  - `test_detect_prefers_test_host` (method, line 98) `def test_detect_prefers_test_host(self)`
  - `test_detect_falls_back_to_test` (method, line 104) `def test_detect_falls_back_to_test(self)`
  - `test_detect_falls_back_to_check` (method, line 110) `def test_detect_falls_back_to_check(self)`
  - `test_detect_cmake` (method, line 116) `def test_detect_cmake(self)`
  - `test_load_missing_makefile_uses_make` (method, line 124) `def test_load_missing_makefile_uses_make(self)`
  - `test_python_with_aux_makefile_keeps_pytest` (method, line 133) `def test_python_with_aux_makefile_keeps_pytest(self)`
  - `test_test_host_wins_over_python_tests` (method, line 143) `def test_test_host_wins_over_python_tests(self)`
  - `test_makefile_symlink_rejected` (method, line 153) `def test_makefile_symlink_rejected(self)`
  - `_mk` (method, line 168) `def _mk(self, tmp, content)`
  - `test_detect_combines_test_targets` (method, line 172) `def test_detect_combines_test_targets(self)`
  - `test_detect_test_host_alone_wins` (method, line 179) `def test_detect_test_host_alone_wins(self)`
  - `test_detect_bare_tests_alone_kept` (method, line 186) `def test_detect_bare_tests_alone_kept(self)`
  - `test_auto_pypi_enabled_for_packaging` (method, line 192) `def test_auto_pypi_enabled_for_packaging(self)`
  - `test_auto_pypi_disabled_for_plain_c` (method, line 202) `def test_auto_pypi_disabled_for_plain_c(self)`
  - `test_looks_like_packaging_setup_py` (method, line 210) `def test_looks_like_packaging_setup_py(self)`
- Depends on: `deploynator/_toml.py`
