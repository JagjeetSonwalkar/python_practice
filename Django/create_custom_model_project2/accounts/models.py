from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin
)
from .managers import CustomUserManager

class CustomUser(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(unique=True)
    phNo = models.CharField(max_length=15)

    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    # Required for admin & authentication
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phNo', 'gender']

    objects = CustomUserManager()

    def __str__(self):
        return self.email