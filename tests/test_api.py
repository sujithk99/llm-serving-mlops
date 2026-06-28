from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_ping():
    response = client.get("/ping")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

def test_invocations():
    response = client.post(
        "/invocations",
        json={"prompt": "What is Docker?"}
    )

    assert response.status_code == 200
    assert "response" in response.json()