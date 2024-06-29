#!/usr/bin/python3
"""
A simple flask script to start up an app
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """ Return hello hbnb"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Return hbnb string """
    return "HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
