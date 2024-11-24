from django.contrib import admin
from .models import Booking, Event

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['user', 'event', 'booking_date']
    list_filter = ['booking_date']
    search_fields = ['user__username', 'event__title']  # Добавено поле за търсене

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'date', 'location', 'organizer']
    list_filter = ['date']
    search_fields = ['title', 'location', 'organizer__username']  # Добавено поле за търсене
