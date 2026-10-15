from __future__ import annotations

import os
import subprocess
from typing import Optional

from deploynator._config import Config


class GitOperations:
    def __init__(self, config: Config) -> None:
        self._config = config

    def check_gpg(self) -> tuple[bool, str]:
        try:
            key_id = subprocess.run(
                ["git", "config", "--get", "user.signingkey"],
                capture_output=True, text=True, check=False,
            )
            if key_id.returncode != 0 or not key_id.stdout.strip():
                return False, "GPG signing key not configured"
            gpg_check = subprocess.run(
                ["gpg", "--list-secret-keys", key_id.stdout.strip()],
                capture_output=True, text=True, check=False,
            )
            if gpg_check.returncode == 0:
                return True, key_id.stdout.strip()
            return False, "Secret key not found"
        except FileNotFoundError:
            return False, "gpg or git not found"

    def gpg_sign_flag(self) -> list[str]:
        ok, _ = self.check_gpg()
        return ["-S"] if ok else []

    def clone(self, url: str, dest: str, depth: int = 1) -> bool:
        try:
            result = subprocess.run(
                ["git", "clone", "--depth", str(depth), url, dest],
                capture_output=True, text=True, check=False,
            )
            return result.returncode == 0
        except FileNotFoundError:
            return False

    def add_all(self, repo_path: str) -> bool:
        try:
            result = subprocess.run(
                ["git", "-C", repo_path, "add", "-A"],
                capture_output=True, text=True, check=False,
            )
            return result.returncode == 0
        except FileNotFoundError:
            return False

    def commit(self, repo_path: str, message: str) -> tuple[bool, str]:
        try:
            flags = self.gpg_sign_flag()
            cmd = ["git", "-C", repo_path, "commit"] + flags + ["-m", message]
            result = subprocess.run(cmd, capture_output=True, text=True, check=False)
            if result.returncode != 0:
                err_msg = result.stderr.strip() or result.stdout.strip() or "unknown error"
                return False, err_msg
            return True, result.stdout.strip()
        except FileNotFoundError as exc:
            return False, str(exc)

    def amend_no_edit(self, repo_path: str) -> bool:
        try:
            flags = self.gpg_sign_flag()
            cmd = ["git", "-C", repo_path, "commit"] + flags + ["--amend", "--no-edit"]
            result = subprocess.run(cmd, capture_output=True, text=True, check=False)
            return result.returncode == 0
        except FileNotFoundError:
            return False

    def tag(self, repo_path: str, tag_name: str, message: str) -> bool:
        try:
            result = subprocess.run(
                ["git", "-C", repo_path, "tag", "-a", tag_name, "-m", message],
                capture_output=True, text=True, check=False,
            )
            return result.returncode == 0
        except FileNotFoundError:
            return False

    def delete_tag(self, repo_path: str, tag_name: str) -> bool:
        try:
            result = subprocess.run(
                ["git", "-C", repo_path, "tag", "-d", tag_name],
                capture_output=True, text=True, check=False,
            )
            return result.returncode == 0
        except FileNotFoundError:
            return False

    def tag_exists(self, repo_path: str, tag_name: str) -> bool:
        try:
            result = subprocess.run(
                ["git", "-C", repo_path, "rev-parse", "--verify", f"refs/tags/{tag_name}"],
                capture_output=True, text=True, check=False,
            )
            return result.returncode == 0
        except FileNotFoundError:
            return False

    def push(self, repo_path: str, remote: str, branch: str, follow_tags: bool = True) -> bool:
        try:
            cmd = ["git", "-C", repo_path, "push", remote, branch]
            if follow_tags:
                cmd.append("--follow-tags")
            result = subprocess.run(cmd, capture_output=True, text=True, check=False)
            return result.returncode == 0
        except FileNotFoundError:
            return False

    def push_tags(self, repo_path: str, remote: str = "origin") -> bool:
        try:
            result = subprocess.run(
                ["git", "-C", repo_path, "push", remote, "--tags"],
                capture_output=True, text=True, check=False,
            )
            return result.returncode == 0
        except FileNotFoundError:
            return False

    def create_branch(self, repo_path: str, branch_name: str, base: Optional[str] = None) -> bool:
        try:
            if base:
                result = subprocess.run(
                    ["git", "-C", repo_path, "checkout", "-b", branch_name, base],
                    capture_output=True, text=True, check=False,
                )
            else:
                result = subprocess.run(
                    ["git", "-C", repo_path, "checkout", "-b", branch_name],
                    capture_output=True, text=True, check=False,
                )
            return result.returncode == 0
        except FileNotFoundError:
            return False

    def checkout(self, repo_path: str, branch: str) -> bool:
        try:
            result = subprocess.run(
                ["git", "-C", repo_path, "checkout", branch],
                capture_output=True, text=True, check=False,
            )
            return result.returncode == 0
        except FileNotFoundError:
            return False

    def get_changed_files(self, repo_path: str, from_ref: str, to_ref: str = "HEAD") -> dict[str, list[str]]:
        result = {
            "modified": [],
            "deleted": [],
            "created": [],
        }
        try:
            modified = subprocess.run(
                ["git", "-C", repo_path, "diff", "--name-only", f"{from_ref}..{to_ref}"],
                capture_output=True, text=True, check=False,
            )
            if modified.returncode == 0:
                result["modified"] = [f for f in modified.stdout.strip().split("\n") if f]

            deleted = subprocess.run(
                ["git", "-C", repo_path, "diff", "--name-only", "--diff-filter=D", f"{from_ref}..{to_ref}"],
                capture_output=True, text=True, check=False,
            )
            if deleted.returncode == 0:
                result["deleted"] = [f for f in deleted.stdout.strip().split("\n") if f]

            created = subprocess.run(
                ["git", "-C", repo_path, "diff", "--name-only", "--diff-filter=A", f"{from_ref}..{to_ref}"],
                capture_output=True, text=True, check=False,
            )
            if created.returncode == 0:
                result["created"] = [f for f in created.stdout.strip().split("\n") if f]
        except FileNotFoundError:
            pass
        return result

    def get_log(self, repo_path: str, from_ref: str, to_ref: str = "HEAD", format_str: str = "%s|||%an|||%h") -> list[str]:
        try:
            result = subprocess.run(
                ["git", "-C", repo_path, "log", f"{from_ref}..{to_ref}", f"--pretty=format:{format_str}"],
                capture_output=True, text=True, check=False,
            )
            if result.returncode == 0 and result.stdout.strip():
                return result.stdout.strip().split("\n")
        except FileNotFoundError:
            pass
        return []

    def get_start_ref(self, repo_path: str) -> Optional[str]:
        try:
            result = subprocess.run(
                ["git", "-C", repo_path, "describe", "--tags", "--abbrev=0"],
                capture_output=True, text=True, check=False,
            )
            if result.returncode == 0:
                return result.stdout.strip()
            result = subprocess.run(
                ["git", "-C", repo_path, "rev-list", "--max-parents=0", "HEAD"],
                capture_output=True, text=True, check=False,
            )
            if result.returncode == 0:
                return result.stdout.strip()
        except FileNotFoundError:
            pass
        return None

    def current_branch(self, repo_path: str) -> Optional[str]:
        try:
            result = subprocess.run(
                ["git", "-C", repo_path, "rev-parse", "--abbrev-ref", "HEAD"],
                capture_output=True, text=True, check=False,
            )
            if result.returncode == 0:
                return result.stdout.strip()
        except FileNotFoundError:
            pass
        return None

    def is_dirty(self, repo_path: str) -> bool:
        try:
            result = subprocess.run(
                ["git", "-C", repo_path, "status", "--porcelain"],
                capture_output=True, text=True, check=False,
            )
            return bool(result.stdout.strip())
        except FileNotFoundError:
            return True

    def has_remote(self, repo_path: str, remote: str = "origin") -> bool:
        try:
            result = subprocess.run(
                ["git", "-C", repo_path, "remote", "get-url", remote],
                capture_output=True, text=True, check=False,
            )
            return result.returncode == 0
        except FileNotFoundError:
            return False
