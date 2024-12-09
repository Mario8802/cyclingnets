from django.conf import settings
from django.db import models
from django.contrib.auth import get_user_model

from bike_connect.storages import MediaStorage

# Fetch the custom user model (if defined) or the default User model
User = get_user_model()


class BikePost(models.Model):
    """
    Represents a post in a bike marketplace.

    A BikePost can be for buying, selling, repairing, or finding accessories for bikes.
    Each post has attributes like title, description, category, condition, price, location,
    and an optional image, as well as metadata like the user who posted it and the creation date.
    """

    # -------------------------------------------
    # Choices for category and condition
    # -------------------------------------------
    CATEGORY_CHOICES = [
        ('buy', 'Buy'),               # Post related to buying bikes
        ('sell', 'Sell'),             # Post related to selling bikes
        ('repair', 'Repair'),         # Post related to repairing bikes
        ('accessories', 'Accessories')  # Post related to bike accessories
    ]

    CONDITION_CHOICES = [
        ('new', 'New'),               # Brand-new bike
        ('used', 'Used'),             # Pre-owned bike
        ('refurbished', 'Refurbished')  # Refurbished bike
    ]

    # -------------------------------------------
    # Model Fields
    # -------------------------------------------

    # Title of the bike post
    title = models.CharField(
        max_length=100  # Maximum length for the title is 100 characters
    )

    # Detailed description of the post
    description = models.TextField()

    # Category of the post (e.g., Buy, Sell, Repair, Accessories)
    category = models.CharField(
        max_length=20,                # Maximum length for the category is 20 characters
        choices=CATEGORY_CHOICES,     # Limited to the predefined CATEGORY_CHOICES
        default='buy'                 # Default category is "Buy"
    )

    # Condition of the bike (e.g., New, Used, Refurbished)
    condition = models.CharField(
        max_length=15,                # Maximum length for the condition is 15 characters
        choices=CONDITION_CHOICES,    # Limited to the predefined CONDITION_CHOICES
        blank=True,                   # Optional field
        null=True                     # Allows NULL values in the database
    )

    # Price of the bike (optional)
    price = models.DecimalField(
        max_digits=10,                # Maximum number of digits is 10 (e.g., 99999999.99)
        decimal_places=2,             # Allows 2 decimal places for precision
        blank=True,                   # Optional field
        null=True                     # Allows NULL values in the database
    )

    # Location of the bike (optional)
    location = models.CharField(
        max_length=100,               # Maximum length for the location is 100 characters
        blank=True,                   # Optional field
        null=True                     # Allows NULL values in the database
    )

    # Optional image upload for the bike

    image = models.ImageField(
        upload_to='bike_posts/',
        storage=MediaStorage(),
        blank=True,
        null=True,
        max_length=255,
        verbose_name="Post Image",
        help_text="Optional image for the post."
    )



    # Reference to the user who posted this
    posted_by = models.ForeignKey(
        User,                         # Links to the user model (foreign key relationship)
        on_delete=models.CASCADE      # Deletes the post if the associated user is deleted
    )

    # Timestamp for when the post was created
    created_at = models.DateTimeField(
        auto_now_add=True             # Automatically sets the field to the current timestamp on creation
    )

    # -------------------------------------------
    # String Representation
    # -------------------------------------------
    def __str__(self):
        """
        String representation of the BikePost object.
        Returns:
            str: The title and category of the bike post.
        """
        return f"{self.title} ({self.category})"
