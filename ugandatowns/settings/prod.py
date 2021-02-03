from .base import *

DEBUG = False

ALLOWED_HOSTS = ['*']

ADMINS = (
    ('Amos Baranes', 'amos@DrBaranes.com'),
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ['DB_NAME'],
        'USER': os.environ['DB_USER'],
        'PASSWORD': os.environ['DB_PASS'],
        'HOST': os.environ['DB_SERVICE'],
        'PORT': os.environ['DB_PORT']
    },
    'postgres': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ['DB_NAME'],
        'USER': os.environ['DB_USER'],
        'PASSWORD': os.environ['DB_PASS'],
        'HOST': os.environ['DB_SERVICE'],
        'PORT': os.environ['DB_PORT']
    }
}

MEDIA_ROOT = '/usr/src/app/ugandatownsmedia/'  # for nginx
STATIC_ROOT = '/usr/src/app/ugandatownsstatic/'  # for nginx

CURRENT_URL = 'prod'

REDIS_HOST = 'redis'
REDIS_PORT = 6379
REDIS_DB = 0

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('redis', 6379)],
        },
    },
}

DOMAIN = 'https://ugandatowns.com'
