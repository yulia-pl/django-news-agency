from django.urls import path

from . import views


urlpatterns = [
    # URL for login view
    path("login/", views.AccountLoginView.as_view(), name="login"),

    # URL for logout view
    path("logout/", views.AccountLogoutView.as_view(), name="logout"),

    # URL for user registration view
    path("register/", views.AccountRegisterView.as_view(), name="register"),

    # URL for user profile view (changed to plural as per the requirement)
    path("profiles/", views.AccountDetailView.as_view(), name="profile"),

    # URL for editing user profile (changed to plural as per the requirement)
    path("profiles/edit/", views.AccountUpdateView.as_view(), name="edit_profile"),
]
