from app.main.model.test_model import Test
from app.main.model.response_model import Response
import app.main.db.user_db as db

def test(data):
    try:
        id = data["id"]
        email = data["email"]
        db.create_table()
        body = Test(id, email).to_json()
        return Response(200, body).make()
    except KeyError:
        response = Response(404, "Missing Parameter")
        return response.make()
    except Exception as e:
        print(e)
        response = Response(401, "Unknown error")
        return response.make()