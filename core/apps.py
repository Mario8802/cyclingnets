from django.apps import AppConfig

class CoreConfig(AppConfig):
    """
    Configuration class for the 'core' application.

    This class is used by Django to configure the application and manage its settings.
    The settings defined here are specific to the 'core' application.
    """
    # Specifies the default primary key field type for models in the app.
    # 'BigAutoField' is used to handle large datasets with bigger primary key values.
    default_auto_field = 'django.db.models.BigAutoField'

    # The name of the application. This must match the app directory name.
    name = 'core'
