from .base import *

DEBUG = True
ALLOWED_HOSTS = ["*"]

# Banco de dados para desenvolvimento
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Configurações adicionais de desenvolvimento (se necessário)
