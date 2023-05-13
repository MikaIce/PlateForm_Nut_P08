from . import *
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration
from django.urls import path
import raven


SECRET_KEY = 'django-insecure-u78d$ev_m4nli*_jy&%l0%h)tbmh7x%ezn(3fkt%l4i@91!g%*'
DEBUG = False
ALLOWED_HOSTS = ['161.35.27.70']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'purbeurre',
        'USER': 'postgre',
        'PASSWORD': 'root',
        'HOST': '',
        'PORT': '5432',
    }
}
sentry_sdk.init(
    dsn="https://0404f9895b27492080898d015f562eef@o4505016209178624.ingest.sentry.io/4505174046736384",
    integrations=[DjangoIntegration()],
)
INSTALLED_APPS += [
    'raven.contrib.django.raven_compat',
]


RAVEN_CONFIG = {
    'dsn': 'https://somethingverylong@sentry.io/216272', # caution replace by your own!!
    # If you are using git, you can also automatically configure the
    # release based on the git info.
    'release': raven.fetch_git_sha(os.path.dirname(os.pardir)),
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'root': {
        'level': 'INFO', # WARNING by default. Change this to capture more than warnings.
        'handlers': ['sentry'],
    },
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s '
                      '%(process)d %(thread)d %(message)s'
        },
    },
    'handlers': {
        'sentry': {
            'level': 'INFO', # To capture more than ERROR, change to WARNING, INFO, etc.
            'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler',
            'tags': {'custom-tag': 'x'},
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        }
    },
    'loggers': {
        'django.db.backends': {
            'level': 'ERROR',
            'handlers': ['console'],
            'propagate': False,
        },
        'raven': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
        },
        'sentry.errors': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
        },
    },
}
