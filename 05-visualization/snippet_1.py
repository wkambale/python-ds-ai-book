import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Load Anscombe's Quartet dataset, which is included with Seaborn
anscombe = sns.load_dataset("anscombe")

# Group by the 'dataset' column and calculate summary statistics
summary_stats = anscombe.groupby('dataset').agg(
    x_mean=('x', 'mean'),
    y_mean=('y', 'mean'),
    x_std=('x', 'std'),
    y_std=('y', 'std'),
    count=('x', 'count')
).round(2)
print("Summary Statistics:")
print(summary_stats)

# Calculate the correlation between x and y for each dataset
correlations = anscombe.groupby('dataset').apply(
    lambda g: g['x'].corr(g['y'])
).round(3)
print("\nCorrelation (x, y) by dataset:")
print(correlations)