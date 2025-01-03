#!/bin/bash

# Aplicar migrações
python manage.py migrate

# Verificar e criar superusuário, se necessário
python manage.py shell -c "from django.contrib.auth.models import User; \
  from django.core.exceptions import ObjectDoesNotExist; \
  try: \
      User.objects.get(username='$DJANGO_SUPERUSER_USERNAME'); \
  except ObjectDoesNotExist: \
      from django.core.management import call_command; \
      call_command('createsuperuser', '--noinput', '--username', '$DJANGO_SUPERUSER_USERNAME', '--email', '$DJANGO_SUPERUSER_EMAIL')"

# Iniciar o servidor com Gunicorn
exec "$@"
