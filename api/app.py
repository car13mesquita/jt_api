from flask import Flask, Response, jsonify, request
from .companies import companies
from .errors import errors

app = Flask(__name__)
app.register_blueprint(companies)
app.register_blueprint(errors)


@app.route("/")
def index():
    return Response("Hello, world!", status=200)
