import boto3
import json

def lambda_handler(event, context):


    ssm_client = boto3.client('ssm')
    response = ssm_client.get_parameter(Name='/app/myflask/topic_arn')

    topic_arn = response['Parameter']['Value']

    sns = boto3.client('sns')

    if 'body' in event:
      alert_data = json.loads(event['body'])  # API Gateway
    else:
      alert_data = event  # Direct test

    for alert in alert_data.get('alerts', []):
        labels = alert.get('labels', {})
        annotations = alert.get('annotations', {})

        alertname = labels.get('alertname')
        severity = labels.get('severity')
        summary = annotations.get('summary')
        description = annotations.get('description')

        print(f"Alert: {alertname} | Severity: {severity}")
        print(f"Summary: {summary}")
        print(f"Description: {description}")

        response  = sns.publish(
            TopicArn=topic_arn,
            Message=description,
            Subject=summary )

    return {
        'statusCode': 200,
        'body': f"Message sent with ID: {response['MessageId']}"
    }


