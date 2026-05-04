# Causal mask for sequence length 4:
# Position 1 can see: [1, 0, 0, 0]  (only itself)
# Position 2 can see: [1, 1, 0, 0]  (positions 1-2)
# Position 3 can see: [1, 1, 1, 0]  (positions 1-3)
# Position 4 can see: [1, 1, 1, 1]  (all positions)