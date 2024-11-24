from django.contrib import admin
from .models import BikeTrail

@admin.register(BikeTrail)
class BikeTrailAdmin(admin.ModelAdmin):
    list_display = ['name', 'length_km', 'difficulty', 'location']
    search_fields = ['name', 'location']
    list_filter = ['difficulty']
