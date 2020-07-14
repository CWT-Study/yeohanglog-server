import app.main.service.triplog_service as service
from app.main.model.response_model import get_api
from flask import Blueprint, request

user_control = Blueprint("triplog", __name__, url_prefix="/triplog")

@user_control.route("/", methods=["POST"])
@get_api
def create_triplog():
    body = request.get_json()
    return service.signin(body)
