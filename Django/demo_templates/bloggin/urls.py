from django.urls import path
from .views import home_page, blog_details, blog_list

urlpatterns = [
    path("home/", home_page, name="home"),
    path("blog/", blog_details, name = "blog"),
    path("blog_list/", blog_list, name="blong")
]