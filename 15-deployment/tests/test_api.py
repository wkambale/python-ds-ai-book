# tests/test_api.py
import sys
from pathlib import Path

# Add 15-deployment directory to path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.schemas import ChurnPredictionInput

@pytest.fixture
def client():
    """Create a test client."""
    return TestClient(app)

@pytest.fixture
def valid_input():
    """Sample valid prediction input."""
    return {
        "age": 34,
        "tenure_months": 12,
        "account_balance": 25000.50,
        "avg_monthly_deposits": 50000.0,
        "avg_monthly_withdrawals": 30000.0,
        "days_since_last_transaction": 5,
        "customer_support_tickets": 1,
        "location": "Kampala"
    }

def test_health_endpoint(client):
    """Test health check returns 200."""
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"

def test_valid_prediction(client, valid_input):
    """Test prediction with valid input."""
    response = client.post("/predict", json=valid_input)
    assert response.status_code == 200
    assert "churn_probability" in response.json()

def test_invalid_age_rejected(client, valid_input):
    """Test that out-of-range age is rejected."""
    valid_input["age"] = 150
    response = client.post("/predict", json=valid_input)
    assert response.status_code == 422

def test_negative_balance_rejected(valid_input):
    """Test that negative balance is rejected."""
    valid_input["account_balance"] = -100
    with pytest.raises(ValueError):
        ChurnPredictionInput(**valid_input)