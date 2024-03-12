import boto3
import os.path as osp
import mlflow
import numpy as np
from sklearn.linear_model import LinearRegression
from mlflow.models import infer_signature
import os

def main():
    os.environ["AWS_ACCESS_KEY_ID"] = "user"
    os.environ["AWS_SECRET_ACCESS_KEY"] = "password"
    os.environ["MLFLOW_S3_ENDPOINT_URL"] = "http://localhost:8333"

    mlflow.set_tracking_uri("http://localhost:5000")
    experiment_name = "seaweed"

    existing_exp = mlflow.get_experiment_by_name(experiment_name)
    if not existing_exp:
        mlflow.create_experiment(experiment_name)
    mlflow.set_experiment(experiment_name)
    mlflow.set_tag("task", "seaweed_test")

    RANDOM_SEED = 8927
    rng = np.random.default_rng(RANDOM_SEED)
    x = np.linspace(start=0, stop=1, num=100).reshape(-1, 1) 
    y = 0.3 * x + 0.5 + rng.normal(0, 1, len(x))

    model = LinearRegression()
    model.fit(x, y)

    signature = infer_signature(
        x, 
        y,
    )
    
    model_name = "linear_reg"
    run_id = mlflow.active_run().info.run_id

    logged_model = mlflow.sklearn.log_model(
        model, model_name,
        signature = signature
    )

    model_uri = logged_model.model_uri
    mlflow.register_model(model_uri, model_name)

    loaded_model = mlflow.sklearn.load_model(model_uri)
    preds = loaded_model.predict(x)

    print(preds)
    mlflow.end_run()


if __name__ == "__main__":
    main()