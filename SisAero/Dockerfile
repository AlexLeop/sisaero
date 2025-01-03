# Etapa 1: Definir a imagem base com Python 3.12.6
FROM python:3.12.6-slim

# Etapa 2: Definir diretório de trabalho
WORKDIR /app

# Etapa 3: Copiar os arquivos do projeto para o contêiner
COPY . /app/

# Etapa 4: Instalar dependências
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Etapa 5: Expor a porta onde o Django será executado
EXPOSE 8000

# Etapa 6: Definir o comando para rodar o servidor Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
