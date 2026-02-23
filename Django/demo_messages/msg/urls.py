from django.urls import path
from msg.views import show_msg

urlpatterns = [
    path("", show_msg, name="show_msg"),
]