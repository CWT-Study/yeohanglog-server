from pymongo import MongoClient
from functools import wraps

region = "ap-northest-2"
ip = "127.0.0.1"
port = 27017

DATABASE_NAME = "triplog"

USER_TABLE = "user"
TRIP_TABLE = "trip"
TRIP_INFO = 'tripinfo'
TRIP_COST = "tripcost"
TRIP_LOG_TABLE = "triplog"


conn = None


def create_mongo_client():
    global conn
    conn = MongoClient(ip, port)[DATABASE_NAME]


def db_session(fun):
    @wraps(fun)
    def decorate(*args, **kwargs):
        return fun(*args, conn=conn, **kwargs)

    return decorate
