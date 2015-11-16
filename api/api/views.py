from flask.views import MethodView
from flask import jsonify
import json

from api import models

class TodoApi(MethodView):
    def get(self, todo_id):
        if todo_id is None:
            todos = models.Todo.all()
            objs = [{
                'id': t.id,
                'title': t.title,
                'state': t.state,
            } for t in todos]
            return jsonify(**{'items': objs})
