from base import *

with open('/etc/secret_key.txt') as f:
    SECRET_KEY = f.read().strip()


MIDDLEWARE_CLASSES += ['django.middleware.security.SecurityMiddleware']

DEBUG = False

TEMPLATES[0]['OPTIONS']['debug'] = False

STATIC_ROOT = os.path.join(ROOT_DIR, 'static')

SESSION_COOKIE_SECURE = True

CSRF_COOKIE_SECURE = True

CSRF_COOKIE_HTTPONLY = True

X_FRAME_OPTIONS = 'DENY'
