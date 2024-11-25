from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import (
    ListView, CreateView, UpdateView, DeleteView, DetailView, TemplateView
)
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from rest_framework import viewsets

from .models import Event, Participation, Story, Experience
from .forms import EventForm
from .serializers import EventSerializer


class EventViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for viewing and editing Event instances.
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer


# --------------------------
# Public Views
# --------------------------

# Landing Page
def homepage(request):
    events = Event.objects.all()[:5]
    stories = Story.objects.all()[:5]
    participations = Participation.objects.filter(user=request.user) if request.user.is_authenticated else []
    experiences = Experience.objects.filter(participant__user=request.user) if request.user.is_authenticated else []

    return render(request, 'core/landing_page.html', {
        'events': events,
        'stories': stories,
        'participations': participations,
        'experiences': experiences
    })


# About Page
class AboutView(TemplateView):
    template_name = "about/about.html"


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

    def get_queryset(self):
        query = self.request.GET.get('search', '')
        queryset = Event.objects.all()
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


@csrf_exempt
@login_required
def join_or_leave_event(request, event_id):
    if request.method == "POST":
        event = get_object_or_404(Event, id=event_id)
        participation, created = Participation.objects.get_or_create(user=request.user, event=event)

        if created:
            status = "joined"
        else:
            participation.delete()
            status = "left"

        return JsonResponse({"status": status})
    return JsonResponse({"error": "Invalid request"}, status=400)


# --------------------------
# Stories and Experiences
# --------------------------

class StoryListView(ListView):
    model = Story
    template_name = 'stories/story_list.html'
    context_object_name = 'stories'


class StoryCreateView(LoginRequiredMixin, CreateView):
    model = Story
    fields = ['title', 'content', 'image']
    template_name = 'stories/story_create.html'
    success_url = reverse_lazy('stories:story_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ExperienceCreateView(LoginRequiredMixin, CreateView):
    model = Experience
    fields = ['feedback', 'rating']
    template_name = 'experiences/experience_create.html'

    def form_valid(self, form):
        event_id = self.kwargs['event_id']
        form.instance.event = get_object_or_404(Event, id=event_id)
        participation = Participation.objects.filter(user=self.request.user, event=form.instance.event).first()
        if not participation:
            return JsonResponse({"error": "You must join the event first!"}, status=400)
        form.instance.participant = participation
        return super().form_valid(form)
