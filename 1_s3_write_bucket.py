import boto3
import botocore

def main():
    kwrgs = {
        "endpoint_url": "http://localhost:8333",
        "aws_access_key_id": "user",
        "aws_secret_access_key": "password",
    }
    client = boto3.client("s3", **kwrgs)
    print(client.list_buckets())

    response = client.create_bucket(
        ACL='private',
        Bucket='string',
        CreateBucketConfiguration={
            'Location': {
                'Type': 'AvailabilityZone',
                'Name': 'string'
            },
            'Bucket': {
                'DataRedundancy': 'SingleAvailabilityZone',
                'Type': 'Directory'
            }
        },
        GrantFullControl='string',
        GrantRead='string',
        GrantReadACP='string',
        GrantWrite='string',
        GrantWriteACP='string',
        ObjectLockEnabledForBucket=True,
        ObjectOwnership='BucketOwnerPreferred' 
    )

    print(response)
    
    print(client.list_buckets())

if __name__ == "__main__":
    main()