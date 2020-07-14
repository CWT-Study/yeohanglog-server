from app.main.model.response_model import Response
from app.main.model.triplog_model import Triplog
import app.main.db.user_db as db
import app.main.const as const
import os

def create_thema(body):
    try:
        uuid = body["uuid"]
        thema = body["thema"]
    except KeyError:
        None
    except Exception as e:
        None
    finally:
        None