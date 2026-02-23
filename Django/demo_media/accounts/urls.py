from django.urls import path
from accounts.views import upload_profile, view_profile

urlpatterns = [
    path('upload/', upload_profile, name = 'upload_profile'),
    path('profile/', view_profile, name = 'view_profile'),
]