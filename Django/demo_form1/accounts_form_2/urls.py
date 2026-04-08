from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("signup/", views.user_singup_page, name="signup"),
    path("login/", views.user_login_page, name="login"),
    path("logout/", views.user_logout, name="logout"),
    
]