from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Student(models.Model):
    User = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name