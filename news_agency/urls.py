from django.contrib import admin
from django.urls import path, include
from newspapers.views import HomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('editors/', include('editors.urls')),
    path('newspapers/', include('newspapers.urls')),
    path('', HomeView.as_view(), name='home'),
]
