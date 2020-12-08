from flask import make_response
from functools import wraps
from bson import ObjectId
import json
import logging


class Response():
    code = 0
    body = ""

    CODE_SUCCESS = 200
    CODE_ERROR_UNKOWN = 401
    CODE_ERROR_DB = 402
    CODE_ERROR_MISSING_PARAMETER = 403
    CODE_ERROR_NOT_FIND_USER = 403
    CODE_ERROR_NOT_FIND_TRIP = 410

    MESSAGE_SUCCESS = "SUCCESS"
    MESSAGE_UNKOWN = "UNOWN ERROR"
    MESSAGE_ERROR_DB = "DBERROR"
    MESSAGE_ERROR_PARAMETER = "MISSING PARAMETER"
    MESSAGE_NOT_FIND_USER = "NOT FIND USER FROM DB"
    MESSAGE_NOT_FIND_TRIP = "NOT FIND TRIP FROM DB"

    def __init__(self, body, code):
        self.code = code
        self.body = body

    def get_error_message(self, error_message):
        return {"error_message"}

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, indent=4)

    def to_dict(self):
        # self.__dict__
        return json.loads(self.to_json())


# def get_response_model(fun):
#     @wraps(fun)
#     def decorate(*args, **kwargs):
#         return make_response(fun(*args, **kwargs))
#     return decorate
#

def get_response(fun):
    @wraps(fun)
    def decorate(*args, **kwargs):
        response_body : dict = {}
        response_code : int = 0
        try:
            response_body= fun(*args, **kwargs)
            response_code= Response.CODE_SUCCESS
            if isinstance(response_body["_id"], ObjectId):
                response_body["_id"] = response_body["_id"]["ObjectId"]
        except KeyError as e:
            logging.error(e)
            response_body = Response.MESSAGE_ERROR_PARAMETER
            response_code = Response.CODE_ERROR_MISSING_PARAMETER
        except NotFindUserException as e:
            logging.error(e)
            response_body = Response.MESSAGE_NOT_FIND_USER
            response_code = Response.CODE_ERROR_NOT_FIND_USER
        except Exception as e:
            logging.error(e)
            response_body = Response.MESSAGE_UNKOWN
            response_code = Response.CODE_ERROR_UNKOWN
        finally:
            return make_response(response_body, response_code)
    return decorate


class NotFindUserException(Exception):
    def __init__(self):
        super().__init__("Not Find User From Mongo DB")


class NotFindTripException(Exception):
    def __init__(self):
        super().__init__("Not Find User From Mongo DB")