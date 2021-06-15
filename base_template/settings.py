import os
import json
from datetime import timedelta
from pathlib import Path
from django.conf.locale.ru import formats

BASE_DIR = Path(__file__).resolve().parent.parent

try:
    with open(os.path.join(BASE_DIR, 'local', 'config.json')) as handle:
        config = json.load(handle)
except IOError:
    config = {
        'secret_key': 'simple_key',
        'db_type': 'sqlite3'
    }

SECRET_KEY = str(config['secret_key'])

# При False необходимо настроить nginx
DEBUG = True
ALLOWED_HOSTS = ['*']

# Используемые приложения
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'section',
    'config',
    'ckeditor',
    'ckeditor_uploader',
    'account',
    'rest_framework',
    'rest_framework_simplejwt',
    'rest_framework.authtoken',
    'djoser'
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


# API
DJOSER = {
    'PASSWORD_RESET_CONFIRM_URL': '#/password/reset/confirm/{uid}/{token}',
    'USERNAME_RESET_CONFIRM_URL': '#/username/reset/confirm/{uid}/{token}',
    'ACTIVATION_URL': '#/activate/{uid}/{token}',
    'SEND_ACTIVATION_EMAIL': False,
    'SERIALIZERS': {},
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': True,

    'ALGORITHM': 'HS256',
    'SIGNING_KEY': SECRET_KEY,
    'VERIFYING_KEY': None,
    'AUDIENCE': None,
    'ISSUER': None,

    'AUTH_HEADER_TYPES': ('JWT',),
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',

    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',

    'JTI_CLAIM': 'jti',

    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    'SLIDING_TOKEN_LIFETIME': timedelta(minutes=5),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
}

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    # 'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    # 'PAGE_SIZE': 1
}


# Настройка CKeditor
CKEDITOR_JQUERY_URL = '//ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js'
CKEDITOR_UPLOAD_PATH = 'redactor/'
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar_Custom': [
            ['Format'],
            ['JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
            ['Bold', 'Italic', 'Underline', 'Strike'],
            ['TextColor', 'BGColor'],
            ['NumberedList', 'BulletedList', 'Blockquote'],
            ['Image', 'Table', 'HorizontalRule', 'SpecialChar'],
            ['Link', 'Unlink', 'Anchor'],
            '/',
            ['Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord'],
            ['Scayt'],
            ['Maximize'],
            ['RemoveFormat', 'Source'],
        ],
        'toolbar': 'Custom',
        'removePlugins': 'stylesheetparser',
        'allowedContent': True,
        'forcePasteAsPlainText': True,
        'width': 1050,
    },
}


# Настройка шаблонов
ROOT_URLCONF = 'base_template.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
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

WSGI_APPLICATION = 'base_template.wsgi.application'


# Настройки базы данных
if config.get("db_type") == 'sqlite3':
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
elif config.get("db_type") == "psql":
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': config.get("database", ""),
            'USER': config.get("user", ""),
            'PASSWORD': config.get("password", ""),
            'HOST': config.get("host", ""),
            'PORT': config.get("port", ""),
        }
    }
else:
    print("""
Укажите тип базы данных в файле local/config.json
sqlite3 или psql
    """)

# Настройки Auth

AUTH_USER_MODEL = 'account.User'

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


# Настройки локализации
formats.DATETIME_FORMAT = "d.m.Y H:i:s"
LANGUAGE_CODE = 'ru'
TIME_ZONE = 'Europe/Moscow'
USE_I18N = True
USE_L10N = True
USE_TZ = True
get_text = lambda s: s
LANGUAGES = (
    ('ru', get_text('Русский')),
)
LANGUAGES_ADMIN = {
    'ru': 'Русский',
}


# Настройки медиа и статик файлов
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
