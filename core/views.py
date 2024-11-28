from django.shortcuts import render
from django.views.generic import TemplateView

from events.models import Participation, Event


# About Page
class AboutView(TemplateView):
    template_name = "about/about.html"


def landing_page(request):
    # Optimized queries to reduce database load
    events = Event.objects.select_related('organizer').only('id', 'name', 'date')  # Use actual related fields
    participations = Participation.objects.select_related('user').only('user', 'event')

    return render(request, 'core/landing_page.html', {
        'events': events,

        'participations': participations,

    })
