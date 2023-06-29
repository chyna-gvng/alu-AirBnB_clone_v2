#!/usr/bin/python3
"""
    python script that starts a Flask web application
"""

from models import storage
from models.state import State
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states():
    """
        Return: HTML page with list of states
    """
    return render_template('7-states_list.html',
                           states=storage.all('State').values())


@app.teardown_appcontext
def teardown(self):
    """
        Clean-up session
    """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0')