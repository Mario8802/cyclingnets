from django.urls import path
from .views import NewsListView, NewsDetailView, PageDetailView

urlpatterns = [
    path('list/', NewsListView.as_view(), name='news_list'),
    path('<int:pk>/', NewsDetailView.as_view(), name='news_detail'),

    path('page/<slug:slug>/', PageDetailView.as_view(), name='page_detail'),
]
