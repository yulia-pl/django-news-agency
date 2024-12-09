from django import forms
from django.contrib.auth.forms import UserCreationForm
from editors.models import Redactor


class RegisterForm(UserCreationForm):
    class Meta:
        model = Redactor
        fields = ['username', 'email', 'first_name', 'last_name', 'years_of_experience', 'password1', 'password2']
