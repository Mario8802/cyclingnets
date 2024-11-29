from django import template

register = template.Library()

@register.filter
def chunked(iterable, chunk_size):
    """Splits a list into chunks of the specified size."""
    for i in range(0, len(iterable), chunk_size):
        yield iterable[i:i + chunk_size]