# app/main.py
import logging
from typing import List
from fastapi import FastAPI, HTTPException, status

from app.schemas import (
    ChurnPredictionInput,
    ChurnPredictionOutput,
    HealthResponse,
    ErrorResponse
)
from app.model_service import model_service
from app.config import get_settings

settings = get_settings()
app = FastAPI(title=settings.app_name, version=settings.app_version)

@app.get("/health", response_model=HealthResponse)
def health_check():
    """Health check endpoint."""
    return HealthResponse(
        status="healthy",
        model_loaded=True,
        model_version=settings.app_version
    )

@app.post("/predict", response_model=ChurnPredictionOutput)
def predict(request: ChurnPredictionInput):
    """Predict churn for a single customer."""
    try:
        return model_service.predict(request)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )

@app.post("/predict/batch")
def predict_batch(requests: List[ChurnPredictionInput]):
    """Predict churn for a batch of customers."""
    results = []
    errors = []
    for i, req in enumerate(requests):
        try:
            pred = model_service.predict(req)
            results.append(pred.model_dump())
        except Exception as e:
            errors.append({"index": i, "error": str(e)})

    return {
        "predictions": results,
        "errors": errors,
        "total": len(requests),
        "successful": len(results)
    }