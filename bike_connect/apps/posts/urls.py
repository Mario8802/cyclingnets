from django.urls import path
from .views import (
    BikePostListView,
    BikePostDetailView,
    BikePostCreateView,
    BikePostUpdateView,
    delete_post,
    BuySellView,
)

app_name = 'posts'

urlpatterns = [
    path('', BikePostListView.as_view(), name='bikepost_list'),
    path('<int:pk>/', BikePostDetailView.as_view(), name='bikepost_detail'),
    path('create/', BikePostCreateView.as_view(), name='create_post'),
    path('<int:pk>/edit/', BikePostUpdateView.as_view(), name='bikepost_edit'),
    path('<int:pk>/delete/', delete_post, name='bikepost_delete'),
    path('buy-sell/', BuySellView.as_view(), name='buy_sell'),
]
