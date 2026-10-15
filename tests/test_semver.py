import json
import os
import tempfile
import pytest
from deploynator._config import Config
from deploynator._semver import SemverManager
from deploynator._models import VersionInfo, CommitType


class TestSemverManager:
    @pytest.fixture
    def manager(self):
        config = Config.create()
        return SemverManager(config)

    def test_get_current_version_from_file(self, manager):
        with tempfile.TemporaryDirectory() as tmpdir:
            vfile = os.path.join(tmpdir, "version.json")
            with open(vfile, "w") as f:
                json.dump({"version": "2.1.3"}, f)
            ver = manager.get_current_version(tmpdir)
            assert str(ver) == "2.1.3"

    def test_get_current_version_no_file(self, manager):
        with tempfile.TemporaryDirectory() as tmpdir:
            ver = manager.get_current_version(tmpdir)
            assert str(ver) == "0.1.0"

    def test_write_version_file(self, manager):
        with tempfile.TemporaryDirectory() as tmpdir:
            ver = VersionInfo(3, 2, 1)
            path = manager.write_version_file(tmpdir, ver)
            with open(path) as f:
                data = json.load(f)
            assert data["version"] == "3.2.1"

    def test_determine_bump(self, manager):
        assert manager.determine_bump(CommitType.FEAT) == "minor"
        assert manager.determine_bump(CommitType.FIX) == "patch"
        assert manager.determine_bump(CommitType.DOCS) is None
        assert manager.determine_bump(CommitType.RELEASE) == "major"

    def test_calculate_next_version_major(self, manager):
        current = VersionInfo(1, 2, 3)
        next_ver = manager.calculate_next_version(current, "major")
        assert str(next_ver) == "2.0.0"

    def test_calculate_next_version_minor(self, manager):
        current = VersionInfo(1, 2, 3)
        next_ver = manager.calculate_next_version(current, "minor")
        assert str(next_ver) == "1.3.0"

    def test_calculate_next_version_patch(self, manager):
        current = VersionInfo(1, 2, 3)
        next_ver = manager.calculate_next_version(current, "patch")
        assert str(next_ver) == "1.2.4"

    def test_calculate_next_version_none(self, manager):
        current = VersionInfo(1, 2, 3)
        next_ver = manager.calculate_next_version(current, None)
        assert str(next_ver) == "1.2.3"

    @pytest.mark.parametrize("ver_str,expected", [
        ("1.0.0", True),
        ("0.0.1", True),
        ("999.999.999", True),
        ("1.0", False),
        ("v1.0.0", False),
        ("1.0.0-beta", False),
        ("", False),
    ])
    def test_is_valid_version(self, manager, ver_str, expected):
        assert manager.is_valid_version(ver_str) == expected
