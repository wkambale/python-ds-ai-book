# experiments/train_churn.py
"""
Training script for MobiCash churn prediction model.

Usage:
    python train_churn.py --n_estimators 100 --max_depth 10
"""
import argparse
from pathlib import Path
from typing import Dict, Any
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score
)
import argparse
import mlflow

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--data_path", type=str, required=True)
    args = parser.parse_args()

    train_and_log(
        data_path=args.data_path,
        n_estimators=args.n_estimators,
        max_depth=args.max_depth if args.max_depth else None
    )

if __name__ == "__main__":
    main()