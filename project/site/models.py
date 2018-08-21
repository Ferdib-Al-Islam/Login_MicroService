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


def create_user(user_name,email,password):
    table.put_item(
        Item={
            'user_name': user_name,
            'email': email,
            'password': password
        }
    )
