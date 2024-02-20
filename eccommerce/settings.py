"""
Django settings for eccommerce project.

Generated by 'django-admin startproject' using Django 3.2.23.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os
import dj_database_url

from dotenv import load_dotenv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!


AUTHENTICATION_BACKENDS =(
    "django.contrib.auth.backends.ModelBackend"
    "allauth.account.auth_backends.AuthenticationBackend"
)
SECRET_KEY = 'django-insecure-!m4k7cpy&e=g@q0s$66vlgi2v$uurki9!!68hh#oxn9ev!^1$t'
SITE_ID = 1 
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
ACCOUNT_AUTHENTICATION_METHOD = "username_email"
ACCOUNT_EMAIL_REQUIRED = True
# ACCOUNT_EMAIL_VERIFICATION = "mandatory"
ACCOUNT_USERNAME_MIN_LENGTH =4
# ACCOUNT_SIGNUP_EMAIL_ENTER_TWICE=True
LOGIN_URL=""
LOGIN_REDIRECT_URL="/"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ALLOWED_HOSTS = ["*","https://reservebooking-f88a92f8cf30.herokuapp.com/"]


# Application definition

INSTALLED_APPS = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
      'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
     "eccommerce.apps.BaseConfig",
      
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
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

ROOT_URLCONF = 'eccommerce.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [

            os.path.join(BASE_DIR,"templates"),
            os.path.join(BASE_DIR,"templates","allauth")

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

WSGI_APPLICATION = 'eccommerce.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
db_from_env = dj_database_url.config(conn_max_age=600)
DATABASES['default'].update(db_from_env)


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

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

print("weWEEWE",BASE_DIR)
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# Default primary key field typek
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'





JSONFOOD = [
    {
    "id":"1",
    "name":"Barbecue",
    "price":"20",
    "ratings":"2",
    "image":"alex-munsell-auIbTAcSH6E-unsplash.jpg"

},
    {
    "name":"Barbecue",
    "id":"2",
    "price":"20",
    "ratings":"2",
    "image":"alex-munsell-Yr4n8O_3UPc-unsplash.jpg"

},
    {
    "name":"italian beans",
    "id":"3",
    "price":"25",
    "ratings":"2",
    "image":"anh-nguyen-kcA-c3f_3FE-unsplash.jpg"

},
    {
    "name":"straw berry cake",
    "id":"4",
    "price":"30",
    "ratings":"2",
    "image":"anna-tukhfatullina-food-photographer-stylist-Mzy-OjtCI70-unsplash (1).jpg"

},
    {
    "name":"waffles",
    "id":"5",
    "price":"10",
    "ratings":"2",
    "image":"asnim-ansari-SqYmTDQYMjo-unsplash.jpg"

},
    {
    "name":"noodles",
    "id":"6",
    "price":"20",
    "ratings":"2",
    "image":"brooke-lark--F_5g8EEHYE-unsplash.jpg"

},
    {
    "name":"tomato salad",
    "id":"7",
    "price":"20",
    "ratings":"2",
    "image":"brooke-lark-jUPOXXRNdcA-unsplash.jpg"

},
    {
    "name":"burger",
    "id":"8",
    "price":"20",
    "ratings":"5",
    "image":"chad-montano--GFCYhoRe48-unsplash.jpg"

},
    {
    "name":"shawarma",
    "id":"9",
    "price":"20",
    "ratings":"4",
    "image":"chad-montano-lP5MCM6nZ5A-unsplash.jpg"

},
    {
    "name":"pizza",
    "id":"10",
    "price":"30",
    "ratings":"4",
    "image":"chad-montano-MqT0asuoIcU-unsplash.jpg"

},
    {
    "name":"bread salad",
    "id":"11",
    "price":"10",
    "ratings":"4",
    "image":"davide-cantelli-jpkfc5_d-DI-unsplash.jpg"

},
    {
    "name":"oat",
    "id":"12",
    "price":"5",
    "ratings":"3",
    "image":"do-mee-SH8_JmrsQcw-unsplash.jpg"

},
    {
    "name":"pear salad",
    "id":"13",
    "price":"10",
    "ratings":"5",
    "image":"eiliv-aceron-ZuIDLSz3XLg-unsplash.jpg"

},
    {
    "name":"pudding",
    "id":"14",
    "price":"10",
    "ratings":"3",
    "image":"ella-olsson-mmnKI8kMxpc-unsplash.jpg"

},
    {
    "name":"vanilla icecream",
    "id":"15",
    "price":"15",
    "ratings":"5",
    "image":"emile-mbunzama-cLpdEA23Z44-unsplash.jpg"

},
    {
    "name":"porridge",
    "id":"16",
    "price":"15",
    "ratings":"5",
    "image":"emy-XoByiBymX20-unsplash.jpg"

},
    {
    "name":"milk cream",
    "id":"17",
    "price":"10",
    "ratings":"5",
    "image":"ian-dooley-TLD6iCOlyb0-unsplash.jpg"

},
    {
    "name":"pear pud",
    "id":"18",
    "price":"10",
    "ratings":"5",
    "image":"heather-ford-Ug7kk0kThLk-unsplash.jpg"

},
    {
    "name":"steak nd sauce",
    "id":"19",
    "price":"10",
    "ratings":"5",
    "image":"jennifer-burk-gwBcamFtPr4-unsplash.jpg"

},
    {
    "name":"fish meal",
    "id":"20",
    "price":"12",
    "ratings":"5",
    "image":"jonas-allert-MZ0U0g6RQpQ-unsplash.jpg"

},
    {
    "name":"abacha",
    "id":"21",
    "price":"10",
    "ratings":"5",
    "image":"jonathan-borba-Gkc_xM3VY34-unsplash.jpg"

},
    {
    "name":"peanut bread",
    "id":"22",
    "price":"9",
    "ratings":"5",
    "image":"joseph-gonzalez-zcUgjyqEwe8-unsplash.jpg"

},
    {
    "name":"fish soup",
    "id":"23",
    "price":"9",
    "ratings":"5",
    "image":"khloe-arledge-ND3edEmzcdQ-unsplash.jpg"

},
    {
    "name":"frut salad",
    "id":"24",
    "price":"10",
    "ratings":"5",
    "image":"luisa-brimble-vIm26fn_QKg-unsplash.jpg"

},
    {
    "name":"chinese rice",
    "id":"25",
    "price":"20",
    "ratings":"5",
    "image":"michele-blackwell-rAyCBQTH7ws-unsplash.jpg"

},
    {
    "name":"ora soup",
    "id":"26",
    "price":"20",
    "ratings":"5",
    "image":"monika-grabkowska-_y6A9bhILkM-unsplash.jpg"

},
    {
    "name":"bean pudding",
    "id":"14",
    "price":"20",
    "ratings":"5",
    "image":"monika-grabkowska-P1aohbiT-EY-unsplash.jpg"

},
]