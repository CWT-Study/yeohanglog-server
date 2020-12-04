from flask import Blueprint, request

import app.main.service.user_service as user_service
from app.main.model.response_model import get_response

tripcost_blueprint = Blueprint("tripcost", __name__, url_prefix="/TripLog/tripcost")
