#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Django settings for emma
For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

from __future__ import absolute_import, unicode_literals

import environ


# DIRS
# -----------------------------------------------------------------------------
from django.core.urlresolvers import reverse_lazy

ROOT_DIR = environ.Path(__file__) - 3  # (/a/b/myfile.py - 3 = /)
PROJECT_DIR = ROOT_DIR.path('emma')
APPS_DIR = ROOT_DIR.path('emma/apps')

env = environ.Env()

# SECRET CONFIGURATION
# -----------------------------------------------------------------------------
SECRET_KEY = env("DJANGO_SECRET_KEY", default='CHANGEME!!!')

# PROJECT APPS
# -----------------------------------------------------------------------------
DJANGO_APPS = (
    # Default Django apps:
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Useful template tags:
    'django.contrib.humanize',

    # Admin
    'django.contrib.admin',
)

THIRD_PARTY_APPS = (
    'suit',
    'session_security',
)

# Apps specific for this project go here.
LOCAL_APPS = (
    'emma.core',
    'emma.apps.landing',
    'emma.apps.emmas',
    'emma.apps.clients',
    'emma.apps.suscriptions',
    'emma.apps.services',
    'emma.apps.users',
    'emma.apps.adults',
    'emma.apps.doctors',
    'emma.apps.xauth',
    'emma.apps.newsletter',
)

INSTALLED_APPS = THIRD_PARTY_APPS + DJANGO_APPS + LOCAL_APPS

# MIDDLEWARE CLASSES
# -----------------------------------------------------------------------------
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'session_security.middleware.SessionSecurityMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

# MIGRATION
# -----------------------------------------------------------------------------
MIGRATION_MODULES = {
    'sites': 'cookies.contrib.sites.migrations'
}

# FIXTURE CONFIGURATION
# -----------------------------------------------------------------------------
FIXTURE_DIRS = (
    str(PROJECT_DIR.path('fixtures')),
)

# GENERAL CONFIGURATION
# -----------------------------------------------------------------------------
TIME_ZONE = 'America/Mexico_City'

LANGUAGE_CODE = 'es'

SITE_ID = 1

USE_I18N = True

USE_L10N = True

USE_TZ = True

PASSWORD_RESET_TIMEOUT_DAYS = 1

# TEMPLATE CONFIGURATION
# -----------------------------------------------------------------------------
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            str(PROJECT_DIR.path('templates')),
        ],
        'OPTIONS': {
            'debug': True,
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            ],
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# URL Configuration
# -----------------------------------------------------------------------------
ROOT_URLCONF = 'config.urls'

WSGI_APPLICATION = 'config.wsgi.application'

# AUTHENTICATION CONFIGURATION
# -----------------------------------------------------------------------------
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)

# SUIT CONFIGURATION
# -----------------------------------------------------------------------------
SUIT_CONFIG = {
    'ADMIN_NAME': 'Emma',
}

EMAIL_BACKEND = 'django_mailgun.MailgunBackend'
MAILGUN_ACCESS_KEY = env("MAILGUN_ACCESS_KEY")
MAILGUN_SERVER_NAME = env("MAILGUN_SERVER_NAME")

STATICFILES_DIRS = (
    str(PROJECT_DIR.path('static')),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

LOGIN_URL = reverse_lazy('xauth:login')

AUTH_USER_MODEL = "users.CoolUser"

# SESSION SECURITY
# -----------------------------------------------------------------------------
SESSION_EXPIRE_AT_BROWSER_CLOSE = env.bool('SESSION_EXPIRE_AT_BROWSER_CLOSE',
                                           default=True)
SESSION_SECURITY_EXPIRE_AFTER = env.int("SESSION_SECURITY_EXPIRE_AFTER")
SESSION_SECURITY_WARN_AFTER = env.int("SESSION_SECURITY_WARN_AFTER")


DATE_INPUT_FORMATS = [
    '%d/%m/%Y'
]