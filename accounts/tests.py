from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model


class AccountRegisterViewTest(TestCase):

    def test_register_post(self):
        response = self.client.post(reverse('register'), {
            'username': 'newuser',
            'password1': 'password123',
            'password2': 'password123',
            'email': 'newuser@example.com'
        })
        self.assertRedirects(response, reverse('login'))


class AccountLoginViewTest(TestCase):

    def test_login_post(self):
        user = get_user_model().objects.create_user(username='testuser', password='password123')
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'password123'
        })
        self.assertRedirects(response, reverse('home'))
