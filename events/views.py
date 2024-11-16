from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .models import Event, Booking
from .forms import EventForm
from django.views.generic import UpdateView
from django.views.generic import DeleteView

class EventDeleteView(DeleteView):
    model = Event
    template_name = 'events/delete_event.html'
    success_url = reverse_lazy('event_list')

    def dispatch(self, request, *args, **kwargs):
        event = self.get_object()
        if event.organizer != request.user:  # Проверка дали потребителят е организатор
            return redirect('event_list')  # Пренасочване, ако не е
        return super().dispatch(request, *args, **kwargs)



class EventUpdateView(UpdateView):
    model = Event
    form_class = EventForm
    template_name = 'events/update_event.html'
    success_url = reverse_lazy('event_list')

    def dispatch(self, request, *args, **kwargs):
        event = self.get_object()
        if event.organizer != request.user:  # Проверка дали потребителят е организатор
            return redirect('event_list')  # Пренасочване, ако не е
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

