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


@app.route('/c/<text>', strict_slashes=False)
def c_parmeter(text):
    """ View function for c and parameter route

    Args:
        text: parameter to be set as the
        following resource

    Returns:
        Text to be displayed as ouput on the server
    """

    formatted_text = text.replace('_', ' ')
    return 'C ' + formatted_text


@app.route('/python/', defaults={'text': 'is cool'})
@app.route('/python/<text>', strict_slashes=False)
def python_parameter(text):
    """ View function for python and parameter route

    Args:
        text: parameter to be set as the
        following resource

    Returns:
        Text to be displayed as ouput on the server
    """

    formatted_text = text.replace('_', ' ')
    return 'Python ' + formatted_text


if __name__ == "__main__":
    app.run(host='0.0.0.0')
