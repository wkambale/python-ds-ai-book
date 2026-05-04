# GOOD: Production-ready code
from pathlib import Path
from typing import Tuple
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

def load_and_clean_data(filepath: Path) -> pd.DataFrame:
    """
    Load data from CSV and perform basic cleaning.

    Args:
        filepath: Path to the CSV file

    Returns:
        Tuple of X_train, X_test, y_train, y_test
    """
    df = pd.read_csv(filepath)
    X = df.drop('churned', axis=1)
    y = df['churned']
    return train_test_split(X, y, test_size=0.2, random_state=42)

def train_model(X_train: pd.DataFrame, y_train: pd.Series, n_estimators: int = 100) -> RandomForestClassifier:
    """
    Trains a model on the provided data.

    Returns:
        Trained classifier
    """
    model = RandomForestClassifier(
        n_estimators=n_estimators,
        max_depth=max_depth,
        random_state=random_state,
        n_jobs=-1  # Use all CPU cores
    )
    model.fit(X_train, y_train)
    return model