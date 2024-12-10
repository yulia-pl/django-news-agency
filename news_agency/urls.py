from django.urls import path, include

urlpatterns = [
    path("accounts/", include("accounts.urls")),  # Include URLs for accounts
    path("editors/", include("editors.urls")),    # Include URLs for editors
    path("newspapers/", include("newspapers.urls")),  # Include URLs for newspapers

    # Home page
    path("", include("newspapers.urls")),
]
