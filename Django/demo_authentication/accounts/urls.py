from django.urls import path
from .views import register_page, login_page, logout_page, dashboard_page

urlpatterns = [
    path("register/", register_page, name="register"),
    path("login/", login_page, name="login"),
    path("logout/", logout_page, name = "logout"),
    path("dashboard/", dashboard_page, name="dashboard")
]