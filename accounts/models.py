from django.contrib.auth.models import AbstractUser

from django.db import models


# Redactor model, inheriting from AbstractUser
class Redactor(AbstractUser):
    # Field to store the years of experience of the redactor
    years_of_experience = models.PositiveIntegerField(null=True, blank=True)

    # Many-to-many relationship with the Group model to assign groups to the redactor
    groups = models.ManyToManyField(
        "auth.Group",
        related_name="accounts_redactors",
        blank=True,
        help_text="The groups this user belongs to."
    )

    # Many-to-many relationship with the Permission model
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="accounts_redactor_permissions",
        blank=True,
        help_text="Specific permissions for this user."
    )

    # String representation of the Redactor model, returns the username
    def __str__(self):
        return self.username
