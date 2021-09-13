#!/usr/bin/python3
from flask import Flask
from models import storage
from flask import render_template
from models import State

app = Flask(__name__)


@app.teardown_appcontext
def tearDown(exception):
    "remove the current SQLAlchemy Session"
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states():
    """list of all State objects present in
    DBStorage sorted by name"""
    states = storage.all(State)
    render_template('7-states_list.html', states=states)


if name__ == '__main__':
    app.run(host='0.0.0.0')
