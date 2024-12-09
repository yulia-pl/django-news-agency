from django.contrib.auth.models import AbstractUser
from django.db import models

class Redactor(AbstractUser):
    years_of_experience = models.PositiveIntegerField(null=True, blank=True)

    # Задаємо унікальні related_name для полів
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='editors_redactors',  # Унікальне ім'я для цього додатка
        blank=True,
        help_text='The groups this user belongs to.'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='editors_redactor_permissions',  # Унікальне ім'я для цього додатка
        blank=True,
        help_text='Specific permissions for this user.'
    )

    def __str__(self):
        return self.username
