from django.urls import path
from .views import (
    EventListView, EventCreateView, EventUpdateView, EventDeleteView,
    EventDetailView, AboutView, join_or_leave_event,
    StoryListView, StoryCreateView, ExperienceCreateView
)

app_name = 'events'

urlpatterns = [
    path('list/', EventListView.as_view(), name='event_list'),
    path('create/', EventCreateView.as_view(), name='event_create'),
    path('<int:pk>/edit/', EventUpdateView.as_view(), name='event_edit'),
    path('<int:pk>/delete/', EventDeleteView.as_view(), name='event_delete'),
    path('<int:pk>/detail/', EventDetailView.as_view(), name='event_detail'),
    path('<int:event_id>/join/', join_or_leave_event, name='join_or_leave_event'),
    path('about/', AboutView.as_view(), name='about'),
    path('stories/', StoryListView.as_view(), name='story_list'),
    path('stories/create/', StoryCreateView.as_view(), name='story_create'),
    path('experiences/create/<int:event_id>/', ExperienceCreateView.as_view(), name='experience_create'),
]
