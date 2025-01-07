from django.contrib.auth.views import LoginView, LogoutView

from django.views.generic import CreateView, DetailView, UpdateView

from django.urls import reverse_lazy

from .forms import UserRegistrationForm

from django.contrib.auth.models import User


class AccountLoginView(LoginView):
    # Login view template
    template_name = "accounts/login.html"


class AccountLogoutView(LogoutView):
    # Logout view with redirection to the home page after logout
    next_page = "home"


class AccountRegisterView(CreateView):
    # User registration view, using the UserRegistrationForm
    form_class = UserRegistrationForm
    template_name = "accounts/register.html"
    success_url = reverse_lazy("login")


class AccountDetailView(DetailView):
    # User detail view, to show the user's profile
    model = User
    template_name = "accounts/profile.html"
    context_object_name = "user"

    def get_queryset(self):
        # Using select_related to optimize the query by fetching the related Redactor model
        return super().get_queryset().select_related("redactor")


class AccountUpdateView(UpdateView):
    # User profile update view
    model = User
    fields = ["username", "email", "first_name", "last_name"]
    template_name = "editors/redactor_form.html"

    def get_object(self, **kwargs):
        # Return the currently logged-in user object for updating
        return self.request.user

    def get_success_url(self):
        # Redirect to the profile page after updating the user information
        return reverse_lazy("profile")
