import os

CSV_FILE_PATH = os.getenv("CSV_FILE_PATH", "netflix_titles.csv")
OUTPUT_FILE_PATH = os.getenv("OUTPUT_FILE_PATH", "output_clean.parquet")
SECRET_TOKEN = os.getenv("SECRET_TOKEN", "mysecrettoken123")
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_BUCKET_NAME = os.getenv("AWS_BUCKET_NAME")
