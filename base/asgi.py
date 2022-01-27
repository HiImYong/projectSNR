"""
ASGI config for base project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

import dotenv
from django.core.asgi import get_asgi_application
dotenv.read_dotenv(os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env'))

#일반에 메시지 보내기
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'base.settings.prod')

application = get_asgi_application()
