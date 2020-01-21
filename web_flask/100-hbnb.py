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

    
@app.route('/hbnb')
def hbnb_filters():
    """display in the static filters"""
    states = storage.all('State').values()
    amenities = storage.all('Amenity').values()
    places = storage.all('Place').values()
    return render_template('100-hbnb.html',
                           states=states, amenities=amenities, places=places)

if __name__ == '__main__':
    app.run()
