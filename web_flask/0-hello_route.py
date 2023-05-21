#!/usr/bin/python3
"""new flask application
The application listens on 0.0.0.0, port 5000.
Routes:
    Displays 'Hello HBNB!'
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def display():
    """display Hello HBNB!"""
    return ('Hello HBNB!')


if __name__ == "__main__":
    """run when it is not imported as a module"""
    app.run(host='0.0.0.0', port=5000)
