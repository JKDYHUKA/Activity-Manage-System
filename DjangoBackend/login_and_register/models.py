from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin


class CustomUser(AbstractUser):
    nickname = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return self.nickname

