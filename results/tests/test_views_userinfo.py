import json

from django.contrib.auth.models import User
from django.urls import reverse
from django.test import RequestFactory, TestCase
from rest_framework import status


class UserInfoTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.url = reverse('current-user')

    def test_userinfo_access_object_without_user(self):
        data = {
            'is_authenticated': False,
            'is_superuser': False,
            'is_staff': False,
            'first_name': '',
            'last_name': '',
            'email': ''
        }
        response = self.client.get(self.url, follow=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.content.decode(), json.dumps(data))

    def _test_userinfo_access(self, user):
        data = {
            'is_authenticated': True,
            'is_superuser': user.is_superuser,
            'is_staff': user.is_staff,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email
        }
        self.client.force_login(user)
        response = self.client.get(self.url, follow=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.content.decode(), json.dumps(data))

    def test_userinfo_access_object_with_normal_user(self):
        user = User.objects.create(username='tester', first_name="Testname")
        self._test_userinfo_access(user)

    def test_userinfo_access_object_with_superuser(self):
        user = User.objects.create(username="superuser", is_superuser=True, email='admin@example.org')
        self._test_userinfo_access(user)
