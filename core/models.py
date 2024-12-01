from django.db import models

# -------------------------------
# News Model
# -------------------------------
class News(models.Model):
    """
    Represents a news article in the application.

    Attributes:
        title (CharField): The title of the news article (max 200 characters).
        content (TextField): The main content of the news article.
        image (ImageField): Optional image associated with the news, stored in 'news_images/'.
        created_at (DateTimeField): Timestamp of when the news was created (auto-set).
        updated_at (DateTimeField): Timestamp of the last update to the news (auto-updated).
    """
    title = models.CharField(max_length=200)  # Title of the news article
    content = models.TextField()  # Main content of the news article
    image = models.ImageField(upload_to='news_images/', blank=True, null=True)  # Optional associated image
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set on creation
    updated_at = models.DateTimeField(auto_now=True)  # Automatically updated on save

    def __str__(self):
        """
        String representation of the News object.
        Returns:
            str: The title of the news article.
        """
        return self.title


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
        created_at (DateTimeField): Timestamp of when the page was created (auto-set).
        updated_at (DateTimeField): Timestamp of the last update to the page (auto-updated).
    """
    title = models.CharField(max_length=200)  # Title of the static page
    slug = models.SlugField(unique=True)  # Unique URL identifier
    content = models.TextField()  # Main content of the static page
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set on creation
    updated_at = models.DateTimeField(auto_now=True)  # Automatically updated on save

    def __str__(self):
        """
        String representation of the Page object.
        Returns:
            str: The title of the static page.
        """
        return self.title
