# src/config.py
from dataclasses import dataclass
from typing import Optional
import json
from pathlib import Path

@dataclass
class ModelConfig:
    """Configuration for model training."""
    n_estimators: int = 100
    max_depth: Optional[int] = None
    min_samples_split: int = 2

@dataclass
class DataConfig:
    """Configuration for data processing."""
    data_path: Path
    target_column: str = "churned"
    test_size: float = 0.2
    validation_size: float = 0.1
    random_state: int = 42