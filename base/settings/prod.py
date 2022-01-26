from .settings import *

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'snr', # 깃에 올릴거임. 근거리에서밖에 접속 못함. 사람륻이 알아도 접속 불가
        'USER': 'tlsrb0025',
        'PASSWORD': 'server123414',
        'HOST': '172.17.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
            # 추가, 만약에 이 부분 때문에 오류가 난다면, 이 라인을 지우고 다시 시도해주세요.
            # MySQL Strict Mode 켜기
        }
    }
}