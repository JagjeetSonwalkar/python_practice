from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def home_page(request):
    context = {"page":"home"}
    return render(request, "home/index.html", context)

def register_page(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        if User.objects.filter(username = username).exists():
            messages.error(request, "Username already taken")
            return redirect("/register/")

        if password != confirm_password:
            messages.error(request, "Passwords do not match")
            return redirect("/register/")

        user = User.objects.create_user(
            first_name = first_name,
            last_name = last_name,
            username = username,
        )

        user.set_password(password)

        user.save()

        messages.info(request, "User created successfully")
        return redirect("/register/")

    context = {"page":"register"}
    return render(request, "home/register.html", context)

def login_page(request):
    if request.method == "GET":
        context = {"page": "login"}
        return render(request, "home/login.html", context)

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if not User.objects.filter(username = username).exists():
            messages.error(request, "Username does not exist")
            return redirect("/login/")

        user = authenticate(username = username, password=password)

        if user is None:
            messages.error(request, "Invalid password")
            return redirect("/login/")
        
        login(request, user)
        messages.success(request, "Login successful")
        return redirect("/")

    context = {"page":"login"}
    return render(request, "home/login.html", context)

def logout_page(request):
    logout(request)
    messages.success(request, "Logged out successfully")
    return redirect("/login/")