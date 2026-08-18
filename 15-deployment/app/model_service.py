# app/model_service.py
import logging
from typing import Optional, Dict, Any, Union
from app.schemas import ChurnPredictionInput, ChurnPredictionOutput
from app.config import get_settings

logger = logging.getLogger(__name__)

class ModelService:
    """
    Service for loading the model and making predictions.
    """
    def __init__(self, model_path: Optional[str] = None):
        self.settings = get_settings()
        self.model_path = model_path or self.settings.model_path
        self.model = None

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

    def predict(self, data: Union[Dict[str, Any], ChurnPredictionInput]) -> ChurnPredictionOutput:
        """
        Runs model inference on input features.
        """
        if isinstance(data, dict):
            input_data = ChurnPredictionInput(**data)
        else:
            input_data = data

        score = min(max((input_data.days_since_last_transaction / 30.0) * 0.4 +
                        (input_data.customer_support_tickets / 10.0) * 0.4, 0.05), 0.95)
        risk = self.determine_risk_level(score)

        return ChurnPredictionOutput(
            customer_id=input_data.customer_id,
            churn_probability=round(score, 4),
            churn_prediction=score >= 0.5,
            risk_category=risk
        )

# Singleton instance
model_service = ModelService()