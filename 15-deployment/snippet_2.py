# Add timing to identify bottlenecks
import time

@app.post("/predict")
async def predict(data: ChurnPredictionInput):
    start = time.time()
    # ... prediction logic ...
    total_time = time.time() - start
    if total_time > 0.1:  # 100ms threshold
        logger.warning(
            f"Slow prediction: total={total_time:.3f}s"
        )