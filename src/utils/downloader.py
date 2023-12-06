import boto3
import os
import joblib
from dotenv import load_dotenv

load_dotenv()

def s3_model_download():
    
    aws_access_key_id = os.getenv("AWS_ACCESS_KEY_ID")
    aws_secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY")

    bucket_name = 'hotelmlbucket'
    model_file_name = 'model.joblib'

    s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, region_name="us-east-1")
    
    s3.download_file(Bucket=bucket_name, Key=model_file_name, Filename=model_file_name)

    model = joblib.load(model_file_name)
    
    return model

