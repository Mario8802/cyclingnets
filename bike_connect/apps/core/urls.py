from django.urls import path
from .views import (
    NewsListView, NewsDetailView, NewsCreateView, NewsUpdateView, NewsDeleteView,
    custom_404_view  # Import the custom 404 view
)
from .api_views import NewsListAPI, NewsDetailAPI

app_name = 'core'

urlpatterns = [
    # Web views
    path('news/', NewsListView.as_view(), name='news_list'),
    path('news/<int:pk>/', NewsDetailView.as_view(), name='news_detail'),
    path('news/create/', NewsCreateView.as_view(), name='news_create'),
    path('news/<int:pk>/edit/', NewsUpdateView.as_view(), name='news_edit'),
    path('news/<int:pk>/delete/', NewsDeleteView.as_view(), name='news_delete'),

    # API views
    path('api/news/', NewsListAPI.as_view(), name='api_news_list'),
    path('api/news/<int:pk>/', NewsDetailAPI.as_view(), name='api_news_detail'),
]

# Register the custom 404 handler
handler404 = 'bike_connect.apps.core.views.custom_404_view'
