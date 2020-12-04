from app.main.model.response_model import Response
import app.main.const as const
import os
from app.main.db.dbconfig import db_session, USER_TABLE
from app.main.model.user_model import UserModel
from pymongo.database import Database
import app.main.util as util
import logging


@db_session
def user_sign(data, conn: Database = None):
    logging.debug("create user API call")
    response_body = UserModel(
        _id=util.create_uuid(),
        nickname=data["nickname"],
        profile=data["profile"],
        social_type=data["socialType"],
        social_id=data["socialId"],
        invite_code=util.create_invitecode(),
        pushtoken="",
        created_at=util.get_utctime_string(),
        updated_at=util.get_utctime_string(),
        permission=data["permission"],
        push=data["push"]
    ).to_dict()
    conn[USER_TABLE].insert(response_body)
    logging.info(response_body)
    return response_body


@db_session
def get_user_info(arg, conn: Database = None):
    logging.debug("getUser API call")
    response_body = {}
    query_dict = {}
    if "uuid" in arg:
        query_dict["_id"] = arg["uuid"]
    if "nickName" in arg:
        query_dict["nickName"] = arg["nickName"]
    if "inviteCode" in arg:
        query_dict["inviteCode"] = arg["inviteCode"]
    if "socialId" in arg:
        query_dict["socialId"] = arg["socialId"]
    if "socialType" in arg:
        query_dict["socialType"] = arg["socialType"]
    if "createdAt" in arg:
        query_dict["createdAt"] = arg["createdAt"]
    if "updatedAt" in arg:
        query_dict["updatedAt"] = arg["updatedAt"]
    if len(query_dict) == 0:
        logging.debug("Not exit query")
    else:
        logging.debug("User Query = " + str(query_dict))
        response_body = {'result': list(conn[USER_TABLE].find(query_dict))}
    return response_body


def save_profile_image(uuid, files):
        path = os.path.join(const.PROFILE_PATH, uuid)
        if not os.path.isdir(path):
            logging.info(f"make dir {path}")
            os.mkdir(path)
        else:
            logging.info("Exsist Dir")
        file = files["profile"] #form tag에 이름이 profile인 파일 가져오기
        logging.info(file.filename)
        file.save(os.path.join(path, f"profile_{len(os.listdir(path))}.jpg")) # 회원 디렉토리의 프로필 갯수대로 다음 이름이 결정 ex) profile_0
        response_body = Response.MESSAGE_SUCCESS

        return response_body