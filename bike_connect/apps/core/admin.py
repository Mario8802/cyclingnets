from django.contrib import admin
from .models import News, Page


# -------------------------------
# Admin Configuration for News
# -------------------------------
@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    """
    Custom admin configuration for the News model.

    Includes:
    - Display of key fields in the list view.
    - Search functionality for title and content.
    - Filtering by publication status, creation date, and tags.
    - Custom actions for bulk publishing and unpublishing.
    - Read-only fields for timestamps.
    """

    # Fields to display in the admin list view
    list_display = ('title', 'is_published', 'views', 'created_at', 'updated_at')

    # Filters to enable in the sidebar
    list_filter = ('is_published', 'created_at', 'tags')

    # Fields to enable search functionality
    search_fields = ('title', 'content')

    # Default ordering (newest first)
    ordering = ('-created_at',)

    # Fields editable directly in the list view
    list_editable = ('is_published',)

    # Adds date-based navigation in the admin panel
    date_hierarchy = 'created_at'

    # Fields that should be read-only
    readonly_fields = ('created_at', 'updated_at')

    # Custom actions for bulk operations
    actions = ['mark_as_published', 'mark_as_unpublished']

    def mark_as_published(self, request, queryset):
        """
        Custom action to mark selected news articles as published.
        """
        queryset.update(is_published=True)
        self.message_user(request, f"{queryset.count()} articles marked as published.")

    def mark_as_unpublished(self, request, queryset):
        """
        Custom action to mark selected news articles as unpublished.
        """
        queryset.update(is_published=False)
        self.message_user(request, f"{queryset.count()} articles marked as unpublished.")

    # Descriptions for custom actions
    mark_as_published.short_description = "Mark selected articles as published"
    mark_as_unpublished.short_description = "Mark selected articles as unpublished"


# -------------------------------
# Admin Configuration for Page
# -------------------------------
@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    """
    Custom admin configuration for the Page model.

    Includes:
    - Display of key fields in the list view.
    - Search functionality for title and content.
    - Auto-generation of the slug field based on the title.
    - Filtering by activity status and creation date.
    - Read-only fields for timestamps.
    """

    # Fields to display in the admin list view
    list_display = ('title', 'slug', 'is_active', 'created_at', 'updated_at')

    # Fields to enable search functionality
    search_fields = ('title', 'content')

    # Automatically populate the slug field based on the title
    prepopulated_fields = {'slug': ('title',)}

    # Filters to enable in the sidebar
    list_filter = ('is_active', 'created_at')

    # Default ordering (newest first)
    ordering = ('-created_at',)

    # Fields editable directly in the list view
    list_editable = ('is_active',)

    # Adds date-based navigation in the admin panel
    date_hierarchy = 'created_at'

    # Fields that should be read-only
    readonly_fields = ('created_at', 'updated_at')
