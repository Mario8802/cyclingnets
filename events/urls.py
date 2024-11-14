from django.urls import path
from .views import EventListView, EventCreateView, rsvp_event

urlpatterns = [
    path('', EventListView.as_view(), name='event_list'),  # List Events
    path('create/', EventCreateView.as_view(), name='event_create'),  # Create Event
    path('<int:event_id>/rsvp/', rsvp_event, name='event_rsvp'),  # RSVP to Event
]
