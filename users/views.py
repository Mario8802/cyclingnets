from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib import messages
from django.conf import settings  # For LOGIN_REDIRECT_URL
from django.contrib.auth.decorators import login_required


def login_view(request):
    """
    Handles user login. Redirects to the 'next' parameter or the default redirect URL after login.
    """
    next_url = request.GET.get('next', settings.LOGIN_REDIRECT_URL)  # Default to LOGIN_REDIRECT_URL if `next` is not provided
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f"Welcome back, {user.username}!")
            return redirect(next_url)
        else:
            messages.error(request, "Invalid username or password. Please try again.")
    else:
        form = AuthenticationForm()

    background_image = 'static/images/login/somebike.jpg'
    return render(request, 'users/login.html', {'form': form, 'background_image': background_image, 'next': next_url})


def register_view(request):
    """
    Handles user registration. Logs in the user automatically after successful registration.
    """
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f"Welcome, {user.username}! Your account has been successfully created.")
            return redirect('users:profile')  # Use namespace 'users'
        else:
            messages.error(request, "Registration failed. Please check the details and try again.")
    else:
        form = CustomUserCreationForm()

    background_image = 'static/images/register/hero1.jpg'
    return render(request, 'users/register.html', {'form': form, 'background_image': background_image})


def logout_view(request):
    logout(request)
    messages.success(request, "You have successfully logged out. See you again soon!")
    return render(request, 'users/goodbye.html')



@login_required
def profile_view(request):
    """
    Displays the user's profile. Requires the user to be logged in.
    """
    background_image = 'static/images/profile/login_bike.jpg'
    return render(request, 'users/profile.html', {'user': request.user, 'background_image': background_image})

