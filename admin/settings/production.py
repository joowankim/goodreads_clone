from admin.settings.base import *

DEBUG = False

ALLOWED_HOSTS = ['goodreads_clone.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'root',
        'USER': 'root',
        'PASSWORD': 'root'
    }
}