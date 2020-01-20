#!/usr/bin/python3
""" Shows a message """
from flask import Flask
from flask import render_template


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


@app.route('/python/')
@app.route('/python/<text>')
def hello_py(text='is fun'):
    """ Print the message """
    b = text.replace('_', ' ')
    return 'Python {}'.format(b)


@app.route('/number/<int:n>')
def is_number(n):
    """ Print the number """
    if type(n) is int:
        return '{} is a number'.format(n)


@app.route('/number_template/<int:n>')
def number_template(n):
    """ Print the number """
    if type(n) is int:
        return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/<int:n>')
def odd_even(n):
    """ Print the number and defines if is odd/even"""
    if type(n) is int:
        mod = n % 2
        return render_template('6-number_odd_or_even.html', number=n, mod=mod)

if __name__ == '__main__':
    app.run()
