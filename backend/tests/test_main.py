from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_mock_chat():
    response = client.post(
        "/v1/chat",
        json={"message": "Hello"},
    )

    assert response.status_code == 200
    data = response.json()
    assert data["provider"] == "mock"
    assert data["model"] == "demo"
    assert data["answer"] == "Mock response for: Hello"
