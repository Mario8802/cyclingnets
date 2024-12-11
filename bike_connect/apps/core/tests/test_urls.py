from django.test import SimpleTestCase
from django.urls import reverse, resolve
from bike_connect.apps.core.views import landing_page
from bike_connect.apps.users.views import logout_view
from rest_framework.routers import DefaultRouter
from bike_connect.apps.events.views import EventViewSet


class TestUrls(SimpleTestCase):
    """
    Tests for the main urls.py file to ensure proper route resolutions.
    """

    def test_landing_page_url(self):
        """
        Test that the landing page URL resolves correctly.
        """
        url = reverse('home')  # Replace 'home' with the actual name of the landing page URL pattern
        self.assertEqual(resolve(url).func, landing_page)

    def test_logout_url(self):
        """
        Test that the logout URL resolves correctly.
        """
        url = reverse('logout')  # Replace 'logout' with the actual name of the logout URL pattern
        self.assertEqual(resolve(url).func, logout_view)

    def test_api_events_url(self):
        """
        Test that the EventViewSet is registered correctly with the router.
        """
        router = DefaultRouter()
        router.register(r'api/events', EventViewSet, basename='event')
        url = '/api/events/'  # Base URL for the API endpoint
        match = resolve(url)
        self.assertEqual(match.route, 'api/events/')

    def test_admin_url(self):
        """
        Test that the admin URL resolves correctly.
        """
        url = reverse('admin:index')  # Django admin default URL pattern
        self.assertTrue(resolve(url))
