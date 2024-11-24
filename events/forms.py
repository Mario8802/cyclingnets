from django import forms
from .models import Event


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'date', 'location', 'image']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update(
            {'class': 'form-control'}
        )
        self.fields['description'].widget.attrs.update(
            {'class': 'form-control', 'rows': 5}
        )
        self.fields['date'].widget.attrs.update(
            {'class': 'form-control datepicker'}
        )
        self.fields['location'].widget.attrs.update(
            {'class': 'form-control'}
        )
        self.fields['image'].widget.attrs.update(
            {'class': 'form-control'}
        )
