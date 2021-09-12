#!/usr/bin/python3

"""starts a Flask web application"""

from flask import Flask, render_template

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


@app.route('/number/<int:n>', strict_slashes=False)
def number_int_parameter(n):
    """ View function for number and integer parameter route

    Args:
        n: parameter to be set as the
        following resource

    Returns:
        Text to be displayed as ouput on the server
    """

    return str(n) + ' is a number'


@app.route('/number_template/<int:n>')
def number_template_n(n):
    """ View function for number and integer parameter route

    Args:
        n: parameter to be set as the
        following resource

    Returns:
        Text to be displayed as ouput on the server
    """

    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>')
def number_odd_or_even_n(n):
    """ View function for number and integer parameter route

    Args:
        n: parameter to be set as the
        following resource

    Returns:
        Text to be displayed as ouput on the server
    """

    even_or_odd = 'even' if n % 2 == 0 else 'odd'
    return render_template('6-number_odd_or_even.html', n=n,
                           even_or_odd=even_or_odd)


app.run(host='0.0.0.0')
