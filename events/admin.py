from django.contrib import admin
from .models import Participation, Event, Story, Experience


@admin.register(Participation)
class ParticipationAdmin(admin.ModelAdmin):
    # Admin display for Participation model
    list_display = ['user', 'event', 'status', 'created_at']
    list_filter = ['status', 'created_at']
    search_fields = ['user__username', 'event__title']


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    # Admin display for Event model
    list_display = ['title', 'date', 'location', 'organizer']
    list_filter = ['date', 'location']
    search_fields = ['title', 'location', 'organizer__username']


@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    # Admin display for Story model
    list_display = ['title', 'author', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title', 'author__username']


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    # Admin display for Experience model
    list_display = ['event', 'participant', 'rating', 'created_at']
    list_filter = ['rating', 'created_at']
    search_fields = ['event__title', 'participant__user__username']
