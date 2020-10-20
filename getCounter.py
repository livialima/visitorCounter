import boto3
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("VisitorCounter")

response = table.query(
    KeyConditionExpression=Key("id").eq("number_of_visits")
)
data = int(response["Items"][0]["visitors"])
print(data)
