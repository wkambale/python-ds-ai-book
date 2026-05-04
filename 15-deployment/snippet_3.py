from functools import lru_cache
from hashlib import md5
import json
# Simple in-memory cache
prediction_cache = {}
def get_cache_key(data: ChurnPredictionInput) -> str:

    """Generate a cache key from input data."""

@app.post("/predict")
async def predict(data: ChurnPredictionInput, use_cache: bool = True):
    if use_cache:
        if cache_key in prediction_cache:
            return prediction_cache[cache_key]

    # ... prediction logic ...

    if use_cache:
        prediction_cache[cache_key] = result