from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Recipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    recipe_name = models.CharField(max_length=50)
    recipe_description = models.TextField()
    recipe_image = models.ImageField()
    
    recipe_view_count = models.IntegerField(default=1)

'''
You are creating a model (table) named Department
models.Model means: Django ORM will treat this class as a database table

Creates a column named department
CharField → VARCHAR in database
max_length=100 → maximum 100 characters

Python magic method 
Defines how the object is displayed
When you print a Department object: print(dept)
You will see: Computer Science, instead of: Department object (1)

Meta class is used to provide extra configuration for the model
Default ordering when fetching data
'''
class Department(models.Model):
    department = models.CharField(max_length=100)

    def __str__(self)->str:
        return self.department
    
    class Meta:
        ordering = ['department']

'''
Creates a table named studentid

Column student_id
Stores ID
'''
class StudentID(models.Model):
    student_id = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.student_id

'''
Main table: student

ForeignKey (Many-to-One)
Meaning: Each student belongs to one department, One department can have many students
Department: Parent table
related_name="depart" --->Used for reverse access, Means: get all students under that department

OneToOneField
Meaning: One student has one unique student ID, One student ID belongs to only one student

Meta class in Student
Extra configuration.
verbose_name = "student" ----> Display name in Django admin, Instead of: Students
'''
class Student(models.Model):
    department = models.ForeignKey(Department, related_name="depart", on_delete=models.CASCADE)
    student_id = models.OneToOneField(StudentID, related_name="studentid", on_delete=models.CASCADE)
    student_name = models.CharField(max_length=50)
    student_email = models.EmailField(unique=True)
    student_age = models.IntegerField(default=18)
    student_address = models.TextField()

    def __str__(self) -> str:
        return self.student_name

    class Meta:
        ordering = ['student_name'] # Default sorting:
        verbose_name = "student"
