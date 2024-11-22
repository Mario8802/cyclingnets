from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib import messages
from django.conf import settings  # For LOGIN_REDIRECT_URL
from django.contrib.auth.decorators import login_required

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)  # Redirect based on settings
        else:
            messages.error(request, "Invalid username or password. Please try again.")
    else:
        form = AuthenticationForm()
    background_image = 'static/images/login/somebike.jpg'
    return render(request, 'users/login.html', {'form': form, 'background_image': background_image})



def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Automatically log the user in after registration
            login(request, user)
            messages.success(request, f"Welcome, {user.username}! Your account has been successfully created.")
            return redirect('home')  # Redirect to the homepage
        else:
            messages.error(request, "Registration failed. Please check the details and try again.")
            for field, error_list in form.errors.items():
                for error in error_list:
                    messages.error(request, f"{field}: {error}")
    else:
        form = CustomUserCreationForm()
    # Add the background image for the registration page
    background_image = 'static/images/register/hero1.jpg'
    return render(request, 'users/register.html', {'form': form, 'background_image': background_image})



def logout_view(request):
    logout(request)
    messages.success(request, "You have successfully logged out.")
    # Add the background image for the logout page
    background_image = 'static/images/logout/passo_dello_stelvio.jpg'
    return render(request, 'users/logout.html', {'background_image': background_image})


@login_required
def profile_view(request):
    # Add the background image for the profile page
    background_image = 'static/images/profile/login_bike.jpg'
    return render(request, 'users/profile.html', {'user': request.user, 'background_image': background_image})
