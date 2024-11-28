from django.urls import path
from core.views import landing_page
from events.views import homepage
urlpatterns = [
    path('', landing_page, name='landing_page'),
    path('', homepage, name='homepage'),
    path('about/', AboutView.as_view(), name='about'),
]
