from django.urls import path
from .views import NewsListView, NewsDetailView, PageDetailView

# Namespace for the core app URLs
app_name = 'core'

# URL patterns for the core app
urlpatterns = [
    # URL for the news list view
    path('list/', NewsListView.as_view(), name='news_list'),
    # Example: /list/
    # Displays a paginated list of news articles.

    # URL for the news detail view
    path('<int:pk>/', NewsDetailView.as_view(), name='news_detail'),
    # Example: /5/
    # Displays the details of a specific news article identified by its primary key (pk).

    # URL for the page detail view
    path('page/<slug:slug>/', PageDetailView.as_view(), name='page_detail'),
    # Example: /page/about-us/
    # Displays the details of a static page identified by its unique slug.
]
