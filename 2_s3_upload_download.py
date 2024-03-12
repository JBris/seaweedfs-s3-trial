import boto3
import os.path as osp

def main():
    kwrgs = {
        "endpoint_url": "http://localhost:8333",
        "aws_access_key_id": "user",
        "aws_secret_access_key": "password",
    }
    client = boto3.client("s3", **kwrgs)

    BUCKET="string"
    client.upload_file(
        osp.join("data", "test.txt"), BUCKET, osp.join("data", "test.txt")
    )

    bucket = client.list_objects_v2(
        Bucket=BUCKET,
        Prefix='data/'
    )

    for content in bucket.get('Contents', []):
        print(content['Key'])

    client.download_file(
        BUCKET, osp.join("data", "test.txt"), "test.txt"
    )

if __name__ == "__main__":
    main()