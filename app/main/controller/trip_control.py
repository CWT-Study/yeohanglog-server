from flask import Blueprint, request

import app.main.service.trip_service as trip_service
from app.main.model.response_model import get_response

trip_blueprint = Blueprint("trip", __name__)


@trip_blueprint.route("/tl/trip/<uuid>", methods=["POST"])
@get_response
def response_create_trip(uuid):
    """
     create Trip
     make trip by uuid
     ---
     tags:
       - Trip API
     parameters:
       - name: uuid
         in: path
         type: string
         description: description
         required: true
         default: None
     responses:
       200:
         description: success
         schema:
           title: POST Schema
           type: object
           properties:
             _id:
               type: object
             title:
               type: string
             startDt:
               type: string
             endDt:
               type: string
             masterId:
               description: user uuid
               type: string
             repPhoto:
               type: string
             members:
               type: array
               items:
                 type: object
                 properties:
                   uuid:
                     type: string
                     description: user uuid
                   authority:
                     type: object
                     description: auth information
                     properties:
                       plan:
                         type: boolean
                       file:
                         type: boolean
                       cost:
                         type: boolean
             preparation:
               type: array
               items:
                 type: object
             readCnt:
               type: integer
             createdAt:
               type: integer
             updatedAt:
               type: integer
    """
    body = request.get_json()
    return trip_service.create_trip(uuid, body)


@trip_blueprint.route("/tl/trip/", methods=["GET"])
@get_response
def response_trip_list():
    args = request.args
    return trip_service.get_trip_list(args)
