from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase

from drive.users.tests.factories import UserFactory

User = get_user_model()


class ObtainTokenAPITestCase(APITestCase):
    def setUp(self) -> None:
        self.user = User.objects.create_user(
            email="user1@example.com", password="somethinghard2no"
        )
        self.url = "/api/token/"

    def test_token_api(self):
        resp = self.client.post(
            self.url, {"email": "user1@example.com", "password": "somethinghard2no"}
        )
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertIn("access", resp.data)


class UsersAPITestCase(APITestCase):
    def setUp(self) -> None:
        self.url = "/api/v1/users/"

    def test_user_can_signup(self):
        data = {
            "email": "ragner@example.com",
            "password": "somethinghard2no",
        }
        resp = self.client.post(self.url, data)
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
        user = User.objects.get(email="ragner@example.com")
        self.assertEqual(user.email, data["email"])
