#!/usr/bin/python3

"""starts a Flask web application"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """View function for Default

    Returns:
        Text to be displayed as ouput on the server
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """view function for hbnb route

    Returns:
        Text to be displayed as ouput on the server
    """
    return 'HBNB'


app.run(host='0.0.0.0')
