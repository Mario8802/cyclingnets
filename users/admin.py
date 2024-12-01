from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser  # Import the CustomUser model

# Register the CustomUser model with the admin site
@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):  # Extends Django's built-in UserAdmin for custom user management
    model = CustomUser  # Specifies the model to manage
    list_display = ['username', 'email', 'first_name', 'last_name', 'is_active', 'is_staff']  # Fields displayed in the list view
    list_filter = ['is_active', 'is_staff', 'date_joined']  # Filters for the sidebar in the admin list view
    search_fields = ['username', 'email', 'first_name', 'last_name']  # Fields that can be searched in the admin interface
