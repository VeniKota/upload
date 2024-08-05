import os
from pathlib import Path
import boto3
from google.cloud import storage

class Upload:
    def __init__(self, s3_bucket_name, gcs_bucket_name, aws_access_key, aws_secret_key, gcs_credentials_path):
        self.s3_bucket_name = s3_bucket_name
        self.gcs_bucket_name = gcs_bucket_name

        self.s3_client = boto3.client(
            's3',
            aws_access_key_id=aws_access_key,
            aws_secret_access_key=aws_secret_key
        )

        self.gcs_client = storage.Client.from_service_account_json(gcs_credentials_path)
        self.gcs_bucket = self.gcs_client.get_bucket(gcs_bucket_name)

    def upload_images_s3(self, file_path):
        
        try:
            self.s3_client.upload_file(file_path, self.s3_bucket_name, Path(file_path).name)
            print(f"Uploaded {file_path} to S3 bucket {self.s3_bucket_name}.")
        except Exception as e:
            print(f"Failed to upload {file_path} to S3: {e}")

    def upload_files_gcs(self, file_path):
        
        try:
            blob = self.gcs_bucket.blob(Path(file_path).name)
            blob.upload_from_filename(file_path)
            print(f"Uploaded {file_path} to GCS bucket {self.gcs_bucket_name}.")
        except Exception as e:
            print(f"Failed to upload {file_path} to GCS: {e}")

    def dir_walk(self, directory, s3_file_types, gcs_file_types):
        
        for root, _, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                file_extension = Path(file_path).suffix.lower()

                if file_extension in s3_file_types:
                    self.upload_images_s3(file_path)
                elif file_extension in gcs_file_types:
                    self.upload_files_gcs(file_path)
                    
                else:
                    print(f"Skipping {file_path} (unsupported file type).")
