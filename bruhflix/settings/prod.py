from base import *
import os

with open('/etc/secret_key.txt') as f:
    SECRET_KEY = f.read().strip()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '/srv/bruhflix/db/bruhflix.db',
    }
}

MIDDLEWARE_CLASSES += ['django.middleware.security.SecurityMiddleware']

DEBUG = False

TEMPLATES[0]['OPTIONS']['debug'] = False 

STATIC_ROOT = "/srv/bruhflix/static/"

SESSION_COOKIE_SECURE = True

CSRF_COOKIE_SECURE = True

CSRF_COOKIE_HTTPONLY = True

X_FRAME_OPTIONS = 'DENY'
