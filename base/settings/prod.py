from .settings import *

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'snr',
        'USER': 'sbsst',
        'PASSWORD': 'sbs123414',
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