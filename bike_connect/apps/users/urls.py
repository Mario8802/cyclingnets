from django.urls import path  # Import the path function for URL configuration
from bike_connect.apps.users import views  # Import views from the current app

app_name = 'users'  # Namespace for the 'users' app

urlpatterns = [
    path('login/', views.login_view, name='login'),             # Login page
    path('register/', views.register_view, name='register'),        # Registration page
    path('logout/', views.logout_view, name='logout'),                  # Logout functionality
    path('profile/', views.profile_view, name='profile'),                   # Profile page
    path('profile/edit/', views.edit_profile_view, name='edit_profile'),          # Edit profile page
    path('password/change/', views.change_password_view, name='change_password'),     # Change password page
]
