import boto3

#creating s3 client
def get_s3_client(region="us-east-2"):
    return boto3.client("s3", region_name=region)

#uploading files to bucket
def upload_file(filename, bucket, key, region="us-east-2"):
    s3 = get_s3_client(region)
    s3.upload_file(Filename=filename, Bucket=bucket, Key=key)
    print(f"Uploaded {filename} to s3://{bucket}/{key}")

#dowloading files from bucket
def download_file(bucket, key, filename, region="us-east-2"):
    s3 = get_s3_client(region)
    s3.download_file(Bucket=bucket, Key=key, Filename=filename)
    print(f"Downloaded s3://{bucket}/{key} to {filename}")
