from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    email = models.EmailField(unique=True)
    city = models.CharField(max_length=25, null=True)

    def __str__(self):
        return self.name