"""
Django settings for core project.

Generated by 'django-admin startproject' using Django 5.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-dvs9j_r_$@4gl@w8ko#rwjd8)c3ti(dm2m_t&0_d9uumk2jia^'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crispy_bootstrap4',
    'crispy_forms',
    'malumotlar',
    'ziyoratgoh',
    'xizmat',
    'xabar',
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

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [str(BASE_DIR.joinpath('templates'))],
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

WSGI_APPLICATION = 'core.wsgi.application'

JAZZMIN_SETTINGS = {
    "site_title": "Admin Panel | O'zbegim",
    "site_header": "O'zbegim",
    "site_brand": "O'zbegim",
    "welcome_sign": "Admin Panelga xush kelibsiz!",
    "copyright": "Uzbegim",
    "show_sidebar": True,
    "navigation_expanded": True,
    "topmenu_links": [
        {"name": "Home", "url": "admin:index", "permissions": ["auth.view_user"]},
        {"name": "Yordam", "url": "https://t.me/Abbosbek_Turdaliyev", "new_window": True},
    ],
    "usermenu_links": [
        {"name": "Profile", "url": "/profile", "icon": "fas fa-user"},
    ],
    "icons": {
        "auth.User": "fas fa-user",  # Foydalanuvchilar uchun ikonka
        "auth.Group": "fas fa-users",  # Guruhlar uchun ikonka
        "xizmat.Oshxona": "fas fa-utensils", 
        "xizmat.Ustaxona": "fas fa-car",  
        "xizmat.Shifoxona": "fas fa-hospital", 
        "xizmat.Mehmonxona": "fas fa-hotel",  
        "malumotlar.Region": "fas fa-map-marked-alt", 
        "malumotlar.District": "fas fa-map-pin", 
        "malumotlar.Ish_kuni": "fas fa-calendar-check",  
        "xabar.Xabar": "fas fa-message", 
        "ziyoratgoh.Carusel": "fas fa-cogs",  
        "ziyoratgoh.Ziyoratgoh": "fas fa-place-of-worship",  
    },
    "changeform_format": "horizontal_tabs",
    "changeform_format_overrides": {
        "auth.user": "collapsible",
    },
}

JAZZMIN_UI_TWEAKS = {
    "navbar": "navbar-dark bg-primary",
    "sidebar": "sidebar-dark-primary",
    "theme": "darkly",
    "dark_mode_theme": "darkly",
}
# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
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

STATIC_URL = '/static/'
STATICFILES_DIRS = [str(BASE_DIR.joinpath('static'))]
STATIC_ROOT = str(BASE_DIR.joinpath('staticfiles'))
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

# Media saqlash joyi
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')  # asosiy loyiha katalogidan boshlanadi
MEDIA_URL = '/media/'  # brauzer orqali kirish uchun URL

# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'uz'

TIME_ZONE = 'Asia/Tashkent'

USE_I18N = True

USE_TZ = True



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CRISPY_TEMPLATE_PACK = 'bootstrap4'