from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
from typing import Tuple

def load_model_and_tokenizer(
    model_name: str
) -> Tuple[AutoTokenizer, AutoModelForSequenceClassification]:
    """
    Load a pre-trained model and its tokenizer.

    Args:
        model_name: Hugging Face model identifier

    Returns:
        Tuple of (tokenizer, model)
    """
    from transformers import AutoTokenizer, AutoModelForSequenceClassification
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSequenceClassification.from_pretrained(model_name)
    return tokenizer, model

tokenizer, model = load_swahili_sentiment_model()

# Analyze text
text = "The harvest this year was poor due to the drought."
predictions = predict_with_model(text, tokenizer, model, labels)

print(f"Text: '{text}'")
print("Predictions:")
for label, score in predictions.items():
    bar = "█" * int(score * 20)
    print(f"  {label:10} {bar} {score:.4f}")