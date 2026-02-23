from django.contrib.admin import AdminSite
from django.contrib import admin
from .models import Blog

class JaggiAdminSite(AdminSite):
    site_header = "Jaggi Blog Admin"
    site_title = "Marvellous Admin"
    index_title = "Control Panel"

jaggi_admin_site = JaggiAdminSite(name="jaggi_admin")

@jaggi_admin_site.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('name',)

    def has_add_permission(self, request):
        return request.user.is_superuser

    def has_change_permission(self, request, obj=None):
        if obj and obj.created_by != request.user:
            return False
        return True

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_view_permission(self, request, obj=None):
        return request.user.is_staff 