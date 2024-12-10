from django.test import TestCase
from django.urls import reverse
from .models import Newspaper, Topic
from django.contrib.auth.models import User


class NewspaperListViewTest(TestCase):
    def test_newspaper_list_view(self):
        response = self.client.get(reverse('newspaper-list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Newspaper List')


class NewspaperCreateViewTest(TestCase):
    def test_newspaper_create_view(self):
        response = self.client.get(reverse('newspaper-create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'newspapers/newspaper_form.html')
