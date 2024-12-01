from django.apps import AppConfig


class PostsConfig(AppConfig):
    """
    Configuration class for the 'posts' application.

    This class is used by Django to manage app-specific settings
    and perform initialization tasks when the application is loaded.
    """
    # Specifies the default primary key field type for models in the app.
    # 'BigAutoField' is used to handle large datasets with bigger primary key values.
    default_auto_field = 'django.db.models.BigAutoField'

    # The name of the application. This must match the app directory name.
    name = 'posts'
