from base import *

DEBUG = True

BROKER_URL = 'django://'

INSTALLED_APPS += ['kombu.transport.django', ]

MEDIA_ROOT = '/home/david/Documents/Software/Django/bruhflix/media'

MEDIA_URL = 'media/'

STATIC_ROOT = ''

FILE_UPLOAD_TEMP_DIR = '/home/david/Documents/Software/Django/temp'
