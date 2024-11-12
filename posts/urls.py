from django.urls import path
from .views import BikePostListView

urlpatterns = [
    path('bike-posts/', BikePostListView.as_view(), name='bikepost_list'),
]
