from flask import Blueprint, request

import app.main.service.trip_plan_service as trip_plan_service
from app.main.model.response_model import get_response


trip_plan_blueprint = Blueprint("triplan", __name__, url_prefix="/tl/tripplan")


@trip_plan_service.route("/<tpid>", methods=["GET", "POST", "DELETE"])
@get_response
def response_trip(tid):
    if request.method == 'GET':
        args = request.args
        return None
    elif request.method == 'POST':
        body = request.get_json()
        return trip_plan_service.create_trip_plan(body)
    elif request.method == 'DELETE':
        body = request.get_json()
        return None