"""
This module will run the specified AWS Lambda function and return the results.
Need to create IAM user with programmatic access to Lambda.
Need to store IAM credentials in ~/.aws/credentials
Need to store region in ~/.aws/config

credentials file:
[default]
aws_access_key_id = blahblah
aws_secret_access_key = blahblah

config file:
[default]
region = us-east-1 (or whatever region you created function in)
"""
import json
import boto3
import botocore.response as br

# connect to AWS lambda
lambda_client = boto3.client("lambda")

# dictionary containing function input data
p = {"nums": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]}

# invoke the function with input and fetch result
response = lambda_client.invoke(FunctionName="StandardDev", Payload=json.dumps(p))

# convert result (StreamingBody) into a regular Python dictionary
payload = json.loads(response["Payload"].read())

# print original list of numbers and result, rounded to 3 decimal places
print(f"StdDev of nums {payload['nums']} is: {float(payload['result']):.3f}")
