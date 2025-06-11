# educa/settings/prod.py

from .base import *
from decouple import config


DEBUG = False

ADMINS = [
    ('Erfan Azari', 'eazari.dev@gmail.com'),
    
]

ALLOWED_HOSTS = ['https://e-learning-platform.up.railway.app', 'http://e-learning-platform.up.railway.app', '*e-learning-platform.up.railway.app', 'e-learning-platform.up.railway.app']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('POSTGRES_DB'),
        'USER': config('POSTGRES_USER'),
        'PASSWORD': config('POSTGRES_PASSWORD'),
        'HOST': 'db',
        'PORT': 5432,
    }
}

REDIS_URL = 'redis://cache:6379'
CACHES['default']['LOCATION'] = REDIS_URL
CHANNEL_LAYERS['default']['CONFIG']['hosts'] = [REDIS_URL]

# Security
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True
