from app.main.model.response_model import Response



class Permission():

    def __init__(self, info=True, ad=True):
        self.info = info
        self.ad = ad


class Push():

    def __init__(self, app_push=True, add_push=True):
        self.app_push = app_push
        self.add_push = add_push


class UserModel(Response):

    def __init__(self, _id="", nickname="", email="", social_id="", pushtoken="", profile="", created_at="",
                 updated_at="", permisision=Permission(), push=Push()):
        self._id = _id
        self.nickname = nickname
        self.email = email
        self.social_id = social_id
        self.pushtoken = pushtoken
        self.profile = profile
        self.created_at = created_at
        self.updated_at = updated_at
        self.permission = permisision
        self.push = push
