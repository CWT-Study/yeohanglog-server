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
import app.main.db.dbconfig as dbconfig
from app.main.model.user_model import UserModel

def create_table():
    table = dbconfig.getDBResourceInstance().create_table(
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
    table_list = dbconfig.getDBClientInstance().list_tables()
    print(table_list)

def delete_table():
    table = dbconfig.getDBResourceInstance().Table('Test')
    table.delete()
    print("Table status:", table.table_status)
    return table.table_status

def insert_user(uuid, nickname, created_at):
    try:
        coll = dbconfig.get_user_collection()
        user = UserModel(_id=uuid, nickname=nickname, created_at=created_at).to_dict()
        coll.insert(user)
        return user
    except Exception as e:
        print(e)
        return None

def find_user(dict):
    try:
        coll = dbconfig.get_user_collection()
        result = coll.find(dict)
        item_array = []
        for item in result:
            item_array.append(item)
        return { "result" : item_array}
    except Exception as e:
        print(e)
        return None




# create_table()
# delete_table()
# show_table()