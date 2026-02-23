from .views import set_session, get_session, delete_session, get_cookie, set_cookie, delete_cookie
from django.urls import path

urlpatterns = [
    # for session
    path("get_session/", get_session, name = "get_session"),
    path("set_session/", set_session, name = "set_session"),
    path("delete_session/", delete_session, name = "delete_session"),

    # for cookies
    path("get_cookie/", get_cookie, name="get_cookie"),
    path("set_cookie/", set_cookie, name="set_cookie"),
    path("delete_cookie/", delete_cookie, name="delete_cookie")
]