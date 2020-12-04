from flask import Blueprint, request
import app.main.service.user_service as user_service
from app.main.model.response_model import get_response

user_blueprint = Blueprint("user", __name__, url_prefix="/TripLog/user")


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

@user_blueprint.route("/sign", methods=["POST"])
@get_response
def sign_in():
    body = request.get_json()
    return user_service.user_sign(body)


@user_blueprint.route("/", methods=["GET"])
@get_response
def get_user():
    args = request.args
    return user_service.get_user_info(args)


@user_blueprint.route("/profile/<uuid>", methods=["GET", "POST"])
@get_response
def profile(uuid):
    if request.method == 'GET':
        None
    if request.method == 'POST':
        files = request.files
        return user_service.save_profile_image(uuid, files)
