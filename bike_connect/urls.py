from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter
from events.views import EventViewSet
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views


app_name = 'posts'
router = DefaultRouter()
router.register(r'api/events', EventViewSet)
urlpatterns = [
    path('', TemplateView.as_view(template_name='core/landing_page.html'), name='landing_page'),
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('posts/', include('posts.urls')),
    path('events/', include('events.urls')),
    path('', include('core.urls')),
    path('', include(router.urls)),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
