from flask import Blueprint, request

import app.main.service.user_service as user_service
from app.main.model.response_model import get_api
import app.main.db.dbconfig as db

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

@user_control.route("/signin", methods=["POST"])
@get_api
def sign_in():
    body = request.get_json()
    return user_service.signin(body)


@user_control.route("/", methods=["GET"])
@get_api
def get_user():
    args = request.args
    return user_service.get_user_info(args)


@user_control.route("/profile/<uuid>", methods=["GET", "POST"])
@get_api
def profile(uuid):
    if request.method == 'GET':
        None
    if request.method == 'POST':
        files = request.files
        return user_service.save_profile_image(uuid, files)
