# Etapa 1: Definir a imagem base com Python 3.12.6
FROM python:3.12.6-slim

# Etapa 2: Instalar dependências do sistema
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Etapa 3: Definir diretório de trabalho
WORKDIR /app

# Etapa 4: Copiar os arquivos do projeto para o contêiner
COPY . /app/

# Etapa 5: Instalar dependências do Python
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Etapa 6: Configurar variáveis de ambiente para produção
ENV PYTHONUNBUFFERED=1 \
    DJANGO_SETTINGS_MODULE=seu_projeto.settings.production \
    PORT=8000

# Etapa 7: Coletar arquivos estáticos (executar antes de iniciar o servidor)
RUN python manage.py collectstatic --noinput

# Etapa 8: Expor a porta que o contêiner vai escutar
EXPOSE 8000

# Etapa 9: Comando para iniciar o servidor com Gunicorn
CMD ["gunicorn", "seu_projeto.wsgi:application", "--bind", "0.0.0.0:${PORT}"]

# Etapa 10: Iniciar o servidor de desenvolvimento no caso de não usar o Gunicorn (para debug, se necessário)
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
