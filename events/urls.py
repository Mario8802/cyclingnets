from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EventListView, EventCreateView, rsvp_event, AboutView
from .views import EventUpdateView
from .views import EventDeleteView
from .views import EventViewSet

router = DefaultRouter()
router.register(r'api/events', EventViewSet)

urlpatterns = [
    path('', EventListView.as_view(), name='event_list'),
    path('create/', EventCreateView.as_view(), name='event_create'),
    path('<int:event_id>/rsvp/', rsvp_event, name='event_rsvp'),
    path('<int:pk>/edit/', EventUpdateView.as_view(), name='event_edit'),
    path('<int:pk>/delete/', EventDeleteView.as_view(), name='event_delete'),
    path('<int:event_id>/rsvp/', rsvp_event, name='event_rsvp'),
    path('about/', AboutView.as_view(), name='about'),
    ]

urlpatterns += router.urls
