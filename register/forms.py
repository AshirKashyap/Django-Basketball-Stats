from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User




class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta: #defining that this form above will save into the user's database
        model = User #changing the User model
        fields = ["username", "email", "password1", "password2"] #order these will show up
