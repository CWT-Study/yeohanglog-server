from flask import Blueprint, request

import app.main.service.trip_service as trip_service
from app.main.model.response_model import get_response

trip_blueprint = Blueprint("trip", __name__, url_prefix="/tl/trip")


@trip_blueprint.route("/<uuid>", methods=["POST"])
@get_response
def response_create_trip(uuid):
    body = request.get_json()
    return trip_service.create_trip(uuid, body)


@trip_blueprint.route("/", methods=["GET"])
@get_response
def response_trip_list():
    args = request.args
    return trip_service.get_trip_list(args)
