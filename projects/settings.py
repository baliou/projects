"""
Django settings for projects project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'vokx(^rpf)+am_)i8glq&cf4tk)x=a2&huv2g%g25qcgd@6&9+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sites',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'registration',
    'bootstrap3',
    'taxi',
)

ACCOUNT_ACTIVATION_DAYS = 2
SITE_ID = 1 

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'projects.urls'

WSGI_APPLICATION = 'projects.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
    'ENGINE': 'django.db.backends.postgresql_psycopg2',
    'NAME': 'taxi',
    'USER': 'admin',
    'PASSWORD': 'adminuser',
    'HOST': 'localhost',
    'PORT': '',
                        }
 }
# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'fr-fr'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


TEMPLATE_DIRS = (
	"/home/adminuser/workspace/django/projects/Templates/"
)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/


STATIC_URL = '/static/'
STATIC_ROOT = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
    '/home/adminuser/workspace/django/projects/static/',
)


MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = '/media/'

ADMIN_MEDIA_PREFIX = '/static/admin/'


EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'mba.aliou@gmail.com'
EMAIL_HOST_PASSWORD = 'aliouBa$123'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

AUTH_PROFILE_MODULE = 'facturedevis.UserEntreprise'
LOGIN_REDIRECT_URL = '/'
LOGIN_URL = '/accounts/login'
INTERNAL_IPS = '127.0.0.1:8000'

