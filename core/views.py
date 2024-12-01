from itertools import zip_longest

from django.core.paginator import Paginator
from django.db.models import QuerySet
from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView

from events.models import Event, Participation
from .models import News, Page


# -------------------------------
# News Views
# -------------------------------

class NewsListView(ListView):
    """
    Displays a list of news articles.

    Attributes:
        model: The News model.
        template_name: Template to render the list of news articles.
        context_object_name: Context variable for the news list in the template.
    """
    model = News
    template_name = 'core/news_list.html'
    context_object_name = 'news_list'


class NewsDetailView(DetailView):
    """
    Displays the details of a specific news article.

    Attributes:
        model: The News model.
        template_name: Template to render the news details.
        context_object_name: Context variable for the news in the template.
    """
    model = News
    template_name = 'core/news_detail.html'
    context_object_name = 'news'


# -------------------------------
# Static Page View
# -------------------------------

class PageDetailView(DetailView):
    """
    Displays the details of a static page.

    Attributes:
        model: The Page model.
        template_name: Template to render the page details.
        context_object_name: Context variable for the page in the template.
    """
    model = Page
    template_name = 'core/page_detail.html'
    context_object_name = 'page'


class AboutView(TemplateView):
    """
    Displays the About page of the site.

    Attributes:
        template_name: Template to render the About page.
    """
    template_name = "core/about.html"


# -------------------------------
# Utility Function for Event Grouping
# -------------------------------

def group_events(events: QuerySet, group_size: int):
    """
    Utility to group events into chunks of a specified size.

    Args:
        events (QuerySet): QuerySet of events to group.
        group_size (int): Number of events per group.

    Returns:
        An iterator of grouped events, with each group containing up to `group_size` events.
        Uses `zip_longest` to fill shorter groups with `None` if needed.
    """
    args = [iter(events)] * group_size
    return zip_longest(*args)


# -------------------------------
# Landing Page View
# -------------------------------

def landing_page(request):
    """
    Renders the landing page with events, participations, and recent news.

    - Fetches all events and paginates them (9 events per page).
    - Fetches participations for the logged-in user.
    - Fetches the latest 3 news articles.

    Args:
        request: The HTTP request object.

    Returns:
        Rendered HTML template for the landing page with context variables:
        - `paginated_events`: Paginated events for the current page.
        - `participations`: User's participations (if authenticated).
        - `news_list`: Latest 3 news articles.
    """
    # Fetch all events ordered by date
    all_events = Event.objects.order_by('date')

    # Fetch user participations if the user is logged in
    participations = Participation.objects.filter(user=request.user) if request.user.is_authenticated else []

    # Fetch the latest 3 news articles
    news_list = News.objects.order_by('-created_at')[:3]

    # Paginate events - 9 events per page
    paginator = Paginator(all_events, 9)
    page_number = request.GET.get('page', 1)  # Get the current page number from the query string
    paginated_events = paginator.get_page(page_number)  # Get the paginated events for the current page

    # Render the landing page with context
    return render(request, 'core/landing_page.html', {
        'paginated_events': paginated_events,
        'participations': participations,
        'news_list': news_list,
    })
