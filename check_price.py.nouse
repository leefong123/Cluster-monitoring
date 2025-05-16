import json
import boto3
import yfinance as yf

def get_stock():    ## to retrieve price, copy content of  this function into get_price() function in lambda_funciton.py
    print("Retrieving data...")
    threshold = 48
    ticker = yf.Ticker("D05.SI")
    price = ticker.info.get('regularMarketPrice')
    currency = ticker.info.get('currency')
    name = ticker.info.get('longName')
    report = ""

    if price < threshold:
        report = f"{name} is below target ${threshold}, Price is ${price}\n"
    else:
        report = "--"
    return report




report = get_stock()  
print(report)


'''
if report != "--":
    topic_arn = os.getenv("SNS_TOPIC_ARN")
    event = { "message" : report, 
             "topic_arn" : topic_arn }
    lambda_client = boto3.client('lambda', region_name='ap-southeast-1')

    response = lambda_client.invoke(FunctionName='SendSNSEmail', InvocationType='Event', Payload=json.dumps(event))
    print("lambda client invocation response", response)
else:
    print("Not Match")

'''
'''
topic_arn = os.getenv("SNS_TOPIC_ARN")
sns = boto3.client('sns')

response  = sns.publish(
    TopicArn=topic_arn,
    Message=report,
    Subject="Share Price Application Email Notification"
) 

print(f"Message sent with ID (SNS): {response['MessageId']}")
'''







