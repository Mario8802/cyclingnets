from django.http import HttpRequest
from django.urls import reverse_lazy
from django.utils.timezone import now
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from django.core.paginator import Paginator
from itertools import zip_longest
from .models import News, Page
from .forms import NewsForm
from bike_connect.apps.events.models import Event, Participation

# -------------------------------
# Admin Mixin
# -------------------------------

class AdminRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    """
    Mixin to restrict access to staff members only.
    Combines LoginRequiredMixin and UserPassesTestMixin to ensure:
    - The user is authenticated.
    - The user is a staff member.
    """

    request: HttpRequest

    def test_func(self):
        """
        Check if the user is a staff member.
        """
        return self.request.user.is_staff


# -------------------------------
# News Views
# -------------------------------

class NewsListView(ListView):
    """
    Displays a paginated list of news articles with optional filtering.
    - Filters by year, month, or a search query if provided.
    """
    model = News
    template_name = 'core/news_list.html'
    context_object_name = 'news_list'
    paginate_by = 6  # Number of news articles per page

    def get_queryset(self):
        """
        Customizes the queryset to filter by year, month, or search query.
        """
        queryset = super().get_queryset()
        year = self.request.GET.get('year')
        month = self.request.GET.get('month')
        search_query = self.request.GET.get('q')

        if year:
            queryset = queryset.filter(created_at__year=year)
        if month:
            queryset = queryset.filter(created_at__month=month)
        if search_query:
            queryset = queryset.filter(title__icontains=search_query)

        return queryset

    def get_context_data(self, **kwargs):
        """
        Adds additional context for year and month filtering options.
        """
        context = super().get_context_data(**kwargs)
        current_year = now().year
        context['years'] = range(current_year - 10, current_year + 1)
        context['months'] = range(1, 13)
        return context


class NewsDetailView(DetailView):
    """
    Displays the details of a news article and increments its view count.
    """
    model = News
    template_name = 'core/news_detail.html'
    context_object_name = 'news'

    def get(self, request, *args, **kwargs):
        """
        Overrides the default GET method to increment the view count.
        """
        news = self.get_object()
        news.views += 1
        news.save(update_fields=['views'])
        return super().get(request, *args, **kwargs)


class NewsCreateView(AdminRequiredMixin, CreateView):
    """
    View for creating a new news article (restricted to staff users).
    """
    model = News
    form_class = NewsForm
    template_name = 'core/news_form.html'
    success_url = reverse_lazy('core:news_list')


class NewsUpdateView(AdminRequiredMixin, UpdateView):
    """
    View for editing an existing news article (restricted to staff users).
    """
    model = News
    form_class = NewsForm
    template_name = 'core/news_form.html'
    success_url = reverse_lazy('core:news_list')


class NewsDeleteView(AdminRequiredMixin, DeleteView):
    """
    View for deleting a news article (restricted to staff users).
    """
    model = News
    template_name = 'core/confirm_delete.html'
    success_url = reverse_lazy('core:news_list')


# -------------------------------
# Static Page Views
# -------------------------------

class PageDetailView(DetailView):
    """
    Displays the details of a static page.
    """
    model = Page
    template_name = 'core/page_detail.html'
    context_object_name = 'page'


class AboutView(TemplateView):
    """
    Displays the About page of the site.
    """
    template_name = "core/about.html"


# -------------------------------
# Utility Function for Event Grouping
# -------------------------------

def group_events(events, group_size):
    """
    Utility to group events into chunks of a specified size.
    Args:
        events (QuerySet): QuerySet of events to group.
        group_size (int): Number of events per group.
    Returns:
        An iterator of grouped events.
    """
    args = [iter(events)] * group_size
    return zip_longest(*args)


# -------------------------------
# Landing Page View
# -------------------------------

def landing_page(request):
    """
    Renders the landing page with:
    - Paginated events (9 per page).
    - Participations for the logged-in user.
    - Latest 3 published news articles.
    """
    # Fetch all events ordered by date
    all_events = Event.objects.order_by('date')

    # Fetch user participations if the user is logged in
    participations = (
        Participation.objects.filter(user=request.user)
        if request.user.is_authenticated
        else []
    )

    # Fetch the latest 3 news articles
    news_list = News.objects.filter(is_published=True).order_by('-created_at')[:3]

    # Paginate events - 9 events per page
    paginator = Paginator(all_events, 9)
    page_number = request.GET.get('page', 1)  # Current page number
    paginated_events = paginator.get_page(page_number)  # Paginated events for the page

    # Render the landing page with the context
    return render(request, 'core/landing_page.html', {
        'paginated_events': paginated_events,
        'participations': participations,
        'news_list': news_list,
    })


def custom_404_view(request, exception):
    """
    Custom 404 error handler.
    """
    return render(request, '404.html', status=404)