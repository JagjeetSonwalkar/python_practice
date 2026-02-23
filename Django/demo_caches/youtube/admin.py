from django.contrib import admin
from .models import YoutubeUser
from django.core.cache import cache
from django.contrib import messages

@admin.action(description="clear users cache")
def clear_users_cache(modeladmin, request, queryset):
    cache.delete("user_data")
    messages.success(request, "cache cleared successfully")

# Register your models here.
@admin.register(YoutubeUser)
class YoutubeUserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subscribers')
    actions = [clear_users_cache]