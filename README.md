This pipeline runs via an API trigger
Currentlu uploading files inside data directory and running the api which parses csv converts into polar data frame ansd stores it in aws s3 bucket
aws credentials are encoded in secret.yaml file which is pushed by kuberentes into the os environment variables
