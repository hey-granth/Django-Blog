from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        # If the form is valid, then we are going to save the user.
        if form.is_valid():
            form.save()
            # it saves the user to the database.

            username = form.cleaned_data.get('username')
            # 'form.cleaned_data' is a dictionary that contains all the data that was inputted into the form.
            messages.success(request, f'Account created for {username}!')
            return redirect('blog-home')

    else:
        form = UserCreationForm()
    # 'UerCreationForm' is a form that is already provided by Django. It is a form that has a username, email, and password field.
    # We are going to pass this form to our template.

    return render(request, 'users/register.html', {'form': form})

