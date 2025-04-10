from fastapi.testclient import TestClient
from main import app
import re

client = TestClient(app)


def test_get_time():
    """
    Prueba que el endpoint /time devuelva un código 200 y un campo 'time' en formato correcto.
    """
    response = client.get("/time")
    assert response.status_code == 200
    data = response.json()
    assert "time" in data

    # Validar formato YYYY-MM-DD HH:MM:SS usando regex
    pattern = r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}"
    assert re.fullmatch(pattern, data["time"]) is not None


def test_redirect_root_to_time():
    """
    Prueba que la raíz (/) redirige correctamente al endpoint /time.
    """
    response = client.get("/", allow_redirects=False)  # No seguir redirecciones automáticamente
    assert response.status_code == 307 or response.status_code == 302
    assert response.headers["location"] == "/time"
