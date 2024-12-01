from django.contrib.auth import login, authenticate, logout  # Import Django's authentication functions
from django.contrib.auth.forms import AuthenticationForm  # Import built-in form for login
from django.shortcuts import render, redirect  # Import render and redirect for handling views
from .forms import CustomUserCreationForm  # Import custom form for user registration
from django.contrib import messages  # Import messages framework for user notifications
from django.conf import settings  # Import settings to access LOGIN_REDIRECT_URL
from django.contrib.auth.decorators import login_required  # Import decorator to restrict access to logged-in users


def login_view(request):
    """
    Handles the user login request. Redirects to the 'next' parameter or
    the default redirect URL after a successful login.
    """
    # Get the URL to redirect to after login, or use the default redirect URL from settings
    next_url = request.GET.get('next', settings.LOGIN_REDIRECT_URL)

    # Check if the request is a POST (form submission)
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)  # Initialize the form with submitted data
        if form.is_valid():  # Validate the form
            user = form.get_user()  # Retrieve the authenticated user
            login(request, user)  # Log the user in
            messages.success(request, f"Welcome back, {user.username}!")  # Display a success message
            return redirect(next_url)  # Redirect to the 'next' URL or the default redirect
        else:
            # Display an error message if login fails
            messages.error(request, "Invalid username or password. Please try again.")
    else:
        form = AuthenticationForm()  # Initialize an empty form for GET requests

    # Background image for the login page
    background_image = 'static/images/login/somebike.jpg'

    # Render the login page with the form and additional context
    return render(request, 'users/login.html', {'form': form, 'background_image': background_image, 'next': next_url})


def register_view(request):
    """
    Handles user registration. Automatically logs the user in after successful registration.
    """
    # Check if the request is a POST (form submission)
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)  # Initialize the registration form with submitted data
        if form.is_valid():  # Validate the form
            user = form.save()  # Save the new user to the database
            login(request, user)  # Log the user in after registration
            # Display a success message for the new user
            messages.success(request, f"Welcome, {user.username}! Your account has been successfully created.")
            return redirect('users:profile')  # Redirect to the user's profile page
        else:
            # Display an error message if registration fails
            messages.error(request, "Registration failed. Please check the details and try again.")
    else:
        form = CustomUserCreationForm()  # Initialize an empty form for GET requests

    # Background image for the registration page
    background_image = 'static/images/register/hero1.jpg'

    # Render the registration page with the form and additional context
    return render(request, 'users/register.html', {'form': form, 'background_image': background_image})


def logout_view(request):
    """
    Handles the logout request. Logs the user out and displays a success message.
    """
    logout(request)  # Log the user out
    # Display a success message after logout
    messages.success(request, "You have successfully logged out. See you again soon!")
    # Render a goodbye page to confirm logout
    return render(request, 'users/goodbye.html')


@login_required
def profile_view(request):
    """
    Displays the user's profile. Requires the user to be logged in.
    """
    # Background image for the profile page
    background_image = 'static/images/profile/login_bike.jpg'

    # Render the profile page with the current user's data and background image
    return render(request, 'users/profile.html', {'user': request.user, 'background_image': background_image})
