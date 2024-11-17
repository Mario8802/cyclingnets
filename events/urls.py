from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import (
    EventListView, EventCreateView, EventUpdateView, EventDeleteView,
    EventDetailView, EventViewSet, AboutView, rsvp_event, upcoming_events
)

# Initialize API Router
router = DefaultRouter()
router.register(r'api/events', EventViewSet)

# URL Patterns
urlpatterns = [
    # List of events
    path('', EventListView.as_view(), name='event_list'),
    # Create an event
    path('create/', EventCreateView.as_view(), name='event_create'),
    # Update event
    path('<int:pk>/edit/', EventUpdateView.as_view(), name='event_edit'),
    # Delete event
    path('<int:pk>/delete/', EventDeleteView.as_view(), name='event_delete'),
    # Event details
    path('<int:pk>/detail/', EventDetailView.as_view(), name='event_detail'),
    # RSVP to event
    path('<int:event_id>/rsvp/', rsvp_event, name='event_rsvp'),
    # About page
    path('about/', AboutView.as_view(), name='about'),
    # API endpoint for upcoming events
    path('api/upcoming-events/', upcoming_events, name='upcoming_events'),
]

# Append API Routes (for DRF ViewSet)
urlpatterns += router.urls
