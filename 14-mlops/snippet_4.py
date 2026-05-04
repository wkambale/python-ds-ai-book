import hashlib
import pandas as pd
from pathlib import Path

def compute_data_hash(df: pd.DataFrame) -> str:
    """Compute a hash of DataFrame contents for versioning."""
    # Convert to bytes and hash
    content = pd.util.hash_pandas_object(df).values.tobytes()
    return hashlib.sha256(content).hexdigest()[:12]

def log_data_version(df: pd.DataFrame, filepath: Path) -> dict:
    """
    Create a data version record for MLflow logging.

    Args:
        df: Training DataFrame
        filepath: Path to data file

    Returns:
        Dictionary of data version info
    """
    return {
        "data_path": str(filepath),
        "data_hash": compute_data_hash(df),
        "num_rows": len(df),
        "num_columns": len(df.columns),
        "columns": ",".join(df.columns.tolist()),
        "file_modified": filepath.stat().st_mtime if filepath.exists() else None
    }