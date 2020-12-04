import os

from app.main import create_app
from flask_restful import Resource, Api
from app.main.controller.user_control import user_blueprint
from app.main.controller.trip_control import trip_blueprint
from app.main.controller.tripinfo_control import tripinfo_blueprint
from app.main.controller.tripcost_config import tripcost_blueprint
from app.main.controller.triplog_control import triplog_blueprint
from app.main.db.dbconfig import create_mongo_client
import logging.config
from app.main.logging_conf import LOGGING_CONFIG

app = create_app(os.getenv('BOILERPLATE_ENV') or 'dev')
app.app_context().push()
app.register_blueprint(user_blueprint)
app.register_blueprint(trip_blueprint)
app.register_blueprint(tripinfo_blueprint)
app.register_blueprint(tripcost_blueprint)
app.register_blueprint(triplog_blueprint)
api = Api(app)
logging.config.dictConfig(LOGGING_CONFIG)

create_mongo_client()

if __name__ == '__main__':
    app.run(host='0.0.0.0')
