"""
Django settings for todolist project.

Generated by 'django-admin startproject' using Django 4.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path

# project root dir
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-_0if70vu4_ux@k)@7f*q&7tt1zafo_c3pq=^b#i!b3kgd@2yfk'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

# apps (installed) in this project
INSTALLED_APPS = [
    # -- added
    # - EventsConfig class in events/apps.py
    'events.apps.EventsConfig',
    'accounts.apps.AccountsConfig',
    # - admin app for the administrator to maintain data
    'django.contrib.admin',
    # - user authorization app
    'django.contrib.auth',
    # - associating models and permissions
    'django.contrib.contenttypes',
    # - managing sessions
    'django.contrib.sessions',
    'django.contrib.messages',
    # - managing static files
    'django.contrib.staticfiles',
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

# root urlconf (here set to (urlpatterns in) todolist/urls.py)
ROOT_URLCONF = 'todolist.urls'

TEMPLATES = [
    {
        # - template rendering engine of django
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # - modified: set additional templates dirs (here to templates/ under
        # - project root dir) in addition to the default templates dirs
        # - (templates/ under apps dirs if 'APP_DIRS' set to True), to save
        # - common templates used by multiple apps in the project, or templates
        # - used by any contrib app which isn't in the project root dir
        'DIRS': [ './templates', ],
        # - using templates/ under each app dir (in turn) as the default
        # - templates dirs; an app can put its templates in a sub-dir with the
        # - same name as the app under its templates/ sub-dir, to add the app
        # - name as the namespace when referencing its templates, for example,
        # - using "events/index.html" to reference
        # - events/templates/events/index.html; of course, the template name can
        # - also be used to distinguish the app it belongs to, for example,
        # - events/templates/event_list.html
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

WSGI_APPLICATION = 'todolist.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        # python has built-in sqlite support, therefore no additional
        # installation or configuration required
        'ENGINE': 'django.db.backends.sqlite3',
        # for sqlite, this is the database file
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

# modified
TIME_ZONE = 'Pacific/Auckland'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

# the "static" statement should be used in a template to generate the url of a
# static file, which includes this STATIC_URL part; django (staticfiles app)
# maps it to static/ under each app dir (in turn) by default; an app will put
# its static files in a sub-dir with the same name as the app under its static/
# sub-dir (instead of distinguishing by the static file name), for example,
# using "events/style.css" to reference events/static/events/style.css; note
# that the "static" statement can only be used in templates, in static files,
# the relative path should be used instead
STATIC_URL = 'static/'
# added: set additional static dirs (here to static/ under project root dir) in
# addition to the default static dirs (static/ under apps dirs), to save common
# static files used by multiple apps in the project
STATICFILES_DIRS = [
    BASE_DIR / "static", ]

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
