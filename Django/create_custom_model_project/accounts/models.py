from django.contrib.auth.models import AbstractUser
from django.db import models
from .managers import CustomUserManager

class CustomUser(AbstractUser):
    username = None # not using this field
    email = models.EmailField(unique=True)

    phNo = models.CharField(max_length=15)

    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager() # create the object of CustomUserManager

    def __str__(self):
        return self.email