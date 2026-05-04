# app/schemas.py
from pydantic import BaseModel, Field, field_validator
from typing import Literal, Optional
from datetime import datetime

class ChurnPredictionInput(BaseModel):
    """
    Input schema for churn prediction requests.

    This defines exactly what the client must send.
    All fields are validated before reaching the model.
    """
    customer_id: Optional[str] = Field(
        default=None,
        description="Unique customer identifier for tracking"
    )
    age: int = Field(ge=18, le=100, description="Customer age")
    tenure_months: int = Field(ge=0, description="Months as customer")
    account_balance: float = Field(ge=0, description="Balance in UGX")
    avg_monthly_deposits: float = Field(ge=0)
    avg_monthly_withdrawals: float = Field(ge=0)
    days_since_last_transaction: int = Field(ge=0)
    customer_support_tickets: int = Field(ge=0)
    location: str = Field(description="Customer location")

class ChurnPredictionOutput(BaseModel):
    """Output schema for churn predictions."""
    customer_id: Optional[str]
    churn_probability: float
    churn_prediction: bool
    risk_category: Literal["Low", "Medium", "High"]
    timestamp: datetime = Field(default_factory=datetime.utcnow)

class HealthResponse(BaseModel):
    """API health check response."""
    status: Literal['healthy', 'unhealthy']
    model_loaded: bool
    model_version: Optional[str]
    timestamp: datetime = Field(default_factory=datetime.utcnow)

class ErrorResponse(BaseModel):
    """Standard error response format."""
    error: str
    detail: str
    timestamp: datetime = Field(default_factory=datetime.utcnow)