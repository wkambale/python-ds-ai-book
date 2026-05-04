import joblib
from datetime import datetime

def save_tuned_model(search_results,
                     model_name: str,
                     output_dir: str = 'models') -> str:
    """
    Save the best model from hyperparameter search with metadata.

    Args:
        search_results: Fitted GridSearchCV or RandomizedSearchCV object
        model_name: Descriptive name for the model
        output_dir: Directory to save model files

    Returns:
        Path to saved model file
    """
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f"{output_dir}/{model_name}_{timestamp}.joblib"

    model_artifact = {
        'model': search_results.best_estimator_,
        'params': search_results.best_params_,
        'cv_score': search_results.best_score_,
        'timestamp': timestamp
    }

    joblib.dump(model_artifact, filename)
    print(f"Model saved to {filename}")
    print(f"Best CV Score: {search_results.best_score_:.4f}")

    return filename