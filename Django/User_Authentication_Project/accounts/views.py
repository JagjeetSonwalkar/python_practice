from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from accounts.forms import RegistrationsForm

# Create your views here.
def register_page(request):
    if request.method == "POST":
        form = RegistrationsForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registrations Success and logged in.")
            return redirect('dashboard')
        else:
            messages.error(request, "Registrations Failed. pls correct the details")
    else:
        form = RegistrationsForm()
    return render(request, "accounts/register.html", {'form':form})

def login_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "login succesfully ")
            return redirect("dashboard")
        else:
            messages.error(request, "Invalid username or password")
    return render(request, "accounts/login.html")

def logout_page(request):
    logout(request)
    messages.success(request, "You have be logout")
    return redirect('login')

@login_required(login_url='login')
def dashboard_page(request):
    return render(request, "accounts/dashboard.html")