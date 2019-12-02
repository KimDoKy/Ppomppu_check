from .base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

WSGI_APPLICATION = 'conf.wsgi.dev.application'

ALLOWED_HOSTS = ['*']

#CORS_ORIGIN_WHITELIST = (
#    'localhost:8001',
#    CONF_FILES['URL']['app'],
#    CONF_FILES['URL']['api']
# )

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': CONF_FILES['postgresql_dev']['NAME'],
        'USER': CONF_FILES['postgresql_dev']['USER'],
        'PASSWORD': CONF_FILES['postgresql_dev']['PASSWORD'],
        'HOST': CONF_FILES['postgresql_dev']['HOST'],
        'PORT': CONF_FILES['postgresql_dev']['PORT'],
    }
}

# Caches settings
CACHES = {
    'default': {
        'BACKEND': 'redis_cache.RedisCache',
        'LOCATION': 'redis://localhost:6379',
        },
    }

# Celery Settings
CELERY_BROKER_URL = 'redis://localhost:6379'
CELERY_TRANSPORT_OPTIONS = {'region':CONF_FILES['AWS']['region']}
CELERY_RESULT_BACKEND = 'redis://localhost:6379'
CELERY_TAST_SERIALIZER = 'json'

