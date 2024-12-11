from django.contrib.auth.forms import UserCreationForm  # Import the base form for user creation
from django import forms
from .models import CustomUser  # Import the custom user model


class CustomUserCreationForm(UserCreationForm):
    """
    A custom user creation form that uses the CustomUser model
    and specifies the fields to be included in the form.
    """
    class Meta:
        model = CustomUser  # Use the CustomUser model for this form
        fields = ['username', 'email', 'password1', 'password2', 'profile_picture']  # Specify fields to display in the form


class UserEditForm(forms.ModelForm):
    """
    A form to allow users to edit their profile details and upload a profile picture.
    """
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'profile_picture']  # Include profile_picture
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your username'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your email'
            }),
            'profile_picture': forms.ClearableFileInput(attrs={
                'class': 'form-control',
            }),
        }


class PasswordChangeCustomForm(forms.Form):
    """
    A simple form for allowing users to change their password.
    """
    old_password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter old password'
        }),
        label="Old Password",
    )
    new_password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter new password'
        }),
        label="New Password",
    )
    new_password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Confirm new password'
        }),
        label="Confirm New Password",
    )
