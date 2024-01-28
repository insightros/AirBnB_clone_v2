#!/usr/bin/python3
"starts a web flash application"
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    "prints a message when / is called"
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    "prints a message when /hbnb is called"
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    "prints a message when /c is called"
    return "C " + text.replace('_', ' ')


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_is_cool(text='is_cool'):
    "prints a message when /python is called"
    return "Python " + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def is_n_number(n):
    "prints a message when /number is called"
    return "{:d} is a number".format(n)

if __name__ == "__main__":
    "main function"
    app.run(host='0.0.0.0', port=5000)
