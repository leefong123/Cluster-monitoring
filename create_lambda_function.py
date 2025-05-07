# Work in progress...
# automate creation and deletion of lambda  function and sns topic in separate program
# fire api call tfire api o perform real-time purchasing

import boto3
import sys

if len(sys.argv) < 2:
    print("Usage: python script.py <function name> <role name>")
    sys.exit(1)

func_name = sys.argv[1]  
role_name = sys.argv[2]

lambda_client = boto3.client('lambda', region_name='ap-southeast-1')
#execute_role = os.getenv("LAMBDA_ROLE")

iam = boto3.client('iam')
response = iam.get_role(RoleName=role_name)
role_arn = response['Role']['Arn']

with open('function.zip', 'rb') as f:
    zipped_code = f.read()

response = lambda_client.create_function(
        FunctionName=func_name,
        Runtime='python3.12',
        Role=role_arn,
        Handler='lambda_function.lambda_handler',
        Code=dict(ZipFile=zipped_code),
        Timeout=15
)

print("lambda client create function response", response)


