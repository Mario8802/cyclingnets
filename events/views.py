from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.http import urlencode
from django.views.generic import (
    ListView, CreateView, UpdateView, DeleteView, DetailView, TemplateView
)
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from rest_framework import viewsets, filters
from rest_framework.response import Response
from django.http import JsonResponse
from django.utils.timezone import now

from .models import Event
from .forms import EventForm
from .serializers import EventSerializer


# --------------------------
# Public Views
# --------------------------

# Homepage View
def homepage(request):
    events = Event.objects.upcoming()[:5]  # Използване на новия мениджър
    return render(request, 'core/landing_page.html', {'events': events})


# About View
class AboutView(TemplateView):
    template_name = "about/about.html"


# Event Detail View
class EventDetailView(DetailView):
    model = Event
    template_name = 'events/event_detail.html'
    context_object_name = 'event'


# --------------------------
# Event Management Views
# --------------------------

# List Events
class EventListView(ListView):
    model = Event
    template_name = 'events/event_list.html'
    context_object_name = 'events'

    def get_queryset(self):
        query = self.request.GET.get('search', '')
        queryset = Event.objects.all()
        if query:
            queryset = queryset.filter(title__icontains=query)
        return queryset.order_by('-date')


# Create Event
class EventCreateView(LoginRequiredMixin, CreateView):
    model = Event
    form_class = EventForm
    template_name = 'events/create_event.html'
    success_url = reverse_lazy('events:event_list')

    def form_valid(self, form):
        form.instance.organizer = self.request.user  # Задаване на текущия потребител като организатор
        return super().form_valid(form)


# Update Event
class EventUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Event
    form_class = EventForm
    template_name = 'events/update_event.html'
    success_url = reverse_lazy('events:event_list')

    def test_func(self):
        event = self.get_object()
        return self.request.user.is_superuser or event.organizer == self.request.user


# Delete Event
class EventDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Event
    template_name = 'events/delete_event.html'
    success_url = reverse_lazy('events:event_list')

    def test_func(self):
        event = self.get_object()
        return self.request.user.is_superuser or event.organizer == self.request.user


# RSVP Functionality
@login_required
def join_or_leave_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.user in event.participants.all():
        event.participants.remove(request.user)
        status = "left"
    else:
        event.participants.add(request.user)
        status = "joined"

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return JsonResponse({"status": status})
    return redirect('events:event_list')


# --------------------------
# API Views
# --------------------------

# Upcoming Events API
def upcoming_events(request):
    events = Event.objects.upcoming()[:10]
    serializer = EventSerializer(events, many=True)
    return JsonResponse(serializer.data, safe=False)


# Event ViewSet for REST API
class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'location']
    ordering_fields = ['date', 'title']
