# Solemne 1 - API de Hora Actual con FastAPI

![CI/CD](https://github.com/nach0t/solemne1web/actions/workflows/main.yml/badge.svg)

---

## Descripción

Este proyecto consiste en una API sencilla desarrollada con **FastAPI** que expone un endpoint `/time` para entregar la fecha y hora actual en formato JSON.

El objetivo es poner en práctica el uso de contenedores **Docker** y flujos de trabajo de **CI/CD** mediante **GitHub Actions**, automatizando la construcción, pruebas y despliegue de la aplicación.

---

## Tecnologías Utilizadas

- Python 3.12  
- FastAPI  
- Uvicorn  
- Poetry  
- Pytest  
- Docker  
- GitHub Actions (CI/CD)  
- Flake8 y Ruff (linting)  

---

## Estructura del Proyecto

- Proyecto gestionado con entorno virtual usando [Poetry](https://python-poetry.org/)
- Archivo `.gitignore` configurado para excluir archivos innecesarios.

---

## Instrucciones para ejecutar localmente

1. Clona el repositorio:

   ```bash
   git clone https://github.com/Nach0t/Solemne1Webs
   cd Solemne1Webs
   ```

2. Instala Poetry (si no lo tienes):

   ```bash
   pip install poetry
   ```

3. Instala las dependencias del proyecto:

   ```bash
   poetry install
   ```

4. Ejecuta la aplicación localmente:

   ```bash
   uvicorn main:app --reload --host 127.0.0.1 --port 8000
   ```

5. Abre en el navegador o usa curl para probar el endpoint:

   ```bash
   http://127.0.0.1:8000/time
   ```

   ```bash
   curl http://127.0.0.1:8000/time
   ```

---

## Cómo ejecutar con Docker

1. Construye la imagen:

   ```bash
   docker build -t solemne1api .
   ```

2. Ejecuta el contenedor:

   ```bash
   docker run -p 8000:8000 solemne1api
   ```

3. Prueba el endpoint en el navegador o con curl:

   ```bash
   http://localhost:8000/time
   ```

   ```bash
   curl http://localhost:8000/time
   ```

---

## Imagen en Docker Hub  [![Docker](https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=fff)](#)

[![Docker Hub](https://img.shields.io/badge/Docker--Hub-nach0t%2Fsolemne1web-blue?style=for-the-badge&logo=docker)](https://hub.docker.com/r/nach0t/solemne1web)
[![Automated Build](https://img.shields.io/docker/automated/nach0t/solemne1web?style=for-the-badge)](https://hub.docker.com/r/nach0t/solemne1web)
![Image Size](https://img.shields.io/docker/image-size/nach0t/solemne1web/latest?style=for-the-badge)

Puedes usar la imagen directamente desde Docker Hub:

 [https://hub.docker.com/repository/docker/nach0t/solemne1web/general](https://hub.docker.com/repository/docker/nach0t/solemne1web/general)

```bash
docker pull nach0t/solemne1web:latest
```

---

## Cómo testear la API

Para correr las pruebas unitarias con Pytest:

```bash
poetry run pytest test_main.py
```

---

## Ejemplo de salida del endpoint

```json
{
  "time": "2025-04-07 18:30:45"
}
```

---

## CI/CD con GitHub Actions

![CI/CD](https://github.com/nach0t/solemne1web/actions/workflows/main.yml/badge.svg)

Cada push a la rama `main` ejecuta automáticamente:

- Instalación de Python 3.12  
- Instalación de dependencias con Poetry  
- Revisión de código con Flake8 y Ruff  
- Ejecución de pruebas con Pytest  
- Construcción de la imagen Docker  
- Login en Docker Hub  
- Publicación de la imagen como `nach0t/solemne1web:latest`  
