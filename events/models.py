from django.db import models
from django.conf import settings
from django.utils.timezone import now


class Booking(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='bookings'
    )
    event = models.ForeignKey(
        'Event',
        on_delete=models.CASCADE,
        related_name='bookings'
    )
    booking_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (f"{self.user.username} booked"
                f" {self.event.title} on {self.booking_date}")


class Event(models.Model):
    title = models.CharField(
        max_length=255
    )
    date = models.DateField()
    location = models.CharField(
        max_length=255
    )
    description = models.TextField(
        blank=True, null=True
    )
    organizer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='organized_events'
    )
    participants = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='participating_events',
        blank=True
    )

    image = models.ImageField(
        upload_to="event_images/",
        blank=True,
        null=True,
        default="static/login/images/login_bike.jpg"
    )
    created_at = models.DateTimeField(default=now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date']

