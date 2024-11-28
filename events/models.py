from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Event(models.Model):
    # Represents an event created by an organizer
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    location = models.CharField(max_length=200)
    image = models.ImageField(upload_to='events/', blank=True, null=True)
    organizer = models.ForeignKey(User, on_delete=models.CASCADE)  # The creator of the event

    def __str__(self):
        return self.title


class Participation(models.Model):
    # Tracks user participation in events
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='participants')
    status = models.CharField(
        max_length=20,
        choices=[('joined', 'Joined'), ('cancelled', 'Cancelled')],
        default='joined'
    )
    comment = models.TextField(blank=True, null=True)  # Optional comment
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} -> {self.event.title}"


