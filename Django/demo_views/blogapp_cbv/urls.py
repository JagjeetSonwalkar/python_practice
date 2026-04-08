from django.urls import path
from blogapp_cbv.views import (BlogCreateView, BlogListView, BlogDetailView, BlogUpdateView, BlogDeleteView)

urlpatterns = [
    path("blogs", BlogListView.as_view(), name = "blog_list"),
    path("blog/<int:pk>/", BlogDetailView.as_view(), name = "blog"),
    path("blog/update/<int:pk>/", BlogUpdateView.as_view(), name = "blog_update"),
    path("blog/delete/<int:pk>/", BlogDeleteView.as_view(), name = "blog_delete"),
    path("blogs/create/", BlogCreateView.as_view(), name = "blog_create"), 
]