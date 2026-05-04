from transformers import AutoModel
import numpy as np

def extract_attention(text: str,
                      tokenizer: AutoTokenizer,
                      model: AutoModel) -> Tuple[List[str], np.ndarray]:
    """
    Extract attention weights from a transformer model.

    Args:
        text: Input text
        tokenizer: Model tokenizer
        model: Transformer model with attention output

    Returns:
        Attention weights
    """
    inputs = tokenizer(text, return_tensors='pt')
    outputs = model(**inputs, output_attentions=True)
    return outputs.attentions

base_model_name = "bert-base-uncased"
base_tokenizer = AutoTokenizer.from_pretrained(base_model_name)
base_model = AutoModel.from_pretrained(base_model_name)

text = "The animal didn't cross the street because it was too tired"
tokens, attention = extract_attention(text, base_tokenizer, base_model)

print(f"Tokens: {tokens}")

# Find attention pattern for "it"
it_index = tokens.index("it")
display_attention_for_token(tokens, attention, it_index)