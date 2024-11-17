from django.db import models


class BikeTrail(models.Model):
    name = models.CharField(
        max_length=100
    )
    description = models.TextField(
        blank=True,
        null=True
    )
    length_km = models.FloatField()
    difficulty = models.CharField(
        max_length=50,
        choices=[
            ('easy', 'Easy'),
            ('medium', 'Medium'),
            ('hard', 'Hard'),
        ])
    location = models.CharField(
        max_length=255
    )

    def __str__(self):
        return self.name
