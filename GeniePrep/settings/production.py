from .base import *

DEBUG = False

# ALLOWED_HOSTS = []
ALLOWED_HOSTS = ['8c3767f6c672.ngrok.io', '127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': os.environ.get('SQL_ENGINE', 'django.db.backends.sqlite3'),
        'NAME': os.environ.get('SQL_DATABASE', os.path.join(BASE_DIR, 'db.sqlite3')),
        'USER': os.environ.get('SQL_USER', 'user'),
        'PASSWORD': os.environ.get('SQL_PASSWORD', 'password'),
        'HOST': os.environ.get('SQL_HOST', 'localhost'),
        'PORT': os.environ.get('SQL_PORT', ''),
    }
}