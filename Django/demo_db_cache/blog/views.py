from django.shortcuts import render
from .models import UserProfile
from django.core.cache import cache

# Create your views here.
def users_list(request):
    users = cache.get('users_list')

    if not users:
        print("Cache miss")
        users = UserProfile.objects.all()
        cache.set('users_list', users, timeout = 60)
    else:
        print("Cache hit")
    
    return render(request, "users_list.html", {'users':users})
