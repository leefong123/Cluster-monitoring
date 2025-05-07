import boto3
import sys
import json

if len(sys.argv) < 2:
    print("Usage: python script.py <function name>")
    sys.exit(1)

lambda_func_name = sys.argv[1]  

event = { "stock_code": "D05.SI", "threshold" : 50}
lambda_client = boto3.client('lambda', region_name='ap-southeast-1')
response = lambda_client.invoke(FunctionName=lambda_func_name, InvocationType='Event', Payload=json.dumps(event))
print("lambda client invocation response", response)

