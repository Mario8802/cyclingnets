from django import template

# Register the custom template tag or filter library
register = template.Library()


@register.filter
def add_class(field, css_class):
    """
    Custom template filter to add a CSS class to a Django form field.

    This allows you to dynamically add CSS classes to form fields directly in templates.
    For example:
        {{ form.field_name|add_class:"my-css-class" }}
    This appends the specified CSS class to the existing classes of the form field.

    Args:
        field: The Django form field to which the class will be added.
        css_class: The CSS class to append to the field's existing classes.

    Returns:
        The form field as a widget with the updated "class" attribute.
    """
    # Get the existing classes from the field's widget attributes.
    existing_classes = field.field.widget.attrs.get("class", "")

    # Combine existing classes with the new CSS class and strip any extra whitespace.
    new_classes = f"{existing_classes} {css_class}".strip()

    # Render the field as a widget with the updated "class" attribute.
    return field.as_widget(attrs={"class": new_classes})
