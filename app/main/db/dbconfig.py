import boto3
from pymongo import MongoClient

region = "ap-northest-2"
ip = "127.0.0.1"
port = 27017

conn = None


def create_mongoClient():
    global conn
    conn = MongoClient(ip, port)["triplog"]


def get_connection():
    return conn


def get_user_collection():
    return get_connection()["user"]


def get_trip_collection():
    return get_connection()["trip"]


def get_trip_collection():
    return get_connection()["triplog"]

