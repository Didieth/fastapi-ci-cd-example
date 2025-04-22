from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello CI/CD"}


def test_read_2_root():
    response = client.get("/hello")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello world"}
    
#nuevooooooooooooooooooooooo

def test_nuevo_endpoint():
    response = client.get("/nuevo")
    assert response.status_code == 200
    assert response.json() == {"message": "Este es el nuevo endpoint"}

