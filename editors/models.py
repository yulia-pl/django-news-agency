from django.contrib.auth.models import AbstractUser
from django.db import models

class Redactor(AbstractUser):
    years_of_experience = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.username} ({self.years_of_experience} years)"
