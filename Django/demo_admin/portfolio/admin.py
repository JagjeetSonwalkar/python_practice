from django.contrib import admin
from portfolio.models import Student, Profile

admin.site.site_header  = "Jaggi Portfolio Administrations"
admin.site.site_title = 'Jaggi Admin Portal'
admin.site.index_title = 'Welcome to jaggi Dashboard'

# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', "age", 'city') # admin list display: show name, age, city attribute in admin panel
    search_fields = ("name", "city")       # search field: search by name, city
    list_filter = ("name", "age", "city")  # filter data by name, age, city
    ordering = ("name",)                   # admin ordering

    readonly_fields = ('name', 'age')