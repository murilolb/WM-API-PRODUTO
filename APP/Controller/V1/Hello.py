# coding=utf-8
from flask.views import MethodView

class HelloController(MethodView):
    def get(self):
        return '0.00'