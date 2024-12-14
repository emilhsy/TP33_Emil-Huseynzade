from django.shortcuts import render, redirect

# Importing messages for displaying success message after registering or updating profile
from django.contrib import messages

# Importing decorator for checking if user is logged in
from django.contrib.auth.decorators import login_required

# Importing created forms
from .forms import UserRegisterForm, UserUpdateForm

# Register view
def register(request):
    if request.method == 'POST': # Checking if the request if for registering
        form = UserRegisterForm(request.POST) # Using register form
        # Validating form
        if form.is_valid():
            form.save() # Saving form data to database
            messages.success(request, f'Your account has been created! You are now able to log in') # Displaying success message
            return redirect('login') # Redirecting to login page
    else: # If not, then displaying form data
        form = UserRegisterForm() # Using register form
    return render(request, 'users/register.html', {'form': form}) # Displayin register.html as template


@login_required # Checking if user is logged in
def profile(request):
    if request.method == 'POST': # Checking if the request if for updating
        u_form = UserUpdateForm(request.POST, instance=request.user) # Using update form
    
        # Validating form
        if u_form.is_valid():
            u_form.save() # Saving form data to database
            messages.success(request, f'Your account has been updated!') # Displaying success message
            return redirect('profile') # Redirecting to profile page

    else: # If not, then displaying form data
        u_form = UserUpdateForm(instance=request.user) # Using update form

    context = {
        'u_form': u_form, # Passing the form as context
    }

    return render(request, 'users/profile.html', context) # Displayin profile.html as template