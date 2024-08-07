#!/usr/bin/python3

"""
Starting a Flask web application on host ip 0.0.0.0:
running on port 5000
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    return('Hello HBNB!')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
