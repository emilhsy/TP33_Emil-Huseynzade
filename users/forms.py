# Importing django built in forms
from django import forms

# Importing Django's own user creation form
from django.contrib.auth.forms import UserCreationForm

# Importing the User model from Django's authentication system
from django.contrib.auth.models import User

# Creating register form with inheriting Django's own form
class UserRegisterForm(UserCreationForm):

    # Adding this for specifying form fields
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

# Creating update form with inheriting django built in forms
class UserUpdateForm(forms.ModelForm):

    # Adding this for specifying form fields
    class Meta:
        model = User
        fields = ['username']