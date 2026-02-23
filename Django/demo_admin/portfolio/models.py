from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    city = models.CharField(max_length=25)

    def __str__(self):
        return self.name

class Profile(models.Model):
    bio = models.TextField()
    location = models.TextField()
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.bio 