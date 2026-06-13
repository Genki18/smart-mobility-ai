import boto3
import json
import os
from datetime import datetime

R2_ENDPOINT = os.getenv("R2_ENDPOINT_URL")
R2_ACCESS_KEY = os.getenv("R2_ACCESS_KEY_ID")
R2_SECRET_KEY = os.getenv("R2_SECRET_ACCESS_KEY")
R2_BUCKET = os.getenv("R2_BUCKET_NAME", "smart-mobility-logs")

def get_r2_client():
    return boto3.client(
        "s3",
        endpoint_url=R2_ENDPOINT,
        aws_access_key_id=R2_ACCESS_KEY,
        aws_secret_access_key=R2_SECRET_KEY,
        region_name="auto",
    )

def upload_prediction_log(data: dict) -> bool:
    try:
        client = get_r2_client()
        timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S_%f")
        filename = f"predictions/{timestamp}.json"
        client.put_object(
            Bucket=R2_BUCKET,
            Key=filename,
            Body=json.dumps(data),
            ContentType="application/json",
        )
        return True
    except Exception as e:
        print(f"R2 upload error: {e}")
        return False
