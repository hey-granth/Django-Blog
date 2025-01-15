from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        # If the form is valid, then we are going to save the user.
        if form.is_valid():
            form.save()
            # it saves the user to the database.

            username = form.cleaned_data.get('username')
            # 'form.cleaned_data' is a dictionary that contains all the data that was inputted into the form.
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')

    else:
        form = UserRegisterForm()
        # UserRegisterForm is a form that is already provided by Django. It is a form that has a username, email, and password field.

    # 'UerCreationForm' is a form that is already provided by Django. It is a form that has a username, email, and password field.
    # We are going to pass this form to our template.

    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        # We are going to create a form instance with the new data.
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        # If the form is valid, then we are going to save the user.
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            # it saves the user to the database.

            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
        # it will redirect to the profile page.
