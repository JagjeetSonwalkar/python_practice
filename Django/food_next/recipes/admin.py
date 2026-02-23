# Register your models here.

'''Imports Django’s admin framework
Required to enable admin features'''
from django.contrib import admin

'''
Imports all models from models.py
Example: Recipe, StudentID, Student, Department
So Django knows which tables exist.
'''
from .models import *

'''
Registering Models  
Displays Recipe table in admin panel
Allows CRUD operations
'''
admin.site.register(Recipe)
admin.site.register(StudentID)
admin.site.register(Student)
admin.site.register(Department)