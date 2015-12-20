#!/usr/bin/env python3

from flask import Flask, g
app = Flask(__name__)

from api import views, db

@app.before_request
def setup_transaction():
    g.txn = db.session.begin_nested()

@app.teardown_request
def teardown_request(exception):
    if app.debug:
        return
    txn = getattr(g, 'txn')
    if txn is None:
        return
        
    if exception:
        db.session.rollback()
    else:
        db.session.commit()


@app.route('/')
def hello_world():
    return 'Hello World!'

todo_view = views.TodoApi.as_view('todo_api')
app.add_url_rule('/todos/', defaults={'todo_id': None},
                 view_func=todo_view, methods=['GET',])
app.add_url_rule('/todos/', view_func=todo_view, methods=['POST',])
app.add_url_rule('/todos/<int:todo_id>', view_func=todo_view,
                 methods=['GET', 'PUT', 'DELETE'])

if not db.session:
    db.init_db()
