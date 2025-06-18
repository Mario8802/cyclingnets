from __future__ import annotations

import os
from pathlib import Path

import dj_database_url
from decouple import config

# ──────────────────────────────
# Paths
# ──────────────────────────────
BASE_DIR: Path = Path(__file__).resolve().parent.parent

# ──────────────────────────────
# Core settings
# ──────────────────────────────
SECRET_KEY: str = config("DJANGO_SECRET_KEY", default="unsafe-secret-key")
DEBUG: bool = config("DEBUG", default=False, cast=bool)

ALLOWED_HOSTS: list[str] = config(
    "ALLOWED_HOSTS",
    default="127.0.0.1,localhost",
).split(",")

CSRF_TRUSTED_ORIGINS: list[str] = [
    f"https://{h}" for h in ALLOWED_HOSTS if not h.startswith("127.")
]

# ──────────────────────────────
# Installed apps
# ──────────────────────────────
DJANGO_APPS: list[str] = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

THIRD_PARTY_APPS: list[str] = [
    "jazzmin",
    "rest_framework",
    "django_filters",
    "corsheaders",
    "cloudinary",
    "cloudinary_storage",
]

LOCAL_APPS: list[str] = [
    "bike_connect.apps.core",
    "bike_connect.apps.users",
    "bike_connect.apps.posts",
    "bike_connect.apps.events",
]

INSTALLED_APPS: list[str] = [
    *DJANGO_APPS,
    *THIRD_PARTY_APPS,
    *LOCAL_APPS,
]

# ──────────────────────────────
# Cloudinary (optional)
# ──────────────────────────────
CLOUDINARY_CLOUD_NAME = config("CLOUDINARY_CLOUD_NAME", default=None)
CLOUDINARY_API_KEY = config("CLOUDINARY_API_KEY", default=None)
CLOUDINARY_API_SECRET = config("CLOUDINARY_API_SECRET", default=None)

if all((CLOUDINARY_CLOUD_NAME, CLOUDINARY_API_KEY, CLOUDINARY_API_SECRET)):
    CLOUDINARY_STORAGE = {
        "CLOUD_NAME": CLOUDINARY_CLOUD_NAME,
        "API_KEY": CLOUDINARY_API_KEY,
        "API_SECRET": CLOUDINARY_API_SECRET,
    }
    DEFAULT_FILE_STORAGE = "cloudinary_storage.storage.MediaCloudinaryStorage"
else:
    DEFAULT_FILE_STORAGE = "django.core.files.storage.FileSystemStorage"

# ──────────────────────────────
# Middleware
# ──────────────────────────────
MIDDLEWARE: list[str] = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# ──────────────────────────────
# CORS
# ──────────────────────────────
CORS_ALLOW_ALL_ORIGINS: bool = config("CORS_ALLOW_ALL_ORIGINS", default=False, cast=bool)
if not CORS_ALLOW_ALL_ORIGINS:
    CORS_ALLOWED_ORIGINS: list[str] = config("CORS_ALLOWED_ORIGINS", default="").split(",")

CORS_ALLOW_CREDENTIALS: bool = True

# ──────────────────────────────
# URLs / WSGI
# ──────────────────────────────
ROOT_URLCONF = "bike_connect.urls"
WSGI_APPLICATION = "bike_connect.wsgi.application"

# ──────────────────────────────
# Templates
# ──────────────────────────────
TEMPLATES: list[dict] = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    }
]

# ──────────────────────────────
# Database
# ──────────────────────────────
DATABASES = {
    "default": dj_database_url.config(
        default="sqlite:///db.sqlite3",
        conn_max_age=600,
        ssl_require=not DEBUG,
    )
}

# ──────────────────────────────
# Static / Media
# ──────────────────────────────
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_DIRS = [BASE_DIR / "static"]
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# ──────────────────────────────
# Authentication
# ──────────────────────────────
AUTH_USER_MODEL = "users.CustomUser"
LOGIN_URL = "users:login"
LOGIN_REDIRECT_URL = "users:profile"
LOGOUT_REDIRECT_URL = "home"

# ──────────────────────────────
# Password validation
# ──────────────────────────────
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# ──────────────────────────────
# Internationalisation
# ──────────────────────────────
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# ──────────────────────────────
# Logging
# ──────────────────────────────
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {"class": "logging.StreamHandler"},
    },
    "root": {
        "handlers": ["console"],
        "level": config("DJANGO_LOG_LEVEL", default="INFO"),
    },
}

# ──────────────────────────────
# Custom flags for CI / tests
# ──────────────────────────────
if os.getenv("GITHUB_ACTIONS") == "true":
    DATABASES["default"] = {"ENGINE": "django.db.backends.sqlite3", "NAME": ":memory:"}
    PASSWORD_HASHERS = ["django.contrib.auth.hashers.MD5PasswordHasher"]
