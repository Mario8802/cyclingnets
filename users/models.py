from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

from django.contrib.auth.models import BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError("The Username field must be set")
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get('is_superuser') is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(username, password, **extra_fields)



class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('registered', 'Registered'),
        ('staff', 'Staff'),
        ('superuser', 'Superuser'),
    )
    role = models.CharField(max_length=50, choices=ROLE_CHOICES, default='registered')

    objects = CustomUserManager()  # Тук добавяме CustomUserManager

    def save(self, *args, **kwargs):
        if self.role == 'staff':
            self.is_staff = True
            self.is_superuser = False
        elif self.role == 'superuser':
            self.is_staff = True
            self.is_superuser = True
        else:
            self.is_staff = False
            self.is_superuser = False
        super().save(*args, **kwargs)

