import boto3
import pymongo

region = "ap-northest-2"
ip = "127.0.0.1"
port = 27017

def get_connection():
    return pymongo.MongoClient(ip, port)["triplog"]


def get_user_collection():
    return get_connection()["user"]