from django.db import models
from django.contrib.auth import get_user_model

# Get the custom User model for use in ForeignKey relationships
User = get_user_model()

class Event(models.Model):
    """
    Represents a cycling or related event in the application.

    Attributes:
        title (CharField): The name of the event.
        description (TextField): A detailed description of the event.
        date (DateField): The date when the event is scheduled to occur.
        location (CharField): The location where the event will take place.
        image (ImageField): An optional image associated with the event, stored in the 'events/' directory.
        organizer (ForeignKey): The user who created the event; deletes the event if the organizer is removed.
    """
    title = models.CharField(max_length=200)  # Event title, max 200 characters
    description = models.TextField()  # Detailed description of the event
    date = models.DateField()  # Event date
    location = models.CharField(max_length=200)  # Event location, max 200 characters
    image = models.ImageField(upload_to='events/', blank=True, null=True)  # Optional event image
    organizer = models.ForeignKey(
        User,
        on_delete=models.CASCADE  # Delete the event if the organizer is deleted
    )

    def __str__(self):
        """
        String representation of the Event object.
        Returns the event title.
        """
        return self.title


class Participation(models.Model):
    """
    Tracks user participation in events.

    Attributes:
        user (ForeignKey): The user who is participating in the event.
        event (ForeignKey): The event the user is participating in, with a reverse relation 'participants'.
        status (CharField): The user's participation status, either 'joined' or 'cancelled'.
        comment (TextField): An optional comment about the user's participation.
        created_at (DateTimeField): The timestamp when the participation was created.
    """
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE  # Delete participation if the user is deleted
    )
    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,  # Delete participation if the event is deleted
        related_name='participants'  # Enables reverse lookup from the Event model
    )
    status = models.CharField(
        max_length=20,  # Maximum length for status field
        choices=[('joined', 'Joined'), ('cancelled', 'Cancelled')],  # Available choices for status
        default='joined'  # Default status is 'joined'
    )
    comment = models.TextField(blank=True, null=True)  # Optional comment for additional context
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set the timestamp on creation

    def __str__(self):
        """
        String representation of the Participation object.
        Returns a formatted string showing the user and the event title.
        """
        return f"{self.user.username} -> {self.event.title}"
