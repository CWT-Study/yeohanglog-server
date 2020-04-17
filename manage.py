import os
import unittest

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from app.main import create_app
from flask import Flask, url_for, render_template, request, redirect, sessions, jsonify
from flask_restful import Resource, Api
import app.main.service.test_service as testAPI
import app.main.controller.test_db as testDB

app = create_app(os.getenv('BOILERPLATE_ENV') or 'dev')
app.app_context().push()
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
# api.add_resource()

@app.route('/test', methods = ['POST'])
def test():
    data = request.get_json()
    print(str(data))
    body = testAPI.test(data)
    return jsonify(body)

@app.route('/user', methods = ['POST'])
def user():
    data = request.get_json()
    print(str(data))
    body = testAPI.test(data)
    return jsonify(body)

if __name__ == '__main__':
	manager.run()
