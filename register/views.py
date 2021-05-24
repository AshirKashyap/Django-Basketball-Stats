from django.shortcuts import render, redirect
from .forms import RegisterForm

# Create your views here.

def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        print("REGISTRATION WHOOO")

        if form.is_valid():
            form.save() #save a user in the user's database

            return redirect("/polls/rebounds") # need to fix this and redirect to a useful page  ################################
    else:
        form = RegisterForm()



    return render(response, "register/register.html", {"form":form})
