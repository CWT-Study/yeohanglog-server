from app.main.model.response_model import Response
from app.main.model.user_model import UserModel
import app.main.db.user_db as db
import app.main.const as const


def test(data):
    # 기능추가는 여기서

    response_body = UserModel(data['a'], data['b']).to_json()  # Model을 사용할 경우 (Model은 Response(response_model)을상속받음)
    print(response_body)

    response_body = {  # Model을 사용 안할경우
        'model': 'no',
        'name': 'sangmin'
    }

    return response_body, Response.CODE_SUCCESS


def signin(data):
    response_body = {}
    response_code = 200
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
    if "_id" in arg:

    if "nickName" in arg:

    if "inviteCode" in arg:

    if "socialId" in arg:

    if "type" in arg:

    if "createdAt" in arg:

    if "updatedAt" in arg:


