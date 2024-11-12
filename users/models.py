from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('anonymous', 'Anonymous'),
        ('registered', 'Registered'),
        ('staff', 'Staff'),
        ('superuser', 'Superuser'),
    )
    role = models.CharField(max_length=50, choices=ROLE_CHOICES, blank=True, null=True)

    def save(self, *args, **kwargs):
        # Automatically set is_staff and is_superuser based on the role
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
