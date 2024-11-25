from django import forms
from .models import Event, Story, Experience


class EventForm(forms.ModelForm):
    # Form for creating or updating events
    class Meta:
        model = Event
        fields = ['title', 'description', 'date', 'location', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter event title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Describe the event'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter location'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }


class StoryForm(forms.ModelForm):
    # Form for creating a story
    class Meta:
        model = Story
        fields = ['title', 'content', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter story title'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Share your story'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }


class ExperienceForm(forms.ModelForm):
    # Form for submitting feedback and ratings
    class Meta:
        model = Experience
        fields = ['feedback', 'rating']
        widgets = {
            'feedback': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Write your feedback'}),
            'rating': forms.NumberInput(attrs={'class': 'form-control', 'min': 1, 'max': 5}),
        }
