from flask.views import MethodView
from flask import jsonify, request

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
        t = models.Todo.query.get(todo_id)
        return jsonify(
            id=t.id,
            title=t.title,
            state=t.state
        )

    def post(self):
        t = models.Todo()
        t.set_fields(request.json)
        t.save()
        return jsonify(id=t.id, title=t.title, state=t.state)
