#!/usr/bin/python3
"""Web App"""

from models import storage
from models.state import State
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states_list():
    """Return HTML page with a list of states"""
    states = storage.all(State).values()
    return render_template('9-states.html', states=states, id=None)


@app.route('/states/<id>', strict_slashes=False)
def states_by_id(id):
    """Return HTML page with cities of a specific state"""
    states = storage.all(State)
    key = "State." + id
    state = states.get(key)
    if state is None:
        return render_template('9-states.html', id=None)
    else:
        return render_template('9-states.html', state=state, id=id)


@app.teardown_appcontext
def teardown_appcontext(exception):
    """Close the current SQLAlchemy session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
