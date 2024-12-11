from django.test import TestCase
from bike_connect.apps.core.models import News, Page
from django.urls import reverse


class NewsModelTest(TestCase):
    """
    Tests for the News model.
    """

    def setUp(self):
        """
        Create a sample News instance for testing.
        """
        self.news = News.objects.create(
            title="Test News Title",
            content="This is a test content for the news.",
        )

    def test_news_string_representation(self):
        """
        Test that the __str__ method returns the title of the news.
        """
        self.assertEqual(str(self.news), "Test News Title")

    def test_news_absolute_url(self):
        """
        Test that get_absolute_url returns the correct URL for a news instance.
        """
        expected_url = reverse('core:news_detail', kwargs={'pk': self.news.pk})
        self.assertEqual(self.news.get_absolute_url(), expected_url)

    def test_news_defaults(self):
        """
        Test that default values are set correctly for a news instance.
        """
        self.assertTrue(self.news.is_published)  # Default is True
        self.assertEqual(self.news.views, 0)    # Default value
        self.assertIsNone(self.news.image)      # Not provided


class PageModelTest(TestCase):
    """
    Tests for the Page model.
    """

    def setUp(self):
        """
        Create a sample Page instance for testing.
        """
        self.page = Page.objects.create(
            title="Test Page Title",
            slug="test-page-title",
        )

    def test_page_string_representation(self):
        """
        Test that the __str__ method returns the title of the page.
        """
        self.assertEqual(str(self.page), "Test Page Title")

    def test_page_absolute_url(self):
        """
        Test that get_absolute_url returns the correct URL for a page instance.
        """
        expected_url = reverse('core:page_detail', kwargs={'slug': self.page.slug})
        self.assertEqual(self.page.get_absolute_url(), expected_url)

    def test_page_defaults(self):
        """
        Test that default values are set correctly for a page instance.
        """
        self.assertTrue(self.page.is_active)  # Default is True
