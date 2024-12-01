from django.apps import AppConfig

class UsersConfig(AppConfig):  # Configures the 'users' app in the Django project
    default_auto_field = 'django.db.models.BigAutoField'  # Sets the default primary key type to BigAutoField
    name = 'users'  # Specifies the name of the application as 'users'
