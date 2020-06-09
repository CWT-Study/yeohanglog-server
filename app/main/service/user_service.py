from app.main.model.response_model import Response
from app.main.model.user_model import UserModel


def test(data):
    # 기능추가는 여기서

    response_body = UserModel(data['a'], data['b']).to_json()  # Model을 사용할 경우 (Model은 Response(response_model)을상속받음)
    print(response_body)

    response_body = {  # Model을 사용 안할경우
        'model': 'no',
        'name': 'sangmin'
    }

    #
    return response_body, Response.CODE_SUCCESS
