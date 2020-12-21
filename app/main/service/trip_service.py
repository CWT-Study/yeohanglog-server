from app.main.model.response_model import Response, NotFindUserException
import app.main.const as const
import os
from app.main.db.dbconfig import db_session, TRIP_TABLE
from pymongo.database import Database
from bson.objectid import ObjectId
import app.main.util as util
import logging


@db_session
def get_trip_list(arg, conn: Database = None):
    logging.debug("getTrip API call")
    response_body = {}
    query_dict = {}
    if "tid" in arg:
        query_dict["_id"] = ObjectId(arg["tid"])
    if "uuid" in arg:
        query_dict["members.uuid"] = arg["uuid"]
    if "masterId" in arg:
        query_dict["masterId"] = arg["masterId"]
    if "startDt" in arg or "endDt" in arg:
        if "startDt" in arg and "endDt" in arg:
            date_query_dict = {
                '$or': [
                    {
                        '$and': [
                            {'startDt': {'$gte': util.string_to_isotime(arg["startDt"])}},
                            {'startDt': {'$lte': util.string_to_isotime(arg["endDt"])}}
                        ]
                    },
                    {
                        '$and': [
                            {'endDt': {'$gte': util.string_to_isotime(arg["startDt"])}},
                            {'endDt': {'$lte': util.string_to_isotime(arg["endDt"])}}
                        ]
                    }
                ]
            }
        elif "startDt" in arg and not "endDt" in arg:
            date_query_dict = {'endDt': {'$gte': util.string_to_isotime(arg["startDt"])}}
        else:
            date_query_dict = {'startDt': {'$lte': util.string_to_isotime(arg["endDt"])}}
        query_dict.update(date_query_dict)
    if "title" in arg:
        query_dict["title"] = arg["title"]
    if len(query_dict) == 0:
        logging.debug("Not exit query")
    else:
        logging.debug("Trip Query = " + str(query_dict))
        response_body = {"result": list(conn[TRIP_TABLE].find(query_dict))}
    return response_body


@db_session
def create_trip(body, conn: Database = None):
    logging.debug("create Trip API call")
    response_body = {
        "_id": util.create_obejctId(body["uuid"]),
        "title": body["title"],
        "startDt": util.string_to_isotime(body["startDt"]),
        "endDt": util.string_to_isotime(body["endDt"]),
        "masterId": body["uuid"],
        "repPhoto": "",
        "members": [{
            "uuid": body["uuid"],
            "authority": {
                "plan": True,
                "file": True,
                "cost": True,
            }
        }],
        "preparation": [],
        "readCnt": 0,
        "createdAt": util.get_now_isotime(),
        "updatedAt": util.get_now_isotime()
    }
    logging.info(response_body)
    conn[TRIP_TABLE].insert(response_body)
    return response_body


@db_session
def delete_trip(body, conn: Database = None):
    logging.debug("delete Trip API call")
    delete_dict = {
        "_id": body["tid"]
    }
    conn[TRIP_TABLE].remove(delete_dict)
    return Response.MESSAGE_SUCCESS
