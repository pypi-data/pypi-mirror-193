# Copyright 2016 to 2021, Cisco Systems, Inc., all rights reserved.

from __future__ import unicode_literals

import json
import configparser

from django_webtest import WebTest
from django.test.client import RequestFactory
from django.contrib.auth.models import User
from django.urls import reverse
import yangsuite.views
from yangsuite.application import read_prefs, write_prefs


class TestViewDecorators(WebTest):
    """Test the view decorator functions."""

    def setUp(self):
        self.factory = RequestFactory()

        @yangsuite.views.json_request
        def test_view(request, *args, jsondata=None, **kwargs):
            return jsondata

        self.test_view = test_view

    def test_success_empty(self):
        """View decorator correctly handles case of no request body."""
        request = self.factory.get('/test')
        result = self.test_view(request)
        self.assertEqual({}, result)

    def test_success_with_data(self):
        """View decorator correctly handles JSON data."""
        request = self.factory.post('/test', json.dumps({"foo": "bar"}),
                                    content_type="application/json")
        result = self.test_view(request)
        self.assertEqual({"foo": "bar"}, result)

    def test_success_remove_csrf_token(self):
        """View decorator strips out csrfmiddlewaretoken."""
        request = self.factory.post(
            '/test', json.dumps({
                "param1": "value1",
                "csrfmiddlewaretoken": "7UfbyWvG9TD9djDEgNjZp29Aa6MVtff",
                "param2": "value2",
            }),
            content_type="application/json")
        result = self.test_view(request)
        self.assertEqual({"param1": "value1", "param2": "value2"}, result)

    def test_failure_bad_json(self):
        """View decorator handles malformed JSON"""
        request = self.factory.post("/test", "foo{",
                                    content_type="application/json")
        result = self.test_view(request)
        self.assertEqual(400, result.status_code)
        self.assertEqual("Malformed JSON request", result.reason_phrase)


class TestHelpViews(WebTest):
    """Test the help page views."""

    @classmethod
    def setUpClass(cls):
        # make sure EULA does not get in the way of tests
        cfg = read_prefs()
        prefs = cfg[configparser.DEFAULTSECT]
        prefs['eula_agreement'] = 'accepted'
        write_prefs(cfg)

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        User.objects.create_superuser('admin', 'admin@localhost', 'superadmin')
        User.objects.create_user('user', 'user@localhost', 'ordinaryuser')

    def test_help_access_restriction(self):
        """No user --> login page; logged in --> help index page."""
        self.url = reverse(yangsuite.views.help_view,
                           kwargs={'section': 'yangsuite'})

        resp = self.app.get(self.url)
        self.assertRedirects(resp, '/accounts/login/?next=' + self.url)

        resp = self.app.get(self.url, user='user')
        self.assertTemplateUsed(resp, 'yangsuite/help.html')

        resp = self.app.get(self.url, user='admin')
        self.assertTemplateUsed(resp, 'yangsuite/help.html')

    def test_help_search_access_restriction(self):
        """No user --> login page; logged in --> help search page."""
        self.url = reverse(yangsuite.views.help_search)

        resp = self.app.get(self.url)
        self.assertRedirects(resp, '/accounts/login/?next=' + self.url)

        resp = self.app.get(self.url, user='user')
        self.assertTemplateUsed(resp, 'yangsuite/help_search.html')

        resp = self.app.get(self.url, user='admin')
        self.assertTemplateUsed(resp, 'yangsuite/help_search.html')

    def test_help_view_success(self):
        """Successfully request a specific help page."""
        self.url = reverse(yangsuite.views.help_view,
                           kwargs={'section': 'yangsuite'})
        resp = self.app.get(self.url, user='user')
        self.assertTemplateUsed(resp, 'yangsuite/help.html')

        self.url = reverse(yangsuite.views.help_view,
                           kwargs={'section': 'yangsuite',
                                   'document': 'index'})
        resp = self.app.get(self.url, user='user')
        self.assertTemplateUsed(resp, 'yangsuite/help.html')


class TestLogViews(WebTest):
    """Test the /logs/ views."""

    def setUp(self):
        User.objects.create_superuser('admin', 'admin@localhost', 'superadmin')
        User.objects.create_user('user', 'user@localhost', 'ordinaryuser')

    def test_access_restriction_log_view(self):
        """Only a logged-in admin can get the logs page."""
        url = reverse(yangsuite.views.log_view)

        # If not logged in, get redirected to admin login page
        resp = self.app.get(url)
        self.assertRedirects(resp, '/admin/login/?next=' + url)

        # Same if logged in as non-admin
        resp = self.app.get(url, user='user')
        self.assertRedirects(resp, '/admin/login/?next=' + url)

        # Admin user can get the actual page
        resp = self.app.get(url, user='admin')
        self.assertEqual(200, resp.status_code)
        self.assertTemplateUsed(resp, 'yangsuite/logs.html')

    def test_access_restriction_log_data(self):
        """Only a logged-in admin can get the logs data."""
        url = reverse(yangsuite.views.get_log)

        # If not logged in, get redirected to admin login page
        resp = self.app.get(url)
        self.assertRedirects(resp, '/admin/login/?next=' + url)

        # Same if logged in as non-admin
        resp = self.app.get(url, user='user')
        self.assertRedirects(resp, '/admin/login/?next=' + url)

        # Admin user can get the data
        resp = self.app.get(url, user='admin')
        self.assertEqual(200, resp.status_code)
        self.assertIn('result', resp.json)

    def test_log_page(self):
        """Make sure the logs page submits and gets log data."""
        url = reverse(yangsuite.views.log_view)
        logpage = self.app.get(url, user='admin')
        form = logpage.form
        form['levelname'] = 'DEBUG'
        form['maxlines'] = "10"
        data = form.submit().json
        self.assertIn('result', data)
        # We requested max 10 lines
        self.assertLessEqual(len(data['result']), 10)
        # We should absolutely have *something*
        self.assertGreater(len(data['result']), 0)
        # Each line should have the following keys
        for line in data['result']:
            keys = line.keys()
            for key in ['levelname', 'timestamp', 'message',
                        'name', 'lineno', 'funcName']:
                self.assertIn(key, keys)


class TestPluginViews(WebTest):
    """Test the /plugins/ views."""

    def test_plugin_page(self):
        """Only a logged-in user can check plugins."""
        url = reverse(yangsuite.views.plugins)

        resp = self.app.get(url)
        self.assertRedirects(resp, '/accounts/login/?next=' + url)

        resp = self.app.get(url, user='user')
        self.assertTemplateUsed(resp, 'yangsuite/plugins.html')

    def test_plugins_list(self):
        url = reverse(yangsuite.views.list_plugins)

        resp = self.app.get(url)
        self.assertRedirects(resp, '/accounts/login/?next=' + url)

        resp = self.app.get(url, user='user')
        data = resp.json
        # A few spot checks
        self.assertEqual(['error_message', 'installed_version', 'module_name',
                          'package_name', 'verbose_name'],
                         sorted(data['plugins'][0].keys()))
        self.assertEqual('yangsuite', data['plugins'][0]['package_name'])
        self.assertEqual('yangsuite', data['plugins'][0]['module_name'])


class TestMiddleWare(WebTest):
    """Test the help page views."""

    @classmethod
    def setUpClass(cls):
        cls.urls = [reverse(yangsuite.views.plugins)]
        cls.urls.append(reverse(yangsuite.views.list_plugins))
        cls.urls.append(reverse(yangsuite.views.log_view))
        cls.urls.append(reverse(yangsuite.views.get_log))
        cls.urls.append(reverse(yangsuite.views.help_view,
                        kwargs={'section': 'yangsuite'}))
        cls.urls.append(reverse(yangsuite.views.help_search))
        cls.urls.append(reverse(yangsuite.views.help_view,
                        kwargs={'section': 'yangsuite',
                                'document': 'index'}))

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        User.objects.create_superuser('admin', 'admin@localhost', 'superadmin')

    def tearDown(self):
        cfg = read_prefs()
        prefs = cfg[configparser.DEFAULTSECT]
        prefs['eula_agreement'] = 'accepted'
        write_prefs(cfg)

    def test_eula_not_accepted(self):
        """Test redirect to Cisco EULA if not accepted."""
        cfg = read_prefs()
        prefs = cfg[configparser.DEFAULTSECT]
        prefs['eula_agreement'] = ''
        write_prefs(cfg)
        url = reverse(yangsuite.views.plugins)
        resp = self.app.get(url)
        self.assertRedirects(resp, "/yangsuite/eula/?next=" + url)

    def test_eula_is_accepted(self):
        """Test no redirect to Cisco EULA if it is accepted."""
        url = reverse(yangsuite.views.plugins)
        resp = self.app.get(url)
        self.assertRedirects(resp, '/accounts/login/?next=' + url)
