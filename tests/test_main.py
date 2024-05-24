from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_user():
    response = client.post("/users/", json={"name": "testuser", "email": "testuser@example.com", "password": "password"})
    assert response.status_code == 200
    assert response.json()["email"] == "testuser@example.com"

def test_read_user():
    response = client.get("/users/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1