import json

class Test():
    id = ""
    email = ""

    def __init__(self, id, email):
        self.id = id
        self.email = email

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, indent=4)

