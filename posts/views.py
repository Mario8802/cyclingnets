from django.views.generic import ListView, DetailView
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.contrib import messages
from .models import BikePost
from .forms import BikePostForm

@login_required
def create_post(request):
    if request.method == 'POST':
        form = BikePostForm(request.POST, request.FILES)
        if form.is_valid():
            bike_post = form.save(commit=False)
            bike_post.posted_by = request.user
            if bike_post.category in ['buy', 'sell'] and not bike_post.price:
                form.add_error('price', "Price is required for 'Buy' and 'Sell' categories.")
                return render(request, 'posts/create_post.html', {'form': form})
            bike_post.save()
            messages.success(request, "Your post has been created.")
            return redirect('posts:bikepost_list')
    else:
        form = BikePostForm()
    return render(request, 'posts/create_post.html', {'form': form})

@login_required
def edit_post(request, pk):
    bike_post = get_object_or_404(BikePost, pk=pk)
    if request.user != bike_post.posted_by:
        messages.error(request, "You are not allowed to edit this post.")
        return redirect('posts:bikepost_list')
    if request.method == 'POST':
        form = BikePostForm(request.POST, request.FILES, instance=bike_post)
        if form.is_valid():
            form.save()
            messages.success(request, "Your post has been updated.")
            return redirect('posts:bikepost_detail', pk=bike_post.pk)
    else:
        form = BikePostForm(instance=bike_post)
    return render(request, 'posts/edit_post.html', {'form': form, 'bike_post': bike_post})

@login_required
def delete_post(request, pk):
    bike_post = get_object_or_404(BikePost, pk=pk)
    if request.user == bike_post.posted_by:
        bike_post.delete()
        messages.success(request, "Your post has been deleted.")
    else:
        messages.error(request, "You are not allowed to delete this post.")
    return redirect('posts:bikepost_list')

class BikePostListView(LoginRequiredMixin, ListView):
    model = BikePost
    template_name = 'posts/bikepost_list.html'
    context_object_name = 'bike_posts'
    login_url = 'login'

    def get_queryset(self):
        query = self.request.GET.get('q')
        category = self.request.GET.get('category')
        location = self.request.GET.get('location')
        queryset = BikePost.objects.all()
        if query:
            queryset = queryset.filter(Q(title__icontains=query) | Q(description__icontains=query))
        if category:
            queryset = queryset.filter(category=category)
        if location:
            queryset = queryset.filter(location__icontains=location)
        return queryset

class BikePostDetailView(LoginRequiredMixin, DetailView):
    model = BikePost
    template_name = 'posts/bikepost_detail.html'
    context_object_name = 'bike_post'
    login_url = 'login'

class BuySellView(LoginRequiredMixin, ListView):
    model = BikePost
    template_name = 'posts/buy_sell.html'
    context_object_name = 'bike_posts'
    login_url = 'login'

    def get_queryset(self):
        return BikePost.objects.filter(category__in=['buy', 'sell'])
