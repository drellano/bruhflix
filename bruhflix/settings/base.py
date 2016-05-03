import os
from django.conf.global_settings import FILE_UPLOAD_HANDLERS, AUTH_USER_MODEL

ADMINS = [
    ('David Arellano', 'arellanoda.andres@gmail.com'),
]

MANAGERS = ADMINS
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SECRET_KEY = '3k^gjx(1%r0x+%yx!izffe&l)@5y$r7*x9zh+2uu7+_-pvj%50'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
            os.path.join(BASE_DIR, 'streamingportal/templates'),
            os.path.join(BASE_DIR, 'uploadconvert/templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                # Insert your TEMPLATE_CONTEXT_PROCESSORS here or use this
                # list if you haven't customized them:
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',
            ],
            'debug':
                True,
        },
    },
]


STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static/bruhflix'),
    '/home/david/Documents/Software/Django/bruhflix/static',
]


STATIC_ROOT = "static/"


ALLOWED_HOSTS = ['*']

PREREQ_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

PROJECT_APPS = [
    'streamingportal',
    'uploadconvert',
    'progressbarupload',
    'django_cleanup',
#     'bootstrap3',
]

INSTALLED_APPS = PREREQ_APPS + PROJECT_APPS

MIDDLEWARE_CLASSES = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

FILE_UPLOAD_HANDLERS = [
    "progressbarupload.uploadhandler.ProgressBarUploadHandler",
    "django.core.files.uploadhandler.MemoryFileUploadHandler",
    "django.core.files.uploadhandler.TemporaryFileUploadHandler",]

ROOT_URLCONF = 'bruhflix.urls'

WSGI_APPLICATION = 'bruhflix.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '/home/david/Documents/Software/Django/bruhflix/db/bruhflix.db',
    }
}


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATIC_URL = '/static/'

LOGIN_URL = 'home'
