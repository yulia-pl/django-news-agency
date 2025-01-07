from django.test import TestCase

from django.urls import reverse


class AccountRegisterViewTest(TestCase):
    # Test case for registering a new user via POST request
    def test_register_post(self):
        response = self.client.post(reverse("register"), {
            "username": "newuser",
            "password1": "password123",
            "password2": "password123",
            "email": "newuser@example.com"
        })
        # Check if the response redirects to the login page after successful registration
        self.assertRedirects(response, reverse("login"))


class AccountLoginViewTest(TestCase):
    # Test case for logging in with an existing user via POST request
    def test_login_post(self):
        response = self.client.post(reverse("login"), {
            "username": "testuser",
            "password": "password123"
        })
        # Check if the response redirects to the home page after successful login
        self.assertRedirects(response, reverse("home"))
