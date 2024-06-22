import os
from core.settings.base import *


# Read enviroment variable from .env file
env.read_env(os.path.join(BASE_DIR, ".env"))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env.str("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool("DEBUG", default=False)

ALLOWED_HOSTS = ["your-website-url.domain"]
CSRF_TRUSTED_ORIGINS = ["https://your-website-url.domain"]


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

#Postgres setup
DATABASES = {
    "default": {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env.str("DB_NAME"),
        'USER': env.str("DB_USER"),
        'PASSWORD': env.str("DB_PASSWORD"),
        'HOST': env.str("DB_HOST"),
        'PORT': env.str("DB_PORT"),
    }
}

#AWS S3 settings
AWS_ACCESS_KEY_ID = env.str('AWS_ACCESS_KEY_ID') # add to env.
AWS_SECRET_ACCESS_KEY = env.str('AWS_SECRET_ACCESS_KEY') # add to env
AWS_STORAGE_BUCKET_NAME = env.str('AWS_STORAGE_BUCKET_NAME')
AWS_S3_REGION_NAME = env.str('AWS_S3_REGION_NAME')  # e.g., us-east-1
AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

# For serving static files directly from S3
AWS_S3_URL_PROTOCOL = 'https:'
AWS_S3_USE_SSL = True
AWS_S3_VERIFY = True

# Media S3 settings
MEDIA_URL = f'{AWS_S3_URL_PROTOCOL}://{AWS_S3_CUSTOM_DOMAIN}/media/'
MEDIA_ROOT = f'{AWS_S3_URL_PROTOCOL}://{AWS_S3_CUSTOM_DOMAIN}/'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'