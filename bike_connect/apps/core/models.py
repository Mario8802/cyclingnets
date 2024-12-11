from django.db import models
from django.urls import reverse
from bike_connect.storages import MediaStorage


# -------------------------------
# News Model
# -------------------------------
class News(models.Model):
    """
    Represents a news article with optional tags, views count, and an image.
    """

    # Title of the news article, limited to 200 characters
    title = models.CharField(
        max_length=200,
        verbose_name="Title"  # User-friendly label for the field
    )

    # Main content of the news article
    content = models.TextField(
        verbose_name="Content"  # User-friendly label for the field
    )

    # Optional image for the news article, stored using a custom storage backend
    image = models.ImageField(
        upload_to='news_images/',  # Directory where images will be uploaded
        storage=MediaStorage(),  # Custom storage class for handling media files
        blank=True,  # Allows this field to be optional
        null=True,  # Allows null values in the database
        max_length=255,
        verbose_name="Image"  # User-friendly label for the field
    )

    # Boolean flag indicating whether the news article is published
    is_published = models.BooleanField(
        default=True,
        verbose_name="Published"  # User-friendly label for the field
    )

    # Counter for the number of views the article has received
    views = models.PositiveIntegerField(
        default=0,
        verbose_name="Views Count"  # User-friendly label for the field
    )

    # Comma-separated tags for categorizing the article
    tags = models.CharField(
        max_length=255,
        blank=True,  # Allows this field to be optional
        null=True,  # Allows null values in the database
        verbose_name="Tags",  # User-friendly label for the field
        help_text="Comma-separated tags for the news article."  # Guidance for users
    )

    # Timestamp when the article was created (auto-set)
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Created At"  # User-friendly label for the field
    )

    # Timestamp when the article was last updated (auto-updated)
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Updated At"  # User-friendly label for the field
    )

    def __str__(self):
        """
        Returns the string representation of the News object.
        """
        return self.title

    def get_absolute_url(self):
        """
        Returns the URL to the detail view of the news article.
        """
        return reverse('core:news_detail', kwargs={'pk': self.pk})

    class Meta:
        """
        Meta options for the News model.
        """
        ordering = ['-created_at']  # Default ordering: newest articles first


# -------------------------------
# Page Model
# -------------------------------
class Page(models.Model):
    """
    Represents a static page in the application.
    """

    # Title of the static page, limited to 200 characters
    title = models.CharField(
        max_length=200,
        verbose_name="Title"  # User-friendly label for the field
    )

    # Unique, URL-friendly identifier for the page
    slug = models.SlugField(
        unique=True,
        verbose_name="Slug"  # User-friendly label for the field
    )

    # Main content of the static page
    content = models.TextField(
        verbose_name="Content"  # User-friendly label for the field
    )

    # Boolean flag indicating if the page is active or archived
    is_active = models.BooleanField(
        default=True,
        verbose_name="Active"  # User-friendly label for the field
    )

    # Timestamp when the page was created (auto-set)
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Created At"  # User-friendly label for the field
    )

    # Timestamp when the page was last updated (auto-updated)
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Updated At"  # User-friendly label for the field
    )

    def __str__(self):
        """
        Returns the string representation of the Page object.
        """
        return self.title

    def get_absolute_url(self):
        """
        Returns the URL to the detail view of the static page.
        """
        return reverse('core:page_detail', kwargs={'slug': self.slug})

    class Meta:
        """
        Meta options for the Page model.
        """
        ordering = ['title']  # Default ordering: alphabetically by title
        verbose_name = 'Static Page'  # Singular name in the admin panel
        verbose_name_plural = 'Static Pages'  # Plural name in the admin panel
