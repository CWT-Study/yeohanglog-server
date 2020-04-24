from flask import Blueprint, make_response, jsonify, request
import app.main.service.test_service as testAPI

user_service = Blueprint("user", __name__, url_prefix="/user")


@user_service.route("/", methods=["POST"])
def get_user(id: int):
    data = request.get_json()
    print(str(data))
    return testAPI.test(data)