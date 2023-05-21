#!/usr/bin/python3
"""
This is a flask application
The application listens on 0.0.0.0, port 5000.
Routes:
    /: display “Hello HBNB!”
    /hbnb: display “HBNB”
    """
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def display():
    """display hello HBNB"""
    return ("Hello HBNB!")


@app.route('/hbnb', strict_slashes=False)
def display_hbnb():
    """display HBNB"""
    return ("HBNB")


if __name__ == "__main__":
    app.run('0.0.0.0', 5000)
