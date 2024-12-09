from django.contrib.auth.forms import UserCreationForm  # Import the base form for user creation
from .models import CustomUser  # Import the custom user model

class CustomUserCreationForm(UserCreationForm):  # Subclass the built-in UserCreationForm
    """
    A custom user creation form that uses the CustomUser model
    and specifies the fields to be included in the form.
    """
    class Meta:
        model = CustomUser  # Use the CustomUser model for this form
        fields = ['username', 'email', 'password1', 'password2']  # Specify fields to display in the form
