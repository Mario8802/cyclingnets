from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.BikePostListView.as_view(), name='bikepost_list'),
]
