from flask.views import MethodView
from flask import jsonify, request

from api import models, db

def cors_headers(f):
    def wrapped(*args, **kwargs):
        resp = f(*args, **kwargs)
        resp.headers['Access-Control-Allow-Origin'] = '*'
        return resp
    return wrapped

class TodoApi(MethodView):
    decorators = [cors_headers]

    def get(self, todo_id):
        if todo_id is None:
            todos = models.Todo.all()
            objs = [{
                'id': t.id,
                'title': t.title,
                'state': t.state,
            } for t in todos]
            return jsonify(todos=objs)
        t = models.Todo.query.get(todo_id)
        return jsonify(todo={
            'id' : t.id,
            'title' : t.title,
            'state' : t.state,
        })

    def post(self):
        t = models.Todo()
        t.set_fields(request.json)
        t.save()
        return jsonify(id=t.id, title=t.title, state=t.state)
