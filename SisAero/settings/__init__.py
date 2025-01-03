import os

# Define o módulo de configuração padrão com base no ambiente
settings_module = os.getenv('DJANGO_SETTINGS_MODULE', 'seu_projeto.settings.development')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_module)
