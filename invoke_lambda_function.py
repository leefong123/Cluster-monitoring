import boto3
import sys
import json

if len(sys.argv) < 3:
    print("Usage: python script.py <function name> <region>")
    sys.exit(1)

lambda_func_name = sys.argv[1]  
region = sys.argv[2]  

event = { "stock_code": "D05.SI", "threshold" : 50}
lambda_client = boto3.client('lambda', region_name=region)
response = lambda_client.invoke(FunctionName=lambda_func_name, InvocationType='Event', Payload=json.dumps(event))
print("lambda client invocation response", response)

