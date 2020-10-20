import boto3

dynamodb = boto3.resource("dynamodb")
table = dynamodb.create_table(
  TableName="VisitCount",
  KeySchema=[
    {
        "AttributeName": "id",
        "KeyType": "HASH" #partition key
    }
  ],
  AttributeDefinitions=[
    {
        "AttributeName": "id",
        "AttributeType": "S"
    }
  ],
  ProvisionedThroughput={
    "ReadCapacityUnits": 10,
    "WriteCapacityUnits": 10
  }
)
print("Table status:",table.table_status)

print("Wainting for",table.name,"to complete creation...")
table.meta.client.get_waiter('table_exists').wait(TableName='VisitCount')
print("Table status:",dynamodb.Table('VisitCount').table_status)

table.put_item(
    Item={
        "id": "number_of_visits",
        "visitors": "0"
    }
)
