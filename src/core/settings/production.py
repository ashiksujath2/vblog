from .base import *

DEBUG = True

ADMINS = (
    ('Ashik', 'ashik@agiliq.com'),
)

ALLOWED_HOSTS = ['*']

db_name = get_env_variable('DB_NAME')
db_user = get_env_variable('DB_USER')
db_password = get_env_variable('DB_PASSWORD')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': db_name,
        'USER': db_user,
        'PASSWORD': db_password,
        'HOST': '',
        'PORT': ''
    }
}
