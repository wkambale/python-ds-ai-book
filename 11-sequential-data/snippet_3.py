import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np
from typing import Tuple, List

def create_tokenizer(texts: List[str],
                     vocab_size: int = 1000,
                     oov_token: str = "<OOV>") -> Tokenizer:
    """
    Create and fit a tokenizer on the provided texts.

    Args:
        texts: List of text strings to build vocabulary from
        vocab_size: Maximum vocabulary size
    """
    tokenizer = Tokenizer(num_words=vocab_size, oov_token="<OOV>")
    tokenizer.fit_on_texts(texts)
    return tokenizer

vocab_size = 1000
max_length = 15

tokenizer = create_tokenizer(posts, vocab_size=vocab_size)
padded_sequences = prepare_sequences(posts, tokenizer, max_length)

print(f"Vocabulary size: {len(tokenizer.word_index)}")
print(f"Sequence shape: {padded_sequences.shape}")
print(f"\nSample mapping:")
print(f"  '{posts[0][:30]}...'")
print(f"  -> {padded_sequences[0]}")