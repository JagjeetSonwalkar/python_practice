from django.urls import path, re_path
from .views import post_details, user_profile, article_by_year, article_details

urlpatterns = [
    path("post/<int:post_id>/", post_details, name='post_details'),
    path("user/<str:username>/", user_profile, name='user_profile'),
    
    re_path(r"^article/(?P<year>[0-9]{4})/$", article_by_year, name="article_by_year"),

    path("article/<int:year>/<int:month>/<int:day>/", article_details, name="article_details"),
]