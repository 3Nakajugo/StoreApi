from flask import Flask
from project.db.db import Database

app = Flask(__name__)

from project.views import app

db = Database()
db.create_table()

if __name__ == '__main__':
    app.run(debug=True)
