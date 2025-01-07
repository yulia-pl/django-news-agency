from django.test import TestCase

from django.urls import reverse

from .models import Redactor


class RedactorListViewTest(TestCase):
    # Test case for the Redactor list view
    def test_redactor_list_view(self):
        # Send a GET request to the redactor list page
        response = self.client.get(reverse("redactor-list"))
        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)
        # Check if the page contains the text 'Editor List'
        self.assertContains(response, "Editor List")


class RedactorCreateViewTest(TestCase):
    # Test case for the Redactor create view
    def test_redactor_create_view(self):
        # Send a GET request to the redactor create page
        response = self.client.get(reverse("redactor-create"))
        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)
        # Check if the correct template is used
        self.assertTemplateUsed(response, "editors/redactor_form.html")

    def test_redactor_create_post(self):
        # Send a POST request to create a new redactor
        response = self.client.post(reverse("redactor-create"), {
            "username": "newuser",
            "first_name": "Alice",
            "last_name": "Smith",
            "years_of_experience": 3,
        })
        # Check if the response redirects to the redactor list page
        self.assertRedirects(response, reverse("redactor-list"))
        # Check if the new redactor has been created
        self.assertTrue(Redactor.objects.filter(username="newuser").exists())
