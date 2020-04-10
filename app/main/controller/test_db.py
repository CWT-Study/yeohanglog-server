#
#  Copyright 2010-2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
#  This file is licensed under the Apache License, Version 2.0 (the "License").
#  You may not use this file except in compliance with the License. A copy of
#  the License is located at
#
#  http://aws.amazon.com/apache2.0/
#
#  This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
#  CONDITIONS OF ANY KIND, either express or implied. See the License for the
#  specific language governing permissions and limitations under the License.
#
from __future__ import print_function # Python 2/3 compatibility
import boto3

dynamodb_resource = boto3.resource('dynamodb',
    region_name='ap-northest-2',
    endpoint_url="http://localhost:8000"
)
dynamodb_clinet = boto3.client('dynamodb',
    region_name='ap-northest-2',
    endpoint_url="http://localhost:8000"
)

def create_table():
    table = dynamodb_resource.create_table(
        TableName='Test',
        KeySchema=[
            {
                'AttributeName': 'test_id',
                'KeyType': 'HASH'  # Partition key
            },
            {
                'AttributeName': 'test_pw',
                'KeyType': 'RANGE'  # Partition key
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'test_id',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'test_pw',
                'AttributeType': 'S'
            },

        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 10,
            'WriteCapacityUnits': 10
        }
    )

    print("Table status:", table.table_status)
    return table.table_status

def show_table():
    table_list = dynamodb_clinet.list_tables()
    print(table_list)

def delete_table():
    table = dynamodb_resource.Table('Test')
    table.delete()
    print("Table status:", table.table_status)
    return table.table_status

# create_table()
delete_table()
# show_table()