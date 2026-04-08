from django.shortcuts import render, redirect
from django.http import HttpResponse
from accounts.forms import CustomUserCreationForm, CustomAuthencticationForm
from django import forms
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login


@login_required
def home(request):
    return HttpResponse("Welcome to home")

# Create your views here.
def singup_page(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = CustomUserCreationForm()
    return render(request, "accounts/singup.html", {"form":form})

def login_page(request):
    if request.method == "POST":
        form = CustomAuthencticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")
    else:
        form = CustomAuthencticationForm()
    return render(request, "accounts/login.html", {"form":form})