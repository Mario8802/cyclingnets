from django.contrib import admin
from .models import BikePost


@admin.register(BikePost)
class BikePostAdmin(admin.ModelAdmin):
    list_display = [
        'title', 'category',
        'condition','price',
        'location','posted_by',
        'created_at'
    ]

    list_filter = [
        'category',
        'condition',
        'created_at'
    ]
    search_fields = [
        'title',
        'description',
        'location',
        'posted_by__username'
    ]
