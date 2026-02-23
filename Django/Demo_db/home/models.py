from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

# ---------------------------
# Department Model
# ---------------------------
class Department(models.Model):
    name = models.CharField(max_length=50, unique=True)  # e.g., IT, CSE

    class Meta:
        verbose_name = "Department"
        verbose_name_plural = "Departments"
        ordering = ['name']

    def __str__(self):
        return self.name


# ---------------------------
# Course Model
# ---------------------------
class Course(models.Model):
    name = models.CharField(max_length=100, unique=True)  # e.g., Software Engineering

    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Courses"
        ordering = ['name']

    def __str__(self):
        return self.name


# ---------------------------
# Student Model
# ---------------------------
class Student(models.Model):
    # Optional link to Django User
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True)

    # Text Fields
    name = models.CharField(max_length=50)
    address = models.TextField()

    # Number Fields
    age = models.PositiveIntegerField(validators=[MinValueValidator(18), MaxValueValidator(100)])
    gpa = models.DecimalField(max_digits=4, decimal_places=2, validators=[MinValueValidator(0), MaxValueValidator(4)])

    # Date & Time Fields
    date_of_birth = models.DateField()
    registration_time = models.DateTimeField(auto_now_add=True)
    last_login_time = models.DateTimeField(auto_now=True)

    # Email Field
    email = models.EmailField(unique=True)

    # Boolean Field
    is_active = models.BooleanField(default=True)

    # Relationships
    department = models.ForeignKey(
        Department,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="students"
    )
    courses = models.ManyToManyField(Course, related_name="students", blank=True)

    class Meta:
        db_table = 'student_info'
        verbose_name = 'Student'
        verbose_name_plural = 'Students'
        ordering = ['name']

    def __str__(self):
        return f"{self.name} ({self.email})"





