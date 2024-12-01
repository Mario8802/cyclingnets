from django import template
from ..models import Participation

# Register the custom template tag or filter library
register = template.Library()


@register.filter
def participation_status(user, event):
    """
    Custom template filter to check a user's participation status for a specific event.

    This filter queries the `Participation` model to determine if a user has joined or cancelled
    participation in a given event. It is useful for templates that need to display the status of a
    user's participation (e.g., joined, cancelled, or not participating).

    Usage in templates:
        {{ user|participation_status:event }}

    Args:
        user: The user whose participation status is being checked.
        event: The event for which the participation status is being checked.

    Returns:
        str: The participation status ('joined', 'cancelled') if the user has a record.
        None: If the user does not have a participation record for the event.
    """
    try:
        # Query the Participation model to find the user's participation record for the event.
        participation = Participation.objects.get(user=user, event=event)

        # Return the status of the participation (e.g., 'joined', 'cancelled').
        return participation.status
    except Participation.DoesNotExist:
        # If no participation record exists for the user and event, return None.
        return None
