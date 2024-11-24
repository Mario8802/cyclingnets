from django import forms
from .models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'date', 'location', 'image']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter the title'})
        self.fields['description'].widget.attrs.update({'class': 'form-control', 'rows': 5, 'placeholder': 'Describe the event'})
        self.fields['date'].widget = forms.DateInput(attrs={
            'type': 'date',
            'class': 'form-control'
        })
        self.fields['location'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter the location'})
        self.fields['image'].widget.attrs.update({'class': 'form-control'})
