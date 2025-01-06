# Dockerfile

# Etapa 1: Base da imagem
FROM python:3.12-slim-bullseye

# Etapa 2: Instalar dependências do sistema
RUN apt-get update && apt-get install -y --no-install-recommends \
    postgresql-client build-essential libpq-dev && rm -rf /var/lib/apt/lists/*

# Etapa 3: Diretório de trabalho
WORKDIR /app

# Etapa 4: Copiar os arquivos do projeto
COPY . /app/

# Etapa 5: Instalar dependências do Python
RUN pip install --upgrade pip && pip install -r requirements.txt

# Etapa 6: Coletar arquivos estáticos
RUN python manage.py collectstatic --noinput

# Etapa 7: Configurar variáveis de ambiente para produção
ENV PYTHONUNBUFFERED=1 \
    DJANGO_SETTINGS_MODULE=SisAero.settings.production \
    PORT=8000

# Etapa 8: Copiar o entrypoint
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Etapa 9: Expor a porta da aplicação
EXPOSE 8000

# Etapa 10: Definir o entrypoint e o comando inicial
ENTRYPOINT ["/entrypoint.sh"]
CMD ["gunicorn", "SisAero.wsgi:application", "--bind", "0.0.0.0:8000"]
