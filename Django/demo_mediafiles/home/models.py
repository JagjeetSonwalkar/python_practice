from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50)
    profile_pic = models.ImageField(
        upload_to = "profiles/"
    )
    resume = models.FileField(
        upload_to = "resumes/"
    )

    def __str__(self):
        return self.name