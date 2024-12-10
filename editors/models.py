from django.contrib.auth.models import AbstractUser

from django.db import models


class Redactor(AbstractUser):
    # Field to store the years of experience for the Redactor
    years_of_experience = models.PositiveIntegerField(null=True, blank=True)

    # Define unique related_name for fields to avoid conflicts
    groups = models.ManyToManyField(
        "auth.Group",
        related_name="editors_redactors",  # Unique name for this app
        blank=True,
        help_text="The groups this user belongs to."
    )

    # Define unique related_name for user permissions
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="editors_redactor_permissions",  # Unique name for this app
        blank=True,
        help_text="Specific permissions for this user."
    )

    # String representation of the Redactor model, returns the username
    def __str__(self):
        return self.username
