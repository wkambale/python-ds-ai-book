import pandas as pd
from typing import List
from tensorflow import keras
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

def predict_sentiment(model: keras.Model,
                      tokenizer: Tokenizer,
                      texts: List[str],
                      max_length: int,
                      threshold: float = 0.5) -> pd.DataFrame:
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
        score = float(pred[0])
        sentiment = "Positive" if score > threshold else "Negative"
        confidence = score if score > threshold else 1.0 - score
        results.append({"text": text, "sentiment": sentiment, "score": score, "confidence": confidence})
        
    return pd.DataFrame(results)

new_posts = [
    "Still waiting for the permit after six months",
    "Finally reliable electricity in our village!"
]