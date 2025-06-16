from django.contrib.auth import login, authenticate, logout  # Import Django's authentication functions
from django.contrib.auth.forms import AuthenticationForm  # Import built-in form for login
from django.shortcuts import render, redirect  # Import render and redirect for handling views
from .forms import CustomUserCreationForm, UserEditForm  # Import custom forms
from django.contrib import messages  # Import messages framework for user notifications
from django.conf import settings  # Import settings to access LOGIN_REDIRECT_URL
from django.contrib.auth.decorators import login_required  # Import decorator to restrict access to logged-in users


def login_view(request):
    """
    Handles the user login request. Redirects to the 'next' parameter or
    the default redirect URL after a successful login.
    """
    next_url = request.GET.get('next', settings.LOGIN_REDIRECT_URL)  # Default redirect URL after login

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)  # Validate login form data
        if form.is_valid():
            user = form.get_user()  # Get authenticated user
            login(request, user)  # Log the user in
            messages.success(request, f"Welcome back, {user.username}!")  # Success message
            return redirect(next_url)  # Redirect to 'next' or default URL
        else:
            messages.error(request, "Invalid username or password. Please try again.")  # Error message
    else:
        form = AuthenticationForm()  # Display empty form for GET requests

    # Render login page
    return render(request, 'users/login.html', {
        'form': form,
        'background_image': 'static/images/login/default_image.jpg',
        'next': next_url
    })


def register_view(request):
    """
    Handles user registration. Automatically logs the user in after successful registration.
    """
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)  # Validate registration form data
        if form.is_valid():
            user = form.save()  # Save new user
            login(request, user)  # Log the user in
            messages.success(request, f"Welcome, {user.username}! Your account has been created.")  # Success message
            return redirect('users:profile')  # Redirect to profile page
        else:
            messages.error(request, "Registration failed. Please check the details and try again.")  # Error message
    else:
        form = CustomUserCreationForm()  # Display empty form for GET requests

    # Render registration page
    return render(request, 'users/register.html', {
        'form': form,
        'background_image': 'static/images/register/benefit2.jpg'
    })


def logout_view(request):
    """
    Handles the logout request. Logs the user out and displays a success message.
    """
    logout(request)  # Log the user out
    messages.success(request, "You have successfully logged out. See you again soon!")  # Success message
    return render(request, 'users/goodbye.html')  # Goodbye page


@login_required
def profile_view(request):
    """
    Displays the user's profile. Requires the user to be logged in.
    """
    return render(request, 'users/profile.html', {
        'user': request.user,
        'background_image': 'static/images/profile/login_bike.jpg'
    })


@login_required
def edit_profile_view(request):
    """
    Allows users to edit their profile details, including their profile picture.
    """
    if request.method == 'POST':
        form = UserEditForm(request.POST, request.FILES, instance=request.user)  # Include file data for profile picture
        if form.is_valid():
            form.save()  # Save updated user data
            messages.success(request, "Your profile has been updated successfully.")  # Success message
            return redirect('users:profile')  # Redirect to profile page
        else:
            messages.error(request, "Failed to update your profile. Please check the details and try again.")  # Error message
    else:
        form = UserEditForm(instance=request.user)  # Prepopulate form with current user data

    # Render edit profile page
    return render(request, 'users/edit_profile.html', {
        'form': form,
        'background_image': 'static/images/profile/edit_background.jpg'
    })


@login_required
def change_password_view(request):
    """
    Allows users to change their password.
    """
    if request.method == 'POST':
        old_password = request.POST.get('old_password')
        new_password1 = request.POST.get('new_password1')
        new_password2 = request.POST.get('new_password2')

        if request.user.check_password(old_password):
            if new_password1 == new_password2:
                request.user.set_password(new_password1)  # Set new password
                request.user.save()
                messages.success(request, "Your password has been changed successfully.")  # Success message
                logout(request)  # Log the user out for security
                return redirect('users:login')  # Redirect to login page
            else:
                messages.error(request, "The new passwords do not match. Please try again.")  # Error message
        else:
            messages.error(request, "The old password is incorrect. Please try again.")  # Error message

    # Render change password page
    return render(request, 'users/change_password.html', {
        'background_image': 'static/images/profile/change_password.jpg'
    })
