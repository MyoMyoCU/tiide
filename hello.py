from flask import Flask

myapp = Flask(__name__)

@myapp.route("/")
def hello():
    return "Welcome to my Heroku"
