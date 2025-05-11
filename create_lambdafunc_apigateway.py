# Work in progress...
# automate creation and deletion of lambda  function and sns topic in separate program
# fire api call tfire api o perform real-time purchasing

import boto3
import sys

if len(sys.argv) < 4:
    print("Usage: python script.py <function name> <role name>")
    sys.exit(1)

func_name = sys.argv[1]  # SendSNSEmail
role_name = sys.argv[2]  # lambda-execute-role
region = sys.argv[3] # ap-southeast-1

lambda_client = boto3.client('lambda', region_name=region)
iam = boto3.client('iam')
apigw = boto3.client('apigatewayv2', region_name=region)

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

print("lambda function created:", response['FunctionArn'])
lambda_arn = response['FunctionArn']

response = apigateway2.create_api(Name=f'{func_name}-http-api',ProtocolType='HTTP', Target=lambda_arn)
api_id = response['ApiId']
print(f'Http api id:, {api_id}')

response = apigatewayv2.create_integration(
        ApiId = api_id,
        RouteKey = 'AWS_PROXY',
        IntegrationUri = lambda_arn,  
        IntegrationMethod='POST',   ## alertmanger use POST
        PayloadFormatVersion='2.0'
        )

integration_id = response['IntegrationId']

route_path = '/invoke'
response = apigatewayv2.create_route(
        ApiId = api_id,
        RouteKey = f'POST {route_path}',
        Target=f'integrations/{integration_id}'   ## must need integrations prefix
        )

lambda_client.add_permission(
    FunctionName=func_name,
    StatementId='AllowExecutionFromHttpApiGateway',
    Action='lambda:InvokeFunction',
    Principal='apigateway.amazonaws.com',
    SourceArn=f'arn:aws:execute-api:{region}:*:{api_id}/*/POST{route_path}'
)

stage_name = 'prod'
apigatewayv2.create_stage(
    ApiId=api_id,
    StageName=stage_name,
    AutoDeploy=True
)

# 9. Final URL
url = f"https://{api_id}.execute-api.{region}.amazonaws.com/{stage_name}{route_path}"  
print("Invoke your Lambda using HTTP POST at:", url)





