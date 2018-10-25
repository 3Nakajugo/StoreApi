from flask import Flask

app = Flask(__name__)


@app.route('/')
def greet():
    return ('welcome to my store'), 200
