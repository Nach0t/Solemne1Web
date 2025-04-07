from datetime import datetime

import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get(
    "/time",
    summary="Obtener la fecha y hora actual",
    description="Devuelve la fecha y hora actual en formato JSON.",
)
async def get_time():
    """
    Retorna la fecha y hora actual en formato Año-Mes-Día Hora:Minuto:Segundo.
    """
    now = datetime.now()
    formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")
    return {"time": formatted_time}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
