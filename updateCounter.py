import boto3
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("VisitCount")

response = table.update_item(
    Key={
        "id" : "number_of_visits"
    },
    UpdateExpression="set visitors = :val",
    ExpressionAttributeValues={
        ':val': 1
    },
    ReturnValues="UPDATED_NEW"
)
