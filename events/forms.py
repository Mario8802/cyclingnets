from django import forms
from .models import Event


class EventForm(forms.ModelForm):
    """
    A form for creating or updating Event objects.

    This form is based on the Event model and uses Django's ModelForm
    to automatically generate form fields corresponding to the model's fields.

    It includes custom widgets to style the form fields and improve the user experience.
    """

    class Meta:
        # Specifies the model associated with this form
        model = Event

        # Fields from the Event model to include in the form
        fields = ['title', 'description', 'date', 'location', 'image']

        # Custom widgets for each field to add CSS classes and placeholders
        widgets = {
            'title': forms.TextInput(
                attrs={
                    'class': 'form-control',  # Bootstrap styling class
                    'placeholder': 'Enter event title'  # Placeholder text for the input
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'class': 'form-control',  # Bootstrap styling class
                    'rows': 3,  # Number of rows for the textarea
                    'placeholder': 'Describe the event'  # Placeholder text for the input
                }
            ),
            'date': forms.DateInput(
                attrs={
                    'class': 'form-control',  # Bootstrap styling class
                    'type': 'date'  # HTML5 date picker
                }
            ),
            'location': forms.TextInput(
                attrs={
                    'class': 'form-control',  # Bootstrap styling class
                    'placeholder': 'Enter location'  # Placeholder text for the input
                }
            ),
            'image': forms.ClearableFileInput(
                attrs={
                    'class': 'form-control'  # Bootstrap styling class for file input
                }
            ),
        }
