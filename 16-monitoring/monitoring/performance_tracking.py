# monitoring/performance_tracking.py
"""
Track model performance over time when labels become available.
"""
import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score, f1_score, roc_auc_score
from datetime import datetime
from typing import Dict, List
import logging

logger = logging.getLogger(__name__)

class PerformanceTracker:
    """
    Tracks model performance metrics over time.
    """
    def __init__(self):
        self.history = []
        
    def add_metrics(self, accuracy: float, timestamp: str):
        self.history.append({'accuracy': accuracy, 'time': timestamp})
        
    def detect_degradation(self) -> bool:
        """Check if recent accuracy is dropping."""
        if len(self.history) < 3:
            return False

        recent = self.history[-3:]
        critical_count = sum(
            1 for h in recent
            if any(a['severity'] == 'CRITICAL' for a in h.get('alerts', []))
        )

        return critical_count >= 2