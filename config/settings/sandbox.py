#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Production settings
- Run in production mode
- Use Amazon's S3 for storing static files
"""

from .base import *

import dj_database_url
import openpay

# DEBUG
# -----------------------------------------------------------------------------
DEBUG = env.bool('DJANGO_DEBUG', default=False)
TEMPLATES[0]['OPTIONS']['debug'] = DEBUG

# This ensures that Django will be able to detect a secure connection
# properly on Heroku.
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# SITE CONFIGURATION
# -----------------------------------------------------------------------------
ALLOWED_HOSTS = [".miemma.com"]

# DATABASE
# -----------------------------------------------------------------------------
DATABASES = {
    'default': dj_database_url.config()
}

# STATIC FILE CONFIGURATION
# -----------------------------------------------------------------------------
INSTALLED_APPS += ('storages', )

STATIC_URL = env("AWS_BUCKET_URL")

STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

AWS_STORAGE_BUCKET_NAME = env("AWS_STORAGE_BUCKET_NAME")

AWS_ACCESS_KEY_ID = env("AWS_ACCESS_KEY_ID")

AWS_SECRET_ACCESS_KEY = env("AWS_SECRET_ACCESS_KEY")

AWS_S3_HOST = env("AWS_S3_HOST")

# MEDIA CONFIGURATION
# -----------------------------------------------------------------------------
MEDIA_ROOT = str(PROJECT_DIR('media'))

MEDIA_URL = '/media/'

# EMAIL CONFIGURATION
# -----------------------------------------------------------------------------
DEFAULT_EMAIL_TO = "devsemma@gmail.com"

openpay.api_key = "sk_2ed3e30960384907a0c73444ce6ea1a4"
openpay.verify_ssl_certs = False
openpay.merchant_id = "mg0kzdwsiduimlfaudun"
openpay.production = False