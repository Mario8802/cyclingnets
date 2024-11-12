from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Custom Fields', {'fields': ('role',)}),
    )
    list_display = ['username', 'email', 'role', 'is_active', 'is_staff', 'is_superuser']
    list_filter = ['is_staff', 'is_superuser', 'is_active']
