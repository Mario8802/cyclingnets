from django.contrib.auth.models import AbstractUser, BaseUserManager  # Import base classes for custom user models
from django.db import models  # Import Django's models module


class CustomUserManager(BaseUserManager):
    """
    Custom manager for the CustomUser model to handle user creation.
    """

    def create_user(self, username, password=None, **extra_fields):
        """
        Creates and returns a regular user with the provided username and password.
        """
        if not username:
            raise ValueError("The Username field must be set")  # Validation for username

        # Ensure regular users have the 'registered' role by default
        extra_fields.setdefault('role', 'registered')
        user = self.model(username=username, **extra_fields)  # Create a new user instance
        user.set_password(password)  # Hash the password
        user.save(using=self._db)  # Save the user to the database
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        """
        Creates and returns a superuser with the provided username and password.
        """
        extra_fields.setdefault('is_staff', True)  # Superuser must be staff
        extra_fields.setdefault('is_superuser', True)  # Superuser must have superuser privileges
        extra_fields.setdefault('role', 'superuser')  # Default role for superuser

        # Ensure required flags are correctly set for a superuser
        if extra_fields.get('is_staff') is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get('is_superuser') is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(username, password, **extra_fields)  # Create the superuser


class CustomUser(AbstractUser):
    """
    Custom user model extending the built-in AbstractUser model.
    Includes a role field with predefined choices.
    """

    ROLE_CHOICES = (
        ('registered', 'Registered'),  # Default role for regular users
        ('staff', 'Staff'),  # Staff members
        ('superuser', 'Superuser'),  # Administrators with all permissions
    )
    role = models.CharField(
        max_length=50, choices=ROLE_CHOICES, default='registered'
    )  # Role field with predefined choices and a default

    objects = CustomUserManager()  # Custom manager for the user model

    def save(self, *args, **kwargs):
        """
        Overrides the default save method to set is_staff and is_superuser
        flags based on the role field.
        """
        if self.role == 'staff':  # If role is staff
            self.is_staff = True
            self.is_superuser = False
        elif self.role == 'superuser':  # If role is superuser
            self.is_staff = True
            self.is_superuser = True
        else:  # For registered users
            self.is_staff = False
            self.is_superuser = False
        super().save(*args, **kwargs)  # Call the parent save method
