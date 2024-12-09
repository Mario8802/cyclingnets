from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.files.storage import default_storage
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.core.cache import cache
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from rest_framework import viewsets

from .forms import EventForm
from bike_connect.apps.events.models import Event, Participation
from .serializers import EventSerializer


# -------------------------------
# API ViewSet for Event Management
# -------------------------------
class EventViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for viewing and editing Event instances via the API.
    """
    queryset = Event.objects.select_related('organizer').only('id', 'title', 'description', 'date', 'image')
    serializer_class = EventSerializer


# -------------------------------
# Public Views
# -------------------------------
def homepage(request):
    """
    Displays the landing page with events and participations.
    """
    events = cache.get('homepage_events')
    if not events:
        events = Event.objects.select_related('organizer').only('id', 'title', 'date')[:5]
        cache.set('homepage_events', events, 60 * 15)

    participations = (
        Participation.objects.select_related('event')
        .filter(user=request.user)
        .only('event', 'status') if request.user.is_authenticated else []
    )
    return render(request, 'core/landing_page.html', {
        'events': events,
        'participations': participations,
    })


class EventDetailView(DetailView):
    """
    Displays detailed information about a specific event.
    """
    model = Event
    template_name = 'events/event_detail.html'
    context_object_name = 'event'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['participation_status'] = Participation.objects.filter(
                user=self.request.user, event=self.object
            ).exists()
        return context


# -------------------------------
# Event Management Views
# -------------------------------
class EventListView(ListView):
    """
    Displays a paginated list of events with optional search functionality.
    """
    model = Event
    template_name = 'events/event_list.html'
    context_object_name = 'events'
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get('search', '')
        queryset = Event.objects.select_related('organizer').only('id', 'title', 'date', 'organizer__username', 'image')
        if query:
            queryset = queryset.filter(title__icontains=query)
        return queryset.order_by('-date')


class EventCreateView(LoginRequiredMixin, CreateView):
    model = Event
    form_class = EventForm
    template_name = 'events/create_event.html'
    success_url = reverse_lazy('events:event_list')

    def form_valid(self, form):
        form.instance.organizer = self.request.user
        return super().form_valid(form)


class EventUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Event
    form_class = EventForm
    template_name = 'events/edit_event.html'
    success_url = reverse_lazy('events:event_list')

    def test_func(self):
        event = self.get_object()
        return self.request.user == event.organizer or self.request.user.is_superuser


class EventDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    Allows organizers or superusers to delete an event.
    """
    model = Event
    template_name = 'events/delete_event.html'
    success_url = reverse_lazy('events:event_list')

    def test_func(self):
        event = self.get_object()
        return self.request.user.is_superuser or event.organizer == self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Cancel URL redirects to the event detail page or event list
        context['cancel_url'] = reverse_lazy('events:event_list')
        return context


@login_required
def join_event(request, event_id):
    if request.method == "POST":
        event = get_object_or_404(Event, id=event_id)
        participation, created = Participation.objects.get_or_create(user=request.user, event=event)
        if created:
            return JsonResponse({"status": "joined"}, status=200)
        return JsonResponse({"error": "Already joined"}, status=400)

@login_required
def leave_event(request, event_id):
    if request.method == "POST":
        event = get_object_or_404(Event, id=event_id)
        participation = Participation.objects.filter(user=request.user, event=event).first()
        if participation:
            participation.delete()
            return JsonResponse({"status": "left"}, status=200)
        return JsonResponse({"error": "Not a participant"}, status=400)

# -------------------------------
# File Upload to S3 Functionality
# -------------------------------

@login_required
def upload_event_image(request):
    """
    Handles image uploads for events. Saves the image to the S3 bucket and returns the URL.
    """
    if request.method == 'POST' and request.FILES.get('image'):
        uploaded_file = request.FILES['image']
        try:
            path = default_storage.save(f'events/{uploaded_file.name}', uploaded_file)
            file_url = default_storage.url(path)
            return JsonResponse({'url': file_url}, status=200)
        except Exception as e:
            return JsonResponse({'error': f"Failed to upload: {str(e)}"}, status=500)
    return JsonResponse({'error': 'Invalid request or no image provided'}, status=400)