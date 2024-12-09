from django.contrib import admin
from accounts.models import Redactor
from .models import Topic, Newspaper

admin.site.register(Topic)
admin.site.register(Newspaper)
admin.site.register(Redactor)
