from app.main.model.response_model import Response


class Thema():

    def __init__(self, code="", name="", trip=[]):
        self.code = code
        self.name = name
        self.trip = trip


class Triplog(Response):

    def __init__(self, _id="", thema=[]):
        self._id = _id
        self.thema = thema