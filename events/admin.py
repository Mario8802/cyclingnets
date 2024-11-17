from django.contrib import admin
from .models import Event, Booking, TestModel


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'location')
    list_filter = ('date', 'location')
    search_fields = ('title',)


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'event', 'status', 'booking_date')
    list_filter = ('status', 'booking_date')
    search_fields = ('user__username', 'event__title')


@admin.register(TestModel)
class TestModelAdmin(admin.ModelAdmin):
    list_display = ('title',)
