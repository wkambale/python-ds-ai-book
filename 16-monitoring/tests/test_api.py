# tests/test_api.py
"""
API tests for MobiCash churn prediction service.

These tests verify:
1. API endpoints return correct status codes
2. Input validation works correctly
3. Error handling is appropriate
"""
import sys
from pathlib import Path

# Add 15-deployment to sys.path to test the deployment app
app_dir = Path(__file__).resolve().parent.parent.parent / "15-deployment"
sys.path.insert(0, str(app_dir))

import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch, MagicMock
from app.main import app

client = TestClient(app)

valid_payload = {
    "age": 34,
    "tenure_months": 12,
    "account_balance": 25000.50,
    "avg_monthly_deposits": 50000.0,
    "avg_monthly_withdrawals": 30000.0,
    "days_since_last_transaction": 5,
    "customer_support_tickets": 1,
    "location": "Kampala"
}

def test_predict_endpoint():
    response = client.post("/predict", json=valid_payload)
    assert response.status_code == 200
    data = response.json()
    assert 0.0 <= data["churn_probability"] <= 1.0
    assert data["risk_category"] in ["Low", "Medium", "High"]