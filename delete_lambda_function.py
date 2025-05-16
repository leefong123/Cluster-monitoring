import boto3
import sys


if len(sys.argv) < 3:
    print("Usage: python script.py <function name> <region>")
    sys.exit(1)

func_name = sys.argv[1]
region = sys.argv[2]

lambda_client = boto3.client('lambda', region_name=region)

response = lambda_client.delete_function(
    FunctionName=func_name
)

print("Lambda function deleted.", response)

