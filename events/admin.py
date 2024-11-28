from django.contrib import admin
from .models import Participation, Event


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


