import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from typing import Dict, List, Tuple, Any
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score,
    f1_score, roc_auc_score, classification_report,
    confusion_matrix, ConfusionMatrixDisplay
)

def load_and_prepare_churn_data(
    filepath: str
) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray, pd.DataFrame, StandardScaler]:
    """
    Loads data, engineers features, encodes, scales, and splits.
    """
    df = pd.read_csv(filepath)
    
    # Feature engineering
    df['total_transaction_value'] = df['transaction_count'] * df['avg_transaction_fee']
    
    # One-hot encoding
    df_encoded = pd.get_dummies(df, columns=['agent_location', 'account_type'], drop_first=True)
    
    # Separate features and target
    X = df_encoded.drop(['customer_id', 'churned'], axis=1)
    y = df_encoded['churned']
    
    # Split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    
    # Scale
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    return X_train_scaled, X_test_scaled, y_train, y_test, X, scaler

X_train_scaled, X_test_scaled, y_train, y_test, X_encoded, scaler = \
    load_and_prepare_churn_data('mobicash_churn_dataset.csv')

# Also keep unscaled versions for tree-based models
X_train_unscaled = X_encoded.iloc[y_train.index]
X_test_unscaled = X_encoded.iloc[y_test.index]

print(f"Training set: {X_train_scaled.shape[0]} samples")
print(f"Test set: {X_test_scaled.shape[0]} samples")
print(f"Features: {X_encoded.columns.tolist()}")