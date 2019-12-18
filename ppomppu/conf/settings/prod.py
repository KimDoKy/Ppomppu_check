from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

WSGI_APPLICATION = 'conf.wsgi.prod.application'

ALLOWED_HOSTS = [
    CONF_FILES['URL']['app'],
    CONF_FILES['URL']['api']
]


#CORS_ORIGIN_WHITELIST = (
#    CONF_FILES['URL']['app'],
#    CONF_FILES['URL']['api']
#)
#

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': CONF_FILES['postgresql']['NAME'],
        'USER': CONF_FILES['postgresql']['USER'],
        'PASSWORD': CONF_FILES['postgresql']['PASSWORD'],
        'HOST': CONF_FILES['postgresql']['HOST'],
        'PORT': CONF_FILES['postgresql']['PORT'],
    }
}


# Caches settings
CACHES = {
    'default': {
        'BACKEND': 'redis_cache.RedisCache',
        'LOCATION': 'redis://' + CONF_FILES['AWS']['cache'],
        },
    }

# Celery Settings
CELERY_BROKER_URL = 'redis://' + CONF_FILES['AWS']['cache']
CELERY_TRANSPORT_OPTIONS = {'region':CONF_FILES['AWS']['region']}
CELERY_RESULT_BACKEND = 'redis://' + CONF_FILES['AWS']['cache']
