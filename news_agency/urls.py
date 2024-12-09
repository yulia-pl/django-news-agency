from django.urls import path, include

urlpatterns = [
    path('accounts/', include('accounts.urls')),  # Інклюдимо URL для акаунтів
    path('editors/', include('editors.urls')),    # Інклюдимо URL для редакторів
    path('newspapers/', include('newspapers.urls')),  # Інклюдимо URL для газет

    # Головна сторінка
    path('', include('newspapers.urls')),  # Для простоти головна буде по вбудованому додатку
]
