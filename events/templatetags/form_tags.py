from django import template

register = template.Library()


@register.filter
def add_class(field, css_class):
    """
    Adds a CSS class to a Django form field.
    """
    existing_classes = field.field.widget.attrs.get("class", "")
    new_classes = f"{existing_classes} {css_class}".strip()
    return field.as_widget(attrs={"class": new_classes})
