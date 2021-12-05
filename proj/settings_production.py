from .settings import *

DEBUG = False
ALLOWED_HOSTS = ['*']
INTERNAL_IPS = ('127.0.0.1', 'localhost',)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'pessoal',
        'USER': 'postgres',
        'PASSWORD': 'root',
        'HOST': 'pessoal_db',
        'PORT': '5432',
    }
}
