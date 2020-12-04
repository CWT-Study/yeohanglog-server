import app.main.service.triplog_service as service
from app.main.model.response_model import get_response
from flask import Blueprint, request

triplog_blueprint = Blueprint("triplog", __name__, url_prefix="/TripLog/triplog")

triplog_blueprint .route("/", methods=["POST"])
@get_response
def create_triplog():
    body = request.get_json()
    return service.signin(body)
