from .base import *
import os
from urllib.parse import urlparse

# Definir DEBUG como False para produção
DEBUG = False

# Definir ALLOWED_HOSTS com base na variável de ambiente
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', 'web-production-9dd13.up.railway.app').split(',')

# Secret Key
SECRET_KEY = os.getenv('SECRET_KEY')
if not SECRET_KEY:
    raise ValueError("SECRET_KEY is not set in the environment variables")

# Banco de dados para produção (PostgreSQL)
DATABASE_URL = os.getenv('DATABASE_URL')
if not DATABASE_URL:
    raise ValueError("DATABASE_URL is not set in the environment variables")
url = urlparse(DATABASE_URL)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': url.path[1:],  # Remove o primeiro caractere '/' do path
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
SECURE_SSL_REDIRECT = True  # Força redirecionamento para HTTPS
SESSION_COOKIE_SECURE = True  # Garante que a sessão só seja transmitida via HTTPS
CSRF_COOKIE_SECURE = True  # Garante que o CSRF só seja transmitido via HTTPS
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')  # Cabeçalho para proxy reverso

# Configurações de cache para produção
CACHE_MIDDLEWARE_ALIAS = 'default'
CACHE_MIDDLEWARE_SECONDS = 600  # Cache de 10 minutos
CACHE_MIDDLEWARE_KEY_PREFIX = 'sisaero'

# Configuração do Celery (caso necessário)
CELERY_BROKER_URL = os.getenv('CELERY_BROKER_URL', 'redis://localhost:6379/0')

# Definir a configuração de URLs
ROOT_URLCONF = 'SisAero.urls'


# Outras configurações específicas para produção podem ser necessárias
# (como e-mails, armazenamento de arquivos estáticos, etc.)

