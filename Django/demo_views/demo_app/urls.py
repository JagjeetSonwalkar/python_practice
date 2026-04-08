from django.urls import path
from demo_app.views import blog_create, blog_list, blog_detail, blog_update, blog_delete

urlpatterns = [
    path("blogs/", blog_list, name = "blog_list"),
    path('blogs/create-blog/', blog_create, name = "blog_create"),
    path("blogs/blog/<int:id>/", blog_detail, name = "blog_detail"),
    path("blogs/update-blog/<int:id>/", blog_update, name = "blog_update"),
    path("blogs/delete-blog/<int:id>/", blog_delete, name = "blog_delete"),
]