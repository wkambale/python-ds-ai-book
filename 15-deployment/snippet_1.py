# Bad: Loading model on every request
@app.post("/predict")
async def predict(data: Input):
    model = load_model()  # Slow! Loads on every request
    return model.predict(data)

# Good: Load model once at startup (shown in model_service.py above)