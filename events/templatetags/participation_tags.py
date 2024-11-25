from django import template
from ..models import Participation

register = template.Library()


@register.filter
def participation_status(user, event):
    """
    Returns the participation status ('joined', 'cancelled', or None) for a user in a given event.
    """
    try:
        participation = Participation.objects.get(user=user, event=event)
        return participation.status
    except Participation.DoesNotExist:
        return None
