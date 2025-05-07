import boto3
import sys


def create_ssm_para(topic_arn):

    ssm_client = boto3.client('ssm')
    response = ssm_client.put_parameter(Name='/SharePriceChecking/myapp/topic_arn', Description="SNS topic arn to be used by lambda functions", Value=topic_arn, Type='String', Overwrite=True, Tier='Standard')

    print("Parameter store created ==> ", response) 

if len(sys.argv) < 3:
    print("Usage: python script.py <SNS Topic Name> <User Email Address>")
    sys.exit(1)

sns_topic = sys.argv[1]  
user_email = sys.argv[2]

print("Parameters:", sns_topic, user_email)

sns = boto3.client('sns')
response = sns.create_topic(Name=sns_topic)
print(f"Topic ARN: {response['TopicArn']}")

topic_arn =  response['TopicArn']
print ("topic arn:", topic_arn)

response = sns.subscribe(
    TopicArn=topic_arn,
    Protocol='email',
    Endpoint=user_email
)

create_ssm_para(topic_arn)

print(f"Subscription ARN (pending confirmation): {response['SubscriptionArn']}")



