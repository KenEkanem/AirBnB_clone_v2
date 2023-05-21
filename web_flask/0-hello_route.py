#!/usr/bin/python3
from flask import Flask
"""new flask application"""
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def display():
    """display Hello HBNB!"""
    return ('Hello HBNB!')


if __name__ == "__main__":
    """run when it is not imported as a module"""
    app.run(host='0.0.0.0', port=5000)
