# app/main.py
import logging
from contextlib import asynccontextmanager
from typing import Optional

from fastapi import FastAPI, HTTPException, Depends, Security, status
from fastapi.security import APIKeyHeader
from fastapi.middleware.cors import CORSMiddleware

from app.schemas import (
    ChurnPredictionInput,
    ChurnPredictionOutput,
    HealthResponse,
    ErrorResponse
)
from app.services.model_service import ModelService
from fastapi import FastAPI, HTTPException

app = FastAPI(title="MobiCash ML API")
model_service = ModelService("models/model.pkl")

@app.post("/predict/batch", response_model=list[ChurnPredictionOutput])
def predict_batch(requests: list[dict]):
    results = []
    errors = []
    for i, req in enumerate(requests):
        try:
            prediction = model_service.predict(req)
            results.append(prediction.model_dump())
        except Exception as e:
            errors.append({"index": i, "error": str(e)})

    return {
        "predictions": results,
        "errors": errors,
        "total": len(data),
        "successful": len(results)
    }