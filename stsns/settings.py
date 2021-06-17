
from pathlib import Path
from socket import gethostname
import os
import dj_database_url
import sys
import environ
import django_heroku
import dj_database_url
import socket


BASE_DIR = environ.Path(__file__) - 2
env = environ.Env()

READ_ENV_FILE = env.bool('DJANGO_READ_ENV_FILE', default=True)
if READ_ENV_FILE:
    env_file = str(BASE_DIR.path('.env'))
    env.read_env(env_file)

SECRET_KEY = env('SECRET_KEY')
ALLOWED_HOSTS = ["*"]

hostname = socket.gethostname()

if "COMPUTER-NAME" in hostname:
    #デバッグ環境
    DEBUG = True
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
    ALLOWED_HOSTS = ['*'] 
else:
    # 本番環境
    DEBUG = True
    DATABASES = { 'default': {
    'ENGINE': 'django.db.backends.postgresql_psycopg2',
    'NAME': 'dep6t1686mad06',
    'USER': 'yhrhdzwdcelghc',
    'PASSWORD': '6866297a376d70ebb8c4e4772092fe4a9d2aa48e507659e4d8918bada5305e04',
    'HOST': 'ec2-34-193-113-223.compute-1.amazonaws.com',
    'PORT': '5432',
    }
    }


PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
db_from_env = dj_database_url.config()
DATABASES = {
    'default': dj_database_url.config()
}

DATABASES['default'] = dj_database_url.config(default='sqlite://db/sqlite3.db')



INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'stsnsapp.apps.StsnsappConfig',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'stsns.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR +"templates"],
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

WSGI_APPLICATION = 'stsns.wsgi.application'


db_from_env = dj_database_url.config(conn_max_age=600, ssl_require=True)
DATABASES['default'].update(db_from_env)

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

LANGUAGE_CODE = 'ja'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS =[
   os.path.join(BASE_DIR, 'static/img_file'),
]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_URL = 'stsnsapp:login' 
LOGIN_REDIRECT_URL = 'stsnsapp:top_page' 
AUTH_USER_MODEL = "stsnsapp.CustomUser"