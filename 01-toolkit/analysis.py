# analysis.py
"""A script to perform initial analysis of crop yield data."""

import pandas as pd

def load_data(filepath: str) -> pd.DataFrame:
    """Loads crop data from a CSV file.

    Args:
        filepath: Path to the CSV file containing crop data.

    Returns:
        A DataFrame containing the loaded crop data.
    """
    print(f"Loading data from {filepath}...")
    return pd.read_csv(filepath)

def calculate_average_yield(df: pd.DataFrame, crop_name: str) -> float:
    """Calculates the average yield for a specific crop.

    Args:
        df: DataFrame containing crop data with 'crop' and
            'yield_kg_per_hectare' columns.
        crop_name: The name of the crop to filter by.

    Returns:
        The mean yield in kg per hectare for the specified crop.
    """
    crop_df = df[df['crop'] == crop_name]
    average_yield = crop_df['yield_kg_per_hectare'].mean()
    return average_yield