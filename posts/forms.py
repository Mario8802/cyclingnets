from django import forms
from .models import BikePost


class BikePostForm(forms.ModelForm):
    """
    A form for creating or updating BikePost objects.

    This form is based on the BikePost model and automatically generates
    fields for the specified attributes. It is used for user input validation
    and rendering the form in templates.

    Attributes:
        model: Specifies the model associated with the form (BikePost).
        fields: Specifies the fields to include in the form.
    """
    class Meta:
        # Specifies the model associated with this form
        model = BikePost

        # Fields from the BikePost model to include in the form
        fields = [
            'title',        # Title of the bike post
            'description',  # Detailed description of the bike
            'category',     # Category (e.g., Buy/Sell)
            'condition',    # Condition (e.g., New/Used)
            'price',        # Price of the bike
            'location',     # Location where the bike is available
            'image',        # Optional image of the bike
        ]
