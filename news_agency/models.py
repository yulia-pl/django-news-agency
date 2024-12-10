from django.db import models
from django.conf import settings

class Topic(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Newspaper(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateField()
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    publishers = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='news_agency_publishers'  # Унікальне ім'я для зворотного зв'язку
    )

    def __str__(self):
        return self.title
