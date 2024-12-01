from django.urls import path
from . import views

# Namespace for the 'posts' app URLs
app_name = 'posts'

# URL patterns for the 'posts' app
urlpatterns = [
    # List view for all bike posts
    path('', views.BikePostListView.as_view(), name='bikepost_list'),
    # URL: /posts/
    # Displays a list of all bike posts.

    # Detail view for a specific bike post
    path('<int:pk>/', views.BikePostDetailView.as_view(), name='bikepost_detail'),
    # URL: /posts/<post_id>/
    # Displays detailed information about a specific bike post, identified by its primary key (pk).

    # View for creating a new bike post
    path('create/', views.create_post, name='create_post'),
    # URL: /posts/create/
    # Displays a form for creating a new bike post.

    # View for editing an existing bike post
    path('<int:pk>/edit/', views.edit_post, name='bikepost_edit'),
    # URL: /posts/<post_id>/edit/
    # Displays a form for editing an existing bike post.

    # View for deleting an existing bike post
    path('<int:pk>/delete/', views.delete_post, name='bikepost_delete'),
    # URL: /posts/<post_id>/delete/
    # Confirms and processes the deletion of a bike post.

    # View for browsing "Buy" and "Sell" bike posts
    path('buy-sell/', views.BuySellView.as_view(), name='buy_sell'),
    # URL: /posts/buy-sell/
    # Displays a filtered list of posts categorized as "Buy" or "Sell".
]
