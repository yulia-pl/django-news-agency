from django.db import models
from editors.models import Redactor

class Topic(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Newspaper(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    published_date = models.DateField()
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name="newspapers")
    publishers = models.ManyToManyField(Redactor, related_name="newspapers")

    def __str__(self):
        return self.title
