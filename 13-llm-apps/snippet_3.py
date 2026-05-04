import json
from typing import Optional, Dict, Any, List

def validate_json_output(
    response: str,
    required_fields: List[str]
) -> Optional[Dict[str, Any]]:
    """
    Validate that LLM output is valid JSON with required fields.

    Args:
        response: Raw LLM response
        required_fields: Fields that must be present in the JSON

    Returns:
        Parsed dict if valid, None otherwise.
    """
    try:
        data = json.loads(response)
        missing = [f for f in required_fields if f not in data]
        if missing:
            return None
        return data
    except json.JSONDecodeError as e:
        return None