from django.conf import settings
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class BikePost(models.Model):
    CATEGORY_CHOICES = [
        ('buy', 'Buy'),
        ('sell', 'Sell'),
        ('repair', 'Repair'),
        ('accessories', 'Accessories'),
    ]

    CONDITION_CHOICES = [
        ('new', 'New'),
        ('used', 'Used'),
        ('refurbished', 'Refurbished'),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='buy')
    condition = models.CharField(max_length=15, choices=CONDITION_CHOICES, blank=True, null=True)  # Optional
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)  # Optional
    location = models.CharField(max_length=100, blank=True, null=True)  # Optional
    image = models.ImageField(upload_to='bike_posts/', blank=True, null=True)  # Image support
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.category})"
