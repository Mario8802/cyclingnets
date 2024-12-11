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
            raise ValueError("The Username field must be set.")

        # Assign the default role to regular users
        extra_fields.setdefault('role', 'registered')

        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        """
        Creates and returns a superuser with the provided username and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('role', 'superuser')

        if extra_fields.get('is_staff') is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get('is_superuser') is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(username, password, **extra_fields)


class CustomUser(AbstractUser):
    """
    Custom user model extending the built-in AbstractUser model.
    Adds a role field and profile picture for additional functionality.
    """

    ROLE_CHOICES = (
        ('registered', 'Registered'),  # Default role for regular users
        ('staff', 'Staff'),            # Staff members with additional privileges
        ('superuser', 'Superuser'),    # Administrators with full permissions
    )

    role = models.CharField(
        max_length=50,
        choices=ROLE_CHOICES,
        default='registered',
        help_text="The role determines the user's permissions."
    )

    profile_picture = models.ImageField(
        upload_to='profile_pictures/',  # Directory for profile pictures
        null=True,
        blank=True,
        max_length=255,
        default='profile_pictures/default.jpg',
        help_text="Upload a profile picture (optional)."
    )

    objects = CustomUserManager()

    def save(self, *args, **kwargs):
        """
        Overrides the default save method to set is_staff and is_superuser flags
        based on the assigned role.
        """
        # Assign permissions based on the role
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

    def __str__(self):
        """
        String representation of the user, showing the username.
        """
        return self.username
