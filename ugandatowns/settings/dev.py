from .base import *

DEBUG = True

ALLOWED_HOSTS = ['*']

# DATABASES = {
#     'default': {
#         'CONN_MAX_AGE': 0,
#         'ENGINE': 'django.db.backends.sqlite3',
#         'HOST': 'localhost',
#         'NAME': 'project.db',
#         'PASSWORD': '',
#         'PORT': '',
#         'USER': ''
#     }
# }

DATABASES = {
    'default': {
        'CONN_MAX_AGE': 0,
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': 'localhost',
        'NAME': 'ugandatowns',
        'PASSWORD': 'ugandatowns',
        'PORT': '5432',
        'USER': 'ugandatowns'
    }
}


CURRENT_URL = 'dev'

REDIS_HOST = 'localhost'
REDIS_PORT = 6379
REDIS_DB = 0

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('127.0.0.1', 6379)],
            "capacity": 1500,  # default 100
            "expiry": 10,  # default 60
        },
    },
}

DOMAIN = 'http://127.0.0.1:8000'
