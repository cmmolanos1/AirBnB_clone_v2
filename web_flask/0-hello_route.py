#!/usr/bin/python3
""" Shows a message """
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes = False)
def hello_world():
    """ Print the message """
    return 'Hello HBNB!'

if __name__ == '__main__':
    app.run()
