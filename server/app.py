#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"

@app.route('/<string:string>')
def print_string(string):
    return f"{string}"

@app.route('/<integer:number>')
def count(number):
    if number <= 0:
        print ("Kindly don't be stupid. We need a positive number.")
        return
    
    for int in range(1, number + 1):
        print(int)


if __name__ == '__main__':
    app.run(port=5555, debug=True)
