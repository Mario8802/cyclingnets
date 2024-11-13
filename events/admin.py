from django.contrib import admin
from .models import Event, Booking
from .models import TestModel

admin.site.register(TestModel)

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'date', 'location']
    search_fields = ['title', 'location']
    list_filter = ['date']

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['user', 'event', 'status', 'booking_date']
    list_filter = ['status', 'booking_date']
