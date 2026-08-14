from fastapi.testclient import TestClient
from demo_server import app

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_rag():
    response = client.post("/rag/ask", json={"question": "How does AI use retrieval?"})
    assert response.status_code == 200
    assert response.json()["source"] == "ai"


def test_support_routes_security():
    response = client.post("/support/triage", json={"message": "My account was hacked"})
    assert response.status_code == 200
    assert response.json()["route"] == "human_review"


def test_prediction():
    response = client.post("/ml/predict", json={"features": [2, 4, 6]})
    assert response.status_code == 200
    assert response.json()["prediction"] == 4
