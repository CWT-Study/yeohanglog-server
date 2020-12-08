from app.main.model.response_model import Response, NotFindUserException
import app.main.const as const
import os
from app.main.db.dbconfig import db_session, TRIP_TABLE
from pymongo import ReturnDocument
from pymongo.database import Database
import app.main.util as util
import logging


@db_session
def create_trip(uuid, body, conn: Database = None):
    logging.debug("create Trip API call")
    response_body = {
        "title": body["title"],
        "startDt": body["startDt"],
        "endDt": body["startDt"],
        "masterId": uuid,
        "repPhoto": "",
        "members": [{
            "id": uuid,
            "permission": {
                "plan": True,
                "file": True,
                "cost": True,
            }
        }],
        "preparation": [],
        "readCnt": 0,
        "createdAt": util.get_utctime_string(),
        "updatedAt": util.get_utctime_string()
    }
    conn[TRIP_TABLE].insert(response_body)
    logging.info(response_body)
    return response_body
