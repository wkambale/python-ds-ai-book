from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier

def create_classification_pipeline(random_state: int = 42) -> Pipeline:
    """
    Create a pipeline that bundles preprocessing and modeling.
    The pipeline ensures that scaling is applied correctly during
    cross-validation, preventing data leakage.

    Args:
        random_state: Random seed for reproducibility

    Returns:
        Configured sklearn Pipeline
    """
    pipeline = Pipeline([
        ('scaler', StandardScaler()),              # Step 1: Scale
        ('rf', RandomForestClassifier(random_state=random_state))  # Step 2: Model
    ])
    return pipeline

pipeline = create_classification_pipeline()