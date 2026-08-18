# monitoring/drift_detection.py
"""
Drift detection pipeline for MobiCash churn model.

This script compares production data against training data
to detect data drift and model degradation.
"""
import pandas as pd
import numpy as np
from datetime import datetime
from pathlib import Path
from typing import Dict, Any, Optional
import json
import logging

logger = logging.getLogger(__name__)

def calculate_feature_drift(reference_col: pd.Series, production_col: pd.Series, threshold: float = 0.1) -> Dict[str, Any]:
    """
    Calculate summary statistics and drift magnitude for a numeric feature.
    """
    ref_mean = float(reference_col.mean())
    prod_mean = float(production_col.mean())
    mean_diff = abs(prod_mean - ref_mean) / (ref_mean + 1e-6)

    return {
        "reference_mean": round(ref_mean, 4),
        "production_mean": round(prod_mean, 4),
        "relative_mean_shift": round(mean_diff, 4),
        "drift_detected": bool(mean_diff > threshold)
    }

def run_weekly_drift_check(
    reference_path: Path,
    production_logs_path: Path,
    output_dir: Path
) -> Dict[str, Any]:
    """
    Runs drift detection across common numeric features between reference and production datasets.
    """
    results: Dict[str, Any] = {
        "timestamp": datetime.utcnow().isoformat(),
        "features": {},
        "summary": {"total_features": 0, "drifted_features": 0}
    }

    if not reference_path.exists() or not production_logs_path.exists():
        logger.warning("Reference or production file not found for drift check.")
        return results

    ref_df = pd.read_csv(reference_path)
    prod_df = pd.read_csv(production_logs_path)

    numeric_cols = [c for c in ref_df.select_dtypes(include=[np.number]).columns if c in prod_df.columns]
    drifted_count = 0

    for col in numeric_cols:
        col_res = calculate_feature_drift(ref_df[col].dropna(), prod_df[col].dropna())
        results["features"][col] = col_res
        if col_res["drift_detected"]:
            drifted_count += 1

    results["summary"]["total_features"] = len(numeric_cols)
    results["summary"]["drifted_features"] = drifted_count

    output_dir.mkdir(parents=True, exist_ok=True)
    report_path = output_dir / "drift_report.json"
    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)

    return results

if __name__ == "__main__":
    results = run_weekly_drift_check(
        reference_path=Path("../datasets/mobicash_training_data.csv"),
        production_logs_path=Path("../datasets/mobicash_production_logs_jan2025.csv"),
        output_dir=Path("reports/")
    )
    print(f"Drift check completed: {results['summary']}")