from transformers import pipeline
from typing import List, Dict, Any

def analyze_sentiment(texts: List[str]) -> List[Dict[str, Any]]:
    """
    Analyze sentiment of texts using a pre-trained model.

    Args:
        texts: List of text strings to analyze

    Returns:
        List of dictionaries with label and score
    """
    classifier = pipeline("sentiment-analysis")
    return classifier(texts)

# Example usage
sample_texts = [
    "This mobile money app is incredibly fast and reliable.",
    "The network is down again, this is so frustrating!",
    "The new farming techniques have doubled our yield."
]

results = analyze_sentiment(sample_texts)
for text, result in zip(sample_texts, results):
    print(f"Text: '{text[:50]}...'")
    print(f"  Sentiment: {result['label']} ({result['score']:.4f})\n")