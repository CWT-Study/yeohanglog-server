import uuid as uuid_made
import shortuuid
import datetime
import datetime
import pytz
import logging

def create_uuid():
    uuid = uuid_made.uuid1()
    logging.debug(uuid)
    return str(uuid)

# def create_uuid():
#     uuid = shortuuid.uuid(name="triplog")
#     print(uuid)
#     return uuid

def create_invitecode():
    code = shortuuid.ShortUUID().random(6)
    logging.debug(code)
    return str(code)


def get_utctime_string():
    return str(datetime.datetime.now(tz=pytz.utc).isoformat())


create_invitecode()
