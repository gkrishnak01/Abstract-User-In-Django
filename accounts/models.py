from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager

# Create your models here.

#abstract user is used to tweak existing user model. AbstractBaseUser can be used to build model from scratch
class User(AbstractUser):
    username = None
    email = models.EmailField(unique = True)
    address = models.CharField(max_length = 200)
    education = models.CharField(max_length = 100)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []