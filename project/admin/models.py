from botocore.exceptions import ClientError

from project.api.models import get_users
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


def check_user(user_name,password):
    try:
        response = table.get_item(
            Key={
                'user_name': user_name,
            }
        )

    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        if 'Item' in response:
            item = response['Item']
            if(item['password']==password):
                return 1
        else:
            return 0
