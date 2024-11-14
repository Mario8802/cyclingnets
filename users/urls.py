from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
]
from django.urls import path
from .views import register_view, login_view
#
# urlpatterns = [
#     path('register/', register_view, name='register'),
#     path('login/', login_view, name='login'),
# ] ???????????????????????????
