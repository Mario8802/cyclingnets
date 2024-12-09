from rest_framework import serializers
from .models import Event


class EventSerializer(serializers.ModelSerializer):
    """
    A serializer for the Event model, used to convert Event instances to JSON format
    and validate incoming data for creating or updating Event objects.

    This serializer uses Django REST Framework's ModelSerializer, which automatically generates
    fields based on the Event model and includes built-in validation.
    """

    class Meta:
        # Specifies the model associated with this serializer
        model = Event

        # Includes all fields from the Event model in the serialized output
        fields = '__all__'
