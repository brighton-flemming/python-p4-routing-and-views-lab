#!/usr/bin/env python3

from flask import Flask,abort

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"

@app.route('/print/<string:string>')
def print(string):
    return f"{string}"

@app.route('/count/<int:number>')
def count(number):
    if number > 0:
     numbers = [str(int) for int in range(1, number + 1)]
     return "\n".join(numbers)
    else:
         abort("Kindly don't be stupid. We need a positive number.", 400)


@app.route('/math/<float:num1>/<string:operation>/<float:num2>')
def math(num1, operation, num2):
    result = None

    if operation in ("+", "add") :
        result = num1 + num2
    elif operation in ("-", "subtract"):
        result = num1 - num2
    elif operation in ("*", "multiply") :
        result = num1 * num2
    elif operation == "divide":
         if num2 != 0:
            result = num1 / num2
         else:
            abort(400, "Division by zero is mathematically impossible.You should know that.")
    elif operation == "%":
        if num2 != 0:
            result = num1 % num2
        else:
            return "Division by zero is mathematically impossible.You should know that."
    
    if result is not None:
        return f"The result of {num1} {operation} {num2} is {result}"
    else:
        return "The operation is improbable."
    

if __name__ == '__main__':
    app.run(port=5555, debug=True)
