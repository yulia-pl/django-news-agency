from django.conf import settings

from django.db import models

from django.contrib.auth.models import User


# Model for storing information about topics
class Topic(models.Model):
    # Field for the topic's name
    name = models.CharField(max_length=100)

    # String representation of the Topic model
    def __str__(self):
        return self.name


# Model for storing information about newspapers
class Newspaper(models.Model):
    # Field for the newspaper's title
    title = models.CharField(max_length=200)

    # Field for the newspaper's content
    content = models.TextField()

    # Field for the published date of the newspaper
    published_date = models.DateField()

    # Foreign key to associate each newspaper with a topic
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)

    # Many-to-many relationship to assign publishers (users) to each newspaper
    publishers = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                        related_name="newspapers_publishers")

    # String representation of the Newspaper model
    def __str__(self):
        return self.title
