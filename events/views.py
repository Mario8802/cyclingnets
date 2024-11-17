from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import ListView, CreateView, TemplateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from rest_framework import viewsets, filters

from .forms import EventForm
from .models import Event, Booking
from .serializers import EventSerializer


class AboutView(TemplateView):
    template_name = "about.html"


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'location']
    ordering_fields = ['date', 'title']


class EventDeleteView(DeleteView):
    model = Event
    template_name = 'events/delete_event.html'
    success_url = reverse_lazy('event_list')

    def dispatch(self, request, *args, **kwargs):
        event = self.get_object()
        # Allow superusers or the event organizer to delete the event
        if not request.user.is_superuser and event.organizer != request.user:
            return redirect('event_list')  # Redirect if not authorized
        return super().dispatch(request, *args, **kwargs)

class EventUpdateView(UpdateView):
    model = Event
    form_class = EventForm
    template_name = 'events/update_event.html'
    success_url = reverse_lazy('event_list')

    def dispatch(self, request, *args, **kwargs):
        event = self.get_object()
        if not request.user.is_superuser and event.organizer != request.user:
            return redirect('event_list')
        return super().dispatch(request, *args, **kwargs)


# List View for Events
class EventListView(ListView):
    model = Event
    template_name = 'events/event_list.html'
    context_object_name = 'events'


# Create View for Events
class EventCreateView(CreateView):
    model = Event
    form_class = EventForm
    template_name = 'events/create_event.html'
    success_url = reverse_lazy('event_list')

    def form_valid(self, form):
        form.instance.organizer = self.request.user
        return super().form_valid(form)


def rsvp_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    user = request.user

    if request.method == "POST" and user.is_authenticated:
        action = request.POST.get("action")
        if action == "join":
            event.participants.add(user)
        elif action == "cancel":
            event.participants.remove(user)
        event.save()

    return redirect('event_list')

