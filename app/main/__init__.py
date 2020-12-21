from flask import Flask
from flask_bcrypt import Bcrypt

from .config import config_by_name, SWAGGER_CONFIG

# 여기서 DBConnection을 만들어 app에 전달

flask_bcrypt = Bcrypt()


def create_app(config_name):
	app = Flask(__name__)
	try:
		from flasgger import Swagger
		Swagger(app, SWAGGER_CONFIG)
	except ImportError as e:
		print(e)
	app.config.from_object(config_by_name[config_name])
	flask_bcrypt.init_app(app)

	return app