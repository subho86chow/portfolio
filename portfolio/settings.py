from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-y&e1_1@+_ebly!tva)1a3d1eo0-f4!do6u&3)noz(qf=di9xc$'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']
CSRF_TRUSTED_ORIGINS = ['https://*.itsmeshubhajit.online','http://127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'website',
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

ROOT_URLCONF = 'portfolio.urls'

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

WSGI_APPLICATION = 'portfolio.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'verceldb',
        'USER': 'default',
        'PASSWORD': 'jfgU2TZPW6Xm',
        'HOST': 'ep-gentle-shadow-a1kzg23k-pooler.ap-southeast-1.aws.neon.tech',
        'PORT': '5432',
    }
}

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# email
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
PREMAILER_OPTIONS = {'remove_classes': False}
EMAIL_HOST = 'smtp.gmail.com'  # Your SMTP server
EMAIL_PORT = 587  # Your SMTP port (587 for TLS, 465 for SSL)
EMAIL_USE_TLS = True  # Use TLS (True/False)
EMAIL_HOST_USER = 'subho86chow@gmail.com'  # Your email address
EMAIL_HOST_PASSWORD = 'rtmd ejbx fube narb'  # Your email password
DEFAULT_FROM_EMAIL = 'subho@itsmeshubhajit.online' # default email address

# Static files (CSS, JavaScript, Images)

# STATIC_URL = 'static/'

# # Default primary key field type
# # https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

# DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# STATIC_URL = 'static/'


# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, 'static')
# ]
# # STATIC_ROOT=os.path.join(BASE_DIR,'staticfiles_build','static')

# MEDIA_URL = '/static/images/'
# STATIC_ROOT = 'staticfiles'
# # STATIC_ROOT=os.path.join(BASE_DIR,'staticfiles_build','static')

# MEDIA_URLS = 'static/images/'                 
# MEDIA_URL = '/static/images/'

# MEDIA_ROOT = os.path.join(BASE_DIR, 'static/images')


# -----------------dev---------------------

STATIC_URL = 'static/'


STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]
# STATIC_ROOT=os.path.join(BASE_DIR,'staticfiles_build','static')

MEDIA_URL = '/static/images/'
STATIC_ROOT = 'staticfiles'
# STATIC_ROOT=os.path.join(BASE_DIR,'staticfiles_build','static')

MEDIA_URLS = '/media/'                 
MEDIA_URL = 'media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'static/images')


# ---------------vercel--------------------



# STATIC_URL = 'static/'
# DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
# STATIC_URL = 'static/'
# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, 'static')
# ]
# MEDIA_URLS = '/images/'
# STATIC_ROOT=os.path.join(BASE_DIR,'staticfiles_build','static')
# MEDIA_URLS = '/images/'                 
# MEDIA_URL = '/static/images/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'static/images')