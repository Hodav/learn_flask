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


@app.route('/test/<int:id>')
def print_id(id):
    if id == 1:
        return flask.redirect('/test1')
    elif id == 2:
        return flask.redirect('/test2')
    return flask.redirect('/test3')


@app.route('/test1')
def test1():
    return "OK test1"


@app.route('/test2')
def test2():
    return "OK test2"


@app.route('/test3')
def test3():
    return "OK test3"


@app.route("/reg", methods=["GET", "POST"])
def reg():
    if request.method == "POST":  # если пользователь ввел имя и нажал отправить
        name = request.form["username"]  # возьмем текст из формы который он отправил
        return f"Привет {name}!"  # вернем строку "Привет name"
    return """
        <form action="/reg" method="post">
            <p>
	            <label for="username">Username</label>
	            <input type="text" name="username">
	        </p>
	    	<p>
	            <input type="submit" value="Отправить">
	        </p>
        </form>
        """


@app.route('/catalog/<int: id>')
def catalog(id):
    pass


if __name__ == '__main__':
    app.run(debug=True)
