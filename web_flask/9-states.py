#!/usr/bin/python3
"""
    python script that starts a Flask web application
"""

from models import storage
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states_list():
    """
    Display a HTML page with the list of states
    """
    states = storage.all('State').values()
    return render_template('9-states.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def states_by_id(id):
    """
    Display a HTML page with the list of cities for a state
    """
    state = storage.get('State', id)
    if state:
        return render_template('9-states.html', state=state)
    else:
        return render_template('9-states.html', not_found=True)


@app.teardown_appcontext
def app_teardown(arg=None):
    """
    Clean-up session
    """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
