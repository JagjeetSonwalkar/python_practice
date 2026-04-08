from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, UsernameOrEmailAuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST, require_http_methods

@login_required
@require_http_methods("GET")
def home(request):
    return render(request, "accounts/home.html")

@require_http_methods(["GET", "POST"])
def user_singup_page(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = CustomUserCreationForm()
    return render(request, "accounts/singup.html", {"form":form})

@require_http_methods(["GET", "POST"])
def user_login_page(request):
    if request.method == "POST":
        form = UsernameOrEmailAuthenticationForm(request, data = request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UsernameOrEmailAuthenticationForm()
    return render(request, "accounts/login.html", {"form":form})

@login_required
@require_POST
def user_logout(request):
    logout(request)
    return redirect("login")