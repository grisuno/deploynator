import json
import os
import subprocess
import tempfile
from dataclasses import replace

import pytest

from deploynator._config import Config
from deploynator._deploy import DeployOrchestrator
from deploynator._models import CommitType, Platform, PlatformConfig, ProjectConfig
from deploynator._receipt import (
    KIND_CANDIDATE,
    KIND_OBSERVED,
    MODE_PLAN,
    MODE_RUN,
    STATUS_FAILED,
    STATUS_SUCCESS,
    CommandRecord,
    EdgeRecord,
    ReceiptCollector,
    ReleaseReceipt,
    StepRecord,
    build_plan,
    default_receipt_path,
    redact,
)


class TestRedact:
    def test_replaces_secret(self):
        assert "pass123" not in redact("token=pass123 ok", ["pass123"])
        assert "token=***REDACTED*** ok" == redact("token=pass123 ok", ["pass123"])

    def test_empty_text_unchanged(self):
        assert redact("", ["secret"]) == ""

    def test_no_match_unchanged(self):
        assert redact("plain", ["secret"]) == "plain"

    def test_collect_secret_values_from_env(self, monkeypatch):
        monkeypatch.setenv("GITHUB_TOKEN", "ghp_supersecret123")
        monkeypatch.delenv("GITLAB_TOKEN", raising=False)
        values = ["ghp_supersecret123"]
        out = redact("error with ghp_supersecret123 inside", values)
        assert "ghp_supersecret123" not in out

    def test_short_values_not_collected(self, monkeypatch):
        monkeypatch.setenv("GH_TOKEN", "x")
        secrets = []
        from deploynator._receipt import collect_secret_values
        secrets = collect_secret_values()
        assert "x" not in secrets


class TestRecords:
    def test_step_record_roundtrip(self):
        step = StepRecord(step="tests", status=STATUS_SUCCESS, caller="TestRunner.run")
        data = step.to_dict()
        assert data["step"] == "tests"
        assert data["caller"] == "TestRunner.run"

    def test_command_record_defaults_observed(self):
        cmd = CommandRecord(command=["git", "push"], exit_code=0, success=True)
        assert cmd.kind == KIND_OBSERVED
        assert cmd.to_dict()["exit_code"] == 0

    def test_edge_record_fields(self):
        edge = EdgeRecord(caller="a", callee="b", kind=KIND_OBSERVED,
                          evidence="runtime", confidence=1.0)
        data = edge.to_dict()
        assert set(data) == {"caller", "callee", "kind", "evidence",
                             "confidence", "provenance"}


class TestReleaseReceipt:
    def test_to_dict_schema(self):
        receipt = ReleaseReceipt("proj")
        data = receipt.to_dict()
        assert data["schema"] == "deploynator/receipt@v1"
        assert data["status"] == "running"
        assert data["mode"] == MODE_RUN

    def test_platform_merge_not_duplicate(self):
        receipt = ReleaseReceipt("proj")
        receipt.note_platform("github", "user/repo", True)
        receipt.note_platform("github", "user/repo", True, pushed=True)
        assert len(receipt.platforms) == 1
        assert receipt.platforms[0]["pushed"] is True

    def test_platform_disabled_recorded(self):
        receipt = ReleaseReceipt("proj")
        receipt.note_platform("bitbucket", "user/repo", False)
        assert receipt.platforms[0]["enabled"] is False

    def test_load_dict_roundtrip(self):
        receipt = ReleaseReceipt("proj")
        receipt.steps.append(StepRecord("tests", STATUS_SUCCESS, "TestRunner.run"))
        receipt.commands.append(CommandRecord(["git", "tag"], 0, True, stage="tag"))
        receipt.edges.append(EdgeRecord("a", "b", KIND_OBSERVED, "ev", 1.0))
        clone = ReleaseReceipt("other")
        clone.load_dict(receipt.to_dict())
        assert clone.project == "proj"
        assert clone.steps[0].step == "tests"
        assert clone.commands[0].command == ["git", "tag"]
        assert clone.edges[0].callee == "b"


class TestStages:
    def test_stage_success(self):
        collector = ReceiptCollector("proj", secrets=[], tail_chars=100)
        with collector.stage("tests", caller="TestRunner.run") as h:
            h.fail("")
        records = collector.receipt.steps
        assert len(records) == 1
        assert records[0].status == STATUS_SUCCESS
        assert records[0].caller == "TestRunner.run"

    def test_stage_failed_via_handle(self):
        collector = ReceiptCollector("proj", secrets=[], tail_chars=100)
        with collector.stage("tests") as h:
            h.fail("boom")
        assert collector.receipt.steps[0].status == STATUS_FAILED
        assert collector.receipt.steps[0].error == "boom"

    def test_stage_exception_recorded_and_raised(self):
        collector = ReceiptCollector("proj", secrets=[], tail_chars=100)
        with pytest.raises(RuntimeError), collector.stage("tests"):
            raise RuntimeError("kaboom")
        failed = [s for s in collector.receipt.steps if s.status == STATUS_FAILED]
        assert failed and "RuntimeError" in failed[0].error

    def test_stage_nesting_attaches_current(self):
        collector = ReceiptCollector("proj", secrets=[], tail_chars=100)
        with collector.stage("outer"), collector.stage("inner"):
            pass
        assert len(collector.receipt.steps) == 2

    def test_mark_failure(self):
        collector = ReceiptCollector("proj", secrets=[], tail_chars=100)
        collector.mark_failure("remote_check", "No git remote", "GitOperations.has_remote")
        assert collector.receipt.steps[0].step == "remote_check"
        assert collector.receipt.steps[0].status == STATUS_FAILED

    def test_observe_edge(self):
        collector = ReceiptCollector("proj", secrets=[], tail_chars=100)
        collector.observe_edge("DeployOrchestrator.deploy", "GitOperations.tag", "tag:1.2.4")
        edge = collector.receipt.edges[0]
        assert edge.kind == KIND_OBSERVED
        assert edge.confidence == 1.0


class TestCapture:
    def test_records_success_and_failure(self):
        collector = ReceiptCollector("proj", secrets=[], tail_chars=100)
        with collector.capture():
            subprocess.run(["true"], check=False)
            with collector.stage("tests"):
                subprocess.run(["false"], check=False)
        recs = collector.receipt.commands
        assert len(recs) == 2
        assert recs[0].exit_code == 0 and recs[0].success is True
        assert recs[1].exit_code == 1 and recs[1].success is False
        assert recs[1].stage == "tests"
        assert recs[0].command == ["true"]

    def test_records_missing_binary(self):
        collector = ReceiptCollector("proj", secrets=[], tail_chars=100)
        with collector.capture(), pytest.raises(FileNotFoundError):
            subprocess.run(["definitely-not-a-real-binary-xyz"], check=False)
        rec = collector.receipt.commands[-1]
        assert rec.exit_code is None
        assert "FileNotFoundError" in rec.exception

    def test_restores_original_run(self):
        original = subprocess.run
        collector = ReceiptCollector("proj", secrets=[], tail_chars=100)
        with collector.capture():
            pass
        assert subprocess.run is original

    def test_tails_truncated(self):
        collector = ReceiptCollector("proj", secrets=[], tail_chars=10)
        with collector.capture():
            subprocess.run(["echo", "0123456789ABCDEF"], check=False, capture_output=True, text=True)
        rec = collector.receipt.commands[0]
        assert len(rec.stdout_tail) == 10

    def test_redaction_in_tails(self, monkeypatch):
        monkeypatch.setenv("GITHUB_TOKEN", "ghp_supersecret123")
        collector = ReceiptCollector("proj", tail_chars=200)
        with collector.capture():
            subprocess.run(["echo", "leak ghp_supersecret123"],
                           check=False, capture_output=True, text=True)
        rec = collector.receipt.commands[0]
        assert "ghp_supersecret123" not in rec.stdout_tail
        assert "***REDACTED***" in rec.stdout_tail


class TestWrite:
    def test_write_and_reload(self):
        collector = ReceiptCollector("proj", secrets=[], tail_chars=100)
        with tempfile.TemporaryDirectory() as tmp:
            path = os.path.join(tmp, "sub", "receipt.json")
            written = collector.write(path)
            assert written == path
            with open(path) as f:
                data = json.load(f)
            assert data["schema"] == "deploynator/receipt@v1"

    def test_write_rejects_symlink(self):
        collector = ReceiptCollector("proj", secrets=[], tail_chars=100)
        with tempfile.TemporaryDirectory() as tmp:
            real = os.path.join(tmp, "real.json")
            with open(real, "w") as f:
                f.write("{}")
            link = os.path.join(tmp, "link.json")
            os.symlink(real, link)
            with pytest.raises(ValueError):
                collector.write(link)

    def test_write_rejects_symlink_parent(self):
        collector = ReceiptCollector("proj", secrets=[], tail_chars=100)
        with tempfile.TemporaryDirectory() as tmp:
            realdir = os.path.join(tmp, "realdir")
            os.makedirs(realdir)
            linkdir = os.path.join(tmp, "linkdir")
            os.symlink(realdir, linkdir)
            with pytest.raises(ValueError):
                collector.write(os.path.join(linkdir, "receipt.json"))

    def test_default_path_structure(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = default_receipt_path(tmp, "my proj", MODE_PLAN, STATUS_SUCCESS, "1.2.3")
            assert os.path.isdir(os.path.dirname(path))
            name = os.path.basename(path)
            assert name.startswith("receipt-my-proj-plan-success-1.2.3-")
            assert name.endswith(".json")


class TestBuildPlan:
    def _project(self, platforms: dict[str, bool]) -> ProjectConfig:
        configs = [PlatformConfig(platform=Platform.from_string(name),
                                  repo=f"user/{name}", enabled=enabled)
                   for name, enabled in platforms.items()]
        return ProjectConfig(name="p", platforms=configs)

    def _toml(self):
        from deploynator._toml import TomlConfig
        return TomlConfig(project_name="p")

    def test_feasible_set_respects_config(self):
        config = Config.create()
        edges, commands = build_plan(
            config, self._project({"github": True, "gitlab": True, "bitbucket": False}),
            self._toml(), version="1.2.4")
        callees = {(e.caller, e.callee) for e in edges}
        assert ("DeployOrchestrator.deploy", "Platform.create_release") in callees
        assert ("Platform.create_release", "GitHubCLI.create_release") in callees
        assert ("Platform.create_release", "GitLabCLI.create_release") in callees
        # Bitbucket disabled: no dispatch candidate, no command
        assert ("Platform.create_release", "BitbucketCLI.create_release") not in callees
        argvs = [c.command for c in commands]
        assert ["gh", "release", "create", "1.2.4"] in argvs
        assert ["glab", "release", "create", "1.2.4"] in argvs
        assert not any(argv and argv[0] == "bb" for argv in argvs)

    def test_override_changes_evidence_and_confidence(self):
        config = Config.create()
        edges, _ = build_plan(
            config, self._project({"github": True}),
            self._toml(), platforms_override=[Platform.GITHUB], version="1.2.4")
        dispatch = [e for e in edges if e.callee == "GitHubCLI.create_release"]
        assert len(dispatch) == 1
        assert dispatch[0].evidence == "cli:--platforms"
        assert dispatch[0].confidence == 0.9

    def test_test_docs_edges_from_toml(self):
        config = Config.create()
        from deploynator._toml import TomlConfig

        toml = replace(TomlConfig(project_name="p"), test_commands=["python -m pytest"])
        edges, commands = build_plan(config, self._project({}), toml, version="1.2.4")
        tests_edge = [e for e in edges if e.callee == "TestRunner.run"]
        assert len(tests_edge) == 1 and tests_edge[0].kind == KIND_CANDIDATE
        assert any(c.command == ["python", "-m", "pytest"] for c in commands)

    def test_no_test_docs_flag_drops_edges(self):
        config = Config.create()
        edges, _ = build_plan(config, self._project({}), self._toml(),
                              run_tests=False, run_docs=False, version="1.2.4")
        assert all(e.callee not in ("TestRunner.run", "DocsRunner.run") for e in edges)


class _DeployFixture:
    def __init__(self, base: str) -> None:
        self.work = os.path.join(base, "repo")
        os.makedirs(self.work, exist_ok=True)


def _make_repo(base: str) -> str:
    work = os.path.join(base, "repo")
    os.makedirs(work, exist_ok=True)
    subprocess.run(["git", "-C", work, "init", "-q"], check=True)
    with open(os.path.join(work, "version.json"), "w") as f:
        json.dump({"version": "1.2.3"}, f)
    with open(os.path.join(work, "deploynator.toml"), "w") as f:
        f.write("[tests]\nallow_no_tests = true\n[docs]\nauto = false\n"
                "[pypi]\nenabled = false\n")
    subprocess.run(["git", "-C", work, "add", "-A"], check=True, capture_output=True)
    env = {**os.environ, "GIT_AUTHOR_NAME": "t", "GIT_AUTHOR_EMAIL": "t@t",
           "GIT_COMMITTER_NAME": "t", "GIT_COMMITTER_EMAIL": "t@t"}
    subprocess.run(["git", "-C", work, "commit", "-qm", "chore: init"], check=True, env=env,
                   capture_output=True)
    subprocess.run(["git", "-C", work, "remote", "add", "origin",
                    "file:///nonexistent/origin.git"], check=True, capture_output=True)
    subprocess.run(["git", "-C", work, "branch", "-M", "main"], check=True, capture_output=True)
    return work


class TestDeployReceipts:
    def test_dry_run_trace_writes_plan(self):
        config = Config.create()
        with tempfile.TemporaryDirectory() as tmp:
            work = _make_repo(tmp)
            receipt_file = os.path.join(tmp, "out", "receipt.json")
            project = ProjectConfig(name="planp", path=work, platforms=[
                PlatformConfig(platform=Platform.GITHUB, repo="user/p", enabled=True),
                PlatformConfig(platform=Platform.GITLAB, repo="user/p", enabled=False),
            ])
            result = DeployOrchestrator(config).deploy(
                project=project, commit_type=CommitType.PATCH, subject="x",
                dry_run=True, run_tests=True, run_docs=True, run_pypi=False,
                run_deb=False, receipt_path=receipt_file, trace=True,
            )
            assert result.receipt_path == receipt_file
            with open(receipt_file) as f:
                data = json.load(f)
            assert data["mode"] == MODE_PLAN
            assert data["status"] == STATUS_SUCCESS
            assert data["version_from"] == "1.2.3"
            assert data["version_to"] == "1.2.4"
            callee_set = {e["callee"] for e in data["edges"]}
            assert "GitHubCLI.create_release" in callee_set
            assert "GitLabCLI.create_release" not in callee_set
            platforms = {p["platform"]: p for p in data["platforms"]}
            assert platforms["gitlab"]["enabled"] is False
            planned_cmds = [c["command"] for c in data["commands"] if c["kind"] == KIND_CANDIDATE]
            assert ["gh", "release", "create", "1.2.4"] in planned_cmds

    def test_failed_run_records_guard(self):
        config = Config.create()
        with tempfile.TemporaryDirectory() as tmp:
            base = os.path.join(tmp, "proj")
            os.makedirs(base)
            with open(os.path.join(base, "version.json"), "w") as f:
                json.dump({"version": "1.2.3"}, f)
            with open(os.path.join(base, "deploynator.toml"), "w") as f:
                f.write("[tests]\nallow_no_tests = true\n[docs]\nauto = false\n")
            receipt_file = os.path.join(tmp, "out", "receipt.json")
            result = DeployOrchestrator(config).deploy(
                project=ProjectConfig(name="guardp", path=base),
                commit_type=CommitType.FIX, subject="x",
                dry_run=False, run_tests=False, run_docs=False,
                run_pypi=False, run_deb=False, receipt_path=receipt_file,
            )
            assert result.success is False
            assert "No git remote configured" in (result.error or "")
            with open(receipt_file) as f:
                data = json.load(f)
            assert data["status"] == STATUS_FAILED
            step_names = [s["step"] for s in data["steps"]]
            assert "remote_check" in step_names

    def test_full_run_observed_edges(self):
        config = Config.create()
        config = replace(config, gh_cli="definitely-not-gh-xyz")
        with tempfile.TemporaryDirectory() as tmp:
            work = _make_repo(tmp)
            receipt_file = os.path.join(tmp, "out", "receipt.json")
            result = DeployOrchestrator(config).deploy(
                project=ProjectConfig(name="fullp", path=work),
                commit_type=CommitType.PATCH, subject="x",
                dry_run=False, run_tests=False, run_docs=False,
                run_pypi=False, run_deb=False, receipt_path=receipt_file,
            )
            with open(receipt_file) as f:
                data = json.load(f)
            assert data["version_from"] == "1.2.3"
            assert data["tag"] == "1.2.4"
            steps = {s["step"]: s for s in data["steps"]}
            assert steps["commit"]["status"] == STATUS_SUCCESS
            assert steps["tag"]["status"] == STATUS_SUCCESS
            assert steps["push:origin"]["status"] == STATUS_FAILED
            assert steps["gh_release"]["status"] == STATUS_FAILED
            observed = {(e["caller"], e["callee"]) for e in data["edges"]
                        if e["kind"] == KIND_OBSERVED}
            assert ("DeployOrchestrator.deploy", "GitOperations.commit") in observed
            assert ("DeployOrchestrator.deploy", "GitOperations.tag") in observed
            commands = data["commands"]
            assert any(c["command"][0] == "git" and "tag" in c["command"]
                       and c["exit_code"] == 0 for c in commands)
            pushes = [c for c in commands if c["command"][0] == "git" and "push" in c["command"]]
            assert pushes and pushes[-1]["exit_code"] != 0
            assert data["status"] == STATUS_FAILED
            assert result.receipt_path == receipt_file
