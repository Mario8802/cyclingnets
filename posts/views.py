from django.views.generic import ListView
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from events.models import Event
from .models import BikePost
from .forms import BikePostForm
from django.db.models import Q

class EventListView(ListView):
    model = Event
    template_name = 'events/event_list.html'
    context_object_name = 'events'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Event.objects.filter(Q(title__icontains=query) | Q(location__icontains=query))
        return super().get_queryset()
# ListView to display all Bike Posts
class BikePostListView(LoginRequiredMixin, ListView):
    model = BikePost
    template_name = 'posts/bikepost_list.html'
    context_object_name = 'bike_posts'
    login_url = 'login'  # Redirect to login page if not authenticated


# Function-based view to create a new Bike Post
@login_required
def create_post(request):
    if request.method == 'POST':
        form = BikePostForm(request.POST, request.FILES)  # Include request.FILES for image uploads
        if form.is_valid():
            bike_post = form.save(commit=False)
            bike_post.posted_by = request.user  # Set the current logged-in user as the author
            bike_post.save()
            return redirect('posts:bikepost_list')  # Redirect to the list of bike posts
    else:
        form = BikePostForm()

    return render(request, 'posts/create_post.html', {'form': form})


# Function-based view to list all posts (alternative to the ListView)
@login_required
def list_posts(request):
    bike_posts = BikePost.objects.all()
    return render(request, 'posts/list_posts.html', {'bike_posts': bike_posts})
