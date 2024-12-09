from django import template

# Register this module as a template library
register = template.Library()

@register.filter
def chunked(iterable, chunk_size):
    """
    Splits a list or iterable into smaller chunks of the specified size.

    This filter is particularly useful for rendering data in grids or sections
    in templates. For example, displaying a list of items in rows with a specific
    number of items per row.

    Args:
        iterable: The input list or iterable to be chunked.
        chunk_size: The number of items each chunk should contain.

    Yields:
        Lists of the specified chunk size from the original iterable.

    Example:
        In a Django template:
        {% for chunk in items|chunked:3 %}
            <div class="row">
                {% for item in chunk %}
                    <div class="col">{{ item }}</div>
                {% endfor %}
            </div>
        {% endfor %}
    """
    for i in range(0, len(iterable), chunk_size):
        # Yield a slice of the iterable of the specified size
        yield iterable[i:i + chunk_size]
