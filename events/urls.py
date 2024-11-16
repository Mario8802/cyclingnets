from django.urls import path
from .views import EventListView, EventCreateView, rsvp_event
from .views import EventUpdateView
from .views import EventDeleteView

urlpatterns = [
    path('', EventListView.as_view(), name='event_list'),  # List Events
    path('create/', EventCreateView.as_view(), name='event_create'),  # Create Event
    path('<int:event_id>/rsvp/', rsvp_event, name='event_rsvp'),
    path('<int:pk>/edit/', EventUpdateView.as_view(), name='event_edit'),
    path('<int:pk>/delete/', EventDeleteView.as_view(), name='event_delete'),
    ]


