#!/usr/bin/python3
"""a script that starts a Flask web application"""
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    """A function that returns Hello HBNB"""
    return 'Hello, HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """A function that returns HBNB"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def text(text):
    """A function that returns a text variable"""
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def moretext(text='is cool'):
    """A function that returns a text variable"""
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """A func. that returns a number if it is an integer"""
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def template(n):
    """A func. that returns a number if it is an integer"""
    return render_template('5-number.html', number=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
