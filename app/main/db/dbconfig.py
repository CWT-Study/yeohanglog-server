import boto3

region = "ap-northest-2"
ip = "localhost"
port = 8000


def getDBResourceInstance():
    dynamodb_resource = boto3.resource(
        'dynamodb',
        region_name=region,
        endpoint_url=f"http://{ip}:{port}"
    )
    return dynamodb_resource

def getDBClientInstance():
    dynamodb_clinet = boto3.client(
        'dynamodb',
        region_name=region,
        endpoint_url=f"http://{ip}:{port}"
    )
    return dynamodb_clinet
