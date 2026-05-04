def predict_sentiment(model: keras.Model,
                      tokenizer: Tokenizer,
                      texts: List[str],
                      max_length: int,
                      threshold: float = 0.5) -> List[dict]:
    """
    Predict sentiment for new texts.

    Args:
        model: Trained Keras model
        tokenizer: Fitted tokenizer
        texts: List of texts to classify
        max_length: Maximum sequence length
        threshold: Classification threshold
    """
    sequences = tokenizer.texts_to_sequences(texts)
    padded = pad_sequences(sequences, maxlen=max_length, padding='post', truncating='post')
    predictions = model.predict(padded)
    
    results = []
    for text, pred in zip(texts, predictions):
        sentiment = "Positive" if pred[0] > threshold else "Negative"
        results.append({"text": text, "sentiment": sentiment, "score": pred[0]})
        
    return pd.DataFrame(results)

new_posts = [
    "Still waiting for the permit after six months",
    "Finally reliable electricity in our village!"

results = predict_sentiment(model, tokenizer, test_posts, max_length)

for r in results:
    status = "PASS" if r['confidence'] > 0.7 else "?"
    print(f"{status} '{r['text'][:40]}...'")
    print(f"  Sentiment: {r['sentiment']} (confidence: {r['confidence']:.2%})")