from .views import home, about, blog
from django.urls import path

urlpatterns = [
    path("home/", home, name="home"),
    path("about/", about, name="about"),
    path("blog/", blog, name="blog" ),
]