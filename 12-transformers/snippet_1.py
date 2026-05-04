# Example: Padding mask for a batch with sequences of length 5 and 3
# Sequence 1: [word, word, word, word, word] -> mask: [1, 1, 1, 1, 1]
# Sequence 2: [word, word, word, PAD, PAD]   -> mask: [1, 1, 1, 0, 0]