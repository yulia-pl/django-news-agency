from django import forms

from django.contrib.auth import get_user_model


# Get the custom user model
User = get_user_model()


# User registration form class
class UserRegistrationForm(forms.ModelForm):
    # Password field with a password input widget
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        # Define the model and fields to be included in the form
        model = User
        fields = ["username", "email", "password", "years_of_experience"]

    # Override the save method to set the password
    def save(self, commit=True):
        user = super().save(commit=False)
        # Set the user's password using the provided password
        user.set_password(self.cleaned_data["password"])
        if commit:
            # Save the user to the database
            user.save()
        return user
