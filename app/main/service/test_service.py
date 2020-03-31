from app.main.model.test_model import Test
from app.main.model.response_model import Response

def test(data):
    try:
        id = data["id"]
        email = data["email"]
        body = Test(id, email).to_json()
        return body
    except KeyError:
        body = Response(404, "Missing Parameter").to_json()
        return body
    except Exception as e:
        print(e)
        body = Response(401, "Unknown error").to_json()
        return body