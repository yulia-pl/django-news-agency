from django.test import TestCase

from django.urls import reverse


# Test case for listing newspapers
class NewspaperListViewTest(TestCase):
    # Test the newspaper list view
    def test_newspaper_list_view(self):
        # Make a GET request to the newspaper list view
        response = self.client.get(reverse("newspaper-list"))

        # Check if the status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check if the response contains the text 'Newspaper List'
        self.assertContains(response, "Newspaper List")


# Test case for creating a new newspaper
class NewspaperCreateViewTest(TestCase):
    # Test the newspaper create view
    def test_newspaper_create_view(self):
        # Make a GET request to the newspaper create view
        response = self.client.get(reverse("newspaper-create"))

        # Check if the status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check if the correct template is used for the response
        self.assertTemplateUsed(response, "newspapers/newspaper_form.html")
