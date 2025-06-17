from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

# Import views and routers
from cyclingnets.bike_connect.apps.events.views import EventViewSet  # Event API viewset
from cyclingnets.bike_connect.apps.users.views import logout_view   # Custom logout view
from cyclingnets.bike_connect.apps.core.views import landing_page, custom_404_view  # Landing page and custom 404 view
from cyclingnets.bike_connect.apps.posts import views               # Placeholder import for clarity

# -------------------------------
# REST Framework Router
# -------------------------------
# Registers the EventViewSet with the API under the 'api/events' endpoint.
router = DefaultRouter()
router.register(r'api/events', EventViewSet, basename='event')

# -------------------------------
# URL Patterns
# -------------------------------
# Define all URL patterns for the project.
urlpatterns = [
    # Landing page (e.g., http://127.0.0.1:8000/)
    path('', landing_page, name='home'),

    # Core app URLs (e.g., http://127.0.0.1:8000/core/)
    path('core/', include('bike_connect.apps.core.urls')),

    # Admin panel (e.g., http://127.0.0.1:8000/admin/)
    path('admin/', admin.site.urls),

    # User management URLs (e.g., http://127.0.0.1:8000/users/)
    path('users/', include('bike_connect.apps.users.urls')),

    # Posts app URLs (e.g., http://127.0.0.1:8000/posts/)
    path('posts/', include('bike_connect.apps.posts.urls')),

    # Events app URLs (e.g., http://127.0.0.1:8000/events/)
    path('events/', include('bike_connect.apps.events.urls')),

    # Custom logout route (e.g., http://127.0.0.1:8000/logout/)
    path('logout/', logout_view, name='logout'),

    # REST API endpoints (e.g., http://127.0.0.1:8000/api/events/)
    path('api/', include(router.urls)),
]

# -------------------------------
# Serving Media Files (Development Only)
# -------------------------------
# When DEBUG is enabled, add routes to serve media files (e.g., uploaded images).
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# -------------------------------
# Custom Error Handlers
# -------------------------------
# Register the custom 404 handler
handler404 = 'bike_connect.apps.core.views.custom_404_view'
