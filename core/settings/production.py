from .base import *
from dotenv import load_dotenv

DEBUG = False

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}

# SECURITY WARNING: define the correct hosts for production!
ALLOWED_HOSTS = ["127.0.0.1", "mavka.argentum.ua", "show.mavka.ua"]

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

try:
    from .local import *
except ImportError:
    pass
