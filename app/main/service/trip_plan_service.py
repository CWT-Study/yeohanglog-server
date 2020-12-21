from app.main.model.response_model import Response, NotFindTripPlanException
import app.main.const as const
from app.main.db.dbconfig import db_session, TRIP_PLAN_TABLE
from pymongo.database import Database
from bson.objectid import ObjectId
from pymongo import ReturnDocument
import app.main.util as util
import logging

@db_session
def create_trip_plan(body, conn: Database = None):
    logging.debug("create Trip API call")
    response_body = {
        "_id": util.create_obejctId(body["uuid"]),
        "tid": body["tid"],
        "dateIndex": body["dateIndex"],
        "dayIndex": body["dayIndex"],
        "latitude": body["latitude"],
        "longitude": body["longitude"],
        "memo": "",
        "comments": [],
        "complete": False,
        "photos": [],
        "createdAt": util.get_now_isotime(),
        "updatedAt": util.get_now_isotime()
    }
    logging.info(response_body)
    conn[TRIP_PLAN_TABLE].insert(response_body)
    return response_body

