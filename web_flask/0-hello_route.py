#!/usr/bin/python3

"""starts a Flask web application"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """ View function for Default

    Returns:
        Text to be displayed as ouput on the server
    """
    return 'Hello HBNB!'


if __name__ == "__main__":
    app.run(host='0.0.0.0')
