from django.urls import path
from .views import public_view, private_view, blog_list

urlpatterns = [
    path('public/', public_view, name = 'public_view'),
    path('private/', private_view, name = 'private_view'),
    path("blogs/", blog_list, name = "blog_list")
]