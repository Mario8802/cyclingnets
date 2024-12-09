from django.contrib import admin
from .models import BikePost


# -------------------------------
# Admin Configuration for BikePost
# -------------------------------
@admin.register(BikePost)
class BikePostAdmin(admin.ModelAdmin):
    """
    Custom admin configuration for the BikePost model.

    Enhances the admin interface for managing bike posts:
    - Displays key fields in the list view.
    - Allows filtering by specific fields.
    - Enables search functionality for text-based fields.
    """
    # Fields displayed in the list view
    list_display = [
        'title',       # Title of the bike post
        'category',    # Category (e.g., Buy/Sell)
        'condition',   # Condition (e.g., New/Used)
        'price',       # Price of the bike
        'location',    # Location of the bike
        'posted_by',   # User who posted the bike
        'created_at',  # Date when the post was created
    ]

    # Fields to filter by in the admin interface
    list_filter = [
        'category',    # Filter by category
        'condition',   # Filter by condition
        'created_at',  # Filter by creation date
    ]

    # Fields to search in the admin interface
    search_fields = [
        'title',                     # Search by title
        'description',               # Search by description
        'location',                  # Search by location
        'posted_by__username',       # Search by username of the poster
    ]
