from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from events.views import EventViewSet  # Import the EventViewSet for the API
from users.views import logout_view   # Custom logout view
from core.views import landing_page   # Landing page view

# REST framework router for Event API
# Registers the EventViewSet with the router under the 'api/events' endpoint.
router = DefaultRouter()
router.register(r'api/events', EventViewSet, basename='event')

# Define all URL patterns for the project
urlpatterns = [
    # Landing page route (e.g., http://127.0.0.1:8000/)
    path('', landing_page, name='home'),

    # Include URLs from the core app (e.g., http://127.0.0.1:8000/core/)
    path('core/', include('core.urls')),

    # Admin panel route (e.g., http://127.0.0.1:8000/admin/)
    path('admin/', admin.site.urls),

    # Include URLs from the users app (e.g., http://127.0.0.1:8000/users/)
    path('users/', include('users.urls')),

    # Include URLs from the posts app (e.g., http://127.0.0.1:8000/posts/)
    path('posts/', include('posts.urls')),

    # Include URLs from the events app (e.g., http://127.0.0.1:8000/events/)
    path('events/', include('events.urls')),

    # Custom logout route (e.g., http://127.0.0.1:8000/logout/)
    path('logout/', logout_view, name='logout'),

    # Include REST framework router URLs (e.g., http://127.0.0.1:8000/api/events/)
    path('api/', include(router.urls)),
]

# Serve media files during development
# In DEBUG mode, add routes to serve media files (e.g., uploaded images).
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
