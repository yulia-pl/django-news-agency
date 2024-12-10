from django.db import models

from django.conf import settings


class Topic(models.Model):
    # Define the topic with a name field
    name = models.CharField(max_length=100)

    def __str__(self):
        # Return the name of the topic as its string representation
        return self.name


class Newspaper(models.Model):
    # Define the newspaper with title, content, and publication date
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateField()

    # Foreign key relationship with Topic
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)

    # Many-to-many relationship with the users (publishers)
    publishers = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="news_agency_publishers"  # Unique name for the reverse relationship
    )

    def __str__(self):
        # Return the title of the newspaper as its string representation
        return self.title
