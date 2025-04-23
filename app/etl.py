import polars as pl
import os
import boto3
from config import CSV_FILE_PATH, OUTPUT_FILE_PATH, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_BUCKET_NAME

def extract_data():
    if not os.path.exists(CSV_FILE_PATH):
        raise FileNotFoundError(f"CSV file not found at {CSV_FILE_PATH}")
    df = pl.read_csv(CSV_FILE_PATH)
    return df

def transform_data(df):
    df_clean = df.drop_nulls()
    return df_clean

def save_locally(df):
    df.write_parquet(OUTPUT_FILE_PATH)
    df.write_csv(OUTPUT_FILE_PATH.replace(".parquet", ".csv"))
    print(f"Data saved locally at {OUTPUT_FILE_PATH} and CSV.")

def upload_to_s3():
    s3 = boto3.client(
        "s3",
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    )
    parquet_file = OUTPUT_FILE_PATH
    csv_file = OUTPUT_FILE_PATH.replace(".parquet", ".csv")
    
    s3.upload_file(parquet_file, AWS_BUCKET_NAME, os.path.basename(parquet_file))
    print(f"Uploaded {parquet_file} to S3 bucket {AWS_BUCKET_NAME}")
    
    s3.upload_file(csv_file, AWS_BUCKET_NAME, os.path.basename(csv_file))
    print(f"Uploaded {csv_file} to S3 bucket {AWS_BUCKET_NAME}")

def main():
    print("Starting ETL process...")
    df = extract_data()
    df_clean = transform_data(df)
    save_locally(df_clean)
    upload_to_s3()
    print("ETL completed and files uploaded to S3.")
