from django.shortcuts import render, redirect
from django.contrib.auth.forms import (UserCreationForm, AuthenticationForm, PasswordChangeForm, PasswordResetForm)
from django.contrib.auth import update_session_auth_hash
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
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserCreationForm()
    return render(request, "accounts/singup.html", {"form":form})

@require_http_methods(["GET", "POST"])
def user_login_page(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, "accounts/login.html", {"form":form})

@login_required
@require_http_methods(["GET", "POST"])
def change_user_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect("login")
    else:
        form = PasswordChangeForm()
    return render(request, "accounts/change_password.html", {"form":form})

@require_http_methods(["GET", "POST"])
def user_forget_password(request):
    if request.method == "POST":
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            form.save(
                request=request,
                email_template_name="password_forgot_email.html"
            )
            return redirect("password_reset_done")
    else:
        form = PasswordResetForm()
    return render(request, "accounts/password_forgot.html", {"form": form})

@login_required
@require_POST
def user_logout(request):
    logout(request)
    return redirect("login")