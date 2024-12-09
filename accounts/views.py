from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView, DetailView, UpdateView
from django.urls import reverse_lazy
from .forms import UserRegistrationForm
from django.contrib.auth.models import User


class AccountLoginView(LoginView):
    template_name = 'accounts/login.html'


class AccountLogoutView(LogoutView):
    next_page = 'home'


class AccountRegisterView(CreateView):
    form_class = UserRegistrationForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('login')


class AccountDetailView(DetailView):
    model = User
    template_name = 'accounts/profile.html'
    context_object_name = 'user'


class AccountUpdateView(UpdateView):
    model = User
    fields = ['username', 'email', 'first_name', 'last_name']
    template_name = 'editors/redactor_form.html'

    def get_object(self, **kwargs):
        return self.request.user

    def get_success_url(self):
        return reverse_lazy('profile')
