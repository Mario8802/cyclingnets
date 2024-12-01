from django.contrib import admin
from .models import Participation, Event


# Admin customization for the Participation model
@admin.register(Participation)
class ParticipationAdmin(admin.ModelAdmin):
    """
    Custom admin configuration for the Participation model.

    This allows admins to manage Participation records with enhanced UI features such as
    list display, filters, and search functionality.
    """
    # Fields to display in the admin list view
    list_display = ['user', 'event', 'status', 'created_at']

    # Fields to filter by in the admin interface (filter panel on the right)
    list_filter = ['status', 'created_at']

    # Fields that are searchable in the admin interface
    # Enables searching by username of the user and title of the event
    search_fields = ['user__username', 'event__title']


# Admin customization for the Event model
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    """
    Custom admin configuration for the Event model.

    This allows admins to manage Event records with enhanced UI features such as
    list display, filters, and search functionality.
    """
    # Fields to display in the admin list view
    list_display = ['title', 'date', 'location', 'organizer']

    # Fields to filter by in the admin interface (filter panel on the right)
    list_filter = ['date', 'location']

    # Fields that are searchable in the admin interface
    # Enables searching by title, location, and username of the organizer
    search_fields = ['title', 'location', 'organizer__username']
