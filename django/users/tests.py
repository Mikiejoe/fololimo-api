from django.test import TestCase
from rest_framework.test import APITestCase
from .models import User
from django.urls import reverse
from rest_framework.authtoken.models import Token
from rest_framework import status


class UsersTestCase(TestCase):
    def test_create_user(self):
        user = User.objects.create_user(
            username="testuser",
            email="test@user.com",
            password="textMe@325",
        )
        user.save()

    def test_create_superuser(self):
        # Implement this test
        pass


class UserApiTestCase(APITestCase):
    def setUp(self) -> None:
        self.user = User.objects.create_user(
            username="testuser",
            email="test@user.com",
            password="textMe@325",
        )
        data = {
            "username": "testuser",
            "email": "test@user.com",
            "password": "textMe@325",
        }
        url = reverse("rest_login")

        self.res = self.client.post(url, data)
        self.token = Token.objects.get(user=self.user)

    def test_login(self):
        self.assertEqual(self.res.status_code, status.HTTP_200_OK)

    def test_register(self):
        data = {
            "username": "testuser2",
            "email": "test@user2.com",
            "password1": "textMe@325",
            "password2": "textMe@325",
        }
        url = reverse("rest_register")

        res = self.client.post(url, data)
        print(res)
        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)

    def test_the_right_token_is_returned(self):
        self.assertEqual(self.res.json()["key"], self.token.key)

    def test_user_email_must_be_unique(self):
        #  Implement this test
        pass
