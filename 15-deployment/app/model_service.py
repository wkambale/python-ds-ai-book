# app/model_service.py
import pickle
import logging
from pathlib import Path
from typing import Optional, Dict, Any
import pandas as pd
import numpy as np

from app.schemas import ChurnPredictionInput, ChurnPredictionOutput
from app.config import get_settings

logger = logging.getLogger(__name__)

class ModelService:
    """
    Service for loading the model and making predictions.
    """
    def __init__(self, model_path: str):
        import joblib
        self.model = joblib.load(model_path)
        
        # Risk thresholds (mock settings for example)
        class Settings:
            high_risk_threshold = 0.8
            medium_risk_threshold = 0.5
        self.settings = Settings()

    def determine_risk_level(self, probability: float) -> str:
        """
        Maps probability to business risk categories.
        """
        if probability >= self.settings.high_risk_threshold:
            return "High"
        elif probability >= self.settings.medium_risk_threshold:
            return "Medium"
        else:
            return "Low"

# Singleton instance
model_service = ModelService()