from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def home(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        # authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been Logged IN !")
            return redirect('home')
        else:
            messages.success(request, "Thier was an error try Logging In, Please try again later..")
            return redirect('home')
    else:
        return render(request, "home.html", {})


def login_user(request):
    pass


def logout_user(request):
    pass
