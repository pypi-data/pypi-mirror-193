# Copyright 2016 to 2021, Cisco Systems, Inc., all rights reserved.

"""
Auto user registration tests
"""
import re

from django.test import TestCase, override_settings
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.template.loader import render_to_string
from django.core import mail

User = get_user_model()

# List of templates to be used in the registration workflow
REG_APP = 'django_registration'
REG_FORM = '{0}/registration_form.html'.format(REG_APP)
REG_CLOSED = '{0}/registration_closed.html'.format(REG_APP)
REG_COMPLETE = '{0}/registration_complete.html'.format(REG_APP)
ACT_COMPLETE = '{0}/activation_complete.html'.format(REG_APP)
ACT_FAILED = '{0}/activation_failed.html'.format(REG_APP)
ACT_EMAIL_SUB = '{0}/activation_email_subject.txt'.format(REG_APP)

# Settings defaults
DEFAULT_EMAIL_DOMAIN = 'cisco.com'
TEST_USERNAME = 'ys-user'
ADMIN_EMAIL = 'admin@cisco.com'
DEFAULT_GROUP = 'ys-users'


@override_settings(
    ACCOUNT_ACTIVATION_DAYS=7,
    REGISTRATION_OPEN=True,
    REGISTRATION_EMAIL_DOMAIN='cisco.com',
    ADMIN_EMAIL=ADMIN_EMAIL,
    REGISTRATION_INFORM_ADMIN=True,
    REGISTRATION_USER_GROUPS=[DEFAULT_GROUP]
)
class RegistrationTests(TestCase):
    def setUp(self):
        # Create a group to add users to
        self.group = Group(name=DEFAULT_GROUP)
        self.group.save()

    def test_registration_get(self):
        """Check if the user gets the correct registration  page"""
        resp = self.client.get(reverse('ys_user_register'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, REG_FORM)

    @override_settings(REGISTRATION_OPEN=False)
    def test_registration_closed(self):
        """Check if the correct template is used when registration is closed"""
        resp = self.client.get(reverse('ys_user_register'), follow=True)
        self.assertRedirects(resp, reverse('django_registration_disallowed'))
        self.assertTemplateUsed(resp, REG_CLOSED)

    def _test_activation_email_sent(self, email):
        """Common function to test if an activation email is sent to 'email'"""
        self.assertEqual(len(mail.outbox), 1)
        expected_subject = render_to_string(
            template_name=ACT_EMAIL_SUB).strip()
        self.assertEqual(mail.outbox[0].subject, expected_subject)

        # crude way to check if an activation key is sent to the user
        # Look for http(s) link
        self.assertTrue('http' in mail.outbox[0].body)

        # Are we sending to the right recepient?
        self.assertEqual(mail.outbox[0].to[0], email)

    def _test_activation_email_not_sent(self):
        self.assertEqual(len(mail.outbox), 0)

    def _test_register_success(self, response):
        self.assertRedirects(response, reverse('django_registration_complete'))
        self.assertTemplateUsed(response, REG_COMPLETE)

    def _test_register_failure(self, response):
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, REG_FORM)
        self.assertFalse(response.context['form'].is_valid())

    def test_registration_with_email_domain(self):
        """Check if the registration works with email domain fixed"""
        data = {
            'username': TEST_USERNAME,
            'password1': 'YangSuiteRocks',
            'password2': 'YangSuiteRocks',
        }
        resp = self.client.post(reverse('ys_user_register'), data=data,
                                follow=True)
        self._test_register_success(resp)

        # Check if the user is created
        new_user = User.objects.get(username=data['username'])
        self.assertTrue(new_user.check_password(data['password1']))

        user_email = "{0}@{1}".format(data['username'], DEFAULT_EMAIL_DOMAIN)

        # Check if an inactive user account has been created
        self.assertEqual(new_user.email, user_email)
        self.assertFalse(new_user.is_active)

        # Check if the activation email is sent
        self._test_activation_email_sent(user_email)

    def test_registration_with_email_domain_failure(self):
        """Check if the registration with email domain fails for bad data"""
        data = {
            'username': TEST_USERNAME,
            'password1': 'YangSuiteRocks',
            'password2': 'YangSuiteOnRocks',
        }
        resp = self.client.post(reverse('ys_user_register'), data=data,
                                follow=True)
        self._test_register_failure(resp)

        # Check if the user is NOT created
        self.assertFalse(bool(User.objects.filter(username=data['username'])))

        # Check if the activation email is NOT sent
        self._test_activation_email_not_sent()

    @override_settings(REGISTRATION_EMAIL_DOMAIN=None)
    def test_registration_without_email_domain(self):
        """Check if the registration works without email domain fixed"""
        data = {
            'username': TEST_USERNAME,
            'email': 'ys-user@domain.com',
            'password1': 'YangSuiteRocks',
            'password2': 'YangSuiteRocks',
        }
        resp = self.client.post(reverse('ys_user_register'), data=data,
                                follow=True)
        self.assertRedirects(resp, reverse('django_registration_complete'))
        self.assertTemplateUsed(resp, REG_COMPLETE)

        # Check if the user is created
        new_user = User.objects.get(username=data['username'])
        self.assertTrue(new_user.check_password(data['password1']))

        # Check if an inactive user account has been created
        self.assertEqual(new_user.email, data['email'])
        self.assertFalse(new_user.is_active)

        # Check if the activation email is sent
        self._test_activation_email_sent(data['email'])

    @override_settings(REGISTRATION_EMAIL_DOMAIN=None)
    def test_registration_without_email_domain_failure(self):
        """Check if the registration without email domain fixed fails for
        bad data
        """
        data = {
            'username': TEST_USERNAME,
            'email': 'ys-user@domain.com',
            'password1': 'YangSuiteRocks',
            'password2': 'YangSuiteOnRocks',
        }
        resp = self.client.post(reverse('ys_user_register'), data=data,
                                follow=True)
        self._test_register_failure(resp)

        # Check if the user is NOT created
        self.assertFalse(bool(User.objects.filter(username=data['username'])))

        # Check if the activation email is NOT sent
        self._test_activation_email_not_sent()

    def test_account_activation(self):
        """Check if an account is activated on clicking the activation link"""
        # Run the registration process to extract the activation link
        self.test_registration_with_email_domain()

        match = re.search(r'/accounts/activate/.*$', mail.outbox[0].body,
                          re.MULTILINE)
        activation_link = match.group().strip()

        resp = self.client.get(activation_link, follow=True)
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, ACT_COMPLETE)

        # Make sure the account is active
        new_user = User.objects.get(username=TEST_USERNAME)
        self.assertTrue(new_user.is_active)

        # Check if user is added to the requested group
        self.assertTrue(new_user.groups.filter(name=DEFAULT_GROUP).exists())

    def test_bad_activation_link(self):
        """Check if an error is thrown when a bad activation link is clicked"""
        resp = self.client.get("/accounts/activate/bad_activation_code/",
                               follow=True)
        self.assertTemplateUsed(resp, ACT_FAILED)

    def test_inform_admin(self):
        """Check if an email is sent to admin on user activation"""
        self.test_account_activation()
        # There should be 2 emails, we pop the last one to check if admin
        # is informed
        self.assertEqual(len(mail.outbox), 2)
        self.assertEqual(mail.outbox[1].to[0], ADMIN_EMAIL)

    @override_settings(REGISTRATION_INFORM_ADMIN=False)
    def test_skip_inform_admin(self):
        """Check if no email is sent to admin when not requested"""
        self.test_account_activation()
        self.assertEqual(len(mail.outbox), 1)
