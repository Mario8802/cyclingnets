from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter
from events import views
from events.views import EventViewSet
from users import views
from users.views import logout_view

# REST framework router for Event API
router = DefaultRouter()
router.register(r'api/events', EventViewSet, basename='event')

urlpatterns = [
    # Основна страница (home)
    path('', TemplateView.as_view(template_name='core/landing_page.html'), name='home'),

    # Админ панел
    path('admin/', admin.site.urls),

    # Приложения
    path('users/', include('users.urls')),  # URL-ове за потребители
    path('posts/', include('posts.urls')),  # URL-ове за публикации
    path('events/', include('events.urls')),  # URL-ове за събития

    # Logout с пренасочване
    path('logout/', logout_view, name='logout'),
    path('stories/', include('events.urls', namespace='stories')),
    path('experiences/', include('events.urls', namespace='experiences')),
]

# Добавяне на API маршрути
urlpatterns += router.urls

# Обслужване на медийни файлове в DEBUG режим
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
