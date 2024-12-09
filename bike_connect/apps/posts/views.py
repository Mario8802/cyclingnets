from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.files.storage import default_storage
from django.db.models import Q
from django.contrib import messages
from django.urls import reverse_lazy, reverse
from .models import BikePost
from .forms import BikePostForm


class BikePostCreateView(LoginRequiredMixin, CreateView):
    """
    Handles the creation of a new BikePost, identical to EventCreateView.
    """
    model = BikePost
    form_class = BikePostForm
    template_name = 'posts/create_post.html'
    success_url = reverse_lazy('posts:bikepost_list')

    def form_valid(self, form):
        # Assign the logged-in user as the post creator
        form.instance.posted_by = self.request.user
        return super().form_valid(form)


class BikePostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    Handles the editing of an existing BikePost with image upload to S3.
    """
    model = BikePost
    form_class = BikePostForm
    template_name = 'posts/edit_post.html'
    success_url = reverse_lazy('posts:bikepost_list')

    def form_valid(self, form):
        # Upload new image to S3 if provided
        if self.request.FILES.get('image'):
            uploaded_file = self.request.FILES['image']
            try:
                # Delete old image if exists
                if self.object.image:
                    default_storage.delete(self.object.image.name)
                # Upload new image
                path = default_storage.save(f'bike_posts/{uploaded_file.name}', uploaded_file)
                form.instance.image = path
            except Exception as e:
                form.add_error('image', f"Failed to upload image: {str(e)}")
                return self.form_invalid(form)
        return super().form_valid(form)

    def test_func(self):
        bike_post = self.get_object()
        return self.request.user == bike_post.posted_by


@login_required
def delete_post(request, pk):
    """
    Handles the deletion of a BikePost.
    """
    bike_post = get_object_or_404(BikePost, pk=pk)

    # Ensure only the owner can delete the post
    if request.user != bike_post.posted_by:
        messages.error(request, "You are not allowed to delete this post.")
        return redirect('posts:bikepost_list')

    if request.method == 'POST':
        # Delete image from S3
        if bike_post.image:
            default_storage.delete(bike_post.image.name)

        # Delete the post
        bike_post.delete()
        messages.success(request, "Your post has been successfully deleted.")
        return redirect('posts:bikepost_list')

    # Render the confirmation template
    return render(request, 'posts/confirm_delete.html', {
        'object': bike_post,
        'cancel_url': reverse('posts:bikepost_detail', args=[bike_post.pk])
    })


class BikePostListView(LoginRequiredMixin, ListView):
    """
    Displays a paginated list of BikePosts.
    """
    model = BikePost
    template_name = 'posts/bikepost_list.html'
    context_object_name = 'bike_posts'
    login_url = 'users:login'
    paginate_by = 6  # Number of posts per page

    def get_queryset(self):
        query = self.request.GET.get('q')
        category = self.request.GET.get('category')
        location = self.request.GET.get('location')
        queryset = BikePost.objects.all()
        if query:
            queryset = queryset.filter(
                Q(title__icontains=query)
                | Q(description__icontains=query)
            )
        if category:
            queryset = queryset.filter(category=category)
        if location:
            queryset = queryset.filter(location__icontains=location)
        return queryset


class BikePostDetailView(LoginRequiredMixin, DetailView):
    """
    Displays the details of a specific BikePost.
    """
    model = BikePost
    template_name = 'posts/bikepost_detail.html'
    context_object_name = 'bike_post'
    login_url = 'users:login'


class BuySellView(LoginRequiredMixin, ListView):
    """
    Displays a filtered list of 'Buy' and 'Sell' BikePosts.
    """
    model = BikePost
    template_name = 'posts/buy_sell.html'
    context_object_name = 'bike_posts'
    login_url = 'users:login'

    def get_queryset(self):
        return BikePost.objects.filter(category__in=['buy', 'sell'])
