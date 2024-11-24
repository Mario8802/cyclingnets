from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import (
    EventListView, EventCreateView, EventUpdateView, EventDeleteView,
    EventDetailView, EventViewSet, AboutView, rsvp_event, upcoming_events
)

app_name = 'events'

router = DefaultRouter()
router.register(r'api/events', EventViewSet)

urlpatterns = [
    path('', EventListView.as_view(), name='event_list'),
    path('create/', EventCreateView.as_view(), name='event_create'),
    path('<int:pk>/edit/', EventUpdateView.as_view(), name='event_edit'),
    path('<int:pk>/delete/', EventDeleteView.as_view(), name='event_delete'),
    path('<int:pk>/detail/', EventDetailView.as_view(), name='event_detail'),
    path('<int:event_id>/rsvp/', rsvp_event, name='event_rsvp'),
    path('about/', AboutView.as_view(), name='about'),
    path('api/upcoming-events/', upcoming_events, name='upcoming_events'),
]

urlpatterns += router.urls
