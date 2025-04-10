from datetime import datetime
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
import uvicorn

# Crear una instancia de la aplicación FastAPI
app = FastAPI(
    title="API de Fecha y Hora",
    description="Una pequeña API que retorna la fecha y hora actual, y redirige desde la raíz al endpoint /time.",
    version="1.0.0",
    contact={
        "name": "Tu Nombre",
        "email": "tunombre@ejemplo.com"
    }
)


@app.get(
    "/time",
    summary="Obtener la fecha y hora actual",
    description="Devuelve la fecha y hora actual en formato JSON (Año-Mes-Día Hora:Minuto:Segundo).",
    response_description="Fecha y hora actual formateada."
)
async def get_time():
    """
    Retorna la fecha y hora actual en formato Año-Mes-Día Hora:Minuto:Segundo.

    Returns:
        dict: Un diccionario con la clave "time" y el valor de la fecha y hora actual.
    """
    now = datetime.now()
    formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")
    return {"time": formatted_time}


@app.get(
    "/",
    summary="Redireccionar a /time",
    description="Redirecciona automáticamente desde la raíz del servidor al endpoint /time.",
    include_in_schema=False  # Oculta este endpoint de la documentación interactiva
)
async def redirect_to_time():
    """
    Redirige la raíz del servidor a /time.

    Returns:
        RedirectResponse: Redirección al endpoint /time.
    """
    return RedirectResponse(url="/time")


# Punto de entrada principal si se ejecuta este archivo directamente
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
