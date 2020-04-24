from flask import Blueprint, request
import app.main.service.test_service as testAPI

user_service = Blueprint("user", __name__, url_prefix="/user")


@user_service.route("/", methods=["POST"])
def get_user():
    data = request.get_json()
    print(str(data))
    return testAPI.test(data)