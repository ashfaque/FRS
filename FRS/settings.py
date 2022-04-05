"""
Django settings for FRS project.

Generated by 'django-admin startproject' using Django 3.2.12.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
DJANGO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-wp98oa@e_@*@6f3uhwkbn!$6_565r9_w^*)or6th^5v&o*&igx')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

AUTH_USER_MODEL = 'user.UserDetail'
ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'frsmaster',
    'users',
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

ROOT_URLCONF = 'FRS.urls'

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

WSGI_APPLICATION = 'FRS.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

# PostgreSQL if using Docker else MySQL :-
DATABASES = {
    'default': {
        'ENGINE': os.environ.get('DB_ENGINE', 'django.db.backends.mysql'),
        'NAME': os.environ.get('POSTGRES_DB', 'frsdb'),
        'USER': os.environ.get('POSTGRES_USER', 'root'),
        # 'USER': os.environ.get('POSTGRES_USER', 'postgres'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD', '123456'),
        'HOST': os.environ.get('DB_HOST', '127.0.0.1'),
        'PORT': os.environ.get('DB_PORT', '3306'),
        # 'PORT': os.environ.get('DB_PORT', '5432')
        'OPTIONS' if not os.path.exists(os.path.join(DJANGO_ROOT, '.env')) else '' : {
            'sql_mode': 'traditional',
        } if not os.path.exists(os.path.join(DJANGO_ROOT, '.env')) else '',
    }
}

REDIS = {
    'REDIS_HOST': os.environ.get('REDIS_HOST', '127.0.0.1'),
    'REDIS_PORT': os.environ.get('REDIS_PORT', 6379),
    'REDIS_DB_INDEX': 0,
    'REDIS_AUTH': os.environ.get('REDIS_AUTH', False),
    'REDIS_PASSWORD': os.environ.get('REDIS_PASSWORD', ''),
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

# TIME_ZONE = 'UTC'
TIME_ZONE =  'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

# STATIC_URL = '/static/'

# =========== MEDIA AND URL CONFIG ================= #
STATIC_ROOT = os.path.join(DJANGO_ROOT, "static")
STATIC_FILES_ROOT = os.path.join(DJANGO_ROOT, "staticfiles")
MEDIA_ROOT = os.path.join(DJANGO_ROOT, "media")
LOG_ROOT = os.path.join(DJANGO_ROOT, "logs")
# create the folders if not found
if not os.path.exists(STATIC_ROOT):
    os.makedirs(STATIC_ROOT)
if not os.path.exists(STATIC_FILES_ROOT):
    os.makedirs(STATIC_FILES_ROOT)
if not os.path.exists(MEDIA_ROOT):
    os.makedirs(MEDIA_ROOT)
if not os.path.exists(LOG_ROOT):
    os.makedirs(LOG_ROOT)
STATIC_URL = '/FRS/static/'
MEDIA_URL = '/FRS/media/'
# SERVER_URL = 'http://0.0.0.0:00000/'
SERVER_URL = 'http://127.0.0.1:8888/'
FRONTEND_URL = 'http://127.0.0.1/frs/#/'
# =========== MEDIA AND URL CONFIG ================= #

# =========== FILE STORAGE CONFIG ================= #
'''
FILE_STORAGE_CONFIG can be configured for file_system / aws_s3 / ftp and so on
For the primary version of the only file_system type storage is being used
'''
STORAGE_ROOT = os.path.join(DJANGO_ROOT, "storage")
FILE_STORAGE_CONFIG = {
    'type': 'file_system',
    'path': STORAGE_ROOT
}

# =========== FILE STORAGE CONFIG ================= #

# =========== DEBUG LOGGING ============== #
if not os.path.exists(LOG_ROOT + "/django"):
    os.makedirs(LOG_ROOT + "/django")
if not os.path.exists(LOG_ROOT + "/django/debug"):
    os.makedirs(LOG_ROOT + "/django/debug")
if not os.path.exists(LOG_ROOT + "/django/critical"):
    os.makedirs(LOG_ROOT + "/django/critical")
if not os.path.exists(LOG_ROOT + "/django/error"):
    os.makedirs(LOG_ROOT + "/django/error")
if not os.path.exists(LOG_ROOT + "/django/info"):
    os.makedirs(LOG_ROOT + "/django/info")

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] [%(module)s.%(funcName)s] [%(process)d.%(thread)d] %(message)s",
            'datefmt': "%d/%b/%Y %H:%M:%S"
        },
        'simple': {
            'format': '[%(asctime)s] %(levelname)s %(message)s'
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'INFO',
            'formatter': 'verbose',
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(DJANGO_ROOT, 'logs/django/debug/django_debug.log'),
            'maxBytes': 1024 * 1024 * 2, # Max 2 MB
            #'when': 'D', # this specifies the interval
            #'interval': 1, # defaults to 1, only necessary for other values
            'backupCount': 1, # how many backup file to keep
            'formatter': 'verbose',
        },
        # 'filecritical': {
        #     'level': 'CRITICAL',
        #     'class': 'logging.handlers.RotatingFileHandler',
        #     'filename': os.path.join(DJANGO_ROOT, 'logs/django/critical/django_critical.log'),
        #     'maxBytes': 1024 * 1024 * 2, # Max 2 MB
        #     #'when': 'D', # this specifies the interval
        #     #'interval': 1, # defaults to 1, only necessary for other values
        #     'backupCount': 1, # how many backup file to keep
        #     'formatter': 'verbose',
        # },
        'fileerror': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(DJANGO_ROOT, 'logs/django/error/django_error.log'),
            'maxBytes': 1024 * 1024 * 2, # Max 2 MB
            #'when': 'D', # this specifies the interval
            #'interval': 1, # defaults to 1, only necessary for other values
            'backupCount': 1, # how many backup file to keep
            'formatter': 'verbose',
        },
        'fileinfo': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(DJANGO_ROOT, 'logs/django/info/django_info.log'),
            'maxBytes': 1024 * 1024 * 2, # Max 2 MB
            #'when': 'D', # this specifies the interval
            #'interval': 1, # defaults to 1, only necessary for other values
            'backupCount': 1, # how many backup file to keep
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),
        },
        # 'myproject.custom':{
        #     'handlers': ['filecritical'],
        #     'level': os.getenv('DJANGO_LOG_LEVEL', 'CRITICAL'),
        # },
        'django.request':{
            'handlers': ['fileerror'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'ERROR'),
        },
        '': {
            'handlers': ['fileinfo'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
        }
    },
}
# =========== DEBUG LOGGING ============== #

# ============================ Oauth implementation with Knox ===================#
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'knox.auth.TokenAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        # 'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',
        'rest_framework.permissions.IsAuthenticated',
        'rest_framework.permissions.AllowAny',
    ),
    # 'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema'
}
# ============================ Oauth implementation with Knox ==================#

# ============ KNOX Config ============================= #
REST_KNOX = {
    'SECURE_HASH_ALGORITHM': 'cryptography.hazmat.primitives.hashes.SHA512',
    'AUTH_TOKEN_CHARACTER_LENGTH': 64,
    'TOKEN_TTL': None,
    'USER_SERIALIZER': 'knox.serializers.UserSerializer',
    'TOKEN_LIMIT_PER_USER': None,
    'AUTO_REFRESH': False,
}
# ============ KNOX Config ============================= #

# ==================== Email Config ==================== #
EMAIL_FROM = 'facerecognitionsystem@outlook.com'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp-mail.outlook.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'facerecognitionsystem@outlook.com'
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', 'Hu*uw***7')
MAX_ATTACHMENT_SIZE_KB = 15000
# ==================== Email Config ==================== #

# ============= Error Msg configrations ================= #
MSG_SUCCESS = "Data has been fetched successfully"
MSG_SUCCESS_UPDATE = " has been updated successfully"
MSG_SUCCESS_CREATE = " has been created successfully"
MSG_NO_DATA = "No Data Found"
MSG_ERROR = "Failure"
# ============= Error Msg configrations ================= #

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
