import unittest
import requests
from yangsuite import plugins


class TestPublicVersions(unittest.TestCase):

    def test_filtered_pre_releases(self):
        """Pre-release should not be reported for latest version."""
        releases = plugins.check_public_versions()
        for rel in releases:
            self.assertNotIn('.post', rel['latest_version'])

    def test_filtered_yanked_releases(self):
        """Pre-release should not be reported for latest version."""
        releases = plugins.check_public_versions()
        sess = requests.Session()
        sess.headers.update({'Accept': 'application/json'})
        for rel in releases:
            yanked = []
            resp = sess.get(
                "https://pypi.org/pypi/{0}/json".format(rel['package_name']),
                verify=False
            )
            if resp.ok:
                for release, data in resp.json()['releases'].items():
                    yanked = [y for y in data if y['yanked'] is True]
                    if yanked:
                        self.assertNotEqual(rel['latest_version'], release)
