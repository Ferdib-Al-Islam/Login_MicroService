import boto3

# For a Boto3 client.
ddb = boto3.client(
    'dynamodb',
    endpoint_url='http://localhost:8000',
    region_name='ap-southeast-1',
    aws_access_key_id='anything',
    aws_secret_access_key='anything'
)


def list_tables():
    response = ddb.list_tables()
    print(response)


def create_table():
    table = ddb.create_table(
        TableName='registered_users',
        KeySchema=[
            {
                'AttributeName': 'user_name',
                'KeyType': 'HASH'  # Partition key
            },
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'user_name',
                'AttributeType': 'S'
            },
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 10,
            'WriteCapacityUnits': 10
        }
    )

#create_table()
list_tables()
