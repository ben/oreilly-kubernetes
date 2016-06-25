#!/usr/bin/env python3

from flask import Flask, g, request
app = Flask(__name__)
app.debug = True

from flask_cors import CORS
CORS(app)

from api import views, db, models
import requests

@app.teardown_request
def teardown_request(exception):
    if exception:
        db.session.rollback()
    else:
        db.session.commit()

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/send_email', methods=['POST'])
def send_email():
    # print(request.json)
    todos = models.Todo.all()
    email_lines = ['TODOS:', '']
    for t in todos:
        # print(t.id, t.state)
        email_lines.append(
            '  ' + ('x' if t.state == 'complete' else ' ') + '  ' + t.title
        )

    requests.post('http://mailer:3000/outgoing_emails', data={
        'to': request.json['to'],
        'from': 'todos@example.com',
        'subject': 'TODOs',
        'text': '\n'.join(email_lines)
    })
    return '\n'.join(email_lines)

todo_view = views.TodoApi.as_view('todo_api')
app.add_url_rule('/todos', defaults={'todo_id': None},
                 view_func=todo_view, methods=['GET',])
app.add_url_rule('/todos', view_func=todo_view, methods=['POST',])
app.add_url_rule('/todos/<int:todo_id>', view_func=todo_view,
                 methods=['GET', 'PUT', 'DELETE'])

if not db.session:
    db.init_db()
