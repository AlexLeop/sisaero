# Etapa 1: Definir a imagem base com Python 3.12.6
ARG PYTHON_VERSION=3.12-slim-bullseye
FROM python:${PYTHON_VERSION}
# FROM python:3.12.6-slim

# Etapa 2: Instalar dependências do sistema
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
      postgresql-client \
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
    DJANGO_SETTINGS_MODULE=SisAero.settings.production \
    PORT=8000 \
    DJANGO_SUPERUSER_USERNAME=alex.leopoldo \
    DJANGO_SUPERUSER_PASSWORD=Apport@903 \
    DJANGO_SUPERUSER_EMAIL=alex.leopoldo@apportnegocios.com.br

# Etapa 7: Coletar arquivos estáticos
RUN python manage.py collectstatic --noinput

# Etapa 8: Copiar o script de inicialização
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Etapa 9: Expor a porta que o contêiner vai escutar
EXPOSE 8000

# Etapa 10: Definir o script como ponto de entrada
ENTRYPOINT ["/entrypoint.sh"]

# Etapa 11: Comando para iniciar o servidor com Gunicorn
CMD ["gunicorn", "SisAero.wsgi:application", "--bind", "0.0.0.0:${PORT}"]
