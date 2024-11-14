from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .models import Event
from .forms import EventForm

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
    success_url = reverse_lazy('event_list')  # Redirect to the event list after saving

    def form_valid(self, form):
        """
        Save the event and redirect to success_url
        """
        event = form.save()
        return redirect(self.success_url)

# RSVP Handling View
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
