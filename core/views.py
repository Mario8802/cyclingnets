from itertools import zip_longest

from django.core.paginator import Paginator
from django.db.models import QuerySet
from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from events.models import Event, Participation
from .models import News, Page


class NewsListView(ListView):
    model = News
    template_name = 'core/news_list.html'
    context_object_name = 'news_list'


class NewsDetailView(DetailView):
    model = News
    template_name = 'core/news_detail.html'
    context_object_name = 'news'


class PageDetailView(DetailView):
    model = Page
    template_name = 'core/page_detail.html'
    context_object_name = 'page'


class AboutView(TemplateView):
    template_name = "core/about.html"


def group_events(events: QuerySet, group_size: int):
    """Utility to group events into chunks of a specified size."""
    args = [iter(events)] * group_size
    return zip_longest(*args)


def landing_page(request):
    # Fetch all events ordered by date
    all_events = Event.objects.order_by('date')
    participations = Participation.objects.filter(user=request.user) if request.user.is_authenticated else []
    news_list = News.objects.order_by('-created_at')[:3]  # Latest 3 news articles

    # Paginate events - 9 events per page
    paginator = Paginator(all_events, 9)
    page_number = request.GET.get('page', 1)  # Get the current page number from the query string
    paginated_events = paginator.get_page(page_number)

    return render(request, 'core/landing_page.html', {
        'paginated_events': paginated_events,
        'participations': participations,
        'news_list': news_list,
    })