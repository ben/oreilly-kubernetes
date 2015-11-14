from flask.views import MethodView
import json

from api import models

class TodoApi(MethodView):
    def get(self, user_id):
        if user_id is None:
            todos = models.Todo.all()
            return json.dumps([{
                'id': t.id,
                'title': t.title,
                'state': t.state,
            } for t in todos])
