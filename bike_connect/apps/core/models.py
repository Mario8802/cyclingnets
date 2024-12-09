from django.db import models
from django.urls import reverse

from bike_connect.storages import MediaStorage


# -------------------------------
# News Model
# -------------------------------
class News(models.Model):
    """
    Represents a news article with support for tags and views count.
    """
    title = models.CharField(max_length=200, verbose_name="Title")
    content = models.TextField(verbose_name="Content")
    image = models.ImageField(
        upload_to='news_images/',
        storage=MediaStorage(),
        blank=True,
        null=True,
        max_length=255,
        verbose_name="Image",
    )
    is_published = models.BooleanField(default=True, verbose_name="Published")
    views = models.PositiveIntegerField(default=0, verbose_name="Views Count")
    tags = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="Tags",
        help_text="Comma-separated tags for the news article."
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('core:news_detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['-created_at']



# -------------------------------
# Page Model
# -------------------------------
class Page(models.Model):
    """
    Represents a static page in the application.

    Attributes:
        title (CharField): The title of the static page (max 200 characters).
        slug (SlugField): A unique URL-friendly identifier for the page.
        content (TextField): The main content of the static page.
        is_active (BooleanField): Indicates if the page is active or archived.
        created_at (DateTimeField): Timestamp of when the page was created (auto-set).
        updated_at (DateTimeField): Timestamp of the last update to the page (auto-updated).
    """
    title = models.CharField(
        max_length=200,
        verbose_name="Title"
    )  # Title of the static page

    slug = models.SlugField(
        unique=True,
        verbose_name="Slug"
    )  # Unique URL identifier

    content = models.TextField(
        verbose_name="Content"
    )  # Main content of the static page

    is_active = models.BooleanField(
        default=True, verbose_name="Active"
    )  # Manage active/archive state

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Created At"
    )  # Set on creation

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Updated At"
    )  # Auto-updated on save

    def __str__(self):
        """
        String representation of the Page object.
        Returns:
            str: The title of the static page.
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
        ordering = ['title']  # Default ordering by title
        verbose_name = 'Static Page'
        verbose_name_plural = 'Static Pages'
