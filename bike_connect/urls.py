from django.contrib.auth.views import LogoutView
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter
from events.views import EventViewSet
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


app_name = 'bike_connect'

# REST framework router for Event API
router = DefaultRouter()
router.register(r'api/events', EventViewSet)

urlpatterns = [
    path('', TemplateView.as_view(template_name='core/landing_page.html'), name='landing_page'),
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),  # Include user-related URLs
    path('posts/', include('posts.urls')),  # Include posts-related URLs
    path('events/', include('events.urls')),  # Include event-related URLs
    path('logout/', LogoutView.as_view(next_page='landing_page'), name='logout'),  # Logout URL
]

# Include API router URLs
urlpatterns += router.urls

# Add media files in DEBUG mode
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
