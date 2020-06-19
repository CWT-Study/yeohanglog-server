from flask import make_response
from functools import wraps
import json


class Response():
    code = 0
    body = ""

    CODE_SUCCESS = 200
    CODE_ERROR_UNKOWN = 401
    CODE_ERROR_DB = 402
    CODE_ERROR_MISSING_PARAMETER = 403

    MESSAGE_SUCCESS = "SUCCESS"
    MESSAGE_UNKOWN = "UNOWN ERROR"
    MESSAGE_ERROR_DB = "DBERROR"
    MESSAGE_ERROR_PARAMETER = "MISSING PARAMETER"
    def __init__(self, body, code):
        self.code = code
        self.body = body

    def get_error_message(self, error_message):

        return { "error_message" }

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, indent=4)

    def to_dict(self):
        return json.loads(self.to_json())
def get_api(fun):
    @wraps(fun)
    def decorate(*args, **kwargs):

        return make_response(fun(*args, **kwargs))
    return decorate

