from flask import make_response
from functools import wraps
import json


class Response():
    code = 0
    body = ""

    CODE_SUCCESS = 200
    CODE_ERROR_UNKOWN = 401
    CODE_ERROR_MISSING_PARAMETER = 404

    def __init__(self, body, code):
        self.code = code
        self.body = body

    def get_error_message(self, error_message):
        return

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, indent=4)


def get_api(fun):
    @wraps(fun)
    def decorate(*args, **kwargs):
        return make_response(fun(*args, **kwargs))
    return decorate

