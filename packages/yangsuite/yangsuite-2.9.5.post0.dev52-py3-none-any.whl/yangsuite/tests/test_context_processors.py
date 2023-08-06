# Copyright 2016 to 2021, Cisco Systems, Inc., all rights reserved.

import unittest
import mock

from yangsuite.apps import YSAppConfig, _YangsuiteConfig
import yangsuite.context_processors as ycp
from yangsuite.context_processors import (
    _build_url, yangsuite_menus, YSMenuItem
)


class TestYangsuiteContextProcessors(unittest.TestCase):
    """Tests for the YANG Suite context_processors module."""

    def test_build_url(self):
        """Make sure the _build_url function constructs appropriate URLs."""
        # We must be tolerant of variant inputs
        for prefix, suffix in [
                ('plugin', 'action'),
                ('/plugin', 'action'),
                ('/plugin', '/action'),
                ('plugin', '/action'),
                ('plugin/action', ''),
                ('', 'plugin/action'),
                ('/plugin/action', ''),
                ('', '/plugin/action'),
                ('/plugin/', '/action'),
                ('/plugin/', 'action'),
        ]:
            self.assertEqual('/plugin/action', _build_url(prefix, suffix),
                             "bad input: ({0}, {1})".format(prefix, suffix))

    @mock.patch('yangsuite.context_processors.apps')
    def test_yangsuite_menus_order_stable(self, mock_apps):
        """Make sure the order of menus and menu items is stable."""
        # Create our own AppConfig instances so we can mock out get_app_configs
        class MockYS(_YangsuiteConfig):
            """Mockup of yangsuite core app."""
            path = "/path/to/yangsuite"

        ys = MockYS('yangsuite', None)

        class MockFM(YSAppConfig):
            """Mockup of yangsuite-filemanager."""
            path = '/path/to/ysfilemanager'
            url_prefix = 'filemanager'
            menus = {
                'Setup': [
                    ('YANG files and repositories', 'repository/manage/'),
                    ('YANG module sets', 'yangsets/manage/'),
                ],
            }

        ysfm = MockFM('ysfilemanager', None)

        class MockD(YSAppConfig):
            """Mockup of yangsuite-devices."""
            path = '/path/to/ysdevices'
            url_prefix = 'devices'
            menus = {
                'Setup': [
                    ('Device profiles', 'devprofile'),
                ],
            }

        ysd = MockD('ysdevices', None)

        class MockYT(YSAppConfig):
            """Mockup of yangsuite-yangtree."""
            path = '/path/to/ysyangtree'
            url_prefix = 'yangtree'
            menus = {
                'Operations': [
                    ('Explore YANG', 'explore'),
                ],
            }

        ysyt = MockYT('ysyangtree', None)

        class App1(YSAppConfig):
            path = '/path/to/app1'
            url_prefix = 'app1'
            menus = {'Accelerate': [('first', 'first'), ('second', 'second')],
                     'z_app1menu': [('last', 'last')]}

        class App2(YSAppConfig):
            path = '/path/to/app2'
            url_prefix = 'app2'
            menus = {'sharedmenu': [('yeah, app2 was here', 'app2')]}

        class App3(YSAppConfig):
            path = '/path/to/app3'
            url_prefix = 'app3'
            menus = {'sharedmenu': [('also, app3 was here', 'app3')],
                     'Setup': [('hello from app3', 'app3')]}

        class BadApp(YSAppConfig):
            path = '/path/to/badapp'
            # No url_prefix, whoops!
            menus = {'badapp': [('badapp', 'badapp')]}

        self.maxDiff = None

        def get_one(name, *args, **kwargs):
            """Function mock for get_app_config()."""
            return [x for x in mock_apps.get_app_configs()
                    if x.name == name][0]

        mock_apps.get_app_config.side_effect = get_one

        app1 = App1('app1', None)
        app2 = App2('app2', None)
        app3 = App3('app3', None)
        badapp = BadApp('badapp', None)

        # Regardless of the order in which the apps are discovered,
        # we want the menus to come out the same.
        for app_ordering in [
                (ys, ysfm, ysd, ysyt, app1, app2, app3),
                (badapp, app3, app2, app1, ysyt, ysd, ysfm, ys),
                (app1, ysyt, app2, badapp, app3, ysd, ys, ysfm),
        ]:
            with self.subTest(app_ordering=[ac.name for ac in app_ordering]):
                mock_apps.get_app_configs.return_value = app_ordering
                ycp._yangsuite_menus.clear()
                menus = yangsuite_menus(None)['yangsuite_menus']
                mock_apps.get_app_configs.assert_called()
                mock_apps.get_app_config.assert_called()

                # First three are *always* Admin, Setup, Operations in order
                # Remaining menus are *always* alphabetized
                self.assertEqual([
                    'Admin', 'Setup', 'Operations',
                    'Accelerate', 'sharedmenu', 'z_app1menu',
                ], list(menus.keys()))

                # Menu items actually built from yangsuite.apps
                self.assertEqual([
                    YSMenuItem('Manage users', '/admin'),
                    YSMenuItem('Manage plugins', '/yangsuite/plugins/'),
                    YSMenuItem('View logs', '/yangsuite/logs'),
                ], menus['Admin'])

                # Menu items from our core app mocks + extra app mocks
                # ysfilemanager is before ysevices is before noncore apps
                self.assertEqual([
                    YSMenuItem('YANG files and repositories',
                               '/filemanager/repository/manage/'),
                    YSMenuItem('YANG module sets',
                               '/filemanager/yangsets/manage/'),
                    YSMenuItem('Device profiles', '/devices/devprofile'),
                    YSMenuItem('--', None),    # core vs. noncore separator
                    YSMenuItem('hello from app3', '/app3/app3'),
                ], menus['Setup'])
                self.assertEqual([
                    YSMenuItem('Explore YANG', '/yangtree/explore'),
                ], menus['Operations'])
                self.assertEqual([
                    YSMenuItem(text='first', url='/app1/first'),
                    YSMenuItem(text='second', url='/app1/second'),
                ], menus['Accelerate'])
                # app2 is always before app3 due to alphabetical sorting
                self.assertEqual([
                    YSMenuItem(text='yeah, app2 was here', url='/app2/app2'),
                    YSMenuItem(text='also, app3 was here', url='/app3/app3'),
                ], menus['sharedmenu'])
                self.assertEqual([YSMenuItem(text='last', url='/app1/last')],
                                 menus['z_app1menu'])
