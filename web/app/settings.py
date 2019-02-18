"""
Django settings for app project.

Generated by 'django-admin startproject' using Django 1.11.10.

For more information on this file, see./
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""
import json
import os
from django.utils.translation import ugettext_lazy as _
from kombu import Exchange, Queue

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'megg_yej86ln@xao^+)it4e&ueu#!4tl9p1h%2sjr7ey0)m25f'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG', 'True') == 'True'

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True


ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '[]')

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, "app/templates"),
)
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework_swagger',
    'fcm_django',
    'mail_templated',
    'import_export',
    'django_twilio',

    'apps.core',
    'apps.notification_user',
    'apps.sender',
    'apps.email_sender'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'apps.sender.middleware.SenderMiddleWare',
    # 'apps.sender.middleware.SenderMiddleWare',
]

ROOT_URLCONF = 'app.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': TEMPLATE_DIRS,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n',
            ],
        },
    },
]

WSGI_APPLICATION = 'app.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ['DB_NAME'],
        'USER': os.environ['DB_USER'],
        'PASSWORD': os.environ['DB_PASS'],
        'HOST': os.environ['DB_SERVICE'],
        'PORT': os.environ['DB_PORT']
    }
}

# Celery settings

CELERY_BROKER_URL = os.environ.get('CELERY_BROKER', '')
CELERY_RESULT_BACKEND = os.environ.get('CELERY_RESULT_BACKEND', '')
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_SERIALIZER = 'json'

# EMAIL

# CELERY_EMAIL_TASK_CONFIG = {
#     'queue' : 'email',
#     'rate_limit' : '50/m',  # * CELERY_EMAIL_CHUNK_SIZE (default: 10)
# }


EMAIL_CONNACTIONS = list([
    {
        "EMAIL_BACKEND": 'django.core.mail.backends.smtp.EmailBackend',
        "EMAIL_HOST": os.environ.get('EMAIL_HOST', ''),
        "EMAIL_PORT": os.environ.get('EMAIL_PORT', ''),
        "EMAIL_FROM": os.environ.get('EMAIL_FROM', 'no-reply@forus.io'),
        "EMAIL_HOST_USER": os.environ.get('EMAIL_HOST_USER', ''),
        "EMAIL_HOST_PASSWORD": os.environ.get('EMAIL_HOST_PASSWORD', ''),
        "EMAIL_USE_TLS": os.environ.get('EMAIL_USE_TLS', 'True') == 'True',
        "EMAIL_USE_SSL": os.environ.get('EMAIL_USE_SSL', 'False') == 'True',
    }
])
EMAIL_CONNACTIONS =  EMAIL_CONNACTIONS + list(json.loads(os.environ.get('EMAIL_CONNACTIONS', '[]')))




# i18
LANGUAGE_CODE = 'nl'

USE_I18N = True
LANGUAGES = (
    ('en', _('English')),
    ('nl', _('Niderlands')),
)
LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)

DATE_FORMAT = "d-m-Y"
USE_L10N = False

ADMIN_ENABLED = os.environ.get('ADMIN_ENABLED', 'False') == 'True'

# TWILLIO
DJANGO_TWILIO_FORGERY_PROTECTION = False
DJANGO_TWILIO_BLACKLIST_CHECK = True

TWILIO_ACCOUNT_SID = os.environ.get('TWILIO_ACCOUNT_SID', None)
TWILIO_AUTH_TOKEN = os.environ.get('TWILIO_AUTH_TOKEN', None)
TWILIO_PHONE_NUMBER = os.environ.get('TWILIO_PHONE_NUMBER', None)

FCM_DJANGO_SETTINGS = {
    "FCM_SERVER_KEY": os.environ.get('FIREBASE_SERVER_KEY', ''),
    # true if you want to have only one active device per registered user at a time
    # default: False
    "ONE_DEVICE_PER_USER": False,
    # devices to which notifications cannot be sent,
    # are deleted upon receiving error response from FCM
    # default: False
    "DELETE_INACTIVE_DEVICES": True,
}


APNS_KEY_LOCATION = os.path.join(BASE_DIR, 'cert', 'key.pem')
APNS_SENDBOX = os.environ.get('APNS_SENDBOX', 'False') =='True'