from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

# Create your views here.
def register_page(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("dashboard")
    else:
        initial_data = {'firstname':"", 'lastname':"", 'username':"", 'email':"", "password1":"", "password2":""}
        form = UserCreationForm(initial = initial_data)
    
    return render(request, "accounts/register.html", context={"page_title":"register", "form":form})

def login_page(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("dashboard")
    else:
        initial_data = {'username':"", "password":""}
        form = AuthenticationForm(initial = initial_data)
    
    return render(request, "accounts/login.html", context={"page_title":"register", "form":form})

def logout_page(request):
    logout(request)
    return render(request, "accounts/login.html", context={"page_title":"logout"})

def dashboard_page(request):
    return render(request, "dashboard.html", context={"page_title":"dashboard"})