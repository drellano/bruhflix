from base import *

with open(os.path.join(ROOT_DIR, 'secret_key.txt')) as f:
    SECRET_KEY = f.read().strip()

DEBUG = True

BROKER_URL = 'django://'

INSTALLED_APPS += ['kombu.transport.django', ]

MEDIA_ROOT = os.path.join(ROOT_DIR, 'media')

MEDIA_URL = 'media/'

STATIC_ROOT = ''

TEMP_DIR = os.path.abspath(os.path.join(ROOT_DIR, os.pardir))
FILE_UPLOAD_TEMP_DIR = os.path.join(TEMP_DIR, 'temp')
