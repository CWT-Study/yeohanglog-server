import os
import unittest

from flask import abort
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from app.main import create_app
from flask import Flask, url_for, render_template, request, redirect, sessions, jsonify
from flask_restful import Resource, Api
from app.main.controller.user_control import user_service

app = create_app(os.getenv('BOILERPLATE_ENV') or 'dev')
app.app_context().push()
app.register_blueprint(user_service)
api = Api(app)
manager = Manager(app)
migrate = Migrate(app)
manager.add_command('db', MigrateCommand)

@manager.command
def run():
    app.run()

@manager.command
def test():
    """Runs the unit tests."""
    tests = unittest.TestLoader().discover('app/test', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1
# # api.add_resource()

# @app.route('/test', methods = ['POST'])
# def test():
#     data = request.get_json()
#     print(str(data))
#     response = testAPI.test(data)
#     return response.body, response.code

# @app.route('/user', methods = ['POST'])
# def user():
#     data = request.get_json()
#     print(str(data))
#     body = testAPI.test(data)
#     return jsonify(body)

if __name__ == '__main__':
	manager.run()
