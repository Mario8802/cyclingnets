from django.shortcuts import render
from events.models import Story, Participation, Experience, Event

def landing_page(request):
    events = Event.objects.all()
    stories = Story.objects.all()
    participations = Participation.objects.all()
    experiences = Experience.objects.all()
    return render(request, 'core/landing_page.html', {
        'events': events,
        'stories': stories,
        'participations': participations,
        'experiences': experiences
    })
