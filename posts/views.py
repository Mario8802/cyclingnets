from django.views.generic import ListView
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q

from events.models import Event

from .models import BikePost
from .forms import BikePostForm


class EventListView(ListView):
    model = Event
    template_name = 'events/event_list.html'
    context_object_name = 'events'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Event.objects.filter(Q(title__icontains=query) | Q(location__icontains=query))
        return super().get_queryset()


class BikePostListView(LoginRequiredMixin, ListView):
    model = BikePost
    template_name = 'posts/bikepost_list.html'
    context_object_name = 'bike_posts'
    login_url = 'login'  # Redirect to login page if not authenticated


@login_required
def create_post(request):
    if request.method == 'POST':
        form = BikePostForm(request.POST, request.FILES)
        if form.is_valid():
            bike_post = form.save(commit=False)
            bike_post.posted_by = request.user
            bike_post.save()
            return redirect('posts:bikepost_list')
    else:
        form = BikePostForm()

    return render(request, 'posts/create_post.html', {'form': form})


@login_required
def list_posts(request):
    bike_posts = BikePost.objects.all()
    return render(request, 'posts/list_posts.html', {'bike_posts': bike_posts})
