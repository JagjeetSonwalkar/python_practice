from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("signup/", views.user_singup_page, name="signup"),
    path("login/", views.user_login_page, name="login"),
    path("logout/", views.user_logout, name="logout"),
    path("change-password/", views.change_user_password, name="change_password"),
    path("forgot-password/", views.user_forget_password, name="password_forgot"),
]