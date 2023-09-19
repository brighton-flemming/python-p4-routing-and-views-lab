#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"

@app.route('/<string:string>')
def print_string(string):
    print f"{string}"


if __name__ == '__main__':
    app.run(port=5555, debug=True)
