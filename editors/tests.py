from django.test import TestCase
from django.urls import reverse
from .models import Redactor

class RedactorListViewTest(TestCase):
    def test_redactor_list_view(self):
        response = self.client.get(reverse('redactor-list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Editor List')


class RedactorCreateViewTest(TestCase):
    def test_redactor_create_view(self):
        response = self.client.get(reverse('redactor-create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'editors/redactor_form.html')

    def test_redactor_create_post(self):
        response = self.client.post(reverse('redactor-create'), {
            'username': 'newuser',
            'first_name': 'Alice',
            'last_name': 'Smith',
            'years_of_experience': 3,
        })
        self.assertRedirects(response, reverse('redactor-list'))
        self.assertTrue(Redactor.objects.filter(username='newuser').exists())
