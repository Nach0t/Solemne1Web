from datetime import datetime

import uvicorn
from fastapi import FastAPI

# Crear una instancia de la aplicación FastAPI
app = FastAPI()


@app.get(
    "/time",
    summary="Obtener la fecha y hora actual",
    description="Devuelve la fecha y hora actual en formato JSON.",
)
async def get_time():
    """
    Retorna la fecha y hora actual en formato Año-Mes-Día Hora:Minuto:Segundo.

    Esta ruta devuelve un diccionario con la clave 'time' y el valor como la fecha
    y hora actual del servidor en formato legible (ejemplo: 2025-04-09 14:23:45).
    Returns:
        dict: Un diccionario con la hora actual en formato string.
    """
    now = datetime.now()
    formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")
    return {"time": formatted_time}


if __name__ == "__main__":
    # Ejecutar el servidor de desarrollo con recarga automática
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
