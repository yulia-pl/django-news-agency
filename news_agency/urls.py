from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('newspapers/', include('newspapers.urls')),
    path('editors/', include('editors.urls')),
    path('accounts/', include('accounts.urls')),
]
