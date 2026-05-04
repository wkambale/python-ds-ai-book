from transformers import AutoTokenizer

def compare_tokenization(texts: List[str],
                         model_name: str = "bert-base-uncased") -> None:
    """
    Display tokenization details for analysis.

    Args:
        texts: List of texts to tokenize
        model_name: Hugging Face model identifier
    """
    tokenizer = AutoTokenizer.from_pretrained(model_name)

    for text in texts:
        tokens = tokenizer.tokenize(text)
        token_ids = tokenizer.encode(text)

        print(f"Text: '{text}'")
        print(f"  Tokens ({len(tokens)}): {tokens}")
        print(f"  Token IDs: {token_ids}\n")

# Compare English vs Swahili tokenization
compare_tokenization([
    "I love you very much",           # English
    "Ninakupenda sana",               # Swahili (same meaning)
    "The bank is by the river",       # English
    "Benki iko kando ya mto"          # Swahili (same meaning)
])