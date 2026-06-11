import sys
from pathlib import Path

from fastapi.testclient import TestClient

sys.path.append(str(Path(__file__).resolve().parents[1]))

from app.main import app


client = TestClient(app)


def test_health_endpoint():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_predict_endpoint():
    response = client.post(
        "/predict",
        json={"vehicle_count": 120, "temperature_c": 30, "rain_mm": 5, "hour": 17},
    )
    assert response.status_code == 200
    assert response.json()["congestion_score"] >= 0
    assert response.json()["label"] in {"Low", "Moderate", "High", "Critical"}
