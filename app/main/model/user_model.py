from app.main.model.response_model import Response


class UserModel(Response):
    id = ""
    email = ""
    social_id = ""

    def __init__(self, id, email):
        self.id = id
        self.email = email
