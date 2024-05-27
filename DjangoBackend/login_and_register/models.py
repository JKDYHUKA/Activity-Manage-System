import uuid

from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin


class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user


class CustomUser(AbstractUser):
    nickname = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15, unique=True)
    personal_number = models.CharField(max_length=9, editable=False, unique=False, default="000000000")

    objects = CustomUserManager()

    def __str__(self):
        return self.username















