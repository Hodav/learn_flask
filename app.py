import flask
from flask import Flask
from flask import request, g, current_app, session, redirect, abort
import time

app = Flask(__name__)
some_dict = {"data": "01.12.24", "time": "15:30", "test1": 123, "test2": 456}
@app.route('/user/<id>')
def hello_world(id):
    return flask.render_template('index.html')


@app.route('/')
def index():
    data = time.time()
    return flask.render_template('index.html', **some_dict)


@app.route('/test/<int:id>/<id2>')
def print_id(id, id2):
    return f"id = {id}, id2 = {id2}"



if __name__ == '__main__':
    app.run(debug=True)
