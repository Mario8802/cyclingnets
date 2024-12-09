from django.urls import path
from .views import (
    EventListView, EventCreateView, EventUpdateView, EventDeleteView,
    EventDetailView, join_event, leave_event
)

# Namespace for the events app URLs
app_name = 'events'

# Define URL patterns for the events app
urlpatterns = [
    # List view for events
    path('list/', EventListView.as_view(), name='event_list'),
    # URL: /events/list/
    # Displays a list of all events.

    # Create view for events
    path('create/', EventCreateView.as_view(), name='event_create'),
    # URL: /events/create/
    # Allows users to create a new event.

    # Update view for editing an event
    path('<int:pk>/edit/', EventUpdateView.as_view(), name='event_edit'),
    # URL: /events/<event_id>/edit/
    # Allows the organizer to edit an existing event, identified by its primary key (pk).

    # Delete view for removing an event
    path('<int:pk>/delete/', EventDeleteView.as_view(), name='event_delete'),
    # URL: /events/<event_id>/delete/
    # Allows the organizer to delete an event, identified by its primary key (pk).

    # Detail view for a specific event
    path('<int:pk>/detail/', EventDetailView.as_view(), name='event_detail'),
    # URL: /events/<event_id>/detail/
    # Displays detailed information about a specific event, identified by its primary key (pk).

    # Action for joining an event
    path('<int:event_id>/join/', join_event, name='join_event'),
    # URL: /events/<event_id>/join/
    # Allows a user to join a specific event.

    # Action for leaving an event
    path('<int:event_id>/leave/', leave_event, name='leave_event'),
    # URL: /events/<event_id>/leave/
    # Allows a user to leave a specific event.
]
