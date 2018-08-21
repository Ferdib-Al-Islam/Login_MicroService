from botocore.exceptions import ClientError

from project.models import ddb
import boto3

ddb = boto3.resource(
    'dynamodb',
    endpoint_url='http://localhost:8000',
    region_name='ap-southeast-1',
    aws_access_key_id='anything',
    aws_secret_access_key='anything'
)

table = ddb.Table('registered_users')


def get_users():
    try:
        response = table.scan(

        )
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        item = response['Items']
        return item