from django.contrib import admin

from accounts.models import Redactor

from .models import Topic, Newspaper

# Register the Topic model to appear in the admin site
admin.site.register(Topic)

# Register the Newspaper model to appear in the admin site
admin.site.register(Newspaper)

# Register the Redactor model (from the accounts app) to appear in the admin site
admin.site.register(Redactor)
