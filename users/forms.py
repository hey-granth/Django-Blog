from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


# This form is used to register a user.
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    # This is an inner class that gives us a nested namespace for configurations and keeps the configurations in one place.
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

