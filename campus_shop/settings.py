from pathlib import Path
import os
from decouple import config
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure--hl3=j3gz+(xo_gf&bnqsn#b0^@c6r-mgg#yy@-hl33*d8x1a2'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['campusconnect.com', 'localhost', '127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'account.apps.AccountConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # third-party apps
    'phonenumber_field',
    'django_otp',
    'django_otp.plugins.otp_totp',
    'social_django',
    'django_extensions',
    'user_profile',
    'products',
    'django.contrib.postgres',
]


TWILIO_ACCOUNT_SID = config('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = config('TWILIO_AUTH_TOKEN')


AUTHENTICATION_BACKENDS = [
    'account.authenticated.EmailorPhoneBackend',  # Replace with the actual path to your custom backend
    'django.contrib.auth.backends.ModelBackend',
    'social_core.backends.google.GoogleOAuth2',  # Default backend
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

SOCIAL_AUTH_PIPELINE = [
 'social_core.pipeline.social_auth.social_details',
 'social_core.pipeline.social_auth.social_uid',
 'social_core.pipeline.social_auth.auth_allowed',
 'social_core.pipeline.social_auth.social_user',
 'social_core.pipeline.user.get_username',
 'social_core.pipeline.user.create_user',
 'account.authenticated.create_profile',
 'social_core.pipeline.social_auth.associate_user',
 'social_core.pipeline.social_auth.load_extra_data',
 'social_core.pipeline.user.user_details',
]

AUTH_USER_MODEL = 'account.CustomUser'

ROOT_URLCONF = 'campus_shop.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

#EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

WSGI_APPLICATION = 'campus_shop.wsgi.application'

LOGIN_REDIRECT_URL = 'products:product_list'
LOGIN_URL = 'account:login'
LOGOUT_URL = 'account:logout'
LOGOUT_REDIRECT_URL = 'account:login'

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

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

EMAIL_HOST = config('EMAIL_HOST')
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
EMAIL_PORT = config('EMAIL_PORT')
EMAIL_USE_SSL = config('EMAIL_USE_SSL')
DEFAULT_FROM_EMAIL = config('DEFAULT_FROM_EMAIL')

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = config('SOCIAL_AUTH_ID')
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = config('SOCIAL_AUTH_SECRET')


REDIS_HOST = 'localhost'
REDIS_PORT = 6379
REDIS_DB = 0

# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'
#STATICFILES_DIRS = os.path.join(BASE_DIR, 'static')
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles_build', 'static')

MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
