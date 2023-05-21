#!/usr/bin/python3
"""This is a flask application

"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def end_session(f):
    """close the session for that request"""
    storage.close()


@app.route("/states_list", strict_slashes=False)
def list_states():
    """display the states in the database"""
    states = storage.all(State)
    return render_template("7-states_list.html", states=states)


if __name__ == "__main__":
    """run flask app"""
    app.run(host="0.0.0.0", port=5000, debug=True)
