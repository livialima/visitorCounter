import boto3

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("VisitCount")

table.put_item(
    Item={
        "id": "number_of_visits",
        "visitors": "0"
    }
)
