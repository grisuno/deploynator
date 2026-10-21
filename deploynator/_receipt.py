"""Receipt contract: operational trace of a deploynator release.

Evidence hierarchy (golden rule):
  Fact      = step observed at runtime (exit_code recorded)      -> observed
  Candidate = feasible set from config / CLI / interface contract -> candidate
  Predicted = scored by a model; labeled, never presented as fact -> predicted

Every edge follows: (caller, callee, kind, evidence, confidence, provenance).

Receipts are written atomically, streams are tail-truncated and token
environment values are redacted before persisting. Receipt paths (and
their parents) must not be symlinks. With ``--receipt`` omitted, receipts
land in ``<cwd>/release-receipts/`` so target repos are never polluted
by ``git add -A``; if you point the receipt inside a managed repo, add
the directory to its .gitignore.
"""

from __future__ import annotations

import json
import os
import re
import subprocess
import tempfile
import time
from contextlib import contextmanager
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone

from deploynator._config import Config

RECEIPT_SCHEMA = "deploynator/receipt@v1"

KIND_OBSERVED = "observed"
KIND_CANDIDATE = "candidate"
STATUS_RUNNING = "running"
STATUS_SUCCESS = "success"
STATUS_FAILED = "failed"
STATUS_PARTIAL = "partial"
MODE_RUN = "run"
MODE_PLAN = "plan"

REDACTED = "***REDACTED***"

_PLATFORM_CLASS_NAMES = {
    "github": "GitHubCLI",
    "gitlab": "GitLabCLI",
    "bitbucket": "BitbucketCLI",
}

_COMMON_TOKEN_ENV_NAMES = (
    "GH_TOKEN",
    "GLAB_TOKEN",
    "BB_TOKEN",
    "TWINE_PASSWORD",
    "PYPI_TOKEN",
    "TWINE_USERNAME",
)

_MIN_SECRET_LEN = 6
_FILENAME_FALLBACK = "project"
_TIME_FMT = "%Y%m%dT%H%M%SZ"


def _utc_now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def _tail(text: str, limit: int) -> str:
    if len(text) <= limit:
        return text
    return text[-limit:]


def _safe_name(value: str) -> str:
    cleaned = re.sub(r"[^A-Za-z0-9._-]+", "-", value).strip("-")
    return cleaned or _FILENAME_FALLBACK


def collect_secret_values() -> list[str]:
    """Current env token values worth redacting (length >= threshold)."""
    config = Config.create()
    secrets: list[str] = []
    for name in (
        config.github_token_env,
        config.gitlab_token_env,
        config.bitbucket_token_env,
        *_COMMON_TOKEN_ENV_NAMES,
    ):
        value = os.environ.get(name)
        if value and len(value) >= _MIN_SECRET_LEN:
            secrets.append(value)
    return secrets


def redact(text: str, secrets: list[str]) -> str:
    if not text or not secrets:
        return text
    for secret in secrets:
        if secret and secret in text:
            text = text.replace(secret, REDACTED)
    return text


@dataclass(frozen=True)
class StepRecord:
    step: str
    status: str
    caller: str = ""
    error: str = ""
    started_at: str = field(default_factory=_utc_now_iso)
    duration_ms: int = 0

    def to_dict(self) -> dict:
        return asdict(self)


@dataclass(frozen=True)
class CommandRecord:
    command: list[str]
    exit_code: int | None
    success: bool | None
    stage: str = ""
    kind: str = KIND_OBSERVED
    cwd: str = ""
    stdout_tail: str = ""
    stderr_tail: str = ""
    exception: str = ""
    started_at: str = field(default_factory=_utc_now_iso)
    duration_ms: int = 0

    def to_dict(self) -> dict:
        return asdict(self)


@dataclass(frozen=True)
class EdgeRecord:
    caller: str
    callee: str
    kind: str
    evidence: str
    confidence: float
    provenance: str = ""

    def to_dict(self) -> dict:
        return asdict(self)


class ReleaseReceipt:
    """Full release record.

    Mutable by design: the orchestrator mutates it while running;
    ``write()`` serializes the final state. ``load_dict`` supports
    round-trips from plain JSON data.
    """

    def __init__(
        self,
        project: str,
        mode: str = MODE_RUN,
        dry_run: bool = False,
        trace: bool = False,
        flags: dict | None = None,
    ) -> None:
        self.schema = RECEIPT_SCHEMA
        self.project = project
        self.mode = mode
        self.status = STATUS_RUNNING
        self.dry_run = dry_run
        self.trace = trace
        self.flags = dict(flags or {})
        self.version_from = ""
        self.version_to = ""
        self.tag = ""
        self.commit = ""
        self.branch = ""
        self.error = ""
        self.steps: list[StepRecord] = []
        self.commands: list[CommandRecord] = []
        self.edges: list[EdgeRecord] = []
        self.platforms: list[dict] = []
        self.created_at = _utc_now_iso()
        self.duration_ms = 0

    def note_platform(
        self,
        label: str,
        repo: str,
        enabled: bool,
        pushed: bool | None = None,
        released: bool | None = None,
        error: str | None = None,
    ) -> None:
        """Insert or merge a platform state entry (insertion only once)."""
        for info in self.platforms:
            if info.get("platform") == label:
                if pushed is not None:
                    info["pushed"] = pushed
                if released is not None:
                    info["released"] = released
                if error is not None:
                    info["error"] = error
                return
        self.platforms.append({
            "platform": label,
            "repo": repo,
            "enabled": enabled,
            "pushed": pushed,
            "released": released,
            "error": error,
        })

    def to_dict(self) -> dict:
        return {
            "schema": self.schema,
            "mode": self.mode,
            "status": self.status,
            "project": self.project,
            "dry_run": self.dry_run,
            "trace": self.trace,
            "flags": dict(self.flags),
            "version_from": self.version_from,
            "version_to": self.version_to,
            "tag": self.tag,
            "commit": self.commit,
            "branch": self.branch,
            "error": self.error,
            "created_at": self.created_at,
            "duration_ms": self.duration_ms,
            "steps": [s.to_dict() for s in self.steps],
            "commands": [c.to_dict() for c in self.commands],
            "edges": [e.to_dict() for e in self.edges],
            "platforms": [dict(p) for p in self.platforms],
        }

    def load_dict(self, data: dict) -> None:
        """Restore state from a plain dict (round-trip support)."""
        scalar = ("schema", "project", "mode", "status", "dry_run", "trace",
                  "flags", "version_from", "version_to", "tag", "commit",
                  "branch", "error", "created_at", "duration_ms")
        for key in scalar:
            if key in data:
                setattr(self, key, data[key])
        self.steps = [StepRecord(**s) for s in data.get("steps", [])]
        self.commands = [CommandRecord(**c) for c in data.get("commands", [])]
        self.edges = [EdgeRecord(**e) for e in data.get("edges", [])]
        self.platforms = [dict(p) for p in data.get("platforms", [])]


class _StageHandle:
    def __init__(self) -> None:
        self.error = ""

    @property
    def failed(self) -> bool:
        return bool(self.error)

    def fail(self, error: str) -> None:
        if error:
            self.error = str(error)[:2000]


class ReceiptCollector:
    """Collects steps, subprocess calls and evidence edges for one deploy.

    ``capture()`` wraps ``subprocess.run`` with a recorder so every external
    command executed during the deploy (git, gh, glab, bb, pytest, pandoc,
    dpkg, twine...) is captured with argv, exit code and output tails
    without modifying any other contract. Swaps the module attribute and
    always restores it; not reentrant across threads (deploynator deploys
    are CLI-serial).
    """

    def __init__(
        self,
        project: str,
        mode: str = MODE_RUN,
        dry_run: bool = False,
        trace: bool = False,
        flags: dict | None = None,
        secrets: list[str] | None = None,
        tail_chars: int | None = None,
    ) -> None:
        cls_config = Config.create()
        self.receipt = ReleaseReceipt(project, mode=mode, dry_run=dry_run, trace=trace, flags=flags)
        self._secrets = collect_secret_values() if secrets is None else list(secrets)
        self._tail_chars = tail_chars if tail_chars is not None else cls_config.receipt_tail_chars
        self._stage_stack: list[str] = []
        self._started = time.monotonic()
        self._captured = False

    # Stages ---------------------------------------------------------

    @contextmanager
    def stage(self, label: str, caller: str = ""):
        """Record a logical step. Yields a handle; handle.fail(msg) marks
        the stage as failed explicitly, exceptions mark it as failed too."""
        handle = _StageHandle()
        self._stage_stack.append(label)
        started = time.monotonic()
        started_at = _utc_now_iso()
        try:
            yield handle
        except Exception as exc:  # contract boundary: record, re-raise
            handle.error = f"{type(exc).__name__}: {exc}"
            raise
        finally:
            self._stage_stack.pop()
            self.receipt.steps.append(_build_step(
                label, caller, handle.error, started_at, started, self._secrets
            ))

    def mark_failure(self, label: str, error: str, caller: str = "") -> None:
        """Record a guard/condition failure occurring outside stage blocks."""
        self.receipt.steps.append(_build_step(
            label, caller, str(error), _utc_now_iso(), time.monotonic(), self._secrets
        ))

    def note_platform(self, label: str, repo: str, enabled: bool,
                      pushed: bool | None = None, released: bool | None = None,
                      error: str | None = None) -> None:
        """Insert or merge platform state on the underlying receipt."""
        self.receipt.note_platform(label, repo, enabled, pushed=pushed,
                                   released=released, error=error)

    def current_stage(self) -> str:
        return self._stage_stack[-1] if self._stage_stack else ""

    # Evidence edges -------------------------------------------------

    def observe_edge(self, caller: str, callee: str, evidence: str) -> None:
        version = self.receipt.version_to or self.receipt.version_from or "none"
        self.add_edge(EdgeRecord(
            caller=caller,
            callee=callee,
            kind=KIND_OBSERVED,
            evidence=evidence,
            confidence=1.0,
            provenance=f"receipt:{version}",
        ))

    def add_edge(self, edge: EdgeRecord) -> None:
        self.receipt.edges.append(edge)

    def add_edges(self, edges: list[EdgeRecord]) -> None:
        self.receipt.edges.extend(edges)

    def add_commands(self, commands: list[CommandRecord]) -> None:
        self.receipt.commands.extend(commands)

    # Lifecycle ------------------------------------------------------

    def set_run_context(self, version_from: str, version_to: str,
                        commit: str = "", branch: str = "") -> None:
        self.receipt.version_from = version_from
        self.receipt.version_to = version_to
        if commit:
            self.receipt.commit = commit
        if branch:
            self.receipt.branch = branch

    def set_tag(self, tag: str) -> None:
        self.receipt.tag = tag
        if tag:
            self.receipt.version_to = tag

    def set_commit(self, commit: str) -> None:
        if commit:
            self.receipt.commit = commit

    def finalize(self, status: str, error: str = "") -> None:
        self.receipt.status = status
        if error:
            self.receipt.error = redact(str(error)[:2000], self._secrets)
        self.receipt.duration_ms = int((time.monotonic() - self._started) * 1000)

    # Subprocess capture ----------------------------------------------

    @contextmanager
    def capture(self):
        if self._captured:
            yield self
            return
        original = subprocess.run
        collector = self

        def _run_recorded(*args, **kwargs):
            argv = args[0] if args else kwargs.get("args")
            cwd_value = kwargs.get("cwd") or ""
            started = time.monotonic()
            started_at = _utc_now_iso()
            try:
                completed = original(*args, **kwargs)
            except Exception as exc:  # FileNotFoundError, TimeoutExpired, ...
                collector._record_command(
                    argv, None, False, cwd_value, "", "",
                    f"{type(exc).__name__}: {exc}",
                    started_at, time.monotonic() - started,
                )
                raise
            output = completed.stdout if isinstance(completed.stdout, str) else ""
            errors = completed.stderr if isinstance(completed.stderr, str) else ""
            collector._record_command(
                argv, completed.returncode, completed.returncode == 0,
                cwd_value, output, errors, "",
                started_at, time.monotonic() - started,
            )
            return completed

        subprocess.run = _run_recorded
        self._captured = True
        try:
            yield self
        finally:
            subprocess.run = original
            self._captured = False

    def _record_command(self, argv, exit_code, success, cwd_value, output, errors,
                        exception, started_at, elapsed) -> None:
        if not isinstance(argv, list):
            argv = [str(argv)] if argv is not None else []
        self.receipt.commands.append(CommandRecord(
            command=[str(part) for part in argv],
            exit_code=exit_code,
            success=success,
            stage=self.current_stage(),
            kind=KIND_OBSERVED,
            cwd=str(cwd_value) if cwd_value else "",
            stdout_tail=_tail(redact(output, self._secrets), self._tail_chars),
            stderr_tail=_tail(redact(errors, self._secrets), self._tail_chars),
            exception=redact(exception, self._secrets),
            started_at=started_at,
            duration_ms=int(elapsed * 1000),
        ))

    # Writing --------------------------------------------------------

    def write(self, path: str) -> str:
        """Atomic write. Rejects symlink targets and symlink parents."""
        abs_path = os.path.abspath(os.path.expanduser(path))
        if os.path.islink(abs_path):
            raise ValueError(f"Symlink rejected: {abs_path}")
        parent = os.path.dirname(abs_path)
        if parent and os.path.islink(parent):
            raise ValueError(f"Symlink rejected: {parent}")
        os.makedirs(parent, exist_ok=True)
        payload = json.dumps(self.receipt.to_dict(), indent=2, ensure_ascii=False)
        fd, tmp_path = tempfile.mkstemp(dir=parent, prefix=".receipt-", suffix=".tmp")
        try:
            with os.fdopen(fd, "w", encoding="utf-8") as f:
                f.write(payload)
            os.replace(tmp_path, abs_path)
        except OSError:
            try:
                os.unlink(tmp_path)
            except OSError:
                pass
            raise
        return abs_path


def _build_step(label: str, caller: str, error: str, started_at: str,
                started: float, secrets: list[str]) -> StepRecord:
    """Build one step record, truncating and redacting the error string."""
    clean_error = _tail(redact(error or "", secrets), 2000)
    return StepRecord(
        step=label,
        status=(STATUS_FAILED if clean_error else STATUS_SUCCESS),
        caller=caller,
        error=clean_error,
        started_at=started_at,
        duration_ms=int((time.monotonic() - started) * 1000),
    )


def default_receipt_path(base_dir: str, project: str, mode: str, status: str,
                         version: str = "") -> str:
    """Default atomic receipt location: <base_dir>/<receipts_dir>/."""
    config = Config.create()
    receipts_dir = os.path.join(os.path.abspath(base_dir), config.receipts_dir)
    if os.path.islink(receipts_dir):
        raise ValueError(f"Symlink rejected: {receipts_dir}")
    os.makedirs(receipts_dir, exist_ok=True)
    parts = ["receipt", _safe_name(project), mode, _safe_name(status)]
    if version:
        parts.append(_safe_name(version))
    stamp = datetime.now(timezone.utc).strftime(_TIME_FMT)
    return os.path.join(receipts_dir, "-".join(parts) + f"-{stamp}.json")


def build_receipt_from_result(receipt: ReleaseReceipt, result, error: str = "") -> None:
    """Stay consistent with the DeployResult before writing."""
    project_name = result.project
    version = result.version
    if version:
        receipt.version_to = version
    if result.success:
        receipt.status = STATUS_SUCCESS
    elif result.platforms_pushed or result.releases_created:
        receipt.status = STATUS_PARTIAL
    else:
        receipt.status = STATUS_FAILED
    detail = error or (result.error or "")
    if detail:
        receipt.error = redact(str(detail)[:2000], collect_secret_values())
    if project_name:
        receipt.project = project_name


def build_plan(
    config: Config,
    project,
    toml,
    platforms_override: list | None = None,
    run_tests: bool = True,
    run_docs: bool = True,
    run_pypi: bool = True,
    run_deb: bool = True,
    version: str = "",
) -> tuple[list[EdgeRecord], list[CommandRecord]]:
    """Feasible set from effective config + CLI flags + interface contract.

    Never claims what ran: every result is a candidate with provenance.
    """
    edges: list[EdgeRecord] = []
    commands: list[CommandRecord] = []

    deploy_caller = "DeployOrchestrator.deploy"

    if run_tests and toml.test_commands:
        edges.append(EdgeRecord(deploy_caller, "TestRunner.run", KIND_CANDIDATE,
                                "toml:tests.commands", 0.9, "config:deploynator.toml"))
        for cmd_str in toml.test_commands:
            parts = cmd_str.split()
            if parts:
                commands.append(CommandRecord(command=parts, exit_code=None, success=None,
                                              stage="tests", kind=KIND_CANDIDATE))

    if run_docs and toml.docs_command:
        edges.append(EdgeRecord(deploy_caller, "DocsRunner.run", KIND_CANDIDATE,
                                "toml:docs.command", 0.9, "config:deploynator.toml"))
        docs_parts = toml.docs_command.split()
        if docs_parts:
            commands.append(CommandRecord(command=docs_parts, exit_code=None, success=None,
                                          stage="docs", kind=KIND_CANDIDATE))

    edges.append(EdgeRecord(deploy_caller, "GitOperations.commit", KIND_CANDIDATE,
                            "flow:deploy_pipeline", 0.9, "contract:_deploy.py"))
    edges.append(EdgeRecord(deploy_caller, "GitOperations.tag", KIND_CANDIDATE,
                            "flow:deploy_pipeline", 0.9, "contract:_deploy.py"))
    edges.append(EdgeRecord(deploy_caller, "GitOperations.push", KIND_CANDIDATE,
                            "flow:deploy_pipeline", 0.9, "contract:_deploy.py"))

    if run_deb and toml.deb_enabled:
        edges.append(EdgeRecord(deploy_caller, "DebRunner.run", KIND_CANDIDATE,
                                "toml:deb.enabled", 0.7, "config:deploynator.toml"))
        if toml.deb_upload_assets:
            edges.append(EdgeRecord(deploy_caller, "Platform.upload_release_assets", KIND_CANDIDATE,
                                    "toml:deb.upload_assets", 0.6, "contract:_platforms.py"))

    if run_pypi and toml.pypi_enabled:
        edges.append(EdgeRecord(deploy_caller, "PyPIRunner.run", KIND_CANDIDATE,
                                "toml:pypi.enabled", 0.7, "config:deploynator.toml"))

    # Platform dispatch. Sound edge to the interface; per-subclass expansions
    # are dispatch hypotheses, never facts.
    edges.append(EdgeRecord(deploy_caller, "Platform.create_release", KIND_CANDIDATE,
                            "interface:Platform", 1.0, "contract:_platforms.py"))

    for pc in project.platforms:
        if platforms_override and pc.platform not in platforms_override:
            continue
        if not pc.enabled:
            continue
        label = pc.platform.label()
        class_name = _PLATFORM_CLASS_NAMES.get(label, f"{label.capitalize()}CLI")
        edges.append(EdgeRecord(
            caller="Platform.create_release",
            callee=f"{class_name}.create_release",
            kind=KIND_CANDIDATE,
            evidence=("cli:--platforms" if platforms_override else "config:PlatformConfig.enabled"),
            confidence=(0.9 if platforms_override else 0.5),
            provenance=(f"cli:{label}" if platforms_override else f"config:{pc.repo}"),
        ))
        edges.append(EdgeRecord(
            caller=deploy_caller,
            callee="GitOperations.push",
            kind=KIND_CANDIDATE,
            evidence=f"platform:{label}",
            confidence=0.9,
            provenance=f"remote:{pc.repo}",
        ))
        commands.append(CommandRecord(
            command=[_platform_cli(label), "release", "create", version],
            exit_code=None,
            success=None,
            stage=f"release:{label}",
            kind=KIND_CANDIDATE,
        ))

    return edges, commands


def _platform_cli(label: str) -> str:
    config = Config.create()
    mapping = {}
    if config.gh_cli:
        mapping["github"] = config.gh_cli
    if config.glab_cli:
        mapping["gitlab"] = config.glab_cli
    if config.bb_cli:
        mapping["bitbucket"] = config.bb_cli
    return mapping.get(label, label)
