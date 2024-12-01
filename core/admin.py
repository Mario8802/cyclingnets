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
    - Enables filtering by creation date.
    - Orders news articles by the creation date, newest first.
    """
    list_display = ('title', 'created_at', 'updated_at')  # Fields displayed in the admin list view
    search_fields = ('title', 'content')  # Enables search by title and content
    list_filter = ('created_at',)  # Adds a filter sidebar for creation date
    ordering = ('-created_at',)  # Orders news articles by creation date in descending order


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
    - Enables filtering by creation date.
    - Orders pages by the creation date, newest first.
    """
    list_display = ('title', 'slug', 'created_at', 'updated_at')  # Fields displayed in the admin list view
    search_fields = ('title', 'content')  # Enables search by title and content
    prepopulated_fields = {'slug': ('title',)}  # Automatically generates the slug field based on the title
    list_filter = ('created_at',)  # Adds a filter sidebar for creation date
    ordering = ('-created_at',)  # Orders pages by creation date in descending order
