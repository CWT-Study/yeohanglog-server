from flask import make_response
import json

class Response():
    code = 0
    body = ""

    CODE_SUCCESS = 200
    CODE_ERROR_UNKOWN = 401
    CODE_ERROR_MISSING_PARAMETER = 404

    def __init__(self, code, body):
        self.code = code
        self.body = body

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, indent=4)

    def make(self):
        return make_response(self.body, self.code)