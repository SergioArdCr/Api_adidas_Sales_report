from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def get_token():
    client.post("/auth/register", json={"username": "test_ventas", "password": "pass"})
    response = client.post("/auth/login", data={"username": "test_ventas", "password": "pass"})
    return response.json()["access_token"]

def test_regiones_sin_token():
    response = client.get("/regiones")
    assert response.status_code == 401

def test_regiones_con_token():
    token = get_token()
    headers = {"Authorization": f"Bearer {token}"}
    response = client.get("/regiones", headers=headers)
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_ventas_region():
    response = client.get("/ventas/West")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_ventas_region_producto():
    response = client.get("/ventas/producto/West")
    assert response.status_code == 200
    assert isinstance(response.json(), list)