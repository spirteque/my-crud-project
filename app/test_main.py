from fastapi.testclient import TestClient
from .main import app


client = TestClient(app)


def test_create_item():
    response = client.post("/api/items/", json={"name": "test", "description": "test"})
    assert response.status_code == 200

def test_throw_error_on_forbidden_item():
    response = client.post("/api/items/", json={"name": "forbidden", "description": "test"})
    assert response.status_code == 409
