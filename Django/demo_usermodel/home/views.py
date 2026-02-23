from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def home_page(request):
    return render(request, "home/index.html", context = {"page_title":"home"})

def register_page(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        if User.objects.filter(username = username).exists():
            messages.error(request, "Username already taken")
            return redirect("register")

        if password != confirm_password:
            messages.error(request, "password do not match")
            return redirect("register")
        
        user = User.objects.create_user(
            first_name = first_name,
            last_name = last_name,
            username = username,
        )
        user.set_password(password)
        user.save()

        messages.info(request, "Register done.")
        return redirect("/login/")
        
    return render(request, "home/register.html", context = {"page_title":"register"})

def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            messages.error(request, "User not exists")
            return redirect("login")
        
        user = authenticate(username = username, password = password)

        if user is None:
            messages.error(request, "Invalid Password")
            return redirect("login")
        else:
            login(request, user)
            messages.success(request, "Login successfull")
            return redirect("/home/")

    return render(request, "home/login.html", context={"page_title":"login"})