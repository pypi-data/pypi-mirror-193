# Copyright 2016 to 2021, Cisco Systems, Inc., all rights reserved.

import unittest
import mock
import subprocess

from yangsuite.apps import YSAppConfig, _YangsuiteConfig
from yangsuite import plugins


class FakeEntryPoint(object):
    class FakeDistribution(object):
        def __init__(self, project_name, version):
            self.project_name = project_name
            self.version = version

    def __init__(self, project_name, version, appconfig):
        self.dist = self.FakeDistribution(project_name, version)
        self.app_config = appconfig

    def load(self):
        return self.app_config


class FakeAppConfig(YSAppConfig):
    name = "ysfakeapp"
    verbose_name = "a fake plugin"


@mock.patch(
    "yangsuite.plugins.iter_entry_points",
    return_value=[
        FakeEntryPoint("yangsuite", "2.0.0", _YangsuiteConfig),
        FakeEntryPoint("yangsuite-fake-app", "1.2.3", FakeAppConfig),
    ],
)
@mock.patch(
    "yangsuite.plugins.subprocess.check_output",
    side_effect=[
        # pip config list
        """\
global.foobar='ignoreme'
global.extra-index-url='https://engci-maven.cisco.com/.../simple'
""",
        # pip search -i INDEX_URL yangsuite
        """\
extraneous-package (1.5.dev3)             - package that mentions yangsuite?
  INSTALLED: 1.0
  LATEST:    1.5.dev3
yangsuite (22.22.22)                      - YANG Suite core application
  INSTALLED: 2.0.0
  LATEST:    22.22.22
yangsuite-fake-app (1.2.3)                - a putative yangsuite plugin
  INSTALLED: 1.2.3 (latest)
""",
    ],
)
class TestPlugins(unittest.TestCase):
    """Test the plugins infrastructure"""

    def setUp(self):
        """Pre-test setup."""
        self.maxDiff = None

    def test_get_plugin_versions(self, mock_co, *args):
        """Verify get_plugin_versions() reports YANG Suite + app template."""
        self.assertEqual(
            [
                {
                    "package_name": "yangsuite",
                    "module_name": "yangsuite",
                    "verbose_name": _YangsuiteConfig.verbose_name,
                    "installed_version": "2.0.0",
                    "error_message": "",
                },
                {
                    "package_name": "yangsuite-fake-app",
                    "module_name": "(unknown)",
                    "verbose_name": "(unknown)",
                    "installed_version": "1.2.3",
                    "error_message": "No installed app with label 'ysfakeapp'."
                },
            ],
            plugins.get_plugin_versions(),
        )

    def test_get_plugin_public_versions(self, mock_co, *args):
        """Check latest public version from pypi.org."""
        revs = plugins.check_public_versions()
        self.assertGreater(
            len(revs),
            0,
            "Could not retrieve any yangsuite package public versions",
        )
        # Right now, latest version is 2.9.4 so it should be >= that
        latest_yangsuite_ver = "2.9.4"
        yangsuite_entry = list(
            filter(lambda x: x["package_name"] == "yangsuite", revs)
        )
        yangsuite_version_pypi = yangsuite_entry[0]["latest_version"]
        self.assertGreaterEqual(
            yangsuite_version_pypi,
            latest_yangsuite_ver,
            f"Latest public version {yangsuite_version_pypi}"
            + "is not equal or higer than {latest_yangsuite_ver}",
        )

    def test_check_for_plugin_updates(self, mock_co, *args):
        updates = plugins.check_for_plugin_updates()
        core_apps = [
            "yangsuite",
            "yangsuite-devices",
            "yangsuite-filemanager",
            "yangsuite-netconf",
            "yangsuite-yangtree",
        ]
        for p in updates:
            self.assertIn("description", p)
            self.assertIn("latest_version", p)
            self.assertIn("package_name", p)
            if p["package_name"] in core_apps:
                core_apps.remove(p["package_name"])
        self.assertEqual(core_apps, [])

    def test_update_plugins(self, mock_co, *args):
        """Exercise the update_plugins() API."""

        def mock_update_ys_database():
            pass

        plugins.update_ys_database = mock_update_ys_database
        mock_co.side_effect = [
            # Successful update
            """\
Installing collected packages: yangsuite-foo
  Found existing installation: yangsuite-foo 100.200.300.post0.dev10
    Uninstalling yangsuite-foo 100.200.300.post0.dev10:
      Successfully uninstalled yangsuite-foo 100.200.300.post0.dev10
Successfully installed yangsuite-foo 1000.0
""",
            # No update needed
            """Requirement already up-to-date: yangsuite-foo in ...""",
            # Update error
            subprocess.CalledProcessError(cmd="", returncode=1, output=""),
        ]
        # self.assertEqual(
        #     {'message': 'You will need to refresh the browser for
        # these changes to take effect.',  # noqa
        #     'plugins': {'yangsuite-foo': 'updated'}},
        #     plugins.update_plugins([{'plugin': 'yangsuite-foo',
        #                              'version': "1000.0"}])
        # )
        plugins.update_plugins(
            [{"plugin": "yangsuite-foo", "version": "1000.0"}]
        )
        mock_co.assert_called_with(
            [
                "pip",
                "install",
                "--no-cache",
                "--upgrade",
                "--extra-index-url",
                "https://engci-maven.cisco.com/artifactory"
                "/api/pypi/yang-suite-dev-pypi/simple",
                "yangsuite-foo==1000.0",
            ],
            stderr=None,
        )

        self.assertEqual(
            {
                "message": "Check YANG Suite logs for details.",
                "plugins": {
                    "yangsuite-bar": "unchanged",
                    "yangsuite-foo": "unchanged",
                },
            },
            plugins.update_plugins(
                [
                    {"plugin": "yangsuite-foo", "version": "1000.0"},
                    {"plugin": "yangsuite-bar"},
                ]
            ),
        )
        mock_co.assert_called_with(
            [
                "pip",
                "install",
                "--no-cache",
                "--upgrade",
                "--extra-index-url",
                "https://engci-maven.cisco.com/artifactory"
                "/api/pypi/yang-suite-dev-pypi/simple",
                "yangsuite-foo==1000.0",
                "yangsuite-bar",
            ],
            stderr=None,
        )

        self.assertEqual(
            {
                "message": "Check YANG Suite logs for details.",
                "plugins": {
                    "yangsuite-bar": "failed",
                    "yangsuite-foo": "failed",
                },
            },
            plugins.update_plugins(
                [
                    {"plugin": "yangsuite-foo", "version": "1000.0"},
                    {"plugin": "yangsuite-bar"},
                ]
            ),
        )
