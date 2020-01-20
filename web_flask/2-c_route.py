#!/usr/bin/python3
""" Shows a message """
from flask import Flask


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_world():
    """ Print the message """
    return 'Hello HBNB!'


@app.route('/hbnb')
def hello_hbnb():
    """ Print the message """
    return 'HBNB'


@app.route('/c/<text>')
def hello_c(text):
    """ Print the message """
    a = text.replace('_', ' ')
    return 'C {}'.format(a)

if __name__ == '__main__':
    app.run()
