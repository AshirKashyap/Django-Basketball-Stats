from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import login, authenticate
# Importing some very important things for the login function and the form from forms.py

def register(response):
    # Purpose: This function works to authenticate and save a user in the database if they fill out the register form
    # Parameters: The only parameter is the response object which contains the user's data from the form
    # Return: There is a redirect that sends the user back to the home page (if they sucessfully register as a user)
    # and it also returns the response object

    if response.method == "POST":
    # This if statement checks to see if the boolean expression is true
    # If this boolean is true this means that the request from the user was using the POST method (not the GET method)
    # and also means that the form was submitted by the user
        form = RegisterForm(response.POST)

        if form.is_valid():
            # this if statement checks to see if there is user data in the form so that it can save/authenticate a user
            form.save() # save a user in the user's database

            # after saving the user in the database, this is where the user gets authenticated
            # login process

            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            # using the keys from forms.py

            user = authenticate(username = username,
            password = password)

            if user is not None:
                login(response, user = user)

            return redirect("../polls/base")
            # after this process is complete it will return back to polls/base which is the home page
    else:
        # if there is not data, it will try again
        form = RegisterForm()

    # returning the response object
    return render(response, "register/register.html", {"form":form})
