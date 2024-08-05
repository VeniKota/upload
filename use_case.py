from Upload import Upload

s3_bucket_name = 'gobuck'
gcs_bucket_name = 'gobuck'
aws_access_key = 'access_key'
aws_secret_key = 'secret_key'
gcs_credentials_path = r"json_credentials_file_path"

s3_file_types = {'.jpg',  '.png', '.svg', '.webp', '.mp4', '.mpeg4', '.mp3', '.wmv', '.3gp','.webm'}
gcs_file_types = {'.doc', '.docx', '.csv', '.pdf'}

uploader = Upload(s3_bucket_name, gcs_bucket_name, aws_access_key, aws_secret_key, gcs_credentials_path)

directory_path = r"C:\file_upload\storage"
uploader.dir_walk(directory_path, s3_file_types, gcs_file_types)
