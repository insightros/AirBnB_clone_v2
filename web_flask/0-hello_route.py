#!/usr/bin/python3
"starts a flash web application"
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    "prints a message when / is called"
    return 'Hello HBNB!'

if __name__ == "__main__":
    "main function"
    app.run(host='0.0.0.0', port=5000)
