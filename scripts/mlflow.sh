export AWS_ACCESS_KEY_ID=user
export AWS_SECRET_ACCESS_KEY=password
export MLFLOW_S3_ENDPOINT_URL=http://localhost:8333

mlflow server --serve-artifacts --host 0.0.0.0 --port 5000 \
--default-artifact-root s3://data/  
