from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.BikePostListView.as_view(), name='bikepost_list'),
    path('<int:pk>/', views.BikePostDetailView.as_view(), name='bikepost_detail'),
    path('create/', views.create_post, name='create_post'),
    path('<int:pk>/edit/', views.edit_post, name='bikepost_edit'),
    path('<int:pk>/delete/', views.delete_post, name='bikepost_delete'),
    path('buy-sell/', views.BuySellView.as_view(), name='buy_sell'),  # Добавен BuySellView
]
