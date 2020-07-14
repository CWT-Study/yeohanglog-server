from app.main.model.response_model import Response
from app.main.model.user_model import UserModel
import app.main.db.user_db as db
import app.main.const as const
import os


def signin(data):
    try:
        uuid = data["uuid"]
        nickname = data["nickname"]
        print(uuid)
        print(nickname)
        response_body = db.insert_user(uuid, nickname, const.get_utctime_string())
        print(response_body)
        if response_body:
            response_code = Response.CODE_SUCCESS
        else:
            response_body = Response.MESSAGE_ERROR_DB
            response_code = Response.CODE_ERROR_DB
    except KeyError:
        response_body = Response.MESSAGE_ERROR_PARAMETER
        response_code = Response.CODE_ERROR_MISSING_PARAMETER
    except Exception:
        print(Exception)
        response_body = Response.MESSAGE_UNKOWN
        response_code = Response.CODE_ERROR_UNKOWN
    finally:
        return response_body, response_code


def get_user_info(arg):
    try:
        response_body = {}
        response_code = 200
        print(arg.get('asdfasdfasdf', ''))
        query_dict = {}
        if "uuid" in arg:
            query_dict["_id"] = arg["uuid"]
        if "nickName" in arg:
            query_dict["nickName"] = arg["nickName"]
        if "inviteCode" in arg:
            query_dict["inviteCode"] = arg["inviteCode"]
        if "socialId" in arg:
            query_dict["socialId"] = arg["socialId"]
        if "type" in arg:
            query_dict["type"] = arg["type"]
        if "createdAt" in arg:
            query_dict["createdAt"] = arg["createdAt"]
        if "updatedAt" in arg:
            query_dict["updatedAt"] = arg["updatedAt"]
        if len(query_dict) == 0:
            response_body = {}
            response_code = Response.CODE_SUCCESS
        else:
            print("dbconnect")
            response_body = db.find_user(query_dict)
            if response_body:
                response_code = Response.CODE_SUCCESS
            else:
                response_body = Response.MESSAGE_ERROR_DB
                response_code = Response.CODE_ERROR_DB
    except Exception as e:
        print(e)
        response_body = Response.MESSAGE_UNKOWN
        response_code = Response.CODE_ERROR_UNKOWN
    finally:
        return response_body, response_code


def save_profile_image(uuid, files):
    try:
        path = os.path.join(const.PROFILE_PATH, uuid)
        if not os.path.isdir(path):
            print(f"make dir {path}")
            os.mkdir(path)
        else:
            print("Exsist Dir")
        file = files["profile"] #form tag에 이름이 profile인 파일 가져오기
        print(file.filename)
        file.save(os.path.join(path, f"profile_{len(os.listdir(path))}.jpg")) # 회원 디렉토리의 프로필 갯수대로 다음 이름이 결정 ex) profile_0
        response_body = Response.MESSAGE_SUCCESS
        response_code = Response.CODE_SUCCESS
    except KeyError:
        response_body = Response.MESSAGE_ERROR_PARAMETER
        response_code = Response.CODE_ERROR_MISSING_PARAMETER
    except Exception as e:
        print(e)
        response_body = Response.MESSAGE_UNKOWN
        response_code = Response.CODE_ERROR_UNKOWN
    finally:
        return response_body, response_code