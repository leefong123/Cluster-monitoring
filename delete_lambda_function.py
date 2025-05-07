import boto3
import sys


if len(sys.argv) < 2:
    print("Usage: python script.py <function name>")
    sys.exit(1)

func_name = sys.argv[1]

lambda_client = boto3.client('lambda', region_name='ap-southeast-1')

response = lambda_client.delete_function(
    FunctionName=func_name
)

print("Lambda function deleted.", response)

