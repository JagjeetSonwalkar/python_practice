from django.urls import path
from accounts.views import singup_page, login_page, home

urlpatterns = [
    path('singup-form/', singup_page , name = "singup"),
    path("login-form/", login_page, name = "login"),
    path("home/", home, name = "home")
]