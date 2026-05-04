from typing import Callable, Dict, Any

def calculate_loan_interest(
    principal: float,
    annual_rate: float,
    months: int
) -> Dict[str, float]:
    """Calculate simple interest on a loan."""
    interest = principal * (annual_rate / 100) * (months / 12)
    total = principal + interest
    return {
        "principal": principal,
        "interest": interest,
        "total_repayment": total
    }

AVAILABLE_TOOLS: Dict[str, Callable] = {
    "calculate_loan_interest": calculate_loan_interest,
}