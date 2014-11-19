from .base import *

DEBUG = True

TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'vblog.db'),
    }
}

INSTALLED_APPS += (
    'django_extensions',
    # 'debug_toolbar',
)
