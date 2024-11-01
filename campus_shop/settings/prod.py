from decouple import config 
from ..settings import *


DEBUG = False

ADMINS = [
    ('Swallah Tahiru', 'swallaht3@gmail.com')
]

ALLOWED_HOSTS = ['localhost' ,'campusconnect.com', 'www.campusconnect.com', '127.0.0.1']

DATABASES = {
    'default': {
    'ENGINE': 'django.db.backends.postgresql',
    'NAME': config('DB_NAME'),
    'USER': config('DB_USER'),
    'PASSWORD': config('DB_PASSWORD'),
    'HOST': config('DB_HOST'),
    'PORT': config('DB_PORT'),
 }
}

REDIS_URL = 'redis://redis:6379'

CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True
