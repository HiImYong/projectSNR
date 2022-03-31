"""
Django settings for base project.

Generated by 'django-admin startproject' using Django 3.2.9.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-cgtn-ka(zm@d#e^ppv%42!#3l--ben$)37r5+re_$#hq92^os9'

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

    'racket.apps.RacketConfig',
    'account.apps.AccountConfig',
    'racketReview.apps.racketReviewConfig',
    'player.apps.PlayerConfig',
    'playerReview.apps.PlayerreviewConfig',
    'feedback.apps.FeedbackConfig',
    'article.apps.ArticleConfig',


    # 'racketstring.apps.RacketString',

    #'django_bootstrap5',
    # 'django_extensions',

]

MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',  # 추가

    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'base.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates/'],
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

WSGI_APPLICATION = 'base.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'snr',
        'USER': 'snrst',
        'PASSWORD': 'snr123414',
        'HOST': '172.17.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
            # 추가, 만약에 이 부분 때문에 오류가 난다면 삭제할 것
            # MySQL Strict Mode 켜기
            'charset': 'utf8mb4',
            # 이모지 등록 가능
            'use_unicode': True,
        }
    }
}


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

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
#추가
STATICFILES_DIRS = [
    BASE_DIR / 'base/static',
]

# 개발자가 구성한 정적파일들의 폴더 경로
STATIC_ROOT = BASE_DIR / 'static'

# 사용자가 업로드한 정적파일폴더 경로
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'account.User'

# 실제 운영서버 도메인
# 장고 최신버전부터 이걸 안하면 안됨
CSRF_TRUSTED_ORIGINS = ['https://tennis.uyong.site', 'https://cdpn.io']

# 이거 안하면 외부에서 이 서버의 API를 사용하지 못합니다.
CORS_ORIGIN_WHITELIST = CSRF_TRUSTED_ORIGINS

GRAPH_MODELS = {
  'all_applications': True,
  'group_models': True,
}