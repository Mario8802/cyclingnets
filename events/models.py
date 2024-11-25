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


class Story(models.Model):
    # User-submitted stories related to events
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='stories/', blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} by {self.author.username}"


class Experience(models.Model):
    # Participant feedback and ratings for an event
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='experiences')
    participant = models.ForeignKey(Participation, on_delete=models.CASCADE)
    feedback = models.TextField()
    rating = models.PositiveSmallIntegerField()  # Ratings between 1 and 5
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Experience for {self.event.title} by {self.participant.user.username}"
