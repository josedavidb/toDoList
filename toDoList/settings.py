"""
Django settings for toDoList project.

Generated by 'django-admin startproject' using Django 2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '5skl5@ju@lf%=x=05chb77j5pkv8zv=)jhc4x!sz7ltjnt-k+)'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'toDo',
    'accounts',
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

ROOT_URLCONF = 'toDoList.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],
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

WSGI_APPLICATION = 'toDoList.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

try:
    CUR_DOMAIN = os.environ.get('CUR_DOMAIN')
except:
    CUR_DOMAIN = 'default'

if CUR_DOMAIN == '' or CUR_DOMAIN is None:
    CUR_DOMAIN ='default'

DATABASES_LIST = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'toDoListdb',
        'USER': 'toDoList',
        'PASSWORD': 'toDoList',
        'HOST': 'localhost',
        'PORT': 5432,

    },
    'todolist-django-app': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd6qmts10flb9qd',
        'USER': 'oiasvcizlibhvb',
        'PASSWORD': 'afa4da4d60d1b5f749782b0c7887f3e3f43ab754875ce8f52c6ad5557ea6a1e4',
        'HOST': 'ec2-54-243-197-120.compute-1.amazonaws.com',
        'PORT': '5432',
        'OPTIONS': {
            'connect_timeout': None,
        }
    }
}

DATABASES = {'default': DATABASES_LIST[CUR_DOMAIN]}



# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = os.path.join(PROJECT_ROOT, 'static')

LOGIN_REDIRECT_URL = 'index'
LOGOUT_REDIRECT_URL = 'index'