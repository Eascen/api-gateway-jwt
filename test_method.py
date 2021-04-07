import boto3
import json

print('Loading function')

def lambda_handler(event, context):
    return {
        'statusCode': '200',
        'body': 'AccessGranted!'
    }