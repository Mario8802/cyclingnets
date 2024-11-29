from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from events.views import EventViewSet
from users.views import logout_view
from core.views import landing_page

# REST framework router for Event API
router = DefaultRouter()
router.register(r'api/events', EventViewSet, basename='event')

urlpatterns = [
    path('', landing_page, name='home'),

    path('admin/', admin.site.urls),

    path('users/', include('users.urls')),

    path('posts/', include('posts.urls')),

    path('events/', include('events.urls')),

    path('logout/', logout_view, name='logout'),

    path('api/', include(router.urls)),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
