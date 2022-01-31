#!/usr/bin/env python3
import boto3
import os
import sys
from EnvLoad import load_env

load_env()  # take environment variables from .env.

## setup bucket params
cfg = {
    "aws_access_key_id": os.environ['AWS_ACCESS_KEY_ID'],
    "aws_secret_access_key": os.environ['AWS_SECRET_ACCESS_KEY'],
    "endpoint_url": os.environ['AWS_BUCKET_ENDPOINT'],
}

ENCRYPTION_KEY = os.environ['SSE_ENCRYPTION_KEY']
ALGO = os.environ['SSE_ENCRYPTION_ALGO']
BUCKET = os.environ['AWS_BUCKET_FOLDER']

# check args
n = len(sys.argv)

if n != 3:
    print("Nope, try harder. ${sys.argv[0]} <send|restore> <filename>");
    quit()

# check operation arg
if not sys.argv[1] == "send" and not sys.argv[1] == "restore":
    print("Nope, try harder. ${sys.argv[1]} isn't a supported operation, sad!");
    quit()

# check files exist locally
file = sys.argv[2]
if sys.argv[1] == "send" and not os.path.isfile(file):
    print("Nope, try harder. ${sys.argv[2]} isn't a file, sad!")
    quit()

## setup client
client = boto3.client("s3", **cfg)
transfer = boto3.s3.transfer.S3Transfer(client=client)

## try pushing file over
if (sys.argv[1] == "send"):
    base = os.path.basename(file)
    print("Uploading file to Object Storage and encrypting with SSE-C: ", base)
    transfer.upload_file(file,
                        BUCKET, 
                        base,
                        extra_args={'SSECustomerKey':ENCRYPTION_KEY, 
                                    'SSECustomerAlgorithm':ALGO})

## try restoring file
if (sys.argv[1] == "restore"):
    print("Downloading encrypted Object Storage file.")
    transfer.download_file(BUCKET,
                    file, 
                    file,
                    extra_args={'SSECustomerKey':ENCRYPTION_KEY, 
                                'SSECustomerAlgorithm':ALGO})              
