import os
from pathlib import Path
from dotenv import load_dotenv
import sentry_sdk   # Ajouté pour le fonctionnement de Sentry sdk
from sentry_sdk.integrations.django import DjangoIntegration
# from sentry_sdk.integrations.excepthook import ExcepthookIntegration
# from sentry_sdk.integrations.arq import ArqIntegration
import logging


# Set traces_sample_rate to 1.0 to capture 100%
# of transactions for performance monitoring.
# traces_sample_rate=1.0,
# Set profiles_sample_rate to 1.0 to profile 100%
# of sampled transactions.
# We recommend adjusting this value in production.
# profiles_sample_rate=1.0,
# max_breadcrumbs=50,
# debug=True,
#  enable_tracing=True,

load_dotenv()
dsn = os.getenv('dsn')

# ============= Init Sentry ============= #
sentry_sdk.init(dsn,
                integrations=[DjangoIntegration()],
                max_breadcrumbs=50,
                traces_sample_rate=1.0,
                profiles_sample_rate=1.0,
                debug=False,
                )


logging.debug("Lettings_site Program is starting!")
sentry_sdk.add_breadcrumb(category="logger", message="Program is starting! ", level="info")

# division_by_zero = 1 / 0
# logging.debug("Program is starting!")
# ======================================== #
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = '(1vv5^6g#^my$%$6*6is*g!)o4xb%-i3r6m7huek(o72#jdh@4'
SECRET_KEY = os.getenv('SECRET_KEY')
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

if os.getenv('DEBUG') == 'False':
    DEBUG = False


# ALLOWED_HOSTS = ['172.16.1.108', '127.0.0.1', 'localhost']
ALLOWED_HOSTS = ["*"]

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'   # Ajouté pour le fonctionnement de Sentry sdk

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',
    'oc_lettings_site',
    'lettings',
    'profiles',
]

WHITENOISE_MANIFEST_STRICT = False  # Pour éviter l'erreur pytest : missing staticfiles manifest entry

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'oc_lettings_site.urls'

STATICFILES_STORAGES = {
    #
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
            os.path.join(BASE_DIR, 'lettings', 'templates'),
            os.path.join(BASE_DIR, 'profiles', 'templates'),
        ],

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

WSGI_APPLICATION = 'oc_lettings_site.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'oc-lettings-site.sqlite3'),
        # 'NAME': BASE_DIR / 'oc-lettings-site.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [BASE_DIR / "static",]

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
