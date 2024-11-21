from django.db import models
from django.contrib.auth import get_user_model
from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
from django.conf import settings

class Booking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='bookings')
    event = models.ForeignKey('Event', on_delete=models.CASCADE, related_name='bookings')
    booking_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} booked {self.event.title} on {self.booking_date}"


class Event(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateField()
    location = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)  # Add this if it's missing
    organizer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='organized_events')
    participants = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='participating_events', blank=True)

    def __str__(self):
        return self.title




class TestModel(models.Model):
    title = models.CharField(
        max_length=100
    )
    # models.py (Event model)
    image = models.ImageField(
        upload_to="event_images/",
        blank=True,
        null=True,
        default="images/default_event.jpg"
    )

    def __str__(self):
        return self.title
