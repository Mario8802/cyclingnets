from django.apps import AppConfig


class EventsConfig(AppConfig):
    """
    Configuration class for the 'events' application.

    This class is used to define application-specific settings and behaviors.
    Django automatically loads this configuration when the application is included
    in the `INSTALLED_APPS` setting of the project.
    """
    # Specifies the default field type for automatically generated primary keys in models.
    default_auto_field = 'django.db.models.BigAutoField'

    # The name of the application as it appears in the project structure.
    name = 'bike_connect.apps.events'
