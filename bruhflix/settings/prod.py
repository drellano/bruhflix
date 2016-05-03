from base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '/srv/bruhflix/db/bruhflix.db',
    }
}

DEBUG = False

TEMPLATES[0]['OPTIONS']['debug'] = False

STATIC_ROOT = "/srv/bruhflix/static/"
