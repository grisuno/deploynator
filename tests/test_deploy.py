import os
import tempfile

import pytest

from deploynator._config import Config
from deploynator._deploy import ProjectDiscovery
from deploynator._models import Platform, PlatformConfig, ProjectConfig


class TestProjectDiscovery:
    @pytest.fixture
    def discovery(self):
        config = Config.create()
        return ProjectDiscovery(config)

    def test_discover_empty_dir(self, discovery):
        with tempfile.TemporaryDirectory() as tmpdir:
            projects = discovery.discover(tmpdir)
            assert projects == []

    def test_discover_single_yaml(self, discovery):
        with tempfile.TemporaryDirectory() as tmpdir:
            projects_dir = os.path.join(tmpdir, "projects")
            os.makedirs(projects_dir)
            yaml_path = os.path.join(projects_dir, "test.yaml")
            with open(yaml_path, "w") as f:
                f.write("name: test-proj\nplatforms:\n  github:\n    repo: user/repo\n")
            projects = discovery.discover(tmpdir)
            assert len(projects) == 1
            assert projects[0].name == "test-proj"

    def test_discover_multiple_yamls(self, discovery):
        with tempfile.TemporaryDirectory() as tmpdir:
            pd = os.path.join(tmpdir, "projects")
            os.makedirs(pd)
            for name in ["a.yaml", "b.yaml", "c.yaml"]:
                with open(os.path.join(pd, name), "w") as f:
                    f.write(f"name: {name.replace('.yaml', '')}\nplatforms:\n  github:\n    repo: user/repo\n")
            projects = discovery.discover(tmpdir)
            assert len(projects) == 3

    def test_discover_ignores_non_yaml(self, discovery):
        with tempfile.TemporaryDirectory() as tmpdir:
            pd = os.path.join(tmpdir, "projects")
            os.makedirs(pd)
            with open(os.path.join(pd, "test.yaml"), "w") as f:
                f.write("name: real-proj\n")
            with open(os.path.join(pd, "notes.txt"), "w") as f:
                f.write("not a project")
            projects = discovery.discover(tmpdir)
            assert len(projects) == 1

    def test_find_by_name(self, discovery):
        with tempfile.TemporaryDirectory() as tmpdir:
            pd = os.path.join(tmpdir, "projects")
            os.makedirs(pd)
            with open(os.path.join(pd, "myapp.yaml"), "w") as f:
                f.write("name: myapp\nplatforms:\n  github:\n    repo: user/myapp\n")
            project = discovery.find_by_name("myapp", tmpdir)
            assert project is not None
            assert project.name == "myapp"
            assert discovery.find_by_name("nonexistent", tmpdir) is None

    def test_load_single_from_deploynator_yaml(self, discovery):
        with tempfile.TemporaryDirectory() as tmpdir:
            yaml_path = os.path.join(tmpdir, "deploynator.yaml")
            with open(yaml_path, "w") as f:
                f.write("name: root-proj\nplatforms:\n  github:\n    repo: user/root\n")
            project = ProjectDiscovery._load_single(yaml_path)
            assert project.name == "root-proj"

    def test_load_single_invalid(self, discovery):
        with tempfile.TemporaryDirectory() as tmpdir:
            yaml_path = os.path.join(tmpdir, "bad.yaml")
            with open(yaml_path, "w") as f:
                f.write("description: no name field\n")
            with pytest.raises((ValueError, KeyError)):
                ProjectDiscovery._load_single(yaml_path)


class TestDeployOrchestrator:
    def test_install_dependencies_file_not_found(self):
        from deploynator._deploy import DeployOrchestrator
        config = Config.create()
        orch = DeployOrchestrator(config)

        project = ProjectConfig(
            name="test",
            platforms=[
                PlatformConfig(platform=Platform.GITHUB, repo="user/test", enabled=True),
                PlatformConfig(platform=Platform.GITLAB, repo="user/test", enabled=True),
            ],
        )
        deps = orch.install_dependencies(project)
        assert "github" in deps
        assert isinstance(deps["github"], bool)
