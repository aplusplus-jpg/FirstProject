
import boto3
import json


def lambda_handler(event, context):
    print(event)
    texto = event["queryStringParameters"]["texto"]
    idioma = event["queryStringParameters"]["idioma"]

    comprehed = boto3.client('comprehend')

    sentimient = json.dumps(comprehed.detect_sentiment(Text = texto,LanguageCode = idioma),sort_keys = True,indent=4)
    print(sentimient)
    return {
    
        'statusCode': 200,
        'body': sentimient
    }
    