from flask import Blueprint, request

import app.main.service.user_service as user_service
from app.main.model.response_model import get_api

user_control = Blueprint("user", __name__, url_prefix="/user")


# @user_control.route("/", methods=["POST"])
# def signUp():
#     data = request.get_json()
#     print(str(data))
#     return user_service.signUp(data)
#
# @user_control.route("/login", methods=["POST"])
# def signUp():
#     data = request.get_json()
#     print(str(data))
#     return user_service.login(data)

@user_control.route("/login", methods=["GET"])
@get_api
def test():
    data = {'a':'b','b':'a'}
    return user_service.test(data)


@user_control.route("/signin", methods=["POST"])
@get_api
def sign_in():
    data = request.get_json()
    return user_service.signin(data)