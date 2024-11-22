from django.views.generic import ListView, DetailView
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from .models import BikePost
from .forms import BikePostForm
from django.shortcuts import get_object_or_404

@login_required
def edit_post(request, pk):
    bike_post = get_object_or_404(BikePost, pk=pk)
    if request.user != bike_post.posted_by:
        return redirect('posts:bikepost_list')  # Redirect if the user is not the owner

    if request.method == 'POST':
        form = BikePostForm(request.POST, instance=bike_post)
        if form.is_valid():
            form.save()
            return redirect('posts:bikepost_detail', pk=bike_post.pk)
    else:
        form = BikePostForm(instance=bike_post)

    return render(request, 'posts/edit_post.html', {'form': form, 'bike_post': bike_post})


# ListView for BikePost
class BikePostListView(LoginRequiredMixin, ListView):
    model = BikePost
    template_name = 'posts/bikepost_list.html'
    context_object_name = 'bike_posts'
    login_url = 'login'

    def get_queryset(self):
        query = self.request.GET.get('q')
        category = self.request.GET.get('category')
        if query:
            return BikePost.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))
        elif category:
            return BikePost.objects.filter(category=category)
        return super().get_queryset()

# DetailView for BikePost
class BikePostDetailView(LoginRequiredMixin, DetailView):
    model = BikePost
    template_name = 'posts/bikepost_detail.html'
    context_object_name = 'bike_post'
    login_url = 'login'

# Create BikePost view
@login_required
def create_post(request):
    if request.method == 'POST':
        form = BikePostForm(request.POST, request.FILES)
        if form.is_valid():
            bike_post = form.save(commit=False)
            bike_post.posted_by = request.user
            bike_post.save()
            return redirect('posts:bikepost_list')  # Ensure the namespace is used
    else:
        form = BikePostForm()
    return render(request, 'posts/create_post.html', {'form': form})
@login_required
def delete_post(request, pk):
    bike_post = get_object_or_404(BikePost, pk=pk)
    if request.user == bike_post.posted_by:
        bike_post.delete()
    return redirect('posts:bikepost_list')

# Buy/Sell View
class BuySellView(LoginRequiredMixin, ListView):
    model = BikePost
    template_name = 'posts/buy_sell.html'
    context_object_name = 'bike_posts'
    login_url = 'login'
