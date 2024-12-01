from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.decorators.cache import cache_page
from django.views.generic import (
    ListView, CreateView, UpdateView, DeleteView, DetailView
)
from rest_framework import viewsets

from .forms import EventForm
from .models import Event, Participation
from .serializers import EventSerializer


# -------------------------------
# API ViewSet for Event Management
# -------------------------------
class EventViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for viewing and editing Event instances via the API.

    Provides CRUD functionality (list, create, retrieve, update, delete)
    for Event objects, with optimized queries for performance.

    - `queryset`: Uses select_related to optimize database joins for the `organizer` field.
    - `serializer_class`: Specifies the EventSerializer for JSON serialization and validation.
    """
    queryset = Event.objects.select_related('organizer').only('id', 'title', 'description', 'date')
    serializer_class = EventSerializer


# -------------------------------
# Public Views
# -------------------------------

@cache_page(60 * 15)
def homepage(request):
    """
    Renders the landing page with a list of events and user participations.

    - Caches the page for 15 minutes to improve performance and reduce server load.
    - Fetches a limited number of events and user participations if the user is authenticated.

    Args:
        request: The HTTP request object.

    Returns:
        Rendered HTML template with events and participations passed as context.
    """
    events = Event.objects.select_related('organizer').only('id', 'title', 'date')[:5]
    participations = (
        Participation.objects.select_related('event')
        .filter(user=request.user)
        .only('event', 'status') if request.user.is_authenticated else []
    )
    return render(request, 'core/landing_page.html', {
        'events': events,
        'participations': participations,
    })


# -------------------------------
# Detailed Event View
# -------------------------------
class EventDetailView(DetailView):
    """
    Displays detailed information about a specific event.

    - Includes participation status in the context if the user is authenticated.

    Attributes:
        model: The Event model for which details are fetched.
        template_name: The HTML template to render.
        context_object_name: Context variable for the event in the template.
    """
    model = Event
    template_name = 'events/event_detail.html'
    context_object_name = 'event'

    def get_context_data(self, **kwargs):
        """
        Adds additional context to the template, including user participation status.

        Returns:
            Context dictionary with added participation status.
        """
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

    - Uses pagination to handle large datasets efficiently.
    - Supports searching by event titles via the 'search' query parameter.

    Attributes:
        model: The Event model to fetch events.
        template_name: Template to render the event list.
        context_object_name: Context variable for events in the template.
        paginate_by: Number of events per page.
    """
    model = Event
    template_name = 'events/event_list.html'
    context_object_name = 'events'
    paginate_by = 10

    def get_queryset(self):
        """
        Filters events based on the 'search' query parameter.

        Returns:
            Queryset of events ordered by date.
        """
        query = self.request.GET.get('search', '')
        queryset = Event.objects.select_related('organizer').only('id', 'title', 'date', 'organizer__username')
        if query:
            queryset = queryset.filter(title__icontains=query)
        return queryset.order_by('-date')


class EventCreateView(LoginRequiredMixin, CreateView):
    """
    Allows logged-in users to create new events.

    - Automatically assigns the logged-in user as the organizer of the event.
    - Uses EventForm for form validation and rendering.

    Attributes:
        model: The Event model for creating new events.
        form_class: The EventForm class for form handling.
        template_name: The HTML template for event creation.
        success_url: Redirect URL on successful form submission.
    """
    model = Event
    form_class = EventForm
    template_name = 'events/create_event.html'
    success_url = reverse_lazy('events:event_list')

    def form_valid(self, form):
        """
        Automatically assigns the current user as the event organizer.

        Args:
            form: The submitted form instance.

        Returns:
            HTTP response for a valid form.
        """
        form.instance.organizer = self.request.user
        return super().form_valid(form)


class EventUpdateView(UpdateView):
    """
    Allows organizers to edit an existing event.

    Attributes:
        model: The Event model for updating events.
        form_class: The EventForm class for form handling.
        template_name: The HTML template for event editing.
        success_url: Redirect URL on successful form submission.
    """
    model = Event
    form_class = EventForm
    template_name = 'events/edit_event.html'
    success_url = reverse_lazy('events:event_list')


class EventDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    Allows organizers or superusers to delete an event.

    Attributes:
        model: The Event model for deletion.
        template_name: The HTML template for event deletion confirmation.
        success_url: Redirect URL after successful deletion.
    """
    model = Event
    template_name = 'events/delete_event.html'
    success_url = reverse_lazy('events:event_list')

    def test_func(self):
        """
        Ensures only the organizer or a superuser can delete the event.

        Returns:
            Boolean indicating if the user has permission to delete the event.
        """
        event = self.get_object()
        return self.request.user.is_superuser or event.organizer == self.request.user


# -------------------------------
# Join or Leave Event
# -------------------------------
@login_required
def join_or_leave_event(request, event_id):
    """
    Allows a user to join or leave an event.

    - Handles toggling of participation status based on the user's action.

    Args:
        request: The HTTP request object.
        event_id: The ID of the event to join or leave.

    Returns:
        JsonResponse indicating the status of the operation.
    """
    if request.method == "POST":
        event = get_object_or_404(Event, id=event_id)
        participation, created = Participation.objects.get_or_create(user=request.user, event=event)
        status = "joined" if created else "left"
        if not created:
            participation.delete()
        return JsonResponse({"status": status}, status=200)
    return JsonResponse({"error": "Invalid request"}, status=400)
