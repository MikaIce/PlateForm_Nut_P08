from . import *


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
