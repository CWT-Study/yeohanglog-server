from flask import Blueprint, request

import app.main.service.user_service as user_service
from app.main.model.response_model import get_response

tripinfo_blueprint = Blueprint("tripinfo", __name__, url_prefix="/tl/tripinfo")

