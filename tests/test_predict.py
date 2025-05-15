from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_single_prediction():
    payload = {
        "text": "Congratulations! You've won a free lottery. Click here to claim."
    }

    response = client.post("/api/v1/predict", json=payload)

    assert response.status_code == 200
    assert "prediction" in response.json()
    assert response.json()["prediction"] in [0, 1]  # Assuming binary classification
    