from __init__ import app, api
from controller.V1.Hello import HelloController
from flask import jsonify


api.add_resource(HelloController, '/', '/<name>')
