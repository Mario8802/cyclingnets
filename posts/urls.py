from django.urls import path
from . import views

app_name = 'posts'  # Namespace for this app

urlpatterns = [
    path('', views.BikePostListView.as_view(), name='bikepost_list'),  # Correct URL definition
    path('<int:pk>/', views.BikePostDetailView.as_view(), name='bikepost_detail'),
    path('create/', views.create_post, name='create_post'),
    path('<int:pk>/edit/', views.edit_post, name='bikepost_edit'),
    path('<int:pk>/delete/', views.delete_post, name='bikepost_delete'),
]
