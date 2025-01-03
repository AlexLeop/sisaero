from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Defina o módulo de configuração do Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SisAero.settings')

# Criação da instância do Celery
app = Celery('SisAero')

# Usando o backend Redis para tarefas e fila
app.config_from_object('django.conf:settings', namespace='CELERY')

# Carrega as tarefas de todos os apps registrados
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
