from .base import *

DEBUG = True

ADMINS = (
    ('Ashik', 'ashik@agiliq.com'),
)

ALLOWED_HOSTS = ['*']

INSTALLED_APPS += (
    'django_extensions',
    # 'debug_toolbar',
)
