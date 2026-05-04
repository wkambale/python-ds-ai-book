# tests/test_api.py
"""
API tests for MobiCash churn prediction service.

These tests verify:
1. API endpoints return correct status codes
2. Input validation works correctly
3. Error handling is appropriate
"""
import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch, MagicMock
import numpy as np

from app.main import app
from fastapi.testclient import TestClient
import pytest
from unittest.mock import MagicMock, patch

client = TestClient(app)

def test_predict_endpoint():
    with patch('app.main.model_service') as mock_service:
        for prob in [0.9, 0.4, 0.1]:
            if prob >= 0.8:
                mock_service.predict.return_value = MagicMock(
                    churn_probability=prob,
                    risk_level="Medium",
                    model_version="1.0.0"
                )

                response = client.post("/predict", json=valid_payload)
                data = response.json()

                assert 0 <= data["churn_probability"] <= 1