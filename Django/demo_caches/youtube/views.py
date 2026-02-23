from django.shortcuts import render
from .models import YoutubeUser
from django.http import HttpResponse
from django.core.cache import cache

def users_list(request):
    users = cache.get('users_data')
    if not users:
        print("Cache miss: Fetching data from database")
        users = YoutubeUser.objects.all()
        cache.set("users_data", users, timeout = 60) # cache data for 60 seconds
    else:
        print("Cache hit: Feacting data from cache")
    return render(request, 'user_list.html', {"users":users})

