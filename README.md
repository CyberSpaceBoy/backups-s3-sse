# Backup. All. the. Things.

> A simple backup and restore process which supports SSE encryption for S3 object storage :)

## Dependencies

### Install necessary dependencies

* python3
* pip
* boto3
* dotenv

``` bash
# install python and pip (debian/ubuntu)
sudo apt install python3 python-pip -y

# install pip modules
pip install boto3 python-dotenv 
```

## Configure

### Generate a random 32 hexadecimal password

```bash
# Note: Your encryption key must be 32 characters
openssl rand -hex 16
```

### Provide access key, secret, and bucket endpoint settings.

```text
# AWS settings
AWS_ACCESS_KEY_ID="example-access-key"
AWS_SECRET_ACCESS_KEY="example-secret-access-key"
AWS_BUCKET_ENDPOINT="https://example-cluster-url"
AWS_BUCKET_FOLDER="Backups"

# SSE settings
SSE_ENCRYPTION_KEY="example-encryption-key-987654321"
SSE_ENCRYPTION_ALGO="AES256"
```

### Then save it.

## Use

### The process to send and restore a file

``` bash
# send a file backup to remote S3 bucket
python3 s3-sse-backup.py send ~/Pictures/gravatar.jpg

# restore the sent file backup to local
python3 s3-sse-backup.py restore gravatar.jpg
```

## Known Issues

* The process only allows sending or restoring one file at a time.
* The process doesn't support sending files while retaining nested folder structure. (Files are stored in a single folder as specified in `.env` file)
* The process to restore file cannot start with a path name.

## Other Resources

* [How to Use Server-Side Encryption with Linode Object Storage](https://www.linode.com/docs/guides/server-side-encryption/)
* [Guides - Using s3cmd with Object Storage](https://www.linode.com/docs/products/storage/object-storage/guides/s3cmd/)
* [python-dotenv 0.19.2](https://pypi.org/project/python-dotenv/)


