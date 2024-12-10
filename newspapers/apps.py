from django.apps import AppConfig


# Configuration for the Newspapers app
class NewspapersConfig(AppConfig):
    # The default field type for auto-generated primary keys in the app
    default_auto_field = "django.db.models.BigAutoField"

    # The name of the app
    name = "newspapers"
