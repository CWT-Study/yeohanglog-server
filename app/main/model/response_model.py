import json

class Response():
    code = 0
    body = ""

    def __init__(self, code, body):
        self.code = code
        self.body = body

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, indent=4)