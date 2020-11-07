import logging
import boto3
from botocore.exceptions import ClientError
import os

def bucketconn():
    try:
        aws_access_key_id="YOUR_KEY_ID"
        aws_secret_access_key="YOUR_ACCESS_KEY"
        client = boto3.client('s3',
                                 aws_access_key_id=aws_access_key_id,
                                 aws_secret_access_key=aws_secret_access_key)
        return client
    except
        print("'We cannot connect with the database'")
        return False


def read_data_s3(name):
    try:
        bucket="name"
        link="https://"+bucket+".s3.us-east-2.amazonaws.com/"+name
        data_aws = pd.read_csv(link)
        return data_aws
    except:
        print("Error loading data")
        return False

    
def upload_data_s3(data,key):
    try: 
        bucket = "name"
        client=bucketconn()
        csv_buffer = StringIO()
        data.to_csv(csv_buffer, index=False)
        csv_buffer.seek(0)
        obj = client.put_object(Bucket=bucket, 
                                Key=key, 
                                Body=csv_buffer.getvalue(), 
                                ACL='public-read')
        return obj
    except:
        print("Error upload data")
        return False