import os
from pathlib import Path
import decouple

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = decouple.config('DJANGO_SECRET_KEY', default='fallback-secret-key')

DEBUG = True

CSRF_TRUSTED_ORIGINS = ['http://127.0.0.1:8000', 'http://localhost:8000']

CSRF_FAILURE_VIEW = 'django.views.csrf.csrf_failure'
ALLOWED_HOSTS = []

DJANGO_APPS = [
    # 'unfold',  # before django.contrib.admin
    # 'unfold.contrib.filters',  # Optional, for special filters
    # 'unfold.contrib.forms',  # Optional, for special form elements
    # 'unfold.contrib.inlines',  # Optional, for special inlines
    # 'unfold.contrib.import_export',  # Optional, if django-import-export is used
    # 'unfold.contrib.guardian',  # Optional, if django-guardian is used
    # 'unfold.contrib.simple_history',  # Optional, if django-simple-history is used
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

THIRD_PARTY_APPS = [
    'rest_framework',  # Django REST Framework
    'django_filters',  # For filtering in REST views

]

LOCAL_APPS = [
    'core',  # Custom core app
    'users',  # Custom user app
    'posts',  # Posts app
    'events',  # Events app
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'bike_connect.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'bike_connect.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'bike_connect',
        'USER': 'postgres',
        'PASSWORD': 'admin',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# Password validation
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

LANGUAGE_CODE = 'en-us'
USE_L10N = True  # Ensures that localization is applied if needed

TIME_ZONE = 'UTC'

USE_I18N = True
USE_TZ = True

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static'
]
STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
AUTH_USER_MODEL = 'users.CustomUser'

LOGIN_URL = '/users/login/'
LOGIN_REDIRECT_URL = '/users/profile/'
LOGOUT_REDIRECT_URL = 'home'
