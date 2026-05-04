from mlflow.tracking import MlflowClient
from typing import Optional

def register_model(
    run_id: str,
    model_name: str,
    artifact_path: str = "model"
) -> int:
    """
    Register a model from an experiment run.

    Args:
        run_id: MLflow run ID containing the model
        model_name: Name for the registered model
        artifact_path: Path to model artifact within the run
    """
    model_uri = f"runs:/{run_id}/{artifact_path}"
    model_version = mlflow.register_model(model_uri, model_name)
    version = model_version.version
    
    client = mlflow.tracking.MlflowClient()
    client.transition_model_version_stage(
        name=model_name,
        version=version,
        stage="Staging"
    )

    # After validation, promote to production
    # transition_model_stage(
    #     model_name="MobiCash_Churn_Predictor",
    #     version=version,
    #     stage="Production"
    # )