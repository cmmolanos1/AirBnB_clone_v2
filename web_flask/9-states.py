#!/usr/bin/python3
""" Shows a message """
from flask import Flask
from flask import render_template
from models import storage

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown_st(self):
    """ close storage """
    storage.close()


@app.route('/states')
@app.route('/states_list')
def states_list():
    """ Print the number """
    states = storage.all('State').values()
    return render_template('7-states_list.html', states=states)


@app.route('/cities_by_states')
def cities_by_states():
    """ Print cities of a state"""
    states = storage.all('State').values()
    return render_template('8-cities_by_states.html', states=states)


@app.route('/states/<string:id>')
def cities_by_states_id(id):
    """ Print cities by state id"""
    states = storage.all('State')
    key = "State." + id
    if key in states:
        state = states[key]
    else:
        state = None
    return render_template('9-states.html', state=state)

if __name__ == '__main__':
    app.run()
