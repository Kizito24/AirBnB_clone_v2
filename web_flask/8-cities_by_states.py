#!/usr/bin/python3
"""
A simple flask script to start up an app
"""
from flask import Flask
from flask import render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_list():
    """ A function to get all the states in the db"""
    list_of_states = storage.all(State)
    return render_template('8-cities_by_states.html', states=list_of_states)


@app.teardown_appcontext
def handle_close(exception):
    """ To remove current sqlalchemy session """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
