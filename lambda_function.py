import json
import boto3
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("VisitCount")

def get_counter():
    resp_query = table.query(
        KeyConditionExpression=Key("id").eq("number_of_visits")
    )
    data = int(resp_query["Items"][0]["visitors"])
    return data

def update_counter(new_value):
    resp_update = table.update_item(
        Key={
            "id" : "number_of_visits"
        },
        UpdateExpression="set visitors = :val",
        ExpressionAttributeValues={
            ':val': new_value
        },
        ReturnValues="UPDATED_NEW"
    )
    return "All good"

def lambda_handler(event, context):
    number_visits = get_counter()
    number_visits = number_visits + 1
    update_counter(number_visits)

    return {
        'statusCode': 200,
        'body': get_counter()
    }
