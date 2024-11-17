from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import (
    ListView, CreateView, UpdateView, DeleteView, DetailView, TemplateView
)
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets, filters
from .models import Event
from .forms import EventForm
from .serializers import EventSerializer
from django.http import JsonResponse
from django.utils.timezone import now


# API функция за предстоящи събития
def upcoming_events(request):
    events = Event.objects.filter(date__gte=now()).order_by('date')[:10]  # Сортиране по дата
    if not events.exists():
        return JsonResponse({"message": "No upcoming events found."}, status=404)

    data = [
        {
            "id": event.id,
            "title": event.title,
            "description": event.description,
            "location": event.location,
            "date": event.date.strftime('%Y-%m-%d'),
        }
        for event in events
    ]
    return JsonResponse(data, safe=False)


# Функция за начална страница
def homepage(request):
    events = Event.objects.all().order_by('-date')[:10]  # Вземи последните 10 събития
    if not events.exists():
        return render(request, 'core/landing_page.html', {
            'events': [],
            'message': "No events available."
        })
    return render(request, 'core/landing_page.html', {'events': events})


# About View
class AboutView(TemplateView):
    template_name = "about.html"


# Event Detail View
class EventDetailView(DetailView):
    model = Event
    template_name = 'events/event_detail.html'


# Event List View
class EventListView(ListView):
    model = Event
    template_name = 'events/event_list.html'
    context_object_name = 'events'

    def get_queryset(self):
        query = self.request.GET.get('search', '')
        queryset = Event.objects.filter(title__icontains=query) if query else Event.objects.all()
        return queryset.order_by('-date')  # Сортиране по дата


# Event Create View
class EventCreateView(CreateView):
    model = Event
    form_class = EventForm
    template_name = 'events/create_event.html'
    success_url = reverse_lazy('event_list')

    def form_valid(self, form):
        form.instance.organizer = self.request.user  # Задай текущия потребител като организатор
        return super().form_valid(form)

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')  # Пренасочи, ако потребителят не е влязъл
        return super().dispatch(request, *args, **kwargs)


# Event Update View
class EventUpdateView(UpdateView):
    model = Event
    form_class = EventForm
    template_name = 'events/update_event.html'
    success_url = reverse_lazy('event_list')

    def dispatch(self, request, *args, **kwargs):
        event = self.get_object()
        if not request.user.is_superuser and event.organizer != request.user:
            return redirect('event_list')  # Позволи редактиране само за суперпотребители или организатори
        return super().dispatch(request, *args, **kwargs)


# Event Delete View
class EventDeleteView(DeleteView):
    model = Event
    template_name = 'events/delete_event.html'
    success_url = reverse_lazy('event_list')

    def dispatch(self, request, *args, **kwargs):
        event = self.get_object()
        if not request.user.is_superuser and event.organizer != request.user:
            return redirect('event_list')  # Позволи изтриване само за суперпотребители или организатори
        return super().dispatch(request, *args, **kwargs)


# RSVP функционалност
@login_required
def rsvp_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.user in event.participants.all():
        event.participants.remove(request.user)
        rsvp_status = "removed"
    else:
        event.participants.add(request.user)
        rsvp_status = "added"

    if request.is_ajax():
        return JsonResponse({"status": rsvp_status})
    return redirect('event_list')


# API ViewSet за събития
class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'location']
    ordering_fields = ['date', 'title']
