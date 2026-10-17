import os
import subprocess
import tempfile

from deploynator._config import Config
from deploynator._deploy import DeployOrchestrator
from deploynator._git import GitOperations


def _config_git(path: str) -> None:
    subprocess.run(["git", "-C", path, "config", "user.email", "t@t"], check=True)
    subprocess.run(["git", "-C", path, "config", "user.name", "t"], check=True)


class TestGitSync:
    def _make_repo(self, tmp: str) -> str:
        work = os.path.join(tmp, "work")
        subprocess.run(["git", "init", "-q", "-b", "main", work], check=True)
        _config_git(work)
        return work

    def test_branch_exists_is_behind(self):
        with tempfile.TemporaryDirectory() as tmp:
            work = self._make_repo(tmp)
            with open(os.path.join(work, "a.txt"), "w") as f:
                f.write("a")
            subprocess.run(["git", "-C", work, "add", "-A"], check=True)
            subprocess.run(["git", "-C", work, "commit", "-q", "-m", "init"], check=True)
            subprocess.run(["git", "-C", work, "checkout", "-q", "-b", "dev"], check=True)
            subprocess.run(["git", "-C", work, "checkout", "-q", "main"], check=True)

            git = GitOperations(Config.create())
            assert git.branch_exists(work, "main")
            assert git.branch_exists(work, "dev")
            assert not git.branch_exists(work, "nope")
            # main == dev: nada detras
            assert not git.is_behind(work, "dev", "main")
            # un commit solo en main => dev esta atras
            with open(os.path.join(work, "b.txt"), "w") as f:
                f.write("b")
            subprocess.run(["git", "-C", work, "add", "-A"], check=True)
            subprocess.run(["git", "-C", work, "commit", "-q", "-m", "b"], check=True)
            assert git.is_behind(work, "dev", "main")
            assert not git.is_behind(work, "main", "dev")

    def test_sync_dev_to_main_force_pushes(self):
        with tempfile.TemporaryDirectory() as tmp:
            remote = os.path.join(tmp, "origin.git")
            subprocess.run(["git", "init", "--bare", remote], check=True)
            work = self._make_repo(tmp)
            subprocess.run(["git", "-C", work, "remote", "add", "origin", remote], check=True)

            with open(os.path.join(work, "a.txt"), "w") as f:
                f.write("a")
            subprocess.run(["git", "-C", work, "add", "-A"], check=True)
            subprocess.run(["git", "-C", work, "commit", "-q", "-m", "init"], check=True)
            subprocess.run(["git", "-C", work, "checkout", "-q", "-b", "dev"], check=True)
            subprocess.run(["git", "-C", work, "push", "-q", "origin", "main", "dev"], check=True)
            subprocess.run(["git", "-C", work, "checkout", "-q", "main"], check=True)

            with open(os.path.join(work, "b.txt"), "w") as f:
                f.write("b")
            subprocess.run(["git", "-C", work, "add", "-A"], check=True)
            subprocess.run(["git", "-C", work, "commit", "-q", "-m", "b"], check=True)
            subprocess.run(["git", "-C", work, "push", "-q", "origin", "main"], check=True)

            orch = DeployOrchestrator(Config.create())
            orch._sync_dev_to_main(work)

            dev = subprocess.run(
                ["git", "ls-remote", remote, "refs/heads/dev"],
                capture_output=True, text=True, check=True,
            ).stdout.split()[0]
            main = subprocess.run(
                ["git", "ls-remote", remote, "refs/heads/main"],
                capture_output=True, text=True, check=True,
            ).stdout.split()[0]
            assert dev == main

    def test_sync_noop_when_dev_equal_or_missing(self):
        with tempfile.TemporaryDirectory() as tmp:
            remote = os.path.join(tmp, "origin.git")
            subprocess.run(["git", "init", "--bare", remote], check=True)
            work = self._make_repo(tmp)
            subprocess.run(["git", "-C", work, "remote", "add", "origin", remote], check=True)

            with open(os.path.join(work, "a.txt"), "w") as f:
                f.write("a")
            subprocess.run(["git", "-C", work, "add", "-A"], check=True)
            subprocess.run(["git", "-C", work, "commit", "-q", "-m", "init"], check=True)
            subprocess.run(["git", "-C", work, "checkout", "-q", "-b", "dev"], check=True)
            subprocess.run(["git", "-C", work, "push", "-q", "origin", "main", "dev"], check=True)
            subprocess.run(["git", "-C", work, "checkout", "-q", "main"], check=True)

            orch = DeployOrchestrator(Config.create())
            orch._sync_dev_to_main(work)  # dev == main: no-op

            dev = subprocess.run(
                ["git", "ls-remote", remote, "refs/heads/dev"],
                capture_output=True, text=True, check=True,
            ).stdout.split()[0]
            main = subprocess.run(
                ["git", "ls-remote", remote, "refs/heads/main"],
                capture_output=True, text=True, check=True,
            ).stdout.split()[0]
            assert dev == main
