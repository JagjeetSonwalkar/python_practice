from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from .manager import UserManager

class CustomUser(AbstractUser):
    username = None  # not using username field
    email = None 

    phone_number = models.CharField(unique=True, max_length=100)
    user_bio = models.CharField(max_length=50, blank=True)
    user_profile_image = models.ImageField(upload_to="profile/", null=True, blank=True)

    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = [] 

    objects = UserManager()

    def __str__(self):
        return self.phone_number