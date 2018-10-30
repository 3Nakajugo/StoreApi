from flask import Flask

from flask_jwt_extended import JWTManager

from project.security import authenticate, identity


app = Flask(__name__)
# SECRET_KEY = "1234"

app.config['JWT_SECRET_KEY'] = '1234'
jwt = JWTManager(app)
# app.config.update(
# jwt=JWTManager(app.authenticate, identity)
# )

from project.views import app

if __name__ == '__main__':
    app.run(debug=True)
