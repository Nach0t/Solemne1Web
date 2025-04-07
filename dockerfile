# Imagen base
FROM python:3.12-slim

# Establecer el directorio de trabajo en el contenedor
WORKDIR /app

# Copiar los archivos necesarios para instalar dependencias
COPY pyproject.toml poetry.lock* /app/

# Instalar poetry
RUN pip install poetry

# Configurar poetry para no crear entornos virtuales y luego instalar dependencias
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

# Copiar el resto del proyecto al contenedor
COPY . /app

# Exponer el puerto 8000
EXPOSE 8000

# Comando para ejecutar la aplicación FastAPI
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
