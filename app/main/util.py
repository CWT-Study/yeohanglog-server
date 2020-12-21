import uuid as uuid_made
import shortuuid
import datetime
from datetime import datetime
import pytz
import logging
import time
import os
import app.main.const as const


def create_uuid():
    uuid = uuid_made.uuid1()
    logging.debug(uuid)
    return str(uuid)


# def create_uuid():
#     uuid = shortuuid.uuid(name="triplog")
#     print(uuid)
#     return uuid


def create_image_dir():
    if not os.path.isdir(const.IMAGE_ROOT_PATH):
        logging.info("make image root dir")
        os.mkdir(const.IMAGE_ROOT_PATH)
    else:
        logging.info("Exsist Dir Image Root Dir")

    if not os.path.isdir(const.PROFILE_PATH):
        logging.info("make profile dir")
        os.mkdir(const.PROFILE_PATH)
    else:
        logging.info("Exsist Profile Dir")

    if not os.path.isdir(const.TRIP_PICTURE_PATH):
        logging.info("make trip image dir")
        os.mkdir(const.TRIP_PICTURE_PATH)
    else:
        logging.info("Exsist Trip Image Dir")


def create_invitecode():
    code = shortuuid.ShortUUID().random(6)
    logging.debug(code)
    return str(code)


def get_now_isotime():
    return datetime.now()


def string_to_isotime(string):
    return datetime.strptime(string, '%Y-%m-%dT%H:%M:%S%z')


def create_obejctId(uuid: str = ""):
    # 밀리세컨드 + uuid 20글자
    uuid = uuid.replace("-", "")
    logging.debug(uuid[:20])
    object_id = f"{hex(int(round(time.time() * 1000)))[2:]}-{uuid[:20]}"
    return object_id
