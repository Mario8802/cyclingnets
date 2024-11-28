from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.decorators.cache import cache_page
from django.views.generic import (
    ListView, CreateView, UpdateView, DeleteView, DetailView, TemplateView
)
from rest_framework import viewsets

from .forms import EventForm
from .models import Event, Participation
from .serializers import EventSerializer


class EventViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for viewing and editing Event instances.
    """
    queryset = Event.objects.select_related('organizer').only('id', 'title', 'description', 'date')
    serializer_class = EventSerializer

# --------------------------
# Public Views
# --------------------------

# Landing Page
@cache_page(60 * 15)
def homepage(request):
    # Optimized queries
    events = Event.objects.select_related('organizer').only('id', 'title', 'date')[:5]
    participations = (
        Participation.objects.select_related('event')
        .filter(user=request.user)
        .only('event', 'status') if request.user.is_authenticated else []
    )

    # Render the landing page
    return render(request, 'core/landing_page.html', {
        'events': events,
        'participations': participations,

    })


# Event Detail View
class EventDetailView(DetailView):
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


# --------------------------
# Event Management Views
# --------------------------

class EventListView(ListView):
    model = Event
    template_name = 'events/event_list.html'
    context_object_name = 'events'
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get('search', '')
        queryset = Event.objects.select_related('organizer').only('id', 'title', 'date', 'organizer__username')
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


class EventUpdateView(UpdateView):
    model = Event
    form_class = EventForm
    template_name = 'events/edit_event.html'
    success_url = reverse_lazy('events:event_list')


class EventDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Event
    template_name = 'events/delete_event.html'
    success_url = reverse_lazy('events:event_list')

    def test_func(self):
        event = self.get_object()
        return self.request.user.is_superuser or event.organizer == self.request.user


@login_required
def join_or_leave_event(request, event_id):
    if request.method == "POST":
        event = get_object_or_404(Event, id=event_id)
        participation, created = Participation.objects.get_or_create(user=request.user, event=event)
        status = "joined" if created else "left"
        if not created:
            participation.delete()
        return JsonResponse({"status": status}, status=200)
    return JsonResponse({"error": "Invalid request"}, status=400)





