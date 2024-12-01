import os
from pathlib import Path
from decouple import config

# Define the base directory of the project
BASE_DIR = Path(__file__).resolve().parent.parent

# Secret Key and Debug Mode
# SECRET_KEY is fetched from environment variables for security; a fallback value is provided for development.
SECRET_KEY = config('DJANGO_SECRET_KEY', default='fallback-secret-key')

# DEBUG mode should be disabled in production for security reasons.
DEBUG = config('DEBUG', default=True, cast=bool)

# CSRF configuration: Trusted origins to prevent CSRF attacks.
CSRF_TRUSTED_ORIGINS = ['http://127.0.0.1:8000', 'http://localhost:8000']
CSRF_FAILURE_VIEW = 'django.views.csrf.csrf_failure'

# Allowed hosts configuration, fetched from environment variables.
# This prevents host header attacks by restricting the domains the app can serve.
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='').split(',')

# Installed Apps
# DJANGO_APPS contains core Django apps required for basic functionality.
DJANGO_APPS = [
    'django.contrib.admin',          # Admin panel
    'django.contrib.auth',           # Authentication system
    'django.contrib.contenttypes',   # Framework for content types
    'django.contrib.sessions',       # Session management
    'django.contrib.messages',       # Messaging framework
    'django.contrib.staticfiles',    # Static file management
]

# THIRD_PARTY_APPS includes third-party libraries or frameworks used in the project.
THIRD_PARTY_APPS = [
    'rest_framework',  # Django REST Framework for building APIs
    'django_filters',  # Enables filtering for querysets in APIs
]

# LOCAL_APPS includes custom applications created for this project.
LOCAL_APPS = [
    'core',    # Custom core app for shared functionality
    'users',   # Custom user management app
    'posts',   # App for managing posts related to buying/selling bikes
    'events',  # App for managing cycling events
]

# Combine all apps into a single list.
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

# Middleware
# Middleware processes requests/responses at various stages of the request lifecycle.
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',              # Enhances security (e.g., HSTS)
    'django.contrib.sessions.middleware.SessionMiddleware',        # Manages user sessions
    'django.middleware.common.CommonMiddleware',                  # General request/response adjustments
    'django.middleware.csrf.CsrfViewMiddleware',                  # Prevents CSRF attacks
    'django.contrib.auth.middleware.AuthenticationMiddleware',    # Manages user authentication
    'django.contrib.messages.middleware.MessageMiddleware',       # Manages temporary messages
    'django.middleware.clickjacking.XFrameOptionsMiddleware',     # Prevents clickjacking attacks
]

# URL configuration module
ROOT_URLCONF = 'bike_connect.urls'

# Templates configuration
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',  # Use Django's template engine
        'DIRS': [os.path.join(BASE_DIR, 'templates')],                # Custom templates directory
        'APP_DIRS': True,                                             # Look for templates in app directories
        'OPTIONS': {
            'context_processors': [                                  # Functions that inject data into templates
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# WSGI configuration for deployment
WSGI_APPLICATION = 'bike_connect.wsgi.application'

# Database Configuration
# PostgreSQL is used as the database engine, with credentials fetched from environment variables.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DB_NAME'),        # Database name
        'USER': config('DB_USER'),        # Database user
        'PASSWORD': config('DB_PASSWORD'),# Database password
        'HOST': config('DB_HOST', default='localhost'),  # Database host
        'PORT': config('DB_PORT', default='5432'),       # Database port
    }
}

# Password validation rules for enhanced security
# Uncomment and customize validators as needed.
# AUTH_PASSWORD_VALIDATORS = [
#     {
#         'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
#     },
# ]

# Localization
# Define the default language and timezone for the project.
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True   # Enable internationalization
USE_L10N = True   # Format dates, numbers, etc., in the local format
USE_TZ = True     # Enable timezone-aware datetimes

# Static and Media Files
# Static files (CSS, JavaScript, images) and media file configuration
STATIC_URL = '/static/'                           # URL for static files
STATICFILES_DIRS = [BASE_DIR / 'static']          # Directories for additional static files
STATIC_ROOT = BASE_DIR / 'staticfiles'            # Directory for collected static files
MEDIA_URL = '/media/'                             # URL for media files
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')      # Directory for uploaded media files

# Default primary key field type for models
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Custom user model
AUTH_USER_MODEL = 'users.CustomUser'

# Authentication Redirects
# Define the redirects for login and logout.
LOGIN_URL = 'users:login'
LOGIN_REDIRECT_URL = 'users:profile'
LOGOUT_REDIRECT_URL = 'home'
