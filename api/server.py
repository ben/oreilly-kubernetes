#!/usr/bin/env python3

from flask import Flask
app = Flask(__name__)
app.debug = True

from api import views, models

@app.route('/')
def hello_world():
    return 'Hello World!'

app.add_url_rule('/todos/',
                 view_func=views.TodoApi.as_view('todos'))

models.init_db()
