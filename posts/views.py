from django.views.generic import ListView
from .models import BikePost

class BikePostListView(ListView):
    model = BikePost
    template_name = 'posts/bikepost_list.html'
    context_object_name = 'bike_posts'
