from django.urls import path  # Import the path function for URL configuration
from . import views  # Import views from the current app

app_name = 'users'  # Namespace for the 'users' app

urlpatterns = [
    path('login/', views.login_view, name='login'),  # Login page, handled by login_view
    path('register/', views.register_view, name='register'),  # Registration page, handled by register_view
    path('logout/', views.logout_view, name='logout'),  # Logout functionality, handled by logout_view
    path('profile/', views.profile_view, name='profile'),  # Profile page, handled by profile_view
]
