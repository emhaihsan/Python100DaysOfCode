from flask import Flask
from utils import *

app = Flask(__name__)
@app.route("/")
@make_bold 
@make_emphasis
@make_underlined
def hello_world():
    return "Hello, World!"

@app.route("/bye")
def bye():
    return "Bye!"

@app.route("/username/<username>/<int:number>")
def greet(username, number):
    return f"Hello {username}, you are {number} years old!"

if __name__ == "__main__":
    app.run()