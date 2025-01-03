from .base import *
import os
from urllib.parse import urlparse

DEBUG = False
# ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', 'web-production-d72eb.up.railway.app').split(',')
ALLOWED_HOSTS = ['web-production-d72eb.up.railway.app']


# Secret Key
SECRET_KEY = os.getenv('SECRET_KEY')

# Banco de dados para produção
DATABASE_URL = os.getenv('DATABASE_URL')
if not DATABASE_URL:
    raise ValueError("DATABASE_URL is not set in the environment variables")
url = urlparse(DATABASE_URL)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': url.path[1:],
        'USER': url.username,
        'PASSWORD': url.password,
        'HOST': url.hostname,
        'PORT': url.port,
    }
}

# Configurações de segurança para produção
SECURE_HSTS_SECONDS = 31536000  # HSTS ativo por um ano
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Configurações adicionais de produção
CACHE_MIDDLEWARE_ALIAS = 'default'
CACHE_MIDDLEWARE_SECONDS = 600
CACHE_MIDDLEWARE_KEY_PREFIX = 'sisaero'

# Configuração do Celery (caso necessário)
CELERY_BROKER_URL = os.getenv('CELERY_BROKER_URL', 'redis://localhost:6379/0')
