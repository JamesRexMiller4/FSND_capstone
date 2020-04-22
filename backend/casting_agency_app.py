import os
from flask import Flask, request, abort, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin
from models import setup_db, Movie, Actor, CastMember, db

app = Flask(__name__)
setup_db(app)
CORS(app)

@app.after_request
def after_request(response):
    response.headers.add(
        "Access-Control-Allow-Headers", "Content-Type, Authorization, true"
    )
    response.headers.add(
        "Access-Control-Allow-Methods", "GET, DELETE, POST, OPTIONS"
    )
    response.headers.add("Access-Control-Allow-Credentials", "true")
    return response

@app.route('/')
def index():
    return 'Working'

