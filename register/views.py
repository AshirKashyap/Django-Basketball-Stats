from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import login, authenticate
# Create your views here.

def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        print("REGISTRATION")

        if form.is_valid():
            form.save() #save a user in the user's database
            #now need to login here

            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(username = username,
            password = password)

            if user is not None:
                login(response, user = user)

            return redirect("../polls/base")
    else:
        form = RegisterForm()

    return render(response, "register/register.html", {"form":form})
