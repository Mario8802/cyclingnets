from django.contrib import admin
from .models import News, Page


# -------------------------------
# Admin Configuration for News
# -------------------------------
@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    """
    Custom admin configuration for the News model.

    Enhances the admin interface for managing news articles:
    - Displays key fields in the list view.
    - Allows search functionality for title and content.
    - Enables filtering by publication status and creation date.
    - Orders news articles by the creation date, newest first.
    """
    list_display = ('title', 'is_published', 'created_at', 'updated_at')  # Fields displayed in the admin list view
    search_fields = ('title', 'content')  # Enables search by title and content
    list_filter = ('is_published', 'created_at')  # Adds filters for publication status and creation date
    ordering = ('-created_at',)  # Orders news articles by creation date in descending order
    list_editable = ('is_published',)  # Allows editing of the publication status directly in the list view
    date_hierarchy = 'created_at'  # Adds a date hierarchy for filtering by date


# -------------------------------
# Admin Configuration for Page
# -------------------------------
@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    """
    Custom admin configuration for the Page model.

    Enhances the admin interface for managing static pages:
    - Displays key fields in the list view.
    - Allows search functionality for title and content.
    - Automatically generates the slug field based on the title.
    - Enables filtering by activity status and creation date.
    - Orders pages by the creation date, newest first.
    """
    list_display = ('title', 'slug', 'is_active', 'created_at', 'updated_at')  # Fields displayed in the admin list view
    search_fields = ('title', 'content')  # Enables search by title and content
    prepopulated_fields = {'slug': ('title',)}  # Automatically generates the slug field based on the title
    list_filter = ('is_active', 'created_at')  # Adds filters for activity status and creation date
    ordering = ('-created_at',)  # Orders pages by creation date in descending order
    list_editable = ('is_active',)  # Allows editing of the activity status directly in the list view
    date_hierarchy = 'created_at'  # Adds a date hierarchy for filtering by date
