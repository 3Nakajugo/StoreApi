from flask import Flask

app = Flask(__name__)

from project.views import app

if __name__ == '__main__':
    app.run(debug = True)
