import os

from app.main import create_app
from flask_restful import Resource, Api
from app.main.controller.user_control import user_control
from app.main.db.dbconfig import create_mongo_client
import logging.config
from logging_conf import LOGGING_CONFIG

app = create_app(os.getenv('BOILERPLATE_ENV') or 'dev')
app.app_context().push()
app.register_blueprint(user_control)
api = Api(app)
logging.config.dictConfig(LOGGING_CONFIG)


create_mongo_client()


if __name__ == '__main__':
    app.run()
