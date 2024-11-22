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
    title = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='buy')
    posted_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)



class Post(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


