from django.contrib import admin
from .models import Booking, Event


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['user', 'event', 'booking_date']  # Removed 'status'
    list_filter = ['booking_date']  # Removed 'status'

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'date', 'location', 'organizer']
    list_filter = ['date']



