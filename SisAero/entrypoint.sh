#!/bin/bash

# Executar migrações do banco de dados
echo "Executando migrações do banco de dados..."
python manage.py migrate --noinput

# Criar superusuário, se necessário
echo "Verificando se o superusuário existe..."
python manage.py shell -c "
from django.contrib.auth.models import User;
from django.core.exceptions import ObjectDoesNotExist;

username = '${DJANGO_SUPERUSER_USERNAME}'
email = '${DJANGO_SUPERUSER_EMAIL}'
password = '${DJANGO_SUPERUSER_PASSWORD}'

try:
    User.objects.get(username=username)
    print(f'Superusuário {username} já existe.')
except ObjectDoesNotExist:
    print(f'Criando superusuário {username}...')
    User.objects.create_superuser(username=username, email=email, password=password)
"

# Iniciar o servidor com Gunicorn
echo "Iniciando o servidor com Gunicorn..."
exec "$@"
