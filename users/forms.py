from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


# This form is used to register a user.
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    # This is an inner class that gives us a nested namespace for configurations and keeps the configurations in one place.
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


# a model form allows us to create a form which will work with a specific database model.
# This form is used to update the user information.
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


# this class
class ProfileUpdateForm(forms.ModelForm):
    # we jump directly to metaclass because we don't need to add any extra fields.
    class Meta:
        model = Profile
        fields = ['image']
