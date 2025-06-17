from django.test import TestCase
from django.urls import reverse
from django.utils.timezone import now
from cyclingnets.bike_connect.apps.core.models import News, Page
from cyclingnets.bike_connect.apps.events.models import Event
from django.contrib.auth.models import User


class NewsViewsTest(TestCase):
    """
    Simplified tests for News views: list, detail, create, update, and delete.
    """

    def setUp(self):
        # Create a staff user for privileged actions
        self.staff_user = User.objects.create_user(username='staff', password='password123', is_staff=True)
        # Create some sample news articles
        self.news_1 = News.objects.create(title="News 1", content="Content for news 1", is_published=True)
        self.news_2 = News.objects.create(title="News 2", content="Content for news 2", is_published=False)

    def test_news_list_view(self):
        # Test that only published news appears in the list
        response = self.client.get(reverse('core:news_list'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(self.news_1, response.context['news_list'])
        self.assertNotIn(self.news_2, response.context['news_list'])  # Unpublished news should not appear

    def test_news_detail_view(self):
        # Test that the news detail view increments the view count
        self.client.get(reverse('core:news_detail', kwargs={'pk': self.news_1.pk}))
        self.news_1.refresh_from_db()
        self.assertEqual(self.news_1.views, 1)

    def test_news_create_view(self):
        # Test that staff users can create news
        self.client.login(username='staff', password='password123')
        response = self.client.post(reverse('core:news_create'), {'title': 'New News', 'content': 'Test content'})
        self.assertEqual(response.status_code, 302)  # Redirects on success
        self.assertTrue(News.objects.filter(title='New News').exists())

    def test_news_update_view(self):
        # Test that staff users can update news
        self.client.login(username='staff', password='password123')
        self.client.post(reverse('core:news_update', kwargs={'pk': self.news_1.pk}),
                         {'title': 'Updated News', 'content': 'Updated content'})
        self.news_1.refresh_from_db()
        self.assertEqual(self.news_1.title, 'Updated News')

    def test_news_delete_view(self):
        # Test that staff users can delete news
        self.client.login(username='staff', password='password123')
        self.client.post(reverse('core:news_delete', kwargs={'pk': self.news_1.pk}))
        self.assertFalse(News.objects.filter(pk=self.news_1.pk).exists())


class PageViewsTest(TestCase):
    """
    Simplified tests for Page views.
    """

    def setUp(self):
        # Create a sample page
        self.page = Page.objects.create(title="About Us", slug="about-us", content="This is a test page.")

    def test_page_detail_view(self):
        # Test that the page detail view loads correctly
        response = self.client.get(reverse('core:page_detail', kwargs={'slug': self.page.slug}))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['page'], self.page)


class LandingPageTest(TestCase):
    """
    Simplified tests for the landing page view.
    """

    def setUp(self):
        # Create some sample events and news
        self.event_1 = Event.objects.create(name="Event 1", date=now())
        self.news_1 = News.objects.create(title="Published News", content="Content", is_published=True)

    def test_landing_page_view(self):
        # Test that the landing page loads and includes required context data
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('paginated_events', response.context)
        self.assertIn('news_list', response.context)
        self.assertIn(self.news_1, response.context['news_list'])  # Only published news appears
