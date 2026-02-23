from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import user_profile, admin_panel

urlpatterns = [
    path('get-token/', obtain_auth_token, name="api_token_auth"),
    path('profile', user_profile, name = 'user_profile'),
    path('admin-panel/', admin_panel, name = 'admin_panel')
]
