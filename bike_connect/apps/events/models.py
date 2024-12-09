from django.core.files.storage import default_storage
from django.db import models
from django.contrib.auth import get_user_model
from bike_connect.storages import MediaStorage

# Get the custom User model for use in ForeignKey relationships
User = get_user_model()


class Event(models.Model):
    """
    Represents a cycling or related event in the application.
    """
    title = models.CharField(
        max_length=200,
        verbose_name="Event Title",
        help_text="Enter the title of the event (max 200 characters)."
    )
    description = models.TextField(
        verbose_name="Event Description",
        help_text="Provide a detailed description of the event."
    )
    date = models.DateField(
        verbose_name="Event Date",
        help_text="Specify the date when the event will take place."
    )
    location = models.CharField(
        max_length=200,
        verbose_name="Event Location",
        help_text="Enter the location of the event (max 200 characters)."
    )
    image = models.ImageField(
        upload_to='events/',
        storage=MediaStorage(),
        blank=True,
        null=True,
        max_length=255,
        verbose_name="Event Image",
        help_text="Optional image for the event."
    )

    def save_image_to_s3(self, uploaded_file):
        """
        Качва изображение в S3 и връща публичния URL.
        """
        try:
            file_path = default_storage.save(f'events/{uploaded_file.name}', uploaded_file)
            return default_storage.url(file_path)
        except Exception as e:
            raise ValueError(f"Failed to upload file: {e}")


    organizer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='organized_events',
        verbose_name="Event Organizer",
        help_text="The user organizing the event. The event will be deleted if the organizer is removed."
    )

    class Meta:
        verbose_name = "Event"
        verbose_name_plural = "Events"
        ordering = ['-date']  # Default ordering by event date (descending)


    def get_image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
        return None


    def __str__(self):
        """
        String representation of the Event object.
        Returns the event title.
        """
        return self.title


class Participation(models.Model):
    """
    Tracks user participation in events.
    """
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='participations',
        verbose_name="Participant",
        help_text="The user participating in the event."
    )
    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        related_name='participants',
        verbose_name="Event",
        help_text="The event the user is participating in."
    )
    status = models.CharField(
        max_length=20,
        choices=[('joined', 'Joined'), ('cancelled', 'Cancelled')],
        default='joined',
        verbose_name="Participation Status",
        help_text="The user's participation status ('joined' or 'cancelled')."
    )
    comment = models.TextField(
        blank=True,
        null=True,
        verbose_name="Comment",
        help_text="Optional comment about the user's participation."
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Participation Created At",
        help_text="Timestamp when the participation was created."
    )

    class Meta:
        verbose_name = "Participation"
        verbose_name_plural = "Participations"
        unique_together = ('user', 'event')  # Prevent duplicate participations for the same user and event

    def __str__(self):
        """
        String representation of the Participation object.
        Returns a formatted string showing the user and the event title.
        """
        return f"{self.user.username} -> {self.event.title}"
